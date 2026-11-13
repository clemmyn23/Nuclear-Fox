<!--
SKILLS-GAP PLAN — 6–12 month moves to convert "Senior, Staff-trending" into a clean Staff-IC OR EM/Lead case.
Grounded in the gaps identified in files 15 (CM-only) and 16 (résumé+SMASH augmented).
-->

# Skills-Gap Plan (6–12 months)

From the IC analysis, your capability isn't the gap — **venue and evidence-shape are.** This plan turns "Senior, Staff-trending" into a closed case on whichever track you choose. Pick a track (or run both for a few months, then commit).

## Where you stand (recap)
- **Met for both tracks:** technical depth, end-to-end ownership, multiplier effect (reviews/mentoring/docs), cross-functional leadership, hiring, resilience, people leadership at scale (SMASH).
  - *Tenure note:* the SMASH leadership is a **~7.5-year arc (founding engineer → Director of IT, Nov 2018–present)** — sustained and progressively-scoped, which is exactly the "consistent track record" EM/Lead loops look for. You're not starting the leadership story from scratch.
- **The remaining gap, both tracks, is the same one:** owning **technical direction at org scope** *inside a software product org* — at CM you author LDRs the architects ratify; at SMASH you own the direction but it's IT/ops, not product engineering. You need one venue where you own product-engineering direction beyond your tribe.

---

## TRACK 1 — Staff / Senior+ IC

**Goal:** evidence that your technical influence reshapes how an *organisation* builds, not just how your tribe ships.

| # | Move | Why it closes the gap | Timeframe |
|---|---|---|---|
| 1 | **Own one org-wide technical initiative end-to-end.** Your JS-crew/front-end-platform lane is the natural one — e.g. "lead the monolith's front-end build modernisation as a program other teams adopt," not just your own PRs. | Converts "tribe-scoped" → "org-scoped" — the #1 Staff blocker. | 3–6 mo |
| 2 | **Write an LDR/RFC that *other teams build on top of*** (a shared contract, a platform pattern, a standard) — and shepherd it through review yourself. | Moves you from "authors LDRs the architects ratify" → "sets the pattern others ratify against." | ongoing |
| 3 | **Get a seat in the architecture-review function** (or its equivalent at your next company). Review others' designs, not just author your own. | Direction-*setting*, the last partial criterion. | 6–12 mo |
| 4 | **Deepen system-design fluency** so you interview at Staff bar. Use your CRM-Lite design (see `interview/system-design-crm-lite.md`) as the anchor; add 4–5 canonical designs (rate limiter, feed, notification system, idempotent job pipeline, multi-tenant throttling). | Staff loops are design-heavy; you have one killer real story, broaden to a portfolio. | 2–3 mo |
| 5 | **Make the multiplier legible.** You already mentor, review 550+ PRs, write onboarding docs — package it: "I uplifted N engineers / set the pattern M teams use." | Staff packets need *named* impact, not implicit. | 1 mo to assemble |

**At CM specifically (despite the promo freeze):** do #1 and #2 anyway — they're the evidence you take to the *next* employer's Staff interview, even if CM never re-titles you. The freeze makes internal promo unlikely, not the work worthless.

---

## TRACK 2 — Engineering Manager / Tech Lead

**Goal:** formalise the leadership you already do at SMASH into hireable EM evidence.

| # | Move | Why | Timeframe |
|---|---|---|---|
| 1 | **Name the SMASH role in EM terms.** You already do: people leadership (25, 3 leads), hiring/growing a team (5→25), strategy (Board roadmap), delivery (zero-failure × 5). Translate "vibe officer / Director of IT" into "manage, grow, and set direction for a 25-person engineering org." | EM interviews screen for exactly these; you have them, mis-labelled. | 1 mo (framing) |
| 2 | **Get reps on EM-specific skills you may not yet have on paper:** performance management / feedback cycles, hiring at volume, headcount/roadmap/OKR planning, managing underperformance, stakeholder comms. | These are the EM gaps a volunteer IT-director role may not fully cover. | 3–6 mo |
| 3 | **Seek a Tech Lead stint at CM or next role** — a small reporting line or formal lead-of-a-pod. Bridges IC→EM with a paid-software-org credential (SMASH is volunteer/IT-flavoured). | Removes the "volunteer discount" and "is it real software management?" objection. | 6–12 mo |
| 4 | **Read/skill up on the management canon** (e.g. *The Manager's Path*, *An Elegant Puzzle*) so you speak the EM interview language. | EM loops have a vocabulary; match it. | 1–2 mo |
| 5 | **Prepare EM behavioral stories** — `interview/star-story-bank.md` #4, #5, #7, #10, #11 are your core set; add a "managed a conflict between team members" and a "performance conversation" story from SMASH. | EM loops are ~60% behavioral leadership. | 1 mo |

---

## Technical breadth (both tracks, optional, by target)
Your stack (.NET/C# + TS/React + gRPC/Kafka/MSSQL) is strong and employable in Sydney as-is. Only add if your *target companies* demand it:
- **Big-tech Sydney (Google/Amazon/Atlassian/Canva):** heavier algorithms + system-design prep; some use Java/Python/Go — you have Java, brush it up if needed.
- **Modern cloud-native shops:** Kubernetes/containers depth, a cloud cert (AWS SA) if a posting lists it — *nice-to-have, not blocking* for someone with your shipping record.
- **Don't** chase certs or new languages speculatively; let target job descriptions drive it.

---

## Sequencing recommendation
1. **Now (weeks):** assemble the legible-impact summary (Track 1 #5 / Track 2 #1) — you mostly have it in this `career-review/` folder already. Polish résumé variants + LinkedIn (done).
2. **0–3 mo:** system-design portfolio (Track 1 #4) + EM story prep (Track 2 #5) in parallel — they're cheap and unlock interviews now. **Start interviewing** (the market is the fastest comp fix per `comp/`).
3. **3–6 mo:** whichever track the interviews respond to best, double down — own the org-wide initiative (T1) or land the tech-lead stint (T2).
4. **6–12 mo:** the architecture-seat (T1) or EM-skills reps (T2) become real at the *new* role you've moved to — which is also where the comp gap finally closes.

**Bottom line:** you don't need 12 months of prep to move. You need ~4–8 weeks to make the existing evidence legible and start interviewing; the deepest gap-closers (org-scope ownership, architecture seat, formal management) are best earned at the next role — the one that pays you correctly while you earn them.

---

## 🆕 Progress check: 2026-11-10

| Gap from this plan | Status now | Evidence |
|---|---|---|
| T1 #1: own an org-wide technical initiative | 🟡 **Started.** JC-411 Docker builds: you created it, it's cross-team, first number in (−41% deploy package build) | data/2026-h2/findings-teamcity.md |
| T1 #2: LDR/RFC others build on | 🟡 Partial. Twilio tech audit adopted by PM; Drip runbook became the team template | Confluence COMPOSE/2451767325, AJ/2350841928 |
| T1 #4: system-design portfolio | ✅ **3 real designs** now (CRM Lite batch, SMASH ticketing burst, **SMS idempotent provisioning**) | interview/system-design-*.md |
| T1 #5: make the multiplier legible | ✅ Brag doc + decision log | growth/brag-doc-promo-packet.md, interview/ownership-and-decisions.md |
| T2 #3: tech-lead stint | 🟡 **De facto, not titled.** SMS onboarding technical lead in practice | 06-year6-current.md ch. 4 |
| **NEW: interview feedback** "ownership/decisions", "pet projects" | 🟡 **Evidence now exists; packaging done; numbers pending** | ownership-and-decisions.md, impact-metrics-playbook.md |

### Revised next-90-days (supersedes "Sequencing" above where they conflict)
1. **Weeks 0–2:** pull the impact numbers (playbook checklist); fill the résumé ⟨⟩; rehearse stories 13/16/17 out loud with the decision + reflection endings.
2. **Weeks 0–4:** ask your EM for the **named tech-lead role on SMS Checkpoints 2–3** (UK/AU sender IDs, Infobip→Twilio for ~250 customers). Bring a one-page plan.
3. **Weeks 4–8:** "Drip Campaigns: 90 days later" readout with the PM. Ship Brand Hub 1A with an agreed success metric.
4. **Ongoing:** keep tooling at ≤20% of your time; finish JC-411 to a before/after dashboard.
5. **Interviewing:** keep going. The technical bar is cleared; the delta is now storytelling plus one or two numbers.
