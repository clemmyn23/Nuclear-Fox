<!--
STAR INTERVIEW STORY BANK — behavioral + technical stories built ONLY from documented real events
(career-review dataset: PRs, the CRM-Lite LDR, Slack threads, SMASH résumé record).
Where a hard metric would strengthen the "Result" but isn't in the data, it's marked ⟨INSERT METRIC⟩ for you to fill from memory.
Rehearse out loud; trim each to ~2 min spoken.
-->

# STAR Interview Story Bank

**25 stories** (12 from May 2026, plus 13 new from Jun–Nov 2026, numbered 13–25), each tagged with the behavioural questions it answers. STAR = Situation · Task · Action · Result. All are drawn from real events in your record.

> **2026-11 update: lead with the new stories.** Interview feedback said your technical rounds land but your stories under-sell **ownership and decisions**, and lean on side projects. Stories **13, 16, 17 and 1** are now your default "project you led" set. Use **21** (Docker builds) only when asked about developer productivity. Every new story ends with a **Decision** line and a **Reflection** line, because that's what final rounds probe. Companion docs: [ownership-and-decisions.md](ownership-and-decisions.md) (decision log, scripted answers) and [impact-metrics-playbook.md](impact-metrics-playbook.md) (how to get the ⟨numbers⟩).

---

# NEW — Jun–Nov 2026

## 13. ⭐ Leading a top-priority feature from blank page to launch: **SMS onboarding (Twilio compliance embed)**
*Answers: "project you led end-to-end" · "ambiguity" · "cross-functional" · "biggest impact" · "a decision you owned"*
- **S:** SMS onboarding was manual. Customers filled in a form, then support provisioned them by hand in an admin tool, and only one person had ever done it. Product wanted Sales to be able to sell SMS as a feature, and called it *"one of Product's highest priorities."* Our team had just merged, our tech lead had left, and Twilio was tightening toll-free compliance.
- **T:** My EM asked me to own discovery. That grew into leading the technical side of the build.
- **A:**
  - Evaluated Twilio's embeddable compliance flow and wrote the technical audit and breakdown. The PM built the rollout plan from it and credited it.
  - Documented the team's **sales-led-first** decision (billing couldn't sell SMS credits yet) and flagged that registrations can't be rolled back, so the rollout had to be staged.
  - Re-estimated 7–11 days against a 5–8 day placeholder and split the work into 11 tickets.
  - Recommended the staffing split (me on the API integration, a teammate on the frontend). My lead adopted it.
  - Designed an **idempotent provisioning API**: a client-derived request key, so retries never buy a second number; region checked before purchase.
  - Found a chicken-and-egg flaw in the partner team's API and got it changed the next day.
  - Merged three duplicate provisioning flows into one service.
  - Parked the status-sync work until the provider's event stream existed, and flagged the dead-end case where a number hard-fails.
- **R:** Dev-complete in about 2 months (US/CA toll-free, AU sender IDs). PM: *"in full glory! Great work Clem, Alexis!!"* Cleared to start testing with real customers on 5 Nov. ⟨INSERT: customers registered / turnaround before vs after⟩. It's the foundation for migrating ~250 customers off the legacy SMS provider (that migration is a later checkpoint, not part of this build). A partner-team engineer, tracing the flow in the code weeks later: *"Looks like Clem did this work."*
- **If they ask "did it slip?":** "Mid-October my EM flagged a lot of cards left and asked whether to add a second engineer. I split my in-flight PR so she could build on it the same week. We missed the 30 Oct target by a couple of days and were dev-complete on 2 Nov."
- **Decision to name:** staged rollout for an irreversible action, plus the idempotent API.
- **Reflection:** "I'd push for the provider's status events on day one. Parking our own poller was right, but it left a manual gap."

## 14. Shaping the plan with your manager: **the SMS staffing call**
*Answers: "disagreed with / influenced your manager" · "prioritisation" · "said no to something"*
- **S:** My lead put two big things on my plate at once: SMS provisioning (one of Product's highest priorities) and an AI-migration experiment.
- **T:** Make both succeed without becoming the bottleneck.
- **A:** Instead of saying yes to everything, I wrote back with a plan: I'd own the API integration with the shared-services team, the riskiest and most context-heavy part, and we'd bring a frontend engineer on to build the embed UI in parallel. I named what would block whom.
- **R:** *"Thank you for a really thoughtful response… we'll go with what you've recommended!"* It went straight into the sprint must-dos, and the frontend and backend ran in parallel.
- **Reflection:** "Owning a project includes owning how it's staffed. A clear proposal beats a silent overload."

## 15. Influence without authority across teams: **the "chicken-egg" API**
*Answers: "influence without authority" · "working with another team" · "unblocking"*
- **S:** The partner team's API needed a phone number before it could issue the embed token. But buying the number required details the embed form collects. As designed, the flow couldn't start.
- **T:** Get it fixed without owning that team's code.
- **A:** Wrote it up in their support channel as a concrete, minimal problem ("chicken-egg"), with the ordering laid out and the evidence attached.
- **R:** They agreed the same day, made the registration info optional, and had it in staging the next day. Our critical path was unblocked.
- **Reflection:** "Frame the other team's change as the smallest possible ask, with the evidence attached."

## 16. ⭐ Owning a launch, not just the code: **Drip Campaigns go-live**
*Answers: "shipped something at scale" · "what does done mean to you" · "quality" · "operational readiness"*
- **S:** Advanced Drip Campaigns (branching email sequences) was about to go to customers. I owned the builder frontend. The send engine was new, with an isolated agent and cohort evaluation, and the existing monitoring didn't cover it.
- **T:** Make sure we'd know if it broke, and what to do when it did.
- **A:** Delivered the launch-readiness ticket:
  - a Datadog dashboard and an alerts channel;
  - a runbook with 7 metrics and 7 anomaly scenarios, each with a remediation path;
  - a list of instrumentation gaps (e.g. no way to tell drip sends from regular ones, so I proposed a tag);
  - the flag and DB release order for the PM.

  I asked the TL and SRE for feedback, then posted to SRE myself: *"live on all prod DBs."* Earlier I had also self-created the final design-alignment card with the designer to drive UX polish before release.
- **R:** Live for Direct customers in July, **every plan in October**. The SRE launch post for the all-plans rollout linked my runbook. The outgoing TL: *"the best playbook in either space; use it as the template."* At GA my team lead posted *"These guys are the real heroes behind this… Thank you Clem, Fan and Chris,"* and the EM added *"huge props."* Support relayed a customer who was *"SO PUMPED about drip campaigns."* ⟨INSERT: accounts / campaigns since launch⟩
- **Be precise:** the TL led overall delivery. I owned the builder and the go-live.
- **Reflection:** "Done means someone else can operate it at 2am without me."

## 17. ⭐ Disagreeing with data: **the `SendingAgentType` schema decision**
*Answers: "disagreed with a senior colleague" · "technical judgment" · "trade-offs"*
- **S:** To stop drip campaigns blocking regular sends, we needed to route them to a dedicated agent. The plan was a new column. A senior reviewer asked: *"Do we really need another column? SendServiceType already exists."*
- **T:** Make the right call, not the comfortable one, without stalling the roadmap.
- **A:** Audited the existing column. It's a claim-state flag that gets reset to zero during sending, so reusing it would clobber itself. Reuse also meant ~20–30 files including the hottest send procedures, against 7 additive files for a new column. I posted the analysis, re-requested DB review (it landed non-null, with the CHECK constraint dropped, after the DB reviewer's input), and offered the legacy cleanup as **separate, logged debt** ("I don't want to pick fight with roadmap deadlines").
- **R:** Approved by three reviewers. That column now marks every Advanced drip campaign, so it can double as the adoption counter.
- **Reflection:** "Answer 'do we need this?' with a cost comparison, and give the purist option its own ticket instead of a veto."

## 18. An experiment whose best output was "no": **AI-driven Node→C# migration**
*Answers: "a project that didn't ship" · "how do you use AI" · "knowing when to stop" · "failure"*
- **S:** As part of an AWS AI-driven-development workshop, my stream was to port our AI brand-scraper service from Node to C# using an AI agent workflow.
- **T:** Complete the build phase and find out what this approach really costs.
- **A:** Drove it to 6 units with SSRF-hardened adapters, a gRPC surface and a C#-vs-Node parity harness: **307/307 unit and 72/72 parity tests** green. I also called out the uncomfortable part: the AI had been *"going back and forth… for the past 2.5 business days… gone a bit pass the whole 'use ai to save time' threshold."* I recommended human review and a staging deploy before anything merged.
- **R:** My lead called it *"such a great call out."* Leadership used the results to decide **not** to migrate: ~16k lines to replace ~8k, ~3× maintenance, loss of LLM observability, a data migration that couldn't be cleanly reversed, and a delay to customer-requested work. *"A worthwhile experiment… That's what made this decision possible."* I moved straight onto that customer work (Brand Hub editing).
- **Reflection:** "I'd set a kill criterion up front ('if the AI loops more than a day, stop and reassess') instead of noticing at day 2.5."

## 19. Cross-team incident without blame: **the UCF dead-letter queue**
*Answers: "debugged a hard production issue" · "it was someone else's fault" · "judgment under pressure"*
- **S:** Recurring alerts on a customer-data workflow service: the error queue climbed from 0–1 to 9 within days, across several customer accounts.
- **T:** Stop the bleeding safely, find the cause, and fix it properly.
- **A:** Decoded the queued protobuf messages and confirmed the operations were idempotent, so a redrive was safe. Reconstructed the cache keys and laid out three options. Late at night I asked for a 👍 before touching prod instead of acting alone: *"It's a bit late and I'm too tired to be touching prod."* Traced the regression to a change another team had shipped. Patched it, with 10 tests, and tagged that team in a factual, no-blame way. Raised follow-ups on the dead-letter semantics and the runbooks.
- **R:** The patch fixed 6 of the 8 failing cases. Lead: *"I can't express how great what you've done here is!"* The other team's engineer apologised for the miss.
- **Reflection:** "Know when you're too tired to touch prod, and say it out loud."

## 20. Owning your own mistake: **the cross-project CI break**
*Answers: "a mistake you made" · "accountability"*
- **S:** While rolling out the Docker build migration I shipped a TeamCity DSL change I believed was scoped to one pipeline chain.
- **A:** It broke builds across several projects. I posted *"I didn't think it would affect everything, my bad"* in the channel, scoped the change properly (`chain=pr`) and restored builds quickly. Then I designed a per-pipeline feature flag and disaster-recovery section for the next stage (in review), so the remaining rollout can't repeat it.
- **R:** **60 check runs on 8 PRs failed over 47 minutes** (6 Nov, 12:39–13:26 AEDT, all from one merge commit; TeamCity: `Unknown DSL context parameter chain`). The same day, the new checks became the only frontend PR checks. The remaining rollout is planned Canary → Hotfix → Deploy, each behind its own switch.
- **Reflection:** "For shared infra, the blast radius is the first thing to test, not the last."

## 21. Developer productivity with a number: **Docker frontend builds**
*Answers: "improved developer experience" · "technical initiative you started" · use only when asked; don't lead with it*
- **S:** The frontend toolchain was baked into hand-maintained Windows build agents, so every Node/TypeScript upgrade was an infra ticket. Every PR push spent 18.5 agent-minutes across five checks, and over half of that was checkout and `npm install` repeated five times.
- **A:**
  - Created the epic and scoped 24 tickets with benchmarks: webpack warm cache 62.5→3.5 s, Closure→esbuild 13.7→0.35 s, TS7 tsc 4.8→0.46 s.
  - Containerised the build with byte-level parity checks across 6,106 files. Found the Closure compiler was printing errors but exiting 0, so incomplete bundles could ship.
  - Ran the Docker and Windows checks side by side on the same PRs for six days, then switched (6 Nov). Staged the deploy package per pipeline with a rollback plan.
- **R:**
  - **69% less compute per PR push** (1,109 s → 348 s, faster on 233 of 233 commits); checks 1.8–8.5× faster; ~72% fewer agent-hours (~4,850 h/yr). Deploy package 41% faster in shadow.
  - Then I measured what developers actually wait for. It hadn't improved: the shared Docker pool had filled with other teams' workloads, and my checks were 4–8% of it. With no queue, feedback is 44% faster, so the remaining fix is pool capacity.
- **Decision:** a parallel shadow run instead of a cut-over, because it gave a same-commit comparison and a free rollback.
- **Reflection:** "Measure the outcome the user feels, not the metric you optimised."
- **Framing:** "I do this in the gaps between roadmap work, and only with a number attached." Full numbers: [portfolio/docker-frontend-builds-results-2026-11.md](../portfolio/docker-frontend-builds-results-2026-11.md).

## 22. Stepping up when the org changed: **team merge + tech-lead departure**
*Answers: "dealing with change" · "ambiguity" · "leadership without the title"*
- **S:** In late August our tech lead left with *"no named successor."* Days later our team merged with another, and two more engineers left. The handover named me as the knowledge holder for the Journey Designer.
- **A:** Posted the team-merge redirect so internal queries reached the new team. Kept monitoring duty and the workflow incident load. Took the new team's top-priority project within days (story 13). In the JavaScript Crew I raised the question of crew direction and leadership in July (no one volunteered as captain), became the interim meeting owner after the crew lead left, opened the recordings to the whole org, then handed it over.
- **R:** Within days, the merged team handed me its top-priority project (story 13).
- **Reflection:** "When there's a leadership gap, act like the lead on the work in front of you, then ask for the title explicitly." (See ownership-and-decisions.md §4.)

## 23. ⭐ A customer-facing incident, end to end: **the broken RSS campaign**
*Answers: "customer obsession" · "debugged under pressure" · "went beyond the code" · "time you owned an outcome"*
- **S:** A UK publisher's automated RSS campaign was sending broken emails intermittently, and a Datadog alert fired. My team lead assigned it: *"blacksmith is looking into this first."*
- **T:** Find out why, stop the damage, and get the customer sending correctly again.
- **A:** Found the root cause in about 80 minutes. Their template nested dynamic-content tags in two layouts, which is why it only broke on some items, and their feed itself was invalid (a duplicated namespace). I **paused the automation** so it couldn't keep sending broken emails, and drafted a customer-ready explanation of both problems for Support. Then I checked previews the next day and confirmed the next scheduled send went out correctly.
- **R:** Six days from alert to a verified good send. The customer, via Support: *"Thanks for spotting the issues and letting me know, both issues should be fixed now."*
- **Decision to name:** pausing a customer's live automation. It's their campaign, but continuing to send broken emails to their subscribers was worse.
- **Reflection:** "The fix was on the customer's side, so the job wasn't 'find the bug'. It was making sure they understood it well enough to fix it, then checking that they had."

## 24. A review I got wrong: **the webpack 5 approval**
*Answers: "a mistake you made" · "what you learned" · "how you review code" · "quality bar"*
- **S:** A colleague's PR moved the monolith build from webpack 4 to 5. I'd reviewed and tested it and was the only approver.
- **A/what happened:** It went out on 3 Jul with a missing import that broke RSS one-click campaigns. Support cases came in, and SRE and others fixed it that night. There was no blame in the thread, but I'd signed off.
- **What I changed:** ⟨Say this only if it's true for you⟩ For build and toolchain changes I now review *what the bundle actually contains*, not only the diff. On the Docker migration I compared the output byte for byte across 6,106 files before switching anything (story 21), and that's what caught a compiler that printed errors but exited successfully.
- **Reflection:** "A green build and a readable diff aren't evidence for a bundler change. The output is the evidence."
- *Use it instead of, or as well as, story 20 when they want a mistake with a lasting process change. Don't present webpack 5 as your migration: you did part 2, the colleague did the monolith build.*

## 25. Raising a risk so precisely someone else can act in minutes: **Pkcs CVE + TeamCity audit**
*Answers: "proactive" · "security" · "making others effective" · short story, good for "anything else?"*
- **Pkcs:** Flagged a high-severity advisory in the C# channel with the exact dependency path (MimeKit 4.15.1 → Pkcs 8.0.1/10.0.0), the patched versions and a local build showing the failure before CI did. A senior engineer had the fix PR up **29 minutes** later.
- **TeamCity audit:** Before adding new frontend pipelines, audited the existing ones: 8 dormant projects (one last built in 2016) and 5 stale configs. DevOps verified it, wrote it up and approved: *"these are all good to go… Thanks blacksmith."*
- **Reflection:** "If you hand someone the full diagnosis, the fix is their easy part."

---

# ORIGINAL — 2021–May 2026

## 1. Leading a feature end-to-end through ambiguity — **CRM Lite**
*Answers: "Tell me about a complex project you led" · "owning ambiguity" · "cross-functional"*
- **S:** CRM Lite needed every subscriber across a client's many lists aggregated into one "single customer view." No existing pattern at the company for backfilling and de-duplicating contacts at that scale; it touched billing, GDPR, and the contact pipeline.
- **T:** As feature tech lead, design it so it was safe, scalable, and shippable — and get the org's specialists to agree.
- **A:** Wrote a Lightweight Design Review and took it through architecture review. Brokered the schema with a DBA (landed an `IsMasterList` flag instead of widening a hot table), negotiated GDPR-delete handling with the platform team, and designed a paged SQS→Kafka backfill pipeline (1,000 records/page) that dedupes by email through the existing contact pipeline. Shipped a pragmatic first iteration (a deliberate flag hack) to hit the deadline, with the clean column carried forward.
- **R:** Delivered to production; I owned the prod-enablement rollout. ⟨INSERT METRIC: client list sizes / contacts processed / rollout outcome⟩
- **Why it lands:** shows design-doc leadership + cross-functional negotiation + pragmatic shipping.

## 2. Persistence on a hard migration — **WorkflowLookupService**
*Answers: "a time you failed / hit setbacks" · "resilience" · "hardest technical problem"*
- **S:** A workflow-lookup service had to move out of a 15-year-old .NET-Framework monolith into a standalone .NET Core gRPC service.
- **T:** Land it without breaking production journey behaviour.
- **A:** First attempt revealed problems under production load → reverted. Second attempt → reverted again. Re-diagnosed each failure, adjusted the approach, and landed it on the third attempt.
- **R:** Migration shipped and held. ⟨INSERT METRIC: what the reverts taught you / latency or reliability after⟩
- **Why it lands:** most candidates hide reverts; owning a 3-try landing is a maturity signal. Emphasise *what you changed between attempts*.

## 3. Disagreeing well on a design — **distributed-work completion detection**
*Answers: "disagreed with a senior person / decision" · "technical judgment"*
- **S:** A senior colleague proposed detecting "is the backfill job done?" by polling the DB on a schedule.
- **T:** I had reservations but it was a reasonable option.
- **A:** Laid out my view in the team channel: stated I disliked scheduled DB-polling, acknowledged it would work, noted it'd be the first time we'd solved "mark a distributed job of non-fixed size as done" at the company, compared it to CSV import (known size) vs our case (list size changes mid-job), and recommended adding a status index if we went that way — then deferred the call to standup.
- **R:** Resolved into a documented design (new job-status lifecycle with a `Finalising` state + DLQ handling).
- **Why it lands:** disagreement expressed as options + tradeoffs, not ego; defers decision appropriately.

## 4. Founding engineer → org leader — **SMASH! 5 → 25**
*Answers: "leadership" · "building a team" · "the thing you're most proud of" · "took something from zero"*
- **S:** I was one of **five founding engineers** for SMASH's technology in 2018 — we built the convention's systems from scratch as it grew toward 45,000+ attendees.
- **T:** First build something that worked at event scale; then build the *organisation* that could run it reliably year after year.
- **A:** Designed and built the integrated **ticketing + mobile-scanning system** (40,000+ attendees/vendors) as a hands-on engineer, then over the next 7 years moved into leadership — planning/delegating/reviewing, growing the team from 5 to **25 across Engineering/Systems/Support with 3 leads**, and stepping up to Director setting Board-level IT strategy and a multi-year roadmap.
- **R:** **5 consecutive conventions with zero critical IT failures** for 45,000+ attendees — on systems I helped originate.
- **Why it lands:** the full arc — built it *and* scaled the org that runs it. Real people-leadership scope with a hard reliability outcome and a from-scratch origin; rare for an IC candidate.

## 5. Operating under pressure — **live event incident response**
*Answers: "high-pressure situation" · "incident / on-call"*
- **S:** On-site IT for a 45,000-attendee convention — ticketing, access control, networking — where failures are immediate and public.
- **T:** Keep critical systems up under peak load with no second chances.
- **A:** Owned on-site setup and live operations; built incident-response capacity into a volunteer team.
- **R:** Zero critical IT failures across five consecutive events. ⟨INSERT METRIC: a specific incident you caught/averted, if you have one⟩
- **Why it lands:** pairs naturally with story #4; this is the "calm under fire" version.

## 6. Production debugging under time pressure — **the Glidewell P2** (CM)
*Answers: "debugged a tricky production issue" · "ownership outside your area"*
- **S:** A client was firing ~800 API requests/minute updating a single subscriber tied to 10 active journeys, creating a huge backlog and badly delayed journey activity.
- **T:** Diagnose and contain a P2 late at night.
- **A:** Worked the incident with a colleague from ~11pm, traced the cause to the abnormal request pattern + the journey-trigger backlog, and helped frame the fix.
- **R:** Incident understood and written up as a postmortem. ⟨INSERT METRIC: time-to-mitigate / resolution⟩
- **Why it lands:** systematic isolation + willingness to own an incident off-hours.

## 7. Raising the engineering bar — **JS Crew standards intervention**
*Answers: "improved code quality / process" · "influence without authority"*
- **S:** A team was merging PRs that added unnecessary abstractions (extra context providers, mocked data left in) — some merged before crew approval.
- **T:** Stop quality drift across a shared front-end codebase.
- **A:** As a JavaScript Crew member I took ownership of the cleanup, escalated the pattern to the right lead, and reinforced the review expectation — while maintaining shared libraries and build standards org-wide.
- **R:** Pattern addressed; standards reasserted. ⟨INSERT METRIC: e.g. crew guideline doc created⟩
- **Why it lands:** influence across teams you don't manage.

## 8. Multi-repo, contract-first delivery — **permission-checking change**
*Answers: "complex system change" · "attention to detail / coordination"*
- **S:** A permission-check feature for copying email templates needed to be consistent across the monolith and several services.
- **T:** Land it coherently without partial/broken states.
- **A:** Coordinated a single change set across 3–4 repositories (monolith + service + datastores + schema), designing the contract first and threading it through each layer.
- **R:** Shipped consistently across all components. Later wrote the system walkthrough doc that now onboards engineers to that service.
- **Why it lands:** shows you think in systems, not files; bonus that the artifact became team documentation.

## 9. Greenfield from zero — **Bloom Bootstrap prototype** (CM)
*Answers: "started something from scratch" · "wore many hats"*
- **S:** A new product prototype needed to exist from nothing.
- **T:** Stand up the foundations fast.
- **A:** Set up the project end-to-end in ~two weeks — docker compose with watch mode, AWS Cognito auth (server + client), change-password flow, DevX — and acted as tech-lead reviewer for others contributing.
- **R:** Working prototype + DevX the team built on. (Be ready to note the product later pivoted — greenfield work isn't wasted when the patterns carry.)
- **Why it lands:** range + speed + setting patterns others follow.

## 10. Mentoring / growing others — **coaching juniors** (CM)
*Answers: "mentored someone" · "helped a struggling teammate"*
- **S:** Junior engineers on the tribe were ramping on CRM Lite work.
- **T:** Unblock them without just taking over.
- **A:** Coached through design tradeoffs in review and DM — e.g. catching a faulty assumption in a subscriber-count query while affirming the QA instinct behind it ("that's a good QA mindset"); guided an endpoint-contract decision by laying out two options and letting them choose.
- **R:** They shipped their pieces; learned the reasoning, not just the answer.
- **Why it lands:** mentoring as teaching judgment, not correcting code.

## 11. Bar-raising in hiring — **technical screening** (CM)
*Answers: "raised the bar / hiring" · "tough judgment call"*
- **S:** Asked to screen a mid-level engineering candidate's take-home.
- **T:** Make an honest level call.
- **A:** Reviewed the code against the spec, flagged concrete issues (unused variables, a solution not to spec, missing rigor), and recommended a no-hire-at-mid with specific reasoning rather than a vibe.
- **R:** Clear, defensible recommendation the hiring manager could act on.
- **Why it lands:** shows you can evaluate others' work to a standard — a lead/Staff signal.

## 12. Responsibility above title — **WiseTech AIS system**
*Answers: "took on more than your role" · "earliest big responsibility"*
- **S:** Titled "Associate Software Developer," ~1 year into my career.
- **T:** A real-time ship-tracking system served to all CargoWise customers needed an owner.
- **A:** Took sole ownership of it (React/TS/Google Maps) and the MAWB air-cargo automation alongside.
- **R:** Delivered and maintained real-time cargo visibility for the entire customer base.
- **Why it lands:** establishes a decade-long pattern of responsibility outrunning title (and quietly frames your current under-levelling as the org's gap, not yours).

---

## Coverage map — which story for which prompt
| Prompt theme | Best stories (lead with the first one listed) |
|---|---|
| **Project you led end-to-end** | **13**, 1, 16 |
| **A decision you owned** | **13** (sales-led rollout), **17**, 14 |
| Ambiguity & ownership | **13**, 22, 1, 9, 12 |
| Conflict / disagreement | **17**, 14, 3, 11 |
| Influencing your manager / prioritisation | **14** |
| Influence without authority | **15**, 7, 10 |
| Cross-functional | **13**, 15, 1, 8 |
| Shipping / launch / quality bar | **16**, 13, 24 |
| Failure / mistake | **24**, 20, 18, 2 |
| Project that didn't ship / knowing when to stop | **18** |
| AI usage & judgment | **18**, (13: AI-assisted delivery) |
| Debugging / incident / pressure | **23**, 19, 5, 6 |
| Customer obsession | **23**, 13 |
| Proactive / security | **25** |
| Technical depth / hardest problem | 13, 1, 2, 21 |
| Developer productivity / tooling | **21** (only if asked) |
| Leadership / building teams | 4, 22, 5, 11 |
| Dealing with change / reorg | **22** |
| Mentoring | 10, 11 (+ junior coaching in 2026: test structure, BEM, review etiquette) |
| "Most proud of" | **13**, 4, 1 |

## Delivery tips
- Lead with the **S/T in one sentence**; spend most of the time on **A**; end on a crisp **R**.
- Fill every ⟨INSERT METRIC⟩ with a number you actually remember — a real "rough" number beats a vague claim, and never invent one you can't defend.
- **2026-11:** stories **13, 16, 17** (plus 1) are your strongest for senior/Staff loops; **14, 15, 22** for leadership/influence; 4–5 for any EM loop. Keep 21 in your pocket.
- End every story with the **decision** you made and one sentence of **reflection**. That's the ownership signal the feedback said was missing.
