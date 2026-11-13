<!--
SYSTEM-DESIGN PREP #3 — built from YOUR real SMS Twilio Compliance Embed work (Sep–Oct 2026).
Sources: Confluence COMPOSE/2451767325 (your breakdown doc), Jira COM-1619/1620/1646–1656/1699–1702/1733,
PRs createsend.com #24875 #24882 #24999 #25031 #25046 #25079 #25080 #25163. See data/2026-h2/.
Problem class: idempotent orchestration of a third-party, money-spending, long-running, non-reversible workflow.
Complements #1 (CRM Lite = batch/throughput) and #2 (SMASH ticketing = low-latency/burst).
-->

# System-Design Prep #3 — "Onboard a customer to a regulated, paid third-party capability"

You designed and shipped the backend for this. It's the best story you have for the **"third-party integration / payments-adjacent / exactly-once side effects"** family of prompts, and it doubles as your strongest **feature-ownership** story (see `interview/ownership-and-decisions.md`).

## The generalised prompt it answers
> "Design the onboarding flow that lets a customer register for SMS sending. Registration goes through a third-party compliance provider, requires buying a phone number (costs money), takes days of carrier review, and can't be undone once submitted."

Maps to: *design a payment/checkout flow*, *integrate with a slow external API*, *design an idempotent provisioning API*, *design a webhook/status-sync system*, *multi-tenant onboarding wizard*.

---

## 1. Clarify (say these first)
**Functional:** eligible customer opens an in-app registration (embedded third-party UI) → backend creates the customer at the SMS provider → buys or reuses a number of the right type for the region → hands the embed a short-lived session token → customer submits compliance details → status moves *Not available → In progress → Available/Enabled*; the app gates SMS features on that status.

**Non-functional — the ones that matter:**
- **Never double-spend.** Retries, double clicks, two admins on two tabs — none may buy a second number. *("A number bought for the wrong region is still paid for.")*
- **Non-reversible.** Once a brand/registration is created at the provider there's no clean rollback → rollout must be **staged**, not big-bang.
- **Slow + async.** Carrier verification takes days; the provider's "completed" callback isn't guaranteed to fire.
- **Multi-tenant + multi-segment.** Direct, Agency, Multi-team accounts; per-brand theming; country rules (US/CA toll-free vs AU alphanumeric sender ID vs UK unsupported).
- **Don't leak internals.** Your public API must not expose the internal shared-services DTOs.

## 2. High-level design
```
 [App UI] ──GET status──►  [CmAPI.NetCore]  ──gRPC──►  [SMS Shared Services] ──► Twilio
    │                         │  (thin, typed proxy;       (owns provider calls,
    │                         │   no internal DTOs out)     number purchase)
    │  POST init (CSRF) ─────►│
    │                         ├─ eligibility rules (ordered): direct/agency? flag? region? billed-out-of-app? already has number?
    │                         ├─ requestId = f(client)  ◄── idempotency key, deterministic
    │                         ├─ create provider customer  (409 ⇒ already exists ⇒ continue)
    │                         ├─ buy-or-reuse number for region (region check BEFORE purchase)
    │                         └─ return session token (24h)
    │
    │  embed iframe ◄── token ── submit compliance details ──► provider
    │  onInquirySubmitted (track THIS, not onComplete — not guaranteed to fire)
    ▼
 [Monolith side-effects, idempotent]  SMS access → Verifying, countries, workflow type,
                                      activity log, compliance Slack post, analytics
 [Status]  GET status re-derives from provider/shared services (or short-TTL cache < 24h)
```

**Why this shape (your actual reasoning):**
- **Thin proxy over an owned service.** Shared Services owns the provider; CmAPI just orchestrates and maps errors. One integration point for the provider, many consumers.
- **Deterministic idempotency key per client** instead of a random per-request key → every retry *by construction* converges on the same provider customer + number. AC you wrote: *"Calling init twice for the same client never buys a second number."*
- **Validate before you spend.** Region/eligibility checks run before the purchase call.
- **Consolidate the side-effect path.** You found **three duplicate provisioning flows** (support tool, legacy self-serve, new embed) and merged them into one `SmsClientProvisioningService` — one place to get side effects right, idempotent on re-run (*"doesn't duplicate rows, posts or log entries"*).

## 3. API contract
| Endpoint | Semantics |
|---|---|
| `GET /sms/compliance-embed-status` | `Not available \| In progress \| Available \| Enabled` + reason; drives UI gating & banner |
| `POST /sms/compliance-embed-init` (CSRF) | idempotent provisioning; returns session token |
| `POST /sms/compliance-embed-session` (CSRF) | re-issue 24h token to resume an in-progress inquiry |

**Error mapping (a decision you documented):** 422 for "valid request, ineligible state" rather than 409/501; typed exceptions for provider failures including **non-JSON 502/504** from upstream gateways (a real-world gotcha most candidates miss).

## 4. State & status sync — the hard part
- Provider status changes over days. Options: (a) **webhook/event stream** from provider → shared services → you; (b) **poll on read** with a short-TTL cache; (c) scheduled reconciler.
- You **parked the status-sync ticket** until the provider + shared-services event stream existed ("Wait for webhook / event-stream work…") rather than build a poller you'd throw away — then it closed as no-work-needed. *Senior move: don't build the temporary thing if the right thing is coming.*
- Lifecycle edge: track `onInquirySubmitted` because `onComplete` isn't guaranteed. Resume is keyed off the client's number so a half-finished registration re-opens where it left off ("We get this for free" — cut a whole ticket).

## 5. Failure modes you designed for
| Failure | Handling |
|---|---|
| Double click / retry / two tabs | deterministic requestId; provider 409 ⇒ treat as success-and-continue |
| Concurrent init for same client | concurrent-init handling in the alphanumeric path (COM-1733) |
| Upstream gateway returns HTML 502/504 | typed exception, not a JSON-parse crash |
| Number hard-fails / released at provider | **you flagged it**: customer hits a dead end with no retry → proposed support-escalation process + named the eng decisions needed (COM-1699) |
| Wrong-region purchase | region check before purchase |
| Partial monolith side effects | single consolidated service, idempotent re-run |
| Tests buying real numbers | integration tests never hit the purchase path; full unit suites green at each merge (2,264 at the last) |

## 6. Rollout (non-reversible ⇒ staged)
- Feature flag routes **US/CA → new embed**, AU/UK stay on the legacy wizard.
- **Sales-led first, self-serve later** (decision recorded 7 Sep): self-serve needs SMS credits the billing system can't sell yet; sales-led lets you onboard known customers with a human in the loop while the irreversible step is new.
- Internal tests → production test with a real customer before widening.
- Scope tracked the provider's reality: AU alphanumeric added once supported; UK removed when the provider said unsupported.

## 7. Scale / cost
Low QPS (onboarding, not sending) — so the design optimises **correctness and cost safety**, not throughput. Say this explicitly: *"This isn't a scale problem, it's an exactly-once-side-effects problem. The expensive failure is buying a number twice or leaving a customer stuck mid-registration."*

## 8. Follow-ups → answers
| They ask | You say |
|---|---|
| "Why not a random idempotency key per request?" | Random keys dedupe *one* retried request; a client-derived key dedupes *every* path (two tabs, two admins, a support-tool retry). The invariant is per-client, so the key is per-client. |
| "Exactly-once?" | Provider-side create returns 409 on duplicate, number purchase is guarded by the same key + a buy-or-reuse check → effectively-once side effects with at-least-once calls. |
| "What if the provider is down mid-flow?" | Each step is resumable; re-calling init picks up from the last completed step because every step is idempotent. |
| "How do you know it worked in prod?" | Analytics + a compliance Slack post per registration; status endpoint; next step is a funnel dashboard (see impact playbook). |
| "What would you change?" | Event-driven status sync end-to-end; a support-tool view for hard-failed numbers; self-serve once billing supports SMS credits. |

## 9. 45-minute whiteboard plan
1. (5m) Requirements — lead with **"never double-spend, can't roll back"**.
2. (10m) Draw UI → API → shared service → provider; mark the idempotency key.
3. (8m) Contract + error mapping + status enum.
4. (10m) Status sync & lifecycle edges (webhook vs poll; `onInquirySubmitted`).
5. (7m) Failure table.
6. (5m) Staged rollout & why sales-led first.

**Emphasise, in order:** deterministic idempotency → validate-before-spend → consolidating three side-effect paths into one → staged rollout for an irreversible action. That's the senior/Staff signal: you designed for the *money* and the *customer stuck in the middle*, not just the happy path.
