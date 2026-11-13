<!--
SECOND SYSTEM-DESIGN STORY — SMASH ticketing + mobile-scanning system (founding-engineer build, 2018–20).
IMPORTANT: Unlike the CRM-Lite doc (which is your real documented design), the verified facts here are only what's on your résumé:
"Designed and built an integrated ticketing and mobile scanning system, supporting 40,000+ attendees and vendors, team of 5."
Everything below is a SCAFFOLD for how to present this problem class. Swap my assumptions for what you ACTUALLY built — every ⟨confirm⟩ tag is a spot to replace with your real decision. Do not claim a design choice you didn't make.
-->

# System-Design Prep #2 — "Ticketing + door-scanning for a 40,000-attendee event"

Your second real system-design story, and a deliberate *contrast* to CRM Lite:

| | CRM Lite (doc #1) | SMASH ticketing (this one) |
|---|---|---|
| Problem class | **Batch / throughput** — backfill millions of records | **Low-latency / availability under burst** — validate entries at the gate in real time |
| Hard part | Knowing when an async job is "done" | Staying up when the venue network dies at doors-open |
| Shows | Pipelines, idempotency, scale math | Offline-tolerance, edge, anti-fraud, peak load |

Having one of each is exactly what a two-round system-design loop wants. Below is a scaffold — **replace assumptions with your real choices.**

## The generalised prompt
> "Design a ticketing and entry-scanning system for a 40,000+ attendee event: sell/issue tickets, validate them at multiple gates in real time, prevent re-use, support different access tiers (attendee/vendor/exhibitor/staff), and keep working when the venue WiFi is unreliable."

Maps to: *design a ticketing/check-in system*, *QR validation at scale*, *offline-first mobile*, *anti-fraud / idempotent validation*, *burst traffic*.

## 1. Clarify requirements (say first)
**Functional:** issue tickets (QR/barcode); validate at gate; one-entry-per-ticket (anti-passback) ⟨confirm: did you allow re-entry?⟩; access tiers; live headcount/capacity ⟨confirm⟩.
**Non-functional:** **gate scans must be fast (<~1s) and must not hard-fail on network loss**; correctness on double-entry; spiky load (most of 40k arrive in a ~2-hour window at doors-open); multiple gates/scanners concurrently.
**Scale anchor:** "40k attendees, say 8–12 gates, peak ~minutes after opening — if half arrive in the first 90 min that's ~3,700/gate over 90 min ≈ a scan every ~1.5s per gate at peak. Modest throughput, but **latency and availability at the edge dominate the design**, not raw QPS." ⟨confirm your real gate count / arrival curve⟩

## 2. High-level design (scaffold — mark your real version)
```
 [Ticketing/sales]  ──issue──►  Ticket store (id, holder, tier, status, signature)
                                      │
                                      ▼  (pre-event sync / push)
 [Gate scanner apps]  ◄── local cache of valid ticket set + tier ──┐
        │  scan QR                                                  │
        ▼                                                           │
   validate LOCALLY (signature + cache + local "already-scanned" set)│
        │  allow/deny in <1s                                         │
        ▼                                                           │
   queue scan event ──► sync to central service when online ───────┘
                                      │
                                      ▼
                         reconcile / dedupe / live dashboard
```
Key design stances to articulate (replace with what you did):
- **Offline-first scanners** ⟨confirm⟩ — each scanner holds a cached copy of the valid-ticket set so a WiFi drop at the gate doesn't stop entry. *This is the headline insight for this problem* — venues have terrible networks.
- **Signed tickets** ⟨confirm⟩ — QR encodes a signed token so a scanner can verify authenticity offline without a round trip.
- **Eventual anti-passback** — each scanner records local "already scanned" IDs; on sync, the central service reconciles to catch a ticket used at two gates. Tradeoff: a determined attacker could double-enter at two offline gates in the sync gap — call this out and justify (acceptable risk vs. the cost of hard-online validation).

## 3. Data model (scaffold)
Ticket: `id, holder, tier, status(valid/used/void), issued_at, signature`. Scan event: `ticket_id, gate_id, scanner_id, ts, result, synced`. Access tier → allowed zones.

## 4. The hard part — staying up at the gate (lead with this)
- **Failure you're designing against:** venue network dies exactly when 40k people are queuing.
- **Answer:** validation works fully offline from the cached signed-ticket set; scans queue locally and sync opportunistically; the door never blocks on the network. Online is an optimisation (live dashboard, faster cross-gate anti-passback), not a dependency.
- This is the availability-under-burst mirror of CRM-Lite's "know when the batch is done."

## 5. Failure / edge handling
- **Network partition at a gate:** offline mode (above).
- **Double-entry across gates:** local dedupe + central reconciliation; flag conflicts.
- **Scanner crash / battery:** stateless-ish client, re-sync cache on restart; ⟨confirm⟩.
- **Bad/forged QR:** signature check rejects offline.
- **Capacity limits / zone full:** ⟨confirm if you handled this⟩.
- **Refunds/void after issue:** push void-list updates to scanners pre-event and on reconnect.

## 6. Tradeoffs to volunteer
- Offline-first ⇒ a small anti-passback gap ⇒ accepted for a one-day event vs. the alternative (queues stall on every network blip). Conscious tradeoff.
- Team of 5, volunteer-run, hard deadline (the event date doesn't move) ⇒ simplicity and reliability over feature richness. *Great framing: "the date is immovable, so we optimised for 'works under stress' over 'does everything.'"*

## 7. Likely follow-ups → answers
| They ask | You say |
|---|---|
| "Why not validate online every scan?" | Venue networks are unreliable and the cost of a stalled gate at doors-open is a crowd-safety issue; offline-first with eventual reconciliation is the right risk tradeoff for a one-day event. |
| "How do you stop ticket sharing?" | Signed single-use tokens + per-scanner used-set + central reconciliation; accept the small offline double-entry window and flag it. |
| "Peak load handling?" | Load is per-gate and modest; the bottleneck is human throughput at the door, so I optimise scan latency (<1s, local) over backend QPS. |
| "How would you evolve it?" | ⟨your real future-work — e.g. live capacity dashboards, NFC, central real-time anti-passback if venue networking improved⟩ |

## 8. 45-minute plan
Clarify (5m, anchor on the arrival curve) → offline-first flow (10m) → data model (6m) → "staying up at the gate" hard part (8m) → anti-passback/dedupe + reconciliation (8m) → tradeoffs (5m) → evolution (3m). **Lead the hard-part section with offline-first** — it's the insight that signals you've actually run a gate.

> **Reminder:** confirm/replace every ⟨confirm⟩ with what you genuinely built. If you can't remember a detail, say "we did X; if I were designing it fresh I'd consider Y" — honest and still strong. Never assert a design choice you didn't make.
