# Year 6 — Drip Campaigns launch → team merge → SMS onboarding lead → Brand Hub

**Window:** 2026-04 → 2026-11-10 (Year 6 runs to 2027-03; this is month 8). *Updated 2026-11-10; earlier version covered Apr–May only.*
**Authored:** 71 PRs (53 merged, 7 open, 11 closed-unmerged) · **+18k / −4.8k LOC merged since June**
**Reviewed:** 84 PRs for others (63 since June, across 22 authors; 3 change-requests)
**Repos (authored):** 9: createsend.com, BrandHubServices, GitHubTeamManagement, localdev-tools, workflowcontext.{runnerservice, triggerservice, metricservice, updatecustomfield}.core, workflowbuildercontext.uiservice.core
**Jira:** AJ (Boole, to Aug) → **COM (Mitnick, from Sep)** · JC (JS Crew)
**Confluence:** 3 pages authored (Twilio compliance tech audit, Drip Campaigns playbook, sales-led dev-account recipe), 3 contributed
**Teams:** Boole (Audience & Journeys) → **merged into Team Mitnick, 1 Sep 2026**
**Raw evidence:** [data/2026-h2/](data/2026-h2/) (GitHub, Jira, Confluence, Slack, TeamCity findings)

---

## The story of Year 6 in one paragraph

Year 6 is the year the work became **product-led**. It opened with you building the frontend of **Advanced Drip Campaigns** (branching campaign sequences) and owning its go-live: dashboards, alerts, the launch runbook, and the "live on all prod DBs" call to SRE in July. It shipped to every plan in October. Then the org changed under you: the Boole tech lead left on 27 Aug with *"no named successor"*, Boole merged into Team Mitnick on 1 Sep, and two more engineers left within a week. Days later the EM asked you to take discovery on **SMS onboarding via Twilio's compliance embed**, *"one of Product's highest priorities"*. You turned that discovery into the technical plan the PM adopted. You documented the sales-led-first rollout decision, designed an idempotent provisioning API, got your staffing proposal adopted, got another team to change its API, and shipped it to dev-complete with public credit from the PM. In parallel you ran the build phase of an **AI-driven Node→C# migration experiment**; its evidence became leadership's no-go decision. You also started a cross-team **Docker frontend-build** epic (PR-check compute −69% per push; deploy package build ~41% faster in shadow), handled **four production incidents** end-to-end, and in November became sole frontend owner for **Brand Hub V2 "Correct the kit"**, Brand Hub's most common customer request.

**What changed vs Year 5:** the work stopped being "the senior who reviews everything and upgrades the toolchain" and became **"the engineer the EM hands the top-priority ambiguous project to."** That is the evidence the 2026 interview feedback said was missing; see [interview/ownership-and-decisions.md](interview/ownership-and-decisions.md).

---

## Chapter 1 — Complex Campaign Series → Advanced Drip Campaigns (Apr–Oct)

**Epic:** [AJ-1111](https://campaignmonitor.atlassian.net/browse/AJ-1111) Advanced Drip Campaigns – Branching (68 tickets; Done 9 Oct). Related: AJ-1158 Simple Drip UI refresh, AJ-1250 fast-follows.
**Your role:** **owner of the drip-builder frontend and of launch readiness.** The team TL was credited publicly with tech-leading overall delivery, and the backend send agent/cohort engine was mostly a peer's work. Be precise about this in interviews.

| Phase | What you did | Evidence |
|---|---|---|
| Apr–May: foundations | Tree API contract (`sequenceTree`, node/edge types) — on the critical path, blocked 3 other tickets; schema `CS_ComplexSequenceNodeTree`; zoomable/pannable canvas with URL-driven focus; add-step, node-limit banner | AJ-1115, AJ-1139, AJ-1140; [#22838](https://git.campmon.com/Freshview/createsend.com/pull/22838), [#22857](https://git.campmon.com/Freshview/createsend.com/pull/22857), [#23083](https://git.campmon.com/Freshview/createsend.com/pull/23083) |
| Jun: **schema decision** | `SendingAgentType` column vs reusing `SendServiceType`. You audited it: reuse self-clobbers a claim flag and costs "~20–30 files incl. hot send procs vs 7 additive". You defended the planned new column, landed it non-null with the CHECK constraint dropped after DB review, and logged the legacy cleanup as debt. Pushed back on an unnecessary key constraint after a call with the senior C# reviewer. | [#23545](https://git.campmon.com/Freshview/createsend.com/pull/23545), AJ-1186 |
| Jun: **kill your own design** | Prototyped the timeline "gutter" and dropped it as unworkable across different scheduled dates. Replaced it with node-level scheduled date/time/GMT offset and branch backdrops. | [#23585](https://git.campmon.com/Freshview/createsend.com/pull/23585) (closed), [#23711](https://git.campmon.com/Freshview/createsend.com/pull/23711) |
| Jun: React Query migration | Moved sequence data to React Query; `invalidateQueries` replaced full-page `reload()`, so the canvas updates in place; load-error banner (previously failed silently). You then **taught the pattern** in reviews across the team. | [#23682](https://git.campmon.com/Freshview/createsend.com/pull/23682) |
| Jun–Jul: **final design alignment** | Self-created AJ-1190 as the card for final design alignment and UX polish before release; ran it with the designer. Rules: no steps under draft parents, conditions disabled after plain-text emails ("No tracking = no open clicks"). | AJ-1190; [#23838](https://git.campmon.com/Freshview/createsend.com/pull/23838), [#23903](https://git.campmon.com/Freshview/createsend.com/pull/23903) |
| Jul: **launch readiness** | AJ-1155: Datadog dashboard, `#campaign-sequence-alerts`, playbook (7 metrics, 7 anomaly runbooks, instrumentation gaps such as the `is_complex_sequence` tag), FF + DB release order for the PM. **27 Jul to SRE: "live on all prod DBs."** | Confluence [AJ/2350841928](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/2350841928); Slack #cm-sre |
| Jul–Aug: fast-follows | Node overlaps, fit view, thumbnails (deliberately didn't touch high-traffic client overview), help-doc links; Simple Drip redesign behind `BasicCampaignSequenceUIRefresh` | AJ-1257/1265/1262/1254/1161 |
| 1 Oct | **All account types, every plan.** The closed pilot was cancelled as unnecessary. The SRE launch post reused your playbook. | AJ-1333; Slack |

**Recognition:** outgoing TL's handover: *"the best playbook in either space; use it as the template."* Handover also names you as the WorkflowBuilder/Journey Designer knowledge holder.

## Chapter 2 — Journey Reporting innovation sprint (late May–Jun)
- Feature-flag gRPC client in RunnerService + monolith flag (AJ-1196); **subscriber activity history UI** so support could diagnose without querying the DB (AJ-1195, [uiservice#317](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/317)); realistic demo mocks (AJ-1213).
- AI work logs with honest deltas: Webpack 5 *"~1 day with AI vs ~1 week"*; gRPC v2 *"1–2 hrs vs half a day"*; Figma→CSS *"roughly halved"*.
- Productionisation (AJ-1307) went to others; GrpcClient v2 PR [#153](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/153) is parked.

## Chapter 3 — The team merge (Aug–Sep)
- **27 Aug:** Boole TL leaves. Handover (AJ-1305): *"There is no named successor tech lead… the biggest structural risk."* Named as the WorkflowBuilder/Journey Designer knowledge holder, and on the handover's "book time with" list.
- **1 Sep:** "4 teams will merge down into 2"; **Boole + Mitnick → Team Mitnick** (AJ & COM). You posted the redirect notice to the old team channel.
- **Early Sep:** two more engineers leave. *[Inference]* you're now one of the most senior engineers holding Journeys/workflow context in the merged team.
- Mitnick contexts: Campaigns UI, SMS, List & Subscribers, Journeys, Integrations; it also inherited Brand Hub from another team.

## Chapter 4 — ⭐ SMS Toll-free Compliance Embed (Sep–Nov): de-facto technical lead
**Epic:** [COM-1620](https://campaignmonitor.atlassian.net/browse/COM-1620) · **Tech audit:** [COMPOSE/2451767325](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/2451767325) · **PRs:** 9 (8 merged, +7.8k/−1.4k)

**Why it mattered:** SMS onboarding was manual. Customers filled in a form, then support provisioned them in the admin tool. *"None of us other than Greg have done provisioning."* Self-serve SMS was off. Product's ideal state was that *Sales can "sell SMS as a feature."* Twilio announced stricter toll-free verification effective 15 Sep. Leadership: *"one of Product's highest priorities."*

| Date | What you did |
|---|---|
| 1 Sep | EM: *"Would you be up for taking the discovery piece of this work on for our team"* |
| 7–15 Sep | Wrote the tech audit and breakdown. Scope: TFN in; AU/UK sender ID blocked; 10DLC out. **Documented the sales-led-first decision** (billing can't sell SMS credits) and the no-rollback risk (→ staged rollout). Flagged the black-box callback risk and asked about early access, so the PM applied. **Re-estimated 7–11 days vs 5–8 placeholder**; created 11 tickets. PM's References page credits your audit; PM's proposal adopts your Checkpoint 1. |
| 17 Sep | Dev-account recipe for spoofing a sales-led account (engineering has no Salesforce access); a teammate later scripted it |
| 28 Sep | Lead puts SMS and AI-DLC both on your plate. **You recommend the staffing split** (you take CmAPI integration, a teammate takes frontend). *"we'll go with what you've recommended!"* |
| 30 Sep–2 Oct | Eligibility/status service + non-dismissable registration banner ([#24875](https://git.campmon.com/Freshview/createsend.com/pull/24875), [#24882](https://git.campmon.com/Freshview/createsend.com/pull/24882)). Owned review catches ("This is my bad"). |
| 7–8 Oct | **"Chicken-egg" API problem** raised with the shared-services team; they made `registrationInfo` optional, in staging the next day |
| 9–14 Oct | **Idempotent provisioning** ([#25046](https://git.campmon.com/Freshview/createsend.com/pull/25046)): client-derived requestId, 409 = continue, region check before purchase ("a number bought for the wrong region is still paid for"), typed upstream errors, "Decisions worth a look" section; moved to CmAPI.NetCore on request ([#25031](https://git.campmon.com/Freshview/createsend.com/pull/25031)) |
| 12–20 Oct | Enabled status + gating ([#25079](https://git.campmon.com/Freshview/createsend.com/pull/25079)); **merged 3 duplicate provisioning flows into one service** ([#25080](https://git.campmon.com/Freshview/createsend.com/pull/25080), 2,264 tests green); parked status-sync until the event stream existed; cut resume ticket ("We get this for free") |
| 13 Oct | Flagged that **a hard-failed number leaves the customer stuck** and proposed a support-escalation process |
| 19–21 Oct | AU alphanumeric sender IDs ([#25163](https://git.campmon.com/Freshview/createsend.com/pull/25163)); per-brand theming (Direct / Agency white-label); live demo at standup |
| 2–5 Nov | Dev complete (US/CA TFN + AU alphanumeric). **PM: *"SMS Compliance Embeddable in full glory! Great work Clem, Alexis!!"*** Cleared to test with real customers 5 Nov |

**Business impact (to measure; see [interview/impact-metrics-playbook.md](interview/impact-metrics-playbook.md)):** time-to-SMS-enabled, manual provisioning requests eliminated, embed registrations, rejection rate. Foundation for the Infobip→Twilio migration (~250 customers) and self-serve (early 2027).

## Chapter 5 — AI-DLC Stream A: the experiment whose output was a decision (Sep–Nov)
- AWS AI-DLC workshop stream: port Brand Hub's AIBrandScraper from Node to C#/.NET. You ran the build phase (COM-1673): 6 units, SSRF-hardened adapters, gRPC surface, C#-vs-Node parity bench, **307/307 unit + 72/72 parity tests**, BrandHubServices #81–86 (+16.4k). Worked past 1am; lead: *"gone above and beyond."*
- **Judgment call:** *"Claude has been going back and forth… for the past 2.5 business days… gone a bit pass the whole 'use ai to save time' threshold."* Recommended human review + staging before merge. Lead: *"Such a great call out."*
- **3 Nov, leadership no-go:** ~16k lines to replace ~8k, ~3× maintenance, loses LLM observability, a migration that can't be cleanly reversed, delays customer work. *"A worthwhile experiment… That's what made this decision possible."* Branches archived; learnings reused for Brand Hub 1A.

## Chapter 6 — Docker frontend builds (JC-411, Oct–Nov): cross-team platform initiative
- **You created the epic and all 24 child tickets in two days.** Goal: toolchain upgrades become a code change, not an agent/AMI change; PR checks from ~10 min toward ~2. Your JC-411 baseline (1,066 s of agent time per push) is confirmed by TeamCity, which measured 1,109 s on Windows.
- **Stage 1** ([#25020](https://git.campmon.com/Freshview/createsend.com/pull/25020)): byte-level parity on 6,106 files; found that Closure prints `ERROR` and exits 0, so bundles could ship incomplete; build now fails correctly.
- **Stage 2–3** ([#25051](https://git.campmon.com/Freshview/createsend.com/pull/25051), [#25501](https://git.campmon.com/Freshview/createsend.com/pull/25501), [#25593](https://git.campmon.com/Freshview/createsend.com/pull/25593)): idempotent package push, one DSL for pr/deploy/canary/hotfix chains, **per-chain flag rollout + disaster-recovery plan** (#25051 open, #25593 in review), quantified risk. One self-caused cross-project CI break, owned and fixed fast.
- **Switched (6 Nov):** the five FE PR merge checks moved to Docker after six days running alongside the Windows checks on the same PRs; Windows checks paused. The deploy package build is in shadow (#25051 and #25593 still open).
- **Measured (TeamCity, 10 Nov, same-commit pairs):**
  - **PR-check compute per push −69%** (1,109 s → 348 s, faster on 233/233 commits).
  - Individual checks 1.8–8.5× faster; slowest check 319 s → 180 s (−44%).
  - FE-check agent-hours −72% (~4,850 h/yr projected).
  - Deploy package −41% like-for-like (459 → 273 s, n=17 shadow).
  - Cause: Windows spent 54% of agent time on checkout + `npm install` repeated five times; Docker's cached deps layer removes it.
- **Honest caveat:** push → all-green has not improved yet (median 488 s after the switch vs 327 s on Windows). The shared Docker pool filled with other teams' workloads from 29 Oct; FE checks are only 4–8% of it. With no queue, feedback would be 44% faster; the fix is pool capacity.
- **Benchmarks still to unlock:** webpack warm cache 62.5→3.5 s, Closure→esbuild 13.7→0.35 s, tsc→TS7 4.8→0.46 s.
- Full write-up: [portfolio/docker-frontend-builds-results-2026-11.md](portfolio/docker-frontend-builds-results-2026-11.md).
- Also: TeamCity dead-project audit (~8 projects, last built 2016–2023); removed node-notifier.

## Chapter 7 — Brand Hub V2 "Correct the kit" (Nov, in flight)
- Epic COM-1629. *"Colour corrections are the most common request (three of four customers)."* You are **sole frontend owner**: data layer with optimistic concurrency (409 "kit changed"), edit/add/delete/save with a 15-colour cap and validation, logo/image delete (open), behind `BrandHubV2` (in prod 6 Nov). Tested your tests: *"I broke the page two ways… The old tests passed against both, and the new ones fail."* PM: *"This is looking great."*

## Chapter 8 — Production ownership (four incidents, each closed out)
| When | Incident | What you did |
|---|---|---|
| 15–25 Jun | Trigger-service healthcheck → 429s | Unblocked on-call; found leader election dropped in the .NET Core port, so all 6 instances ran the heartbeat; advised against restart; stopgap + root-cause fix ([triggerservice#66](https://git.campmon.com/Engineering/workflowcontext.triggerservice.core/pull/66)) |
| 15–22 Jul | RSS customer send failures (UK publisher) | Assigned by the TL (*"blacksmith is looking into this first"*); root cause ~1h20m later: nested `<data>` tags in two template layouts + an invalid feed (duplicate `xmlns:media`); paused the automation, drafted the customer explanation, verified the fixed send 6 days later. Customer via Support: *"Thanks for spotting the issues and letting me know"* |
| 2–9 Sep | Recurring UCF alerts / DLQ | Decoded protobuf, proved redrive safe (idempotent SETs), asked for 👍 before touching prod late at night; traced regression to another team's PR; patch fixes 6 of 8 failure types; DLQ semantics follow-ups ([updatecustomfield#73](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/73)). Lead: *"I can't express how great what you've done here is!"* |
| 9 Oct | GitHub→Slack bot down ~9h40m (engineering dev tooling) | Self-detected; ECS/Datadog timeline; Graylog shutdown as the likely cause (your RCA notes the fix can't be attributed to one change); restored ~2h40m after you reported it (12:39 → 15:21); hardened against injection of user content into Slack markup ([#7](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/7), [#8](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/8); #6 authored via an agent account) |

Plus: Graylog→Datadog migrations before the 30 Sep decommission (AJ-980/971/1292); Hex resource-ownership page, so engineers stop "remoting into prod sql" (*"productivity boosters"*, EM: *"Super useful!"*); flagged a high-severity Pkcs CVE to the C# crew with the exact dependency path (MimeKit 4.15.1 → Pkcs) and patched versions; a senior engineer shipped the fix PR 29 minutes later. **TeamCity audit** (14 Oct): 8 dormant createsend.com projects (oldest last built 2016) + 5 stale configs, to clear room for the new JS pipelines; DevOps verified it, wrote it up and approved (*"Thanks blacksmith 🙌"*). **Local proxy overhaul** ([localdev-tools#74](https://git.campmon.com/Engineering/localdev-tools/pull/74), +6.2k/−21.8k, Jun): once routes moved to CmAPI.NetCore, devs needed it to run the monolith locally. Senior C# engineer: *"you will need the updated version of the local proxy. Which Clem overhauled."*

## Chapter 9 — Multiplier: reviews, standards, mentoring
- **63 reviews across 22 authors** since June; 3 change-requests. Most-reviewed: the team lead (12) and backend peer (8).
- **Standards you set and taught:** React Query invalidation over manual reloads (an AI review bot later quoted it: "Reinforcing @cng's earlier comment"); one component per file; no cross-app imports; valid transpiled CSS (*"I'm gonna veto the earlier change"*); AI hygiene (*"Don't really need these token burning comments"*, "don't push the robot review to repo", which led to a follow-up fix PR).
- **JS Crew:** raised crew direction/leadership in Jul (no replies; 3 Aug notes: *"Crew captain • No direct volunteers"*, so don't claim crew lead); interim meeting owner Sep–Oct, then handed over; roster host Dec 2026 / Jun 2027.
- **Mentoring:** a junior engineer, whose manager pointed her to you: test structure, BEM, naming, how to respond to reviewers, caution on AI-rewritten replies. Also coached on-call and DB tracing for peers.
- **Not yours:** the Biome lint migration (a colleague's initiative; you reviewed it).

## Chapter 10 — What other people said (name-mention + peer sweep, 2026-11-10)
The earlier sweep searched your handle. This one searched **"clem" / "Clement" in other people's messages**, and checked a teammate's AI-generated list thread by thread. Raw: `data/2026-h2/findings-slack-clem-sweep.md`, `findings-slack-peer-verification.md`, `peer-sweep-sha-2026-11-10.md`.

**Public credit**
- Drip GA (#cm-product-updates, 9 Oct). EM: *"huge props to the awesome engineers who worked on this"* (tags you, Fan, Chris). Team lead: *"These guys are the real heroes behind this… Thank you Clem, Fan and Chris."* (The PM's announcement credits the PM for driving the bulk of the project; your credit is in the replies, shared with two peers.)
- SMS: partner-team engineer reading the code: *"Looks like Clem did this work."*
- People Team invited you personally to the mentorship program (Aug): *"someone who could really benefit from (and contribute to) these kinds of conversations… a mentee, a mentor, or both."*

**Other people treating you as the owner.** This is the strongest evidence for the "ownership" gap, because someone else said it.
- Boole TL, on a customer's CRM Lite data question: *"I think clem implemented that work, we can have a chat with him."*
- A peer asked you to confirm it was safe to raise drip's `MAX_SEQUENCE_NODES` from 30 to 60.
- A senior C# engineer asked your sign-off before routing the SMS embed endpoint 100% to netcore in prod and before removing the legacy route.
- *"May need Clem to review this"*: a peer's microservices / Datadog architecture diagram.
- Named publicly as the owner of the new front-end merge checks during the 6 Nov CI break (*"Clem is looking into it"*).
- DevOps engaged on "TeamCity builds as code" (JC-413): *"Interested in how this plays out Clem."*
- On the Mitnick Slack-monitor roster (~20 alert channels, incl. #campaign-sequence-alerts and #sms-compliance-alerts).
- Your Stream A PRs were the handover artefact: *"inspect the PRs that Clem put together, merge them in, test…"*

**Honest negatives (prepare them, don't hide them)**
- **3 Jul production incident from a PR you approved.** The webpack 4→5 monolith build PR ([#23212](https://git.campmon.com/Freshview/createsend.com/pull/23212), a colleague's) had a missing import that broke RSS one-click campaigns; "quite a few support cases"; SRE fixed it that night. You were the sole approver. No blame in the thread. This is a good "what I learned" story (story 24), and a reason to describe webpack 5 as *shared*: you did part 2 (#23354), the colleague did the monolith build.
- **SMS schedule pressure.** 12 Oct, the EM: *"quite a few cards remaining… Would it help if we got Alexis onto it too?"* You split the work so the second engineer could start from your COM-1700 PR. Target 30 Oct; dev-complete reported 2 Nov. Frame it as re-planning with your manager, which is what happened.
- Small: the discovery doc said Twilio didn't support alphanumeric; it did (enabled that day). A reviewer caught endpoints duplicated in legacy + netcore in #25046; fixed that morning.

## Year 6 numbers at a glance
| Metric | Value |
|---|---|
| PRs authored / merged | 71 / 53 |
| PRs reviewed (others) | 84 |
| Jira epics with a lead-type role | 3: SMS embed (de-facto TL), Drip (frontend + launch owner), JC-411 (creator/owner) |
| Tickets reported by you, SMS epic | 16 of 28 |
| Tickets created, JC-411 | 24 + epic |
| Production incidents closed out | 4 |
| Confluence authored | 3 |
| Customer-facing launches | Drip (Direct Jul → all plans 1 Oct); SMS embed (dev-complete Nov; real-customer testing) |
| Measured build win | PR-check compute −69% per push; deploy package −41% (shadow) |

---

## Appendix A — Apr–May 2026 PRs (from the May review; states updated: #23354, #23356, #23265 later merged)

### Authored (Apr–May, 15)

| Date | Repo | # | JIRA | State | Title |
|---|---|---|---|---|---|
| 2026-04-10 | createsend.com | [#22838](https://git.campmon.com/Freshview/createsend.com/pull/22838) | [AJ-1115](https://campaignmonitor.atlassian.net/browse/AJ-1115) | ✅ | AJ-1115-a Add table CS_ComplexSequenceNodeTree |
| 2026-04-13 | createsend.com | [#22857](https://git.campmon.com/Freshview/createsend.com/pull/22857) | [AJ-1115](https://campaignmonitor.atlassian.net/browse/AJ-1115) | ✅ | AJ-1115-b Implement complex campaign series backend  |
| 2026-04-16 | createsend.com | [#22915](https://git.campmon.com/Freshview/createsend.com/pull/22915) | [AJ-1115](https://campaignmonitor.atlassian.net/browse/AJ-1115) | ✅ | AJ-1115-c Campaign series backend - Fix not grabbing condition type |
| 2026-04-20 | createsend.com | [#22934](https://git.campmon.com/Freshview/createsend.com/pull/22934) | — | ✅ | js prefer workspace version typescript |
| 2026-04-21 | createsend.com | [#22945](https://git.campmon.com/Freshview/createsend.com/pull/22945) | [AJ-1115](https://campaignmonitor.atlassian.net/browse/AJ-1115) | ✅ | AJ-1115-d Advanced campaign sequence frontend part 1 |
| 2026-05-04 | createsend.com | [#23083](https://git.campmon.com/Freshview/createsend.com/pull/23083) | [AJ-1139](https://campaignmonitor.atlassian.net/browse/AJ-1139) | ✅ | AJ-1139-a Advanced campaign series - Implement tree rendering  |
| 2026-05-05 | createsend.com | [#23115](https://git.campmon.com/Freshview/createsend.com/pull/23115) | [AJ-1115](https://campaignmonitor.atlassian.net/browse/AJ-1115) | ✅ | AJ-1115-e Fix frontend build |
| 2026-05-11 | createsend.com | [#23156](https://git.campmon.com/Freshview/createsend.com/pull/23156) | [AJ-1139](https://campaignmonitor.atlassian.net/browse/AJ-1139) | ✅ | AJ-1139-b Complex campaign series - improve frontend tree rendering |
| 2026-05-14 | createsend.com | [#23200](https://git.campmon.com/Freshview/createsend.com/pull/23200) | [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) | ✅ | AJ-1140-a Campaign series - fix enum inconsistency |
| 2026-05-20 | createsend.com | [#23243](https://git.campmon.com/Freshview/createsend.com/pull/23243) | [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) | 🔴 | AJ-1140-c Complex sequence - Add campaign nodes to tree |
| 2026-05-22 | createsend.com | [#23265](https://git.campmon.com/Freshview/createsend.com/pull/23265) | [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) | 🟡 | AJ-1140-e Complex sequence - Add campaign nodes to tree |
| 2026-05-25 | Engineering/workflowcontext.runnerservice.core | [#147](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/147) | [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) | ✅ | AJ-1196-a Add feature flag client |
| 2026-05-28 | Engineering/workflowcontext.runnerservice.core | [#153](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/153) | [AJ-1206](https://campaignmonitor.atlassian.net/browse/AJ-1206) | 🟡 | AJ-1206-a Migrate to GrpcClient v2 |
| 2026-05-28 | createsend.com | [#23354](https://git.campmon.com/Freshview/createsend.com/pull/23354) | — | 🟡 | Upgrade webpack 5 - part 2 |
| 2026-05-28 | createsend.com | [#23356](https://git.campmon.com/Freshview/createsend.com/pull/23356) | [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) | 🟡 | AJ-1196-d Pass IsJourneyReportingEnabled feature flag to workflow ui |

### Reviewed (Apr–May, 22)

| Date | Author | Repo | # | JIRA | State | Title |
|---|---|---|---|---|---|---|
| 2026-04-01 | junior engineer | createsend.com | [#22731](https://git.campmon.com/Freshview/createsend.com/pull/22731) | [AJ-1135](https://campaignmonitor.atlassian.net/browse/AJ-1135) | ✅ | AJ-1135 add more logs for CRM opt in, update opt in dialog |
| 2026-04-02 | junior engineer | createsend.com | [#22766](https://git.campmon.com/Freshview/createsend.com/pull/22766) | [AJ-1107](https://campaignmonitor.atlassian.net/browse/AJ-1107) | ✅ | AJ-1107: refactor upsell banner code to be maintainable |
| 2026-04-10 | junior engineer | createsend.com | [#22839](https://git.campmon.com/Freshview/createsend.com/pull/22839) | [AJ-1132](https://campaignmonitor.atlassian.net/browse/AJ-1132) | ✅ | AJ-1132-b selection of Complex vs Simple series |
| 2026-04-14 | junior engineer | createsend.com | [#22865](https://git.campmon.com/Freshview/createsend.com/pull/22865) | [AJ-1130](https://campaignmonitor.atlassian.net/browse/AJ-1130) | ✅ | AJ-1130 Update tooltip copy for Engagement Score help icon |
| 2026-04-14 | senior engineer | createsend.com | [#22873](https://git.campmon.com/Freshview/createsend.com/pull/22873) | [AJ-1117](https://campaignmonitor.atlassian.net/browse/AJ-1117) | ✅ | AJ-1117 - create a campaign in a complex series |
| 2026-04-15 | junior engineer | createsend.com | [#22884](https://git.campmon.com/Freshview/createsend.com/pull/22884) | [AJ-1066](https://campaignmonitor.atlassian.net/browse/AJ-1066) | ✅ | AJ-1066 Frontend custom field sorting in Subscriber Profile |
| 2026-04-15 | junior engineer | createsend.com | [#22903](https://git.campmon.com/Freshview/createsend.com/pull/22903) | [AJ-1108](https://campaignmonitor.atlassian.net/browse/AJ-1108) | ✅ | AJ-1108 refactor crmlist cm api endpoint responses |
| 2026-04-17 | senior engineer | createsend.com | [#22922](https://git.campmon.com/Freshview/createsend.com/pull/22922) | [AJ-1117](https://campaignmonitor.atlassian.net/browse/AJ-1117) | ✅ | AJ-1117b - refactor SequenceDataRepository |
| 2026-04-22 | junior engineer | createsend.com | [#22961](https://git.campmon.com/Freshview/createsend.com/pull/22961) | — | ✅ | AJ- 1116 : Attach conditions to campaigns: API |
| 2026-04-28 | junior engineer | createsend.com | [#23015](https://git.campmon.com/Freshview/createsend.com/pull/23015) | — | ✅ | Schedule campaign validation |
| 2026-04-30 | junior engineer | createsend.com | [#23044](https://git.campmon.com/Freshview/createsend.com/pull/23044) | [AJ-1116](https://campaignmonitor.atlassian.net/browse/AJ-1116) | ✅ | AJ-1116 Attach conditions to campaigns: API |
| 2026-05-04 | engineer | createsend.com | [#23081](https://git.campmon.com/Freshview/createsend.com/pull/23081) | [STRK-174](https://campaignmonitor.atlassian.net/browse/STRK-174) | ✅ | STRK-174 Implement "Existing Components" UI design |
| 2026-05-04 | engineer | Engineering/contentbuildercontext.staticresourceservice.core | [#1186](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1186) | — | ✅ | JS - Upgrade TS to 5.6.2 |
| 2026-05-04 | engineer | createsend.com | [#23093](https://git.campmon.com/Freshview/createsend.com/pull/23093) | [COM-1256](https://campaignmonitor.atlassian.net/browse/COM-1256) | ✅ | COM-1256: Earnings Amount Updates with Client Filter |
| 2026-05-04 | engineer | Engineering/chargebee-custom-codes | [#1](https://git.campmon.com/Engineering/chargebee-custom-codes/pull/1) | [LSK-901](https://campaignmonitor.atlassian.net/browse/LSK-901) | ✅ | LSK-901 Initial version control for Chargebee custom codes |
| 2026-05-08 | junior engineer | Engineering/ContactAttributeService | [#58](https://git.campmon.com/Engineering/ContactAttributeService/pull/58) | [AJ-1124](https://campaignmonitor.atlassian.net/browse/AJ-1124) | ✅ | AJ-1124 add cohort routing to ContactMembershipMultiplexer |
| 2026-05-13 | engineer | createsend.com | [#23185](https://git.campmon.com/Freshview/createsend.com/pull/23185) | [AJ-1145](https://campaignmonitor.atlassian.net/browse/AJ-1145) | ✅ | AJ-1145-a - Update sequence to return date created, new segment endpoint |
| 2026-05-20 | engineer | createsend.com | [#23242](https://git.campmon.com/Freshview/createsend.com/pull/23242) | [AJ-1145](https://campaignmonitor.atlassian.net/browse/AJ-1145) | ✅ | AJ-1145-frontend - Add sequence activity panel, add react query to campaigns |
| 2026-05-25 | junior engineer | Engineering/workflowcontext.runnerservice.core | [#148](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/148) | [AJ-1204](https://campaignmonitor.atlassian.net/browse/AJ-1204) | ✅ | AJ-1204: Add AI code reviewer |
| 2026-05-25 | junior engineer | Engineering/workflowbuildercontext.uiservice.core | [#315](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/315) | [AJ-1204](https://campaignmonitor.atlassian.net/browse/AJ-1204) | 🟡 | AJ-1204: Add AI code reviewer |
| 2026-05-27 | junior engineer | Engineering/workflowcontext.runnerservice.core | [#151](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/151) | [AJ-804](https://campaignmonitor.atlassian.net/browse/AJ-804) | ✅ | AJ-804 : Create PostgresDB Aurora Cluster workflow-context |
| 2026-05-28 | junior engineer | Engineering/workflowcontext.runnerservice.core | [#152](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/152) | [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) | ✅ | AJ-1196 : Add feature flag gRPC client to RunnerService and monolith feature flag for journey reporting UI |

## Appendix B — Jun–Nov 2026 authored PRs (59, from 2026-05-28; 3 overlap with Appendix A)

✅ merged · 🟡 open · ⛔ closed unmerged

| Date | Workstream | Repo | PR | Jira | State | +/− | Title |
|---|---|---|---|---|---|---:|---|
| 2026-05-28 | Journey reporting | workflowcontext.runnerservice.core | [#153](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/153) | [AJ-1206](https://campaignmonitor.atlassian.net/browse/AJ-1206) | 🟡 | +732/−553 | AJ-1206-a Migrate to GrpcClient v2 |
| 2026-05-28 | Tooling | createsend.com | [#23354](https://git.campmon.com/Freshview/createsend.com/pull/23354) | — | ✅ | +464/−308 | Upgrade webpack 5 - part 2 |
| 2026-05-28 | Journey reporting | createsend.com | [#23356](https://git.campmon.com/Freshview/createsend.com/pull/23356) | [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) | ✅ | +3/−1 | AJ-1196-d Pass IsJourneyReportingEnabled feature flag to workflow ui |
| 2026-06-02 | Journey reporting | workflowbuildercontext.uiservice.core | [#317](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/317) | [AJ-1195](https://campaignmonitor.atlassian.net/browse/AJ-1195) | ✅ | +895/−265 | AJ-1195-a Subscriber activity view |
| 2026-06-04 | Journey reporting | workflowbuildercontext.uiservice.core | [#319](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/319) | [AJ-1213](https://campaignmonitor.atlassian.net/browse/AJ-1213) | ✅ | +234/−83 | AJ-1213 realistic mocks |
| 2026-06-09 | Journey reporting | workflowbuildercontext.uiservice.core | [#321](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/321) | [AJ-1213](https://campaignmonitor.atlassian.net/browse/AJ-1213) | ✅ | +251/−138 | AJ-1213 realistic mocks 2 |
| 2026-06-12 | Drip | createsend.com | [#23545](https://git.campmon.com/Freshview/createsend.com/pull/23545) | [AJ-1186](https://campaignmonitor.atlassian.net/browse/AJ-1186) | ✅ | +66/−0 | AJ-1186-a Set agent type for complex sequence campaigns |
| 2026-06-16 | Ops | workflowcontext.triggerservice.core | [#66](https://git.campmon.com/Engineering/workflowcontext.triggerservice.core/pull/66) | — | ✅ | +52/−31 | Fix healthcheck |
| 2026-06-17 | Drip | createsend.com | [#23585](https://git.campmon.com/Freshview/createsend.com/pull/23585) | [AJ-1149](https://campaignmonitor.atlassian.net/browse/AJ-1149) | ⛔ | +300/−2 | AJ-1149-a Complex sequence - Implement timeline gutter |
| 2026-06-22 | Tooling | localdev-tools | [#76](https://git.campmon.com/Engineering/localdev-tools/pull/76) | — | ✅ | +1080/−921 | Add local proxy profiles |
| 2026-06-24 | Drip | createsend.com | [#23666](https://git.campmon.com/Freshview/createsend.com/pull/23666) | [AJ-1149](https://campaignmonitor.atlassian.net/browse/AJ-1149) | ⛔ | +559/−267 | AJ-1149-b2 Complex sequence - scheduled date display etc. |
| 2026-06-24 | Drip | createsend.com | [#23680](https://git.campmon.com/Freshview/createsend.com/pull/23680) | [AJ-1149](https://campaignmonitor.atlassian.net/browse/AJ-1149) | ⛔ | +252/−191 | AJ-1149-c Campaing sequence - code refactor, cleanups, react query. |
| 2026-06-24 | Drip | createsend.com | [#23682](https://git.campmon.com/Freshview/createsend.com/pull/23682) | [AJ-1149](https://campaignmonitor.atlassian.net/browse/AJ-1149) | ✅ | +271/−203 | AJ-1149-c2 Campaing sequence - prep work for design changes |
| 2026-06-26 | Drip | createsend.com | [#23711](https://git.campmon.com/Freshview/createsend.com/pull/23711) | [AJ-1149](https://campaignmonitor.atlassian.net/browse/AJ-1149) | ✅ | +1007/−464 | AJ-1149-d Complex sequence - Display scheduled date |
| 2026-07-08 | Drip | createsend.com | [#23838](https://git.campmon.com/Freshview/createsend.com/pull/23838) | [AJ-1190](https://campaignmonitor.atlassian.net/browse/AJ-1190) | ✅ | +69/−39 | AJ-1190-a Campaign series - frontend design alignment A |
| 2026-07-14 | Drip | createsend.com | [#23903](https://git.campmon.com/Freshview/createsend.com/pull/23903) | [AJ-1190](https://campaignmonitor.atlassian.net/browse/AJ-1190) | ✅ | +208/−43 | AJ-1190-b Drip campaigns - frontend changes 2 |
| 2026-07-16 | Drip | createsend.com | [#23931](https://git.campmon.com/Freshview/createsend.com/pull/23931) | [AJ-1190](https://campaignmonitor.atlassian.net/browse/AJ-1190) | ✅ | +3/−3 | AJ-1190-c Drip campaigns - adjust capitalization on back button |
| 2026-07-16 | Drip | createsend.com | [#23932](https://git.campmon.com/Freshview/createsend.com/pull/23932) | [AJ-1254](https://campaignmonitor.atlassian.net/browse/AJ-1254) | ✅ | +8/−1 | AJ-1254-a Drip campaigns - Help doc update |
| 2026-07-16 | Drip | createsend.com | [#23946](https://git.campmon.com/Freshview/createsend.com/pull/23946) | [AJ-1257](https://campaignmonitor.atlassian.net/browse/AJ-1257) | ✅ | +11/−6 | AJ-1257-a - Drip campaigns - Prevent node overlaps |
| 2026-07-30 | Drip | createsend.com | [#24078](https://git.campmon.com/Freshview/createsend.com/pull/24078) | [AJ-1265](https://campaignmonitor.atlassian.net/browse/AJ-1265) | ✅ | +110/−11 | AJ-1265-a Drip campaigns - Adjust initial fit view |
| 2026-08-05 | Drip | createsend.com | [#24142](https://git.campmon.com/Freshview/createsend.com/pull/24142) | [AJ-1262](https://campaignmonitor.atlassian.net/browse/AJ-1262) | ✅ | +180/−2 | AJ-1262-a / Drip campaigns - Fix fetching campaign thumbnails |
| 2026-08-20 | Drip | createsend.com | [#24309](https://git.campmon.com/Freshview/createsend.com/pull/24309) | [AJ-1161](https://campaignmonitor.atlassian.net/browse/AJ-1161) | ✅ | +669/−406 | AJ-1161-a Simple sequence - Prep work for UI refresh. |
| 2026-08-24 | Drip | createsend.com | [#24355](https://git.campmon.com/Freshview/createsend.com/pull/24355) | [AJ-1161](https://campaignmonitor.atlassian.net/browse/AJ-1161) | ✅ | +786/−38 | AJ-1161-b Simple sequence - Implement new design |
| 2026-09-02 | Tooling | createsend.com | [#24483](https://git.campmon.com/Freshview/createsend.com/pull/24483) | — | ✅ | +803/−3 | [Hex] Get resource ownership from ID |
| 2026-09-03 | Tooling | createsend.com | [#24499](https://git.campmon.com/Freshview/createsend.com/pull/24499) | — | 🟡 | +160/−0 | [Hex] UpdateCustomFieldFromWorkflow proto decoder |
| 2026-09-04 | Ops | workflowcontext.updatecustomfield | [#73](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/73) | [COM-1625](https://campaignmonitor.atlassian.net/browse/COM-1625) | ✅ | +272/−13 | COM-1625-a Handle contact attribute service returning multiple values |
| 2026-09-07 | Ops | workflowcontext.metricservice.core | [#20](https://git.campmon.com/Engineering/workflowcontext.metricservice.core/pull/20) | [AJ-980](https://campaignmonitor.atlassian.net/browse/AJ-980) | ✅ | +4/−14 | AJ-980 remove Graylog |
| 2026-09-09 | Ops | workflowcontext.updatecustomfield | [#74](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/74) | [AJ-1292](https://campaignmonitor.atlassian.net/browse/AJ-1292) | ✅ | +20/−5 | AJ-1292 DD logger impl consistency |
| 2026-09-11 | Ops | workflowcontext.updatecustomfield | [#75](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/75) | [AJ-1292](https://campaignmonitor.atlassian.net/browse/AJ-1292) | ✅ | +40/−43 | AJ-1292-b Use MemoisingConfigFactory, bump jvm-libs |
| 2026-09-23 | AI-DLC | BrandHubServices | [#81](https://git.campmon.com/Engineering/BrandHubServices/pull/81) | AIDLC-A-1 | ⛔ | +3656/−12 | AIDLC-A-1 Migrate backend to c# (unit 1, unit 2) |
| 2026-09-23 | AI-DLC | BrandHubServices | [#82](https://git.campmon.com/Engineering/BrandHubServices/pull/82) | AIDLC-A-2 | ⛔ | +3620/−0 | AIDLC-A-2 Unit 3 code gen |
| 2026-09-23 | AI-DLC | BrandHubServices | [#83](https://git.campmon.com/Engineering/BrandHubServices/pull/83) | AIDLC-A-3 | ⛔ | +3402/−1 | AIDLC-A-3 Unit 4 code gen |
| 2026-09-23 | AI-DLC | BrandHubServices | [#84](https://git.campmon.com/Engineering/BrandHubServices/pull/84) | AIDLC-A-4 | ⛔ | +926/−444 | AIDLC-A-4 Unit 5 code gen |
| 2026-09-23 | AI-DLC | BrandHubServices | [#85](https://git.campmon.com/Engineering/BrandHubServices/pull/85) | AIDLC-A-5 | ⛔ | +4439/−0 | AIDLC-A-5 Unit 6 code gen |
| 2026-09-25 | AI-DLC | BrandHubServices | [#86](https://git.campmon.com/Engineering/BrandHubServices/pull/86) | — | ⛔ | +358/−353 | update all 6 units because stuff doesn't build |
| 2026-09-25 | SMS embed | createsend.com | [#24805](https://git.campmon.com/Freshview/createsend.com/pull/24805) | [COM-1646](https://campaignmonitor.atlassian.net/browse/COM-1646) | ⛔ | +491/−144 | COM-1646-a Setup FF and pass through sms eligibility flag |
| 2026-09-30 | SMS embed | createsend.com | [#24875](https://git.campmon.com/Freshview/createsend.com/pull/24875) | [COM-1646](https://campaignmonitor.atlassian.net/browse/COM-1646) | ✅ | +323/−51 | COM-1646-backend SMS twilio embed - Initial FF and routing |
| 2026-09-30 | SMS embed | createsend.com | [#24882](https://git.campmon.com/Freshview/createsend.com/pull/24882) | [COM-1646](https://campaignmonitor.atlassian.net/browse/COM-1646) | ✅ | +318/−108 | COM-1646-frontend SMS Compliance Embed - Initial set up |
| 2026-10-07 | SMS embed | createsend.com | [#24999](https://git.campmon.com/Freshview/createsend.com/pull/24999) | [COM-1648](https://campaignmonitor.atlassian.net/browse/COM-1648) | ✅ | +1145/−175 | COM-1648: CmAPI endpoint to initialize Twilio Toll-free compliance inquiry |
| 2026-10-08 | Docker builds | createsend.com | [#25020](https://git.campmon.com/Freshview/createsend.com/pull/25020) | [JC-412](https://campaignmonitor.atlassian.net/browse/JC-412) | ✅ | +946/−21 | feat(JC-412): build the app/ frontend in Docker |
| 2026-10-09 | Ops | GitHubTeamManagement | [#7](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/7) | — | ✅ | +75/−5 | Escape user content in Slack notifications |
| 2026-10-09 | Ops | GitHubTeamManagement | [#8](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/8) | — | ✅ | +36/−66 | Bump cm-terraform fargate modules to 0.88 |
| 2026-10-09 | SMS embed | createsend.com | [#25031](https://git.campmon.com/Freshview/createsend.com/pull/25031) | [COM-1648](https://campaignmonitor.atlassian.net/browse/COM-1648) | ✅ | +773/−187 | COM-1648 Move new SMS endpoints to cmapi.netcore |
| 2026-10-09 | SMS embed | createsend.com | [#25046](https://git.campmon.com/Freshview/createsend.com/pull/25046) | [COM-1700](https://campaignmonitor.atlassian.net/browse/COM-1700) | ✅ | +1252/−320 | COM-1700: Provision Toll-free numbers for the SMS compliance embed |
| 2026-10-09 | Docker builds | createsend.com | [#25051](https://git.campmon.com/Freshview/createsend.com/pull/25051) | [JC-413](https://campaignmonitor.atlassian.net/browse/JC-413) | 🟡 | +391/−32 | feat(JC-413): pack and push the createsend.com.fe package in Docker |
| 2026-10-12 | SMS embed | createsend.com | [#25079](https://git.campmon.com/Freshview/createsend.com/pull/25079) | [COM-1699](https://campaignmonitor.atlassian.net/browse/COM-1699) | ✅ | +964/−111 | COM-1699: Add Enabled status to SMS compliance embed gating |
| 2026-10-12 | SMS embed | createsend.com | [#25080](https://git.campmon.com/Freshview/createsend.com/pull/25080) | [COM-1701](https://campaignmonitor.atlassian.net/browse/COM-1701) | ✅ | +897/−102 | COM-1701: Set up the CM client after Toll-free provisioning |
| 2026-10-19 | SMS embed | createsend.com | [#25163](https://git.campmon.com/Freshview/createsend.com/pull/25163) | [COM-1733](https://campaignmonitor.atlassian.net/browse/COM-1733) | ✅ | +1593/−179 | COM-1733 SMS compliance embed Alphanumeric support |
| 2026-11-03 | Brand Hub | createsend.com | [#25460](https://git.campmon.com/Freshview/createsend.com/pull/25460) | [COM-1792](https://campaignmonitor.atlassian.net/browse/COM-1792) | ✅ | +480/−3 | COM-1792: Brand Hub 1A data layer for colour edits and asset deletes |
| 2026-11-04 | Docker builds | createsend.com | [#25500](https://git.campmon.com/Freshview/createsend.com/pull/25500) | — | ✅ | +6/−174 | chore: remove node-notifier (and bundled terminal-notifier) from frontend builds |
| 2026-11-04 | Docker builds | createsend.com | [#25501](https://git.campmon.com/Freshview/createsend.com/pull/25501) | [JC-413](https://campaignmonitor.atlassian.net/browse/JC-413) | ✅ | +213/−41 | feat(JC-413): run the Docker frontend build in each deploy chain's own project |
| 2026-11-05 | Brand Hub | createsend.com | [#25526](https://git.campmon.com/Freshview/createsend.com/pull/25526) | [COM-1793](https://campaignmonitor.atlassian.net/browse/COM-1793) | ✅ | +2/−0 | COM-1793: Add BrandHubV2 feature flag |
| 2026-11-05 | Brand Hub | createsend.com | [#25537](https://git.campmon.com/Freshview/createsend.com/pull/25537) | [COM-1793](https://campaignmonitor.atlassian.net/browse/COM-1793) | ✅ | +411/−16 | COM-1793: Brand Hub colour edit mode layout behind BrandHubV2 |
| 2026-11-05 | Brand Hub | createsend.com | [#25539](https://git.campmon.com/Freshview/createsend.com/pull/25539) | [COM-1793](https://campaignmonitor.atlassian.net/browse/COM-1793) | ✅ | +1080/−116 | COM-1793: Edit, add, delete and save Brand Hub colours behind BrandHubV2 |
| 2026-11-09 | Brand Hub | createsend.com | [#25577](https://git.campmon.com/Freshview/createsend.com/pull/25577) | [COM-1793](https://campaignmonitor.atlassian.net/browse/COM-1793) | ✅ | +51/−41 | COM-1793: Send hex and stored role in the Brand Hub colour Save request |
| 2026-11-09 | Docker builds | createsend.com | [#25593](https://git.campmon.com/Freshview/createsend.com/pull/25593) | [JC-414](https://campaignmonitor.atlassian.net/browse/JC-414) | 🟡 | +67/−21 | feat(JC-414): switch a chain's frontend package to Docker with a flag |
| 2026-11-09 | Brand Hub | createsend.com | [#25595](https://git.campmon.com/Freshview/createsend.com/pull/25595) | [COM-1794](https://campaignmonitor.atlassian.net/browse/COM-1794) | 🟡 | +151/−44 | COM-1794: Prepare the Brand Hub edit components for logo and image delete |
| 2026-11-09 | Brand Hub | createsend.com | [#25596](https://git.campmon.com/Freshview/createsend.com/pull/25596) | [COM-1794](https://campaignmonitor.atlassian.net/browse/COM-1794) | 🟡 | +207/−31 | COM-1794: Always show the Brand Hub logos and images sections behind BrandHubV2 |
| 2026-11-09 | Brand Hub | createsend.com | [#25597](https://git.campmon.com/Freshview/createsend.com/pull/25597) | [COM-1794](https://campaignmonitor.atlassian.net/browse/COM-1794) | 🟡 | +742/−65 | COM-1794: Select, delete and save Brand Hub logos and images behind BrandHubV2 |

## Appendix C — Jun–Nov 2026 reviewed PRs (63)

| Date | Repo | PR | Jira | My review | Title |
|---|---|---|---|---|---|
| 2026-05-28 | workflowcontext.runnerservice.core | [#152](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/152) | [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) | APPROVED | AJ-1196 : Add feature flag gRPC client to RunnerService and monolith feature flag for journey reporting UI |
| 2026-05-29 | workflowbuildercontext.uiservice.core | [#316](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/316) | — | APPROVED | Mock Flow UI - Add mock counts to steps and paths, and add statistic boxes to the sidebar |
| 2026-06-09 | contentbuildercontext.staticresourceservice.core | [#1204](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1204) | — | APPROVED | Change day link changes |
| 2026-06-10 | createsend.com | [#23519](https://git.campmon.com/Freshview/createsend.com/pull/23519) | [AJ-1185](https://campaignmonitor.atlassian.net/browse/AJ-1185) | APPROVED | AJ-1185: ComplexSequenceAgent: scaffold new agent |
| 2026-06-12 | createsend.com | [#23544](https://git.campmon.com/Freshview/createsend.com/pull/23544) | [AJ-1141](https://campaignmonitor.atlassian.net/browse/AJ-1141) | APPROVED,COMMENTED | AJ-1141 Add condition for complex series |
| 2026-06-16 | createsend.com | [#23566](https://git.campmon.com/Freshview/createsend.com/pull/23566) | [AJ-1144](https://campaignmonitor.atlassian.net/browse/AJ-1144) | APPROVED | AJ-1144 - Sidebar for campaign details |
| 2026-06-16 | createsend.com | [#23569](https://git.campmon.com/Freshview/createsend.com/pull/23569) | — | APPROVED | ZUSE-98: Clean up unreleased Shopify forms work |
| 2026-06-17 | workflowcontext.triggereventcatalogservice.core | [#23](https://git.campmon.com/Engineering/workflowcontext.triggereventcatalogservice.core/pull/23) | [AJ-1227](https://campaignmonitor.atlassian.net/browse/AJ-1227) | APPROVED | AJ-1227 : Point production Elasticsearch to campmon.com endpoint |
| 2026-06-24 | createsend.com | [#23660](https://git.campmon.com/Freshview/createsend.com/pull/23660) | [AJ-1148](https://campaignmonitor.atlassian.net/browse/AJ-1148) | APPROVED,COMMENTED | AJ-1148: Cancel schedule cascade and UI warning |
| 2026-06-24 | createsend.com | [#23674](https://git.campmon.com/Freshview/createsend.com/pull/23674) | — | APPROVED | ZUSE-458: Routing and feature flag for AICampaignAgentV2 |
| 2026-06-25 | createsend.com | [#23685](https://git.campmon.com/Freshview/createsend.com/pull/23685) | [AJ-1151](https://campaignmonitor.atlassian.net/browse/AJ-1151) | APPROVED,CHANGES_REQUESTED,COMMENTED | AJ-1151: condition rule selection |
| 2026-06-29 | workflowbuildercontext.uiservice.core | [#334](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/334) | [JC-438](https://campaignmonitor.atlassian.net/browse/JC-438) | APPROVED | JC-438: fix(queue): remove dead replace path + dead urlAndRequests exports |
| 2026-06-29 | workflowbuildercontext.uiservice.core | [#335](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/335) | [JC-438](https://campaignmonitor.atlassian.net/browse/JC-438) | APPROVED | JC-438: fix(EditTextInline): remove dead validity gate |
| 2026-06-29 | createsend.com | [#23724](https://git.campmon.com/Freshview/createsend.com/pull/23724) | [AJ-1234](https://campaignmonitor.atlassian.net/browse/AJ-1234) | APPROVED | AJ-1234: complexsequencemailingsendservice DB shard configuration |
| 2026-06-30 | createsend.com | [#23750](https://git.campmon.com/Freshview/createsend.com/pull/23750) | [AJ-1171](https://campaignmonitor.atlassian.net/browse/AJ-1171) | APPROVED | AJ 1171 : Campaign siblings under conditions validation |
| 2026-07-01 | localdev-tools | [#77](https://git.campmon.com/Engineering/localdev-tools/pull/77) | — | APPROVED | NM-22 Add CmAPI.NetCore to local dev proxy |
| 2026-07-03 | createsend.com | [#23793](https://git.campmon.com/Freshview/createsend.com/pull/23793) | [AJ-1142](https://campaignmonitor.atlassian.net/browse/AJ-1142) | APPROVED | AJ-1142: Delete campaign from the complex series |
| 2026-07-07 | cmds | [#3106](https://git.campmon.com/CMDS/cmds/pull/3106) | — | APPROVED | fix(release): regenerate yarn.lock for newly-declared @cmds/* workspace deps |
| 2026-07-07 | contentbuildercontext.staticresourceservice.core | [#1230](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1230) | — | APPROVED | SHARE-5609: AI image generator — Report image + Rate this image |
| 2026-07-15 | createsend.com | [#23915](https://git.campmon.com/Freshview/createsend.com/pull/23915) | [AJ-1235](https://campaignmonitor.atlassian.net/browse/AJ-1235) | APPROVED | AJ-1235-b: Fix drip campaign icon rendering larger than single campaign icon |
| 2026-07-15 | createsend.com | [#23923](https://git.campmon.com/Freshview/createsend.com/pull/23923) | — | APPROVED | TUR-366 <5 check for lists overview blank state |
| 2026-07-17 | contentbuildercontext.staticresourceservice.core | [#1249](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1249) | — | APPROVED | SHARE-5708 Handle rate limit error types with correct UX copy |
| 2026-07-21 | createsend.com | [#23987](https://git.campmon.com/Freshview/createsend.com/pull/23987) | [AJ-1258](https://campaignmonitor.atlassian.net/browse/AJ-1258) | APPROVED | AJ-1258: Cancel downstream campaigns when a complex-sequence campaign fails to send |
| 2026-07-23 | createsend.com | [#24009](https://git.campmon.com/Freshview/createsend.com/pull/24009) | [AJ-1241](https://campaignmonitor.atlassian.net/browse/AJ-1241) | APPROVED,COMMENTED | AJ-1241-b |
| 2026-07-23 | createsend.com | [#24016](https://git.campmon.com/Freshview/createsend.com/pull/24016) | [AJ-1180](https://campaignmonitor.atlassian.net/browse/AJ-1180) | APPROVED | AJ-1180: drip campaign sending state styling updates |
| 2026-07-27 | createsend.com | [#24044](https://git.campmon.com/Freshview/createsend.com/pull/24044) | [AJ-1176](https://campaignmonitor.atlassian.net/browse/AJ-1176) | APPROVED | AJ-1176-fix - namespace please fix |
| 2026-08-06 | WorkflowEventCatalogIndexer | [#12](https://git.campmon.com/Engineering/WorkflowEventCatalogIndexer/pull/12) | [AJ-969](https://campaignmonitor.atlassian.net/browse/AJ-969) | APPROVED | AJ-969: Migrate WorkflowEventCatalogIndexer off Graylog to Datadog (jvm-libs 3.0.419) |
| 2026-08-06 | workflowcontext.updatecustomfield | [#72](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/72) | [AJ-965](https://campaignmonitor.atlassian.net/browse/AJ-965) | APPROVED,COMMENTED | AJ-965: Graylog migration: Verified parity + Drop GELF |
| 2026-08-20 | createsend.com | [#24308](https://git.campmon.com/Freshview/createsend.com/pull/24308) | [AJ-1294](https://campaignmonitor.atlassian.net/browse/AJ-1294) | APPROVED | AJ-1294: adding RssSchedulingDstFix FF |
| 2026-08-20 | createsend.com | [#24318](https://git.campmon.com/Freshview/createsend.com/pull/24318) | [AJ-1160](https://campaignmonitor.atlassian.net/browse/AJ-1160) | APPROVED,COMMENTED | AJ-1160: Sidebar for campaign |
| 2026-08-21 | chargebee-custom-codes | [#12](https://git.campmon.com/Engineering/chargebee-custom-codes/pull/12) | — | APPROVED | LSK-1414 retract add-ons pending cancellation from the list of pre-selected add-ons during upgrade |
| 2026-08-21 | createsend.com | [#24324](https://git.campmon.com/Freshview/createsend.com/pull/24324) | — | APPROVED | JS - Swap in Biome for ESLint |
| 2026-08-21 | createsend.com | [#24330](https://git.campmon.com/Freshview/createsend.com/pull/24330) | — | APPROVED | JS - Convert linting to Biome in App and Shared |
| 2026-08-24 | createsend.com | [#24346](https://git.campmon.com/Freshview/createsend.com/pull/24346) | — | APPROVED | JS - Fix a bunch of test warnings |
| 2026-08-24 | createsend.com | [#24351](https://git.campmon.com/Freshview/createsend.com/pull/24351) | — | APPROVED | JS - Update browserslist DB, core-js, and remove legacy polyfills |
| 2026-08-25 | createsend.com | [#24365](https://git.campmon.com/Freshview/createsend.com/pull/24365) | — | APPROVED | JS - Use Biome for formatting |
| 2026-08-26 | createsend.com | [#24385](https://git.campmon.com/Freshview/createsend.com/pull/24385) | [AJ-1163](https://campaignmonitor.atlassian.net/browse/AJ-1163) | APPROVED | AJ-1163: Update the warning banner for both basic and advanced drip campaign |
| 2026-08-26 | createsend.com | [#24396](https://git.campmon.com/Freshview/createsend.com/pull/24396) | — | APPROVED,CHANGES_REQUESTED | JS - Add Biome rule to order imports for srcfrontend |
| 2026-09-09 | SmsSendingServices | [#128](https://git.campmon.com/Engineering/SmsSendingServices/pull/128) | [COM-1635](https://campaignmonitor.atlassian.net/browse/COM-1635) | APPROVED | COM-1635 (2/4): Remove unused GELF appender dependency and dead Graylog logger overrides |
| 2026-09-09 | SmsSendingServices | [#133](https://git.campmon.com/Engineering/SmsSendingServices/pull/133) | [COM-1635](https://campaignmonitor.atlassian.net/browse/COM-1635) | APPROVED | COM-1635 (4/4): Retire the Graylog hostnames from Terraform |
| 2026-09-10 | localdev-tools | [#82](https://git.campmon.com/Engineering/localdev-tools/pull/82) | — | APPROVED | Regenerate proxy/yarn.lock with the cross-platform optional binaries |
| 2026-09-17 | localdev-tools | [#84](https://git.campmon.com/Engineering/localdev-tools/pull/84) | — | APPROVED | fix(proxy): support multi-tier environment hostdomains |
| 2026-09-25 | createsend.com | [#24815](https://git.campmon.com/Freshview/createsend.com/pull/24815) | [COM-1005](https://campaignmonitor.atlassian.net/browse/COM-1005) | APPROVED | COM-1005: Remove CustomFieldQueryService gRPC endpoint |
| 2026-09-30 | createsend.com | [#24871](https://git.campmon.com/Freshview/createsend.com/pull/24871) | [COM-452](https://campaignmonitor.atlassian.net/browse/COM-452) | APPROVED,CHANGES_REQUESTED,COMMENTED | COM-452-M: Display "Set by" name on the campaign report header behind a feature flag |
| 2026-09-30 | createsend.com | [#24890](https://git.campmon.com/Freshview/createsend.com/pull/24890) | [COM-1674](https://campaignmonitor.atlassian.net/browse/COM-1674) | APPROVED | COM-1674: Refactor the SMS credit usage CSV uploader |
| 2026-10-06 | createsend.com | [#24978](https://git.campmon.com/Freshview/createsend.com/pull/24978) | [COM-1649](https://campaignmonitor.atlassian.net/browse/COM-1649) | APPROVED | COM-1649 Add Twilio Compliance Embed |
| 2026-10-08 | createsend.com | [#25023](https://git.campmon.com/Freshview/createsend.com/pull/25023) | — | APPROVED | SHARE-6371: Show each Atlas run stage on the generating page |
| 2026-10-09 | GitHubTeamManagement | [#6](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/6) | [JC-436](https://campaignmonitor.atlassian.net/browse/JC-436) | COMMENTED | JC-436 Send logs to Datadog instead of Graylog |
| 2026-10-09 | GitHubTeamManagement | [#9](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/9) | — | APPROVED | SRE-3624: check out on server in TeamCity builds |
| 2026-10-09 | createsend.com | [#25035](https://git.campmon.com/Freshview/createsend.com/pull/25035) | — | APPROVED,COMMENTED | SHARE-6367: Wire up the Atlas review page |
| 2026-10-12 | createsend.com | [#25068](https://git.campmon.com/Freshview/createsend.com/pull/25068) | [COM-1708](https://campaignmonitor.atlassian.net/browse/COM-1708) | APPROVED | feat(COM-1708): add F_AccountClientFeatureBetaAccess table |
| 2026-10-13 | createsend.com | [#25086](https://git.campmon.com/Freshview/createsend.com/pull/25086) | [COM-1712](https://campaignmonitor.atlassian.net/browse/COM-1712) | APPROVED | feat(COM-1712): add admin and client user access columns to F_ClientFeatureControlState |
| 2026-10-13 | createsend.com | [#25098](https://git.campmon.com/Freshview/createsend.com/pull/25098) | [COM-1728](https://campaignmonitor.atlassian.net/browse/COM-1728) | APPROVED | COM-1728 Remove F_ClientFeatureBetaAccess data access code |
| 2026-10-15 | createsend.com | [#25133](https://git.campmon.com/Freshview/createsend.com/pull/25133) | — | APPROVED | fix(CmAPI.NetCore): lift System.Security.Cryptography.Pkcs to 10.0.13 |
| 2026-10-18 | createsend.com | [#25161](https://git.campmon.com/Freshview/createsend.com/pull/25161) | — | APPROVED | SHARE-6397: Let the user opt into the Atlas run's proposed sender name |
| 2026-10-30 | createsend.com | [#25405](https://git.campmon.com/Freshview/createsend.com/pull/25405) | [COM-1781](https://campaignmonitor.atlassian.net/browse/COM-1781) | APPROVED | COM-1781: Remove Live Content from the plan matrix |
| 2026-11-01 | createsend.com | [#25416](https://git.campmon.com/Freshview/createsend.com/pull/25416) | [COM-1767](https://campaignmonitor.atlassian.net/browse/COM-1767) | APPROVED | COM-1767 - Add a shared Brand Hub access service |
| 2026-11-02 | SegmentTrackingPlan | [#698](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/698) | [COM-1799](https://campaignmonitor.atlassian.net/browse/COM-1799) | APPROVED,COMMENTED | [COM-1799] Add Account Settings - Client Features page |
| 2026-11-02 | SegmentTrackingPlan | [#699](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/699) | — | APPROVED | Review skill: save report outside the repo and never commit it |
| 2026-11-02 | createsend.com | [#25442](https://git.campmon.com/Freshview/createsend.com/pull/25442) | [COM-1744](https://campaignmonitor.atlassian.net/browse/COM-1744) | APPROVED,COMMENTED | COM-1744: Basic Drip Campaign Sidebar — List name Linked |
| 2026-11-05 | createsend.com | [#25552](https://git.campmon.com/Freshview/createsend.com/pull/25552) | [COM-1771](https://campaignmonitor.atlassian.net/browse/COM-1771) | APPROVED | COM 1771: Basic Drip Campaign Creating a Tree view context menu for "Edit Campaign |
| 2026-11-09 | createsend.com | [#25582](https://git.campmon.com/Freshview/createsend.com/pull/25582) | [COM-1770](https://campaignmonitor.atlassian.net/browse/COM-1770) | APPROVED | COM-1770: Small UI/Copy Fixes for Basic Drip Campaign and Regular Campaign -> Checklist dialog copy |
| 2026-11-10 | createsend.com | [#25621](https://git.campmon.com/Freshview/createsend.com/pull/25621) | [COM-1804](https://campaignmonitor.atlassian.net/browse/COM-1804) | APPROVED | COM-1804-b: New Images for Client Features Tour |
