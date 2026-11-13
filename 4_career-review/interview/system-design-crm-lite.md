<!--
SYSTEM-DESIGN INTERVIEW PREP — built from YOUR real CRM-Lite LDR (Confluence: arc/1593835523 + AJ/1819312139).
This is your single strongest system-design asset because you designed it, shipped it, and can answer any follow-up from memory.
Names lightly generalised so you can present it at any company; the reasoning is all yours.
-->

# System-Design Prep — "Backfill & aggregate all of a customer's contacts into one view"

You already designed and shipped this (CRM Lite). That makes it the best system-design story you have — you can go deeper than any made-up answer and survive every follow-up. Below is how to *present* it as a 45-minute system-design interview, plus the question bank.

## The generalised prompt it answers
> "Design a system that, when a customer opts in, takes all of their existing records spread across many lists and builds a single de-duplicated 'master' view — at multi-million-record scale, without double-charging them and respecting data-deletion law."

This maps to a huge family of real interview prompts: *build a backfill/migration pipeline*, *de-dup records at scale*, *fan-out batch processing*, *"design X that processes N million rows reliably."*

---

## 1. Clarify requirements (say these out loud first)
**Functional:** opt-in triggers a one-time backfill; aggregate contacts from all of a client's lists into one master list; de-dup by email; carry over a defined set of fields/attributes; show the customer a sane "in progress / ready" status.
**Non-functional:** correctness > speed (it's a one-time job); must not block normal traffic; must be resumable/idempotent (services die); must handle the largest customers; must honour data-deletion (GDPR) and not create a billing side-effect.
**Scale anchor:** "Largest clients are in the millions of contacts. My throughput budget is the existing contact pipeline — empirically 3k–10k records/sec. So ~10M records ≈ ~84 min at a conservative 2k/sec. That tells me this is minutes-to-hours, async, not synchronous."

*(Stating a real number here — 2k/sec, 84 min — instantly signals you've actually built this.)*

## 2. High-level design (the flow)
```
 Customer opts in
      │
      ▼
 [API]  set opt-in flag  ──►  emit  InitiateBackfill{ client_id }   (command)
      │
      ▼
 [Backfill Service]  consume InitiateBackfill
      │   look up all list_ids for the client
      │   for the first list → emit  PopulatePaged{ client_id, master_list_id, page_offset=0, remaining_list_ids[] }  (SQS)
      ▼
 [Backfill Service]  consume PopulatePaged   ◄────────────────┐
      │   query 1000 records at (list, page_offset)            │ re-enqueue next page
      │   emit bulk  RecordDefined  events (Kafka)             │
      │   decide next message: ───────────────────────────────┘
      │     • returned == 1000 → same list, page_offset += 1
      │     • returned  < 1000 → pop next list from remaining_list_ids, offset = 0
      │     • no lists left     → emit final / mark Finalising
      │   delete current SQS message (at-least-once)
      ▼
 [Existing Contact Pipeline]  consume RecordDefined (bulk)
      │   enrich → DEDUPE BY EMAIL → upsert into master list
      ▼
 Done (status flips to Ready)
```

**Why this shape:**
- **SQS self-re-enqueue per page** = backpressure + resumability for free. Each message is one unit of work; if a worker dies, the message redelivers. No giant in-memory cursor.
- **Reuse the existing contact pipeline** for the actual insert + dedupe instead of writing to the table directly — you inherit enrichment, dedupe-by-email, and all downstream consumers. (Key insight: *don't reinvent the write path; feed the one that already exists.*)
- **Bulk events capped at 1000** to match the pipeline's per-event limit.

## 3. Data model & contracts
- **Master-list marker:** an `IsMasterList` flag on the lists table (chosen over a foreign key on the already-wide clients table — a DBA-driven decision).
- **Job-tracking row** (per client): a status enum with a **3-state lifecycle** — `InProgress → Finalising → Completed` (+ `Failed`), plus a `JobDateUpdated` timestamp updated as pages process.
- **Message contracts (protobuf):** `InitiateBackfill{client_id}`; `PopulatePaged{client_id, master_list_id, page_offset, repeated remaining_list_ids}`; bulk `RecordDefined{client_id, list_id, email, changed_via, event_date, attributes...}`.

## 4. "How do I know it's *done*?" (your differentiator)
This is the genuinely hard part and you solved it — lead with it if they probe.
- You can't trust a single "last page" signal because the contact pipeline is async and downstream of you.
- Design: when the last page is emitted, set status `Finalising`. A scheduled reconciler marks `Completed` once `JobDateUpdated + buffer < now` while still `Finalising`. Completion estimate = `avg queue wait + (record_count × pipeline_throughput) + buffer`.
- Call out the tradeoff explicitly: *"Ideally the pipeline would emit a 'done' signal back via SQS; it doesn't, so the pragmatic option is a time-bounded reconciler. I flagged that I dislike scheduled DB-polling and would index the status column if we kept it."* (This is a real, mature judgment you can defend.)

## 5. Failure / edge handling
- **Idempotency / at-least-once:** dedupe-by-email in the pipeline means reprocessing a page is safe; deleting the SQS message only after successful emit.
- **Poison messages:** on repeated processing failure (e.g. 5th attempt) mark `Failed`, route to a **DLQ**, alert engineers.
- **List changes mid-job:** the customer can add contacts while the backfill runs — handled because the live contact-sync path runs concurrently and also dedupes by email; the backfill is "best effort baseline," not a lock.
- **Stale jobs:** the reconciler's time-bound also rescues jobs that silently stall.

## 6. Privacy / compliance (most candidates forget this — you didn't)
- **GDPR delete:** deleting a client wipes the entire master list + its associated custom fields.
- **GDPR retrieval/export:** consciously deferred to a later iteration — *naming what you scoped out is a senior move.*
- **Deletion window:** designed against the 30-day legal SLA; explicitly checked the race between a delete request and an in-flight backfill.

## 7. Tradeoffs & the "pragmatic hack" (great to volunteer)
- First iteration set the master list to `isVisible=0, isDeleted=1` to **bypass the billing/visibility path and ship in ~2 weeks**, with the clean `IsMasterList` column carried forward. Framing: *"I separated 'correct end-state architecture' from 'shippable first slice' and carried both — got customer value out fast without painting us into a corner."* Interviewers love this when you can articulate the debt consciously.
- **Set attributes upfront** in the bulk event rather than a second pass — fewer round trips across systems (a deliberate latency/complexity call).

## 8. Alternatives you considered (have these ready)
- *Direct table writes* instead of the contact pipeline → rejected (loses dedupe/enrichment, risks the hot path).
- *One big query/stream* instead of paged SQS → rejected (no resumability, memory risk, can't backpressure).
- *Event-based completion signal* instead of a reconciler → preferred in theory, blocked by the pipeline not emitting one → documented as future work.

## 9. Likely follow-up questions → your answers
| They ask | You say |
|---|---|
| "What if it's 100M records, not 10M?" | Same design; partition by list across more consumers, raise SQS concurrency, watch the contact-pipeline as the bottleneck (it's shared infra → I'd rate-limit to protect tenants). |
| "How do you not double-count a contact in 5 lists?" | Dedupe-by-email happens in the pipeline finaliser, not in my fan-out — one email → one master record by construction. |
| "Exactly-once?" | At-least-once + idempotent upsert = effectively-once for the end state. Cheaper and safer than true exactly-once here. |
| "Noisy-neighbour / multi-tenant safety?" | The backfill shares the contact pipeline, so I throttle it and treat it as lower priority than live traffic. |
| "How do you test this?" | Idempotency test (replay a page), resumability test (kill a worker mid-job), the completion-reconciler time-bound, and a large-client load test against the 2k–10k/s budget. |
| "What would you change?" | Push for the pipeline to emit a real completion event so I can delete the reconciler; add GDPR export. |

## 10. Whiteboard plan for 45 minutes
1. (5m) Clarify requirements + state the scale anchor (2k/s, ~84 min for 10M).
2. (10m) Draw the opt-in → command → paged-SQS → bulk-Kafka → pipeline flow.
3. (8m) Data model + the 3-state job lifecycle.
4. (8m) "How do we know it's done?" — the hard part; lead with it.
5. (7m) Failure/DLQ/idempotency + multi-tenant throttling.
6. (5m) Privacy/GDPR + the pragmatic-hack tradeoff + alternatives.
7. (2m) "What I'd improve."

**Emphasise, in order:** reuse-the-existing-pipeline insight → resumable paged fan-out → the completion-detection design → conscious privacy + debt tradeoffs. Those four are what separate a Staff-level answer from a mid one — and they're all things you actually did.

---

> **You have a *second* real system-design story.** Loops often ask for two. As a founding engineer at SMASH (Nov 2018–Jan 2020) you designed and built an **integrated ticketing + mobile-scanning system for 40,000+ attendees** — a different problem class (real-time check-in at the door, offline-tolerant scanning, peak-load spikes at gate-open, access control). It complements CRM Lite nicely: that one is *batch/throughput*, this one is *low-latency/availability under burst*. Worth writing up as its own prep doc — say the word and I'll draft it.
