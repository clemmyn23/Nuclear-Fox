<!--
IMPACT METRICS PLAYBOOK — for each flagship project: the user outcome, the business outcome, what you can
claim TODAY from evidence, and exactly how to get the missing number before your next final round.
Rule: never state a number you can't defend. ✅ = measured/sourced. 📐 = projection from measured inputs (say "roughly"/"on track for").
🔍 = go measure it (source + query sketch given). Query sketches are starting points — verify table/column names first.
Confidentiality: in interviews, round and relativise ("~40% faster", "a few hundred customers") — never quote internal revenue.
-->

# Impact Metrics Playbook

Culture-fit / hiring-manager rounds ask some version of **"so what changed for the customer and the business?"** Engineers usually answer with *what they built*. This file gives you the *so-what* for each project, at three confidence levels, so you can say something true and concrete every time.

**The formula for every answer:** *Who was hurting → what I owned/decided → what changed (number) → what it unlocked next.*

---

## 1. SMS Toll-free Compliance Embed — *your flagship ownership story*

**Who was hurting**
- **Customers** wanting SMS had to go through a manual process: a Google form → support staff → someone flipping `SendApprovalStatus` in the admin tool (Hex). Slow, error-prone, with data-quality issues.
- **Sales** couldn't "sell SMS as a feature" — the PM's stated ideal state. Self-serve SMS was switched off (billing couldn't sell SMS credits).
- **Support/ops** carried the manual provisioning load across 3 separate provisioning code paths. The PM in Aug 2026: *"None of us other than Greg have done provisioning"*, meaning a single person was the bottleneck.
- **Context:** Twilio announced stricter toll-free verification compliance effective 15 Sep 2026, and leadership called SMS provisioning *"one of Product's highest priorities"*. (Linking the two is inference, so present it as context, not as the stated cause.)

**What you can claim today**
| Claim | Level | Source |
|---|---|---|
| Ran discovery, wrote the tech audit + breakdown that the PM's proposal adopted as Checkpoint 1 | ✅ | Confluence COMPOSE/2451767325; PM's References page credits you |
| Re-scoped the estimate: ~7–11 days vs a 5–8 day placeholder, broken into 11 tickets | ✅ | same |
| Reported 16 of 28 epic tickets; owned the CmAPI/monolith backend (9 PRs, +7.8k LOC; the shared-services team owns the Twilio integration) | ✅ | Jira COM-1620; GitHub |
| Built the in-app registration flow that replaces a manual support-tool workflow | ✅ | COM-1702, COM-1619 |
| **Consolidated 3 duplicate provisioning flows into 1 service** | ✅ | PR #25080 |
| Idempotent by design: retries can never buy a second number (direct cost protection) | ✅ | COM-1700 AC, PR #25046 |
| Paves the way for ~250 Infobip customers to migrate (CP3) and self-serve SMS (CP5, early 2027) | ✅ (as roadmap) | PM Proposal |
| Your staffing recommendation (you on the CmAPI integration, a teammate on the frontend) was adopted by the team lead | ✅ | Slack DM 28 Sep |
| Found a "chicken-egg" API-design flaw in the shared-services team's API; they changed it within a day | ✅ | Slack #cm-thompson-support, 7–8 Oct |
| Dev complete; PM on 4 Nov: "in full glory! Great work Clem, Alexis!!"; cleared for real-customer testing 5 Nov | ✅ | Slack |

**What to go measure (🔍) — do this before the next final round**
| Metric | Why it sells | Where |
|---|---|---|
| **Time-to-SMS-enabled** (request → can send): before (manual) vs after (embed) | User-impact headline: "days → minutes to submit; carrier review is the only wait" | Ask support/PM for typical manual turnaround; after = embed analytics timestamps (init → `onInquirySubmitted` → Enabled) |
| **# customers registered via embed** since launch | Adoption | Compliance Slack-post channel count; analytics event from COM-1646 frontend; `SMS_Client` rows created by the new service |
| **Manual provisioning requests eliminated** | Support-cost headline | Hex audit/CAL for `SendApprovalStatus` flips per month, before vs after |
| **Registration rejection/rework rate** | "reduce human error" was a stated goal | Provider status (rejected vs approved) |
| **Sales-led SMS deals enabled** | Revenue *enablement* (don't quote $) | Ask PM: "how many sales-led SMS customers onboarded since launch?" |

**Interview line (today):** *"I took SMS onboarding from a manual, support-driven process to an in-app flow. I ran the discovery, documented the sales-led-first plan and made sure we staged it because the registration can't be undone, and built the backend so a retry can never buy a second phone number. Along the way I collapsed three duplicate provisioning paths into one. It's the foundation for migrating our ~250 legacy-provider customers and for self-serve next year."*

---

## 2. Drip Campaigns (Advanced, branching) — *feature delivery at product scale*

**Who was hurting:** marketers wanting branching, conditional email sequences had to leave the campaign tool for the heavier Journeys product. Agencies and multi-team accounts were the target segment.

**What you can claim today**
| Claim | Level | Source |
|---|---|---|
| Owned the drip-builder tree canvas: tree API contract (on the critical path, blocked 3 tickets), zoomable canvas, add-step, timeline, scheduled dates | ✅ | AJ-1115/1139/1140/1149; 15 PRs |
| Self-created and drove the final design + UX alignment card before release | ✅ | AJ-1190 |
| Defended the planned schema change with an audit (`SendingAgentType` column: 7 additive files vs ~20–30 incl. hot send procs) | ✅ | PR #23545 |
| Wrote the launch playbook (7 metrics, 7 anomaly runbooks, instrumentation gaps) — outgoing TL: "the best playbook in either space; use it as the template" | ✅ | Confluence AJ/2350841928; handover doc |
| Owned launch readiness (AJ-1155): Datadog dashboard, alerts channel, playbook, FF + DB release-order steps; announced "live on all prod DBs" to SRE on 27 Jul | ✅ | Slack #cm-sre; Jira |
| Rollout: Direct customers 22–27 Jul → **every account type, all plans, 1 Oct** (closed pilot cancelled as unnecessary); the 1 Oct SRE launch post linked your playbook | ✅ | AJ-1333; Slack |

> ⚠️ **Be precise about your role.** The team's tech lead was credited with "tech leading this through to delivery". Your claim is **"I owned the builder frontend and launch readiness"**, not "I led Drip Campaigns". Owning the customer-facing half and the go-live is plenty, and claiming the whole thing is the kind of inflation a reference check catches.

**🔍 Go measure**
| Metric | Where |
|---|---|
| **# advanced drip campaigns created / # accounts using it** since GA | **The `SendingAgentType` column marks every Advanced drip campaign, so it's your adoption counter.** Sketch: `SELECT COUNT(*), COUNT(DISTINCT ClientID) FROM CS_Campaign WHERE SendingAgentType = <ComplexSequence> AND DateCreated >= '2026-07-01'` |
| **Emails sent via drip** | Datadog — the playbook's send metrics (you proposed the `is_complex_sequence` tag; check if it landed) |
| **Adoption among agency/MT accounts** (% of eligible) | Amplitude — AJ-1176 instrumentation exists |
| **Incidents after launch / normal-send regressions** | Check it. The isolated send agent was a peer's design, so credit it if you cite it (a pre-launch load test did find a concurrency failure) |
| Engagement lift (open/click of drip vs one-off sends) | Reporting DB; nice-to-have |

**Interview line:** *"I owned the canvas where customers build branching drip campaigns, from the API contract through the final UX pass, and I owned go-live: the dashboard, the alerts, and the runbook the team now uses as its template. It went to Direct customers in July and to every plan in October. ⟨N⟩ accounts have built ⟨M⟩ drip campaigns since."*

---

## 3. Frontend build modernisation — Docker builds (JC-411) — *cross-team technical leverage*

> ⚠️ This is the one interviewers flagged as "pet project" energy. **Never lead with it.** Use it as the *technical depth + org influence* supporting act, always with numbers.

| Claim | Level | Source |
|---|---|---|
| Created the epic and scoped 24 tickets in 2 days; per-chain flag rollout + disaster-recovery plan designed (in review) | ✅ | JC-411; PR #25593 |
| Byte-level parity verification; found the Closure compiler exits 0 on errors (prints ERROR), so incomplete bundles would ship → build now fails correctly | ✅ | JC-412, PR #25020 |
| FE PR merge checks **switched to Docker on 6 Nov**, after six days running alongside Windows on the same PRs | ✅ | TeamCity |
| **PR-check compute per push −69%** (1,109 s → 348 s, same commits, faster on 233/233); the JC-411 baseline (1,066 s) holds, and the saving is 12 agent-min per push, above the "~5–9 min" estimate | ✅ | TeamCity, [portfolio/docker-frontend-builds-results-2026-11.md](../portfolio/docker-frontend-builds-results-2026-11.md) |
| Individual checks 1.8–8.5× faster; slowest check 319 s → 180 s (−44%); same tests, same hardware class | ✅ | TeamCity |
| FE-check agent-hours −72% (18.4 → 5.1 h/day) → **~4,850 agent-h/yr** | 📐 annualised from 6 days | TeamCity |
| Deploy package build **−41% like-for-like** (459 → 273 s; 523 → 290 s whole job), still shadow | ✅ early (n=17 paired) | TeamCity |
| ⚠️ **Don't claim faster PR feedback.** Push → all-green is 488 s median after the switch vs 327 s before: the shared Docker pool is congested by other workloads (FE checks are 4–8% of it). With no queue it would be 44% faster | ✅ (caveat) | TeamCity pool data |
| ⚠️ **Don't claim faster deploys.** The backend package (~21.5 min) is the long pole of the deploy chain | ✅ | TeamCity |
| Toolchain upgrades become a code change, not an AMI/agent change → unblocks Node 24, TS 7, faster bundler | ✅ (design) | JC-411 goal |
| Spike results: webpack warm cache 62.5→3.5 s; Closure→esbuild 13.7→0.35 s; tsc→TS7 4.8→0.46 s | ✅ (benchmarks) | JC-411 |

**🔍 Re-measure in 3–4 weeks:** package-build median after canary/hotfix/deploy chains flip; push → all-green median and p90 once the Docker pool's capacity is raised.

**Interview line:** *"Our frontend toolchain was baked into build-agent images, so every Node or TypeScript upgrade was an infra ticket. I moved the builds into Docker, verified byte-for-byte and run side by side on the same PRs before switching. PR checks now use about 70% less compute. Then I checked what developers actually wait for, found the shared agent pool had become the bottleneck, and showed it wasn't our checks."*

---

## 4. Brand Hub V2 "Correct the kit" — *customer-requested, in flight*

- **Who was hurting:** Brand Hub V1 was view-only; customers couldn't fix wrong auto-detected brand colours. **"Colour corrections are the most common request (three of four customers)."** ✅ (COM-1629)
- **You:** sole frontend author — data layer with optimistic concurrency (409 "kit changed"), edit/add/delete/save with validation, behind a flag. ✅
- **🔍 Measure after release:** % of kits edited; support requests about wrong brand colours; downstream — share of AI-generated content using an edited kit.

## 5. Production ownership stories — *small, but they show you own outcomes*
| Story | Number | Level |
|---|---|---|
| UCF alert regression traced to another team's PR | error queue 0–1 → stepped to 9 from 2 Sep; fixed + DLQ follow-ups | ✅ |
| RSS customer campaign (UK publisher) | root cause ~1h20m after assignment; automation paused; verified good send 6 days later; customer thanked you via Support | ✅ |
| GitHub→Slack bot outage (engineering dev tooling) | down ~9h40m; restored ~2h40m after you reported it; 2 hardening PRs (incl. escaping user content) + RCA | ✅ |
| Trigger-service healthcheck | 6 instances firing the same check → 429s; root-caused a scheduler/leader-election conflict | ✅ |
| Pkcs CVE flag | exact dependency path + patched versions → fix PR 29 min later (a colleague shipped it) | ✅ |
| TeamCity audit | 8 dormant projects (oldest 2016) + 5 stale configs; DevOps verified and approved | ✅ |
| Hex resource-ownership page | removes manual SQL against prod DBs for support lookups — security + speed | ✅ (🔍 ask how often support uses it) |

## 6. AI-DLC experiment — *the "good no" story*
- ✅ Completed the build phase of an AI-driven Node→C# port (+16k lines, 6 units, parity bench).
- ✅ Outcome: leadership chose **not** to ship — it would have replaced ~8k lines with ~16k, ~tripled maintenance, lost LLM observability, and delayed customer-requested work. Branches archived; learnings reused for Brand Hub 1A.
- **Impact framing:** *"The most valuable output was the decision. We learned in two weeks what AI-generated migrations really cost, and that fed the plan for Brand Hub editing."*

---

## The 10-minute data-gathering checklist (do this week)
1. [ ] Run the `SendingAgentType` count (drip adoption) — or ask a DBA/analyst.
2. [ ] Ask the SMS PM: customers registered via embed; typical manual turnaround before.
3. [ ] Check Amplitude for drip events (AJ-1176) — accounts using it.
4. [ ] Re-pull TeamCity Docker vs legacy medians after more chains flip (`scripts/teamcity-docker-builds/` has the method).
5. [ ] Ask support how often they use the Hex resource-ownership page.
6. [ ] Paste results into the ⟨⟩ slots in `cv/clement-ng-resume-2026-11.md` and `interview/star-story-bank.md`.
