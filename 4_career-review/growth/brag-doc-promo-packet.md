<!--
BRAG DOC / PROMO PACKET — a living record of impact, structured to a generic Senior→Staff ladder.
Uses: (1) your next employer's first performance cycle; (2) one more internal CM attempt if it thaws; (3) raw material for résumé/interview refreshes.
All entries trace to the career-review dataset. ⟨add metric⟩ = a real number to insert; never fabricate.
-->

# Brag Doc / Promo Packet — Clement Ng

A running record of impact, mapped to the dimensions Senior→Staff/Lead is judged on. Keep adding to it as you ship. (Most engineers under-promote because they never wrote it down — this is the antidote.)

## How to use
- **At a new job:** start logging from day one; by review time you'll have the packet most people scramble to reconstruct.
- **For a promo case:** map entries to your company's actual ladder rubric.
- **For interviews/résumé:** mine it for STAR stories and bullets.

---

## Dimension 1 — Technical scope & depth
- **CRM Lite, feature tech lead** — designed (architecture-reviewed LDR), built, and shipped end-to-end: protobuf/Kafka contracts, paged backfill pipeline, subscriber-profile UI, prod rollout. ⟨add: contacts processed / clients live⟩
- **WorkflowLookupService migration** — extracted a service from a 15-yr .NET-Framework monolith to standalone .NET Core gRPC; landed under production load after iterating through reverts.
- **SMS product** — full vertical slice: UI → CmAPI → gRPC → Kafka link-tracking taxonomy across multiple repos.
- **Multi-repo, contract-first delivery** — permission/failure-handling features across 3–4 repos in single coordinated sets.
- **Breadth** — shipped across 6 product domains (Audience, Campaign Authoring, SMS, Commerce, Automation Recipes, Journeys/CRM).

## Dimension 2 — Scope of influence (beyond your own keyboard)
- **JavaScript Crew** — reviewed JS merges org-wide; owned shared libraries and build tooling; set front-end standards.
- **Front-end modernisation program** — yarn workspaces, Vite/esbuild, Node LTS, TS 4→5, React 18, Webpack 5 part 2 (the monolith build was a colleague's) — work the whole front-end org builds on.
- **Reviewed 550+ PRs across 120+ engineers** — the de-facto reviewer-of-record for the team. [verify count]
- **20+ architecture/reference docs** — incl. system walkthroughs used to onboard new engineers; an LDR in the architecture-review space.

## Dimension 3 — Leadership & people
- **SMASH! Director of IT** — lead 25 volunteers / 3 leads; set Board-level IT strategy; multi-year roadmap. (7+ yr arc, founding engineer → Director.)
- **Grew an engineering team 5 → 25** over the SMASH tenure.
- **Hiring** — technical screener for mid-level candidates; made hire/no-hire calls with reasoning.
- **Mentoring** — coached junior engineers (design tradeoffs, query/contract decisions) through review and 1:1.
- **Bug-bash organiser** — ran 4 cross-functional pre-release QA sessions for major features.

## Dimension 4 — Reliability & ownership
- **Zero critical IT failures across 5 consecutive conventions** (45,000+ attendees) — live ops under peak load.
- **Production incident response** — e.g. the late-night P2 (abnormal API load vs. journey backlog); diagnosed and helped frame the fix. ⟨add: time-to-mitigate⟩
- **GDPR/privacy-by-design** — baked deletion handling and CAL-audit into feature work.

## Dimension 5 — Direction-setting & ambiguity (the Staff growth edge)
- **Multi-year IT strategy & roadmap (SMASH)** — owned end-to-end, no one ratifying above.
- **3-option tech investigations** (e.g. onboarding rework) that let product/leadership make slicing decisions.
- *Growth target (per `growth/skills-gap-plan.md`):* own an org-wide initiative inside a software org and a seat in architecture review — the last gap to a clean Staff case.

---

## Impact one-liners (steal these for reviews/résumé)
- "Led CRM Lite end-to-end — design through prod — including the cross-functional DBA/GDPR/platform negotiation."
- "Set front-end standards for the org as a JS-Crew member; ran the build modernisation everyone depends on."
- "Grew and now lead a 25-person engineering org; five years, zero critical failures, 45,000+ attendees."
- "Reviewed 550+ PRs across 120+ engineers — the team's reviewer of record." [verify]

## Maintenance ritual
- Add an entry **every time you ship something or unblock someone** — 1 line, takes 30 seconds, saves hours at review time.
- Quarterly, re-map entries to your ladder and note which dimension is thin → that's your next quarter's focus.
- Tag each entry with a ⟨metric⟩ when you have one; a real rough number beats an adjective, and never invent one.

---

## 🆕 2026-H2 entries (Jun–Nov 2026)

### Dimension 1: Technical scope & depth
- **SMS onboarding (Twilio compliance embed), technical lead in practice.** Discovery → plan (adopted by PM) → idempotent provisioning API (client-derived key, region check before purchase, typed upstream errors) → 3 provisioning flows merged into 1 → US/CA toll-free + AU sender IDs. 9 PRs, +7.8k LOC, 2,264 tests green. Dev-complete ~2 months; real-customer testing from 5 Nov. ⟨add: customers registered; turnaround before/after⟩
- **Drip Campaigns builder.** Tree API contract (critical path), canvas, timeline, React Query migration; schema decision (`SendingAgentType`, 7 vs 20–30 files). ⟨add: adoption from `SendingAgentType` count⟩
- **Brand Hub V2 1A frontend.** Optimistic-concurrency editing for Brand Hub's most common customer request (colour corrections).

### Dimension 2: Scope of influence
- **Docker frontend builds (JC-411).** Created a 24-ticket epic; switched the 5 FE PR checks on 6 Nov after a same-commit shadow run; per-pipeline rollout + DR plan for the deploy chains (in review). **PR-check compute −69% per push** (1,109 → 348 s, 233/233 commits), ~4,850 agent-h/yr; **deploy package build −41%** (shadow, n=17). Measured the developer-facing result too: the wait is now set by a congested shared agent pool (FE checks are 4–8% of it), with the capacity fix sized.
- **Standards:** React Query invalidation championed in reviews (an AI review bot later reinforced it); AI-review hygiene adopted by the TL.
- **JS Crew:** raised crew direction/leadership after a departure; interim meeting owner Jul–Oct.

### Dimension 3: Leadership & people
- **Staffing call adopted:** proposed the SMS backend/frontend split; lead: "we'll go with what you've recommended!"
- **Cross-team influence:** partner team changed its API within a day on your write-up.
- **Mentoring:** a junior engineer (test structure, BEM, naming, review etiquette, AI-reply caution); on-call unblocking.
- **Through the reorg:** named the Journey Designer knowledge holder in the outgoing TL's handover.

### Dimension 4: Reliability & ownership
- **Drip go-live owner:** dashboards, alerts channel, 7-metric/7-runbook playbook ("use it as the template"); announced live to SRE.
- **4 incidents end-to-end:** trigger-service leader-election bug; RSS customer failure (with support, to resolution); UCF DLQ cross-team regression (6 of the 8 failing cases fixed; "I can't express how great what you've done here is!"); engineering GitHub→Slack bot outage (same-day restore + injection hardening).
- **Owned own mistake:** cross-project CI break → "my bad" → fixed fast → flags + DR designed (in review).

### Dimension 5: Direction-setting & ambiguity
- **Documented the sales-led-first, staged rollout** for an irreversible registration flow; adopted as Checkpoint 1.
- **AI-DLC:** delivered the experiment and its honest cost readout. Leadership's no-go was built on it.
- **Don't-build calls:** parked a throwaway status poller; cut a resume ticket ("we get this for free").

### New impact one-liners
- "Led SMS onboarding from discovery to dev-complete: staged rollout, idempotent provisioning, three code paths into one."
- "Owned the builder and the go-live for Drip Campaigns, now on every plan."
- "Cut frontend CI compute by ~70% per PR push and made toolchain upgrades a code change."
- "Ran the build phase of an AI-migration experiment whose evidence informed the no-go (2× the code, ~3× the maintenance)."
