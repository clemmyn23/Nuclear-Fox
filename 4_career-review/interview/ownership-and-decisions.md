<!--
OWNERSHIP & DECISIONS: the direct answer to the 2026 interview feedback:
  (1) "can't see enough ownership of projects / owning decisions"
  (2) "leads with pet projects instead of the bread-and-butter feature work that sells a senior"
Built from Jun–Nov 2026 GitHub/Jira/Confluence/Slack evidence (data/2026-h2/) plus earlier years.
Teammates are named by role only.
-->

# Ownership & Decisions Playbook

## 0. What the feedback actually means

| What they said | What they heard in the room | Fix |
|---|---|---|
| "Strong technically" | Your design and coding rounds are at or above the bar. **This is solved, so stop proving it in behavioural rounds.** | Spend behavioural minutes on *decisions and outcomes*, not on how clever the implementation was. |
| "Lacking ownership / owning decisions" | Your stories said **"we"**, described **work you did**, and ended at **"it merged"**. They didn't hear *"I decided X over Y because Z, I was accountable for the result, and here's what happened."* | Every story names **the decision you made**, **the alternative you rejected**, **who you had to convince**, and **the outcome after launch**. |
| "Focuses on pet projects" | You led with build tooling, the webpack/Vite/TS upgrades and side quests, which read as *mid-level engineer with a hobby*. Seniors are hired to **ship the product that makes money** and take the team with them. | **Lead with customer-facing features you drove.** Tooling becomes a 15-second "and I also keep the platform healthy, e.g. a ~40% faster build" coda, never the headline. |

**The rule for every senior story:**
> *Business problem → my role, said plainly ("I was the technical lead for…") → the 1–2 decisions I owned → how I brought people along → measurable outcome → what I'd do differently.*

---

## 1. Your project portfolio, re-ranked for how it *sells*

| Tier | Project | Why it sells | Lead with it for |
|---|---|---|---|
| **1: Lead with** | **SMS Toll-free Compliance Embed** (Sep–Nov 2026) | You led the technical side of one of Product's *highest priorities*: you ran discovery, documented the rollout decision, designed the CmAPI/monolith architecture (on top of the shared-services team's Twilio integration), had your staffing proposal adopted, got another team's API changed, reached dev-complete, and got public PM credit. | "Project you led", "ambiguity", "cross-functional", "a decision you owned" |
| **1: Lead with** | **CRM Lite** (2025–26) | Feature tech lead with an LDR through architecture review, plus DBA and privacy negotiations. Already in your STAR bank. | "Most complex project", system design |
| **2: Strong support** | **Drip Campaigns builder + launch** (Apr–Oct 2026) | Shipped to **every plan**. You owned the customer-facing canvas and the go-live (dashboards, alerts, runbook). You made and defended a schema call. ⚠️ The team TL was credited for overall delivery, so say "I owned the builder and the launch readiness". | "Shipping at scale", "quality bar", "launch" |
| **2: Strong support** | **Brand Hub V2 "Correct the kit"** (Nov 2026, in flight) | Brand Hub's most common customer request (3 of 4 customers in research). You are the sole frontend owner. | "Customer focus", recent work |
| **3: Depth coda** | **Docker frontend builds (JC-411)** | Real cross-team leverage with a number: ~41% faster deploy package build (early). You can call it a project you initiated and staged safely. **This is the one they'll read as "pet project" if it leads.** | "Technical initiative", "improving dev productivity" (only when asked) |
| **3: Judgment stories** | **AI-DLC C# port, shelved**; **4 production incidents** | Show judgment, owning mistakes, and calm under pressure. | "Failure", "pressure", "AI usage", "disagreement" |
| **Don't claim** | Biome migration; the webpack 4→5 monolith build; "JS Crew lead" | Biome and the monolith webpack build were colleagues' work (you did webpack 5 part 2 and approved theirs). The crew never named a captain; you were interim meeting owner. | Never |

---

## 2. The decision log: 17 decisions you made or drove (Jun–Nov 2026)

> **Label them honestly in the room:** D1 was a team decision you documented and sharpened; D3 was your proposal, which the lead adopted; D10 was defending a planned change with evidence. That's still ownership. Just don't present any of them as a solo call.

Use these as ammunition. An interviewer who asks "tell me about a decision you made" wants **context → options → choice → why → outcome → reflection**.

### SMS Toll-free Compliance Embed
| # | Decision | Options | What you chose and why | Outcome | Reflection / "what I'd do differently" |
|---|---|---|---|---|---|
| D1 | **Rollout model** | Self-serve big-bang vs sales-led first | **Sales-led first** (team decision on 7 Sep, which you documented): self-serve needed SMS credits the billing system couldn't sell yet. You added the risk that a registration **can't be rolled back** once created at the provider, so the rollout must be **staged, not big-bang**. | The PM's proposal adopted it as Checkpoint 1; self-serve was pushed to early 2027 | "Start where a human can catch mistakes when the action is irreversible." |
| D2 | **Idempotency design** | Per-request dedupe vs a key derived from the client | **Derived from the client**, so retries and double submits converge, and a second number is never bought. | Written as an acceptance criterion, built and tested; integration tests never buy real numbers | "Put the invariant where the money is." |
| D3 | **Who builds what** | You do the full stack vs splitting frontend and backend | When the team lead put SMS and the AI experiment both on your plate, you **recommended you take the API integration and a teammate take the frontend**. | Lead: "a really thoughtful response… we'll go with what you've recommended!" Adopted into sprint must-dos. | You shaped the staffing with a clear proposal, and the lead adopted it. **Say this one out loud in interviews.** |
| D4 | **Fix another team's API** | Work around it vs push the owning team to change | You flagged a **"chicken-egg" problem**: a phone number was needed before the token, but the number needed details the form collects. You took it to the shared-services team. | They made the field optional and it was in staging the next day | Influence without authority, across team lines. |
| D5 | **Consolidate provisioning** | Add a third path vs merge the existing ones | **Merged 3 duplicate provisioning flows** (support tool, legacy self-serve, new embed) into one idempotent service. | One place to get side effects right; all 2,264 unit tests passing at merge | You left the codebase simpler than you found it while shipping a feature. |
| D6 | **Don't build the throwaway** | Build a status poller now vs wait for the provider's event stream | **Parked** status-sync until the event stream existed. | The ticket later closed as no work needed, so you saved building throwaway code | "The cheapest code is the code you correctly didn't write." |
| D7 | **Scope cuts** | Build resume/resubmit and status display as separate tickets | You found resume came **"for free"** from the provider and merged status display into another ticket. | 2 tickets cut | Active scope management, not just ticket execution. |
| D8 | **Honest estimate** | Accept the 5–8 day placeholder vs re-estimate | **Re-estimated at 7–11 days.** Later told the team "I might have underestimated the work" when you found reusable scaffolding that changed the plan. | You gave "~2 weeks left" on 1 Oct; endpoints were merged and in staging 20 Oct | Raise estimate changes early and plainly. *Be ready:* 7–11 dev-days became ~7 weeks elapsed (scope grew: AU sender IDs, partner API change; parallel AI-DLC work; leave). |
| D9 | **Surface the dead end** | Ship and move on vs raise the edge case | You flagged that a **hard-failed number leaves a customer stuck with no retry**, and proposed a support-escalation process plus the engineering decisions needed. | Logged before any real customer could hit it | Owning the customer's experience after the happy path. |

### Drip Campaigns
| # | Decision | What you chose and why | Outcome |
|---|---|---|---|
| D10 | **Schema: reuse `SendServiceType` or add `SendingAgentType`?** A reviewer asked "do we really need another column?" | The column was planned in the ticket; you **defended it with an audit**. The existing column is a claim-state flag that gets reset to 0, so reuse would clobber itself. Reuse meant ~20–30 files including hot send procedures, versus 7 additive files for a new column. After the DB reviewer's input it landed **non-null with the CHECK constraint dropped**, and the legacy cleanup was logged as separate debt ("I don't want to pick fight with roadmap deadlines"). | 3 approvals. That column marks every Advanced drip campaign, **so it can serve as your adoption counter.** |
| D11 | **Kill your own design** | You prototyped the "timeline gutter", then closed it: "too difficult to present multiple campaigns with different scheduled dates on the same X axis." | Changed course within a week, across three short-lived PRs |
| D12 | **Own go-live** | You delivered the launch-readiness ticket (dashboard, alerts channel, runbook) and added the flag and DB release order for the PM. You told SRE it was live. | The all-plans launch post linked your runbook; the outgoing TL called it "the best playbook… use it as the template" |
| D13 | **Contain scope on a high-traffic page** | You fixed thumbnails in drip, but deliberately didn't touch the high-traffic client overview without React Query in place ("I'll make a separate card"). | Risk contained; follow-up ticketed |

### Platform / judgment
| # | Decision | What you chose and why | Outcome |
|---|---|---|---|
| D14 | **Call time on the AI loop** | During the AI-DLC port you said the AI had been "going back and forth… for the past 2.5 business days… gone a bit pass the whole 'use ai to save time' threshold". You recommended human review and a staging deploy before any merge. | The lead called it "such a great call out". The experiment (307/307 unit tests, 72/72 parity tests) became the evidence for leadership's no-go: about 16k lines to replace about 8k. |
| D15 | **Staged infrastructure change** | For Docker builds, you started small ("let's start small and verify my little pet project works first"), quantified the risk, and designed a per-chain flag rollout (Canary → Hotfix → Deploy) with a disaster-recovery section (in review). You rejected agent-side checkout because of about 700 CRLF diffs. | Docker package build is about 41% faster at first measure. You also caused one CI break: "I didn't think it would affect everything, my bad", fixed quickly. |
| D16 | **Don't touch prod tired** | During late-night UCF dead-letter-queue triage you offered 3 options and asked for a 👍 before acting: "It's a bit late and I'm too tired to be touching prod." | The root cause was another team's change. Your patch fixed 6 of the 8 failing cases. Lead: "I can't express how great what you've done here is!" |

| D17 | **Pause a customer's live automation** | On the RSS incident you paused the UK publisher's automation rather than let it keep sending broken emails, then wrote the explanation Support sent them. | Verified good send 6 days later; customer: "Thanks for spotting the issues and letting me know" |

### 2b. Third-party evidence: other people already treat you as the owner
The feedback was that interviewers didn't *hear* ownership. These are other people saying it, which lands harder than you saying it. Source: `data/2026-h2/findings-slack-clem-sweep.md`.

| Who (role) | What they said or asked | Use it for |
|---|---|---|
| Boole TL | On a customer's CRM Lite question: *"I think clem implemented that work, we can have a chat with him"* | "Feature you owned" (CRM Lite) |
| Partner-team engineer | Tracing the SMS embed in code: *"Looks like Clem did this work"* | Story 13 |
| Senior C# engineer | Asked your OK before routing the SMS endpoint 100% to netcore in prod, and before deleting the legacy route | "Owner of the API" |
| Peer engineer | Asked you to confirm it was safe to raise drip's node limit from 30 to 60 | "Owner of the builder" |
| Team lead + EM | Drip GA: *"the real heroes behind this… Thank you Clem, Fan and Chris"* / *"huge props"* | Story 16 |
| Peer engineer | *"May need Clem to review this"* (microservices architecture diagram) | "Go-to reviewer" |
| Senior C# engineer | In the 6 Nov CI break: *"Clem is looking into it"* | Owning your own mess (story 20) |
| People Team | Invited you personally to the mentorship program, as mentee *or mentor* | Growth / "how do others see you" |

**How to use it:** one line per answer, never a list. *"When a customer question came in about that data, the lead's reply was 'Clem implemented that, let's ask him'. That's the kind of ownership I want to keep doing."*

---

## 3. Scripted answers for the questions that lost you points

### "Tell me about a project you led end-to-end." (2–3 min, SMS)
> **Problem:** "Getting a customer onto SMS was a manual process. They filled in a form, then support provisioned them by hand in an admin tool, and only one person on the team had ever done it. Product wanted Sales to be able to sell SMS as a feature, and it was one of their highest priorities."
>
> **My role:** "My manager asked me to own discovery, and I ended up leading the technical side of the build. I evaluated Twilio's embeddable compliance flow, wrote the technical breakdown the PM built the rollout plan from, and turned it into 11 tickets with estimates."
>
> **Decisions:** "Two calls mattered most. First, the rollout. The team agreed on sales-led before self-serve, since billing couldn't sell SMS credits yet. I documented it and added the risk that a carrier registration can't be rolled back, so we'd stage it with a human in the loop rather than go big-bang. Second, I made the provisioning API idempotent per customer, so a retry or a double click can never buy a second phone number. I also recommended splitting the work so I owned the backend integration and a teammate owned the frontend, and my lead went with that. Midway I found a chicken-and-egg flaw in the shared-services team's API, and they changed it the next day."
>
> **Outcome:** "We went from discovery on 1 September to dev-complete in early November, with US/Canada toll-free and Australian sender IDs, and cleared to start testing with real customers in early November. Along the way I merged three duplicate provisioning paths into one. ⟨Insert: customers onboarded / turnaround before vs after, from the impact playbook⟩. It's the foundation for migrating ~250 customers off our legacy SMS provider."
>
> **Reflection:** "I'd have pushed harder for the provider's status-event stream on day one. Parking our own status sync was right, but it left our status updates depending on another team's timeline."

### "Tell me about a decision you made that others disagreed with." (D10)
> "On Drip Campaigns, a senior reviewer challenged me on adding a new database column when one already existed. I didn't argue from opinion. I audited it. The existing column gets reset to zero as a claim flag, so reusing it would clobber itself, and the reuse path touched 20–30 files, including the hottest send procedures, against 7 additive files. I posted that, proposed the cleanup as separate tech debt, and we went with the new column. That column now marks every Advanced drip campaign, so it doubles as our adoption counter."

### "Tell me about a time you were wrong." (D15 or D8)
> "I rolled out a build-config change for our frontend Docker migration that I thought was scoped to one pipeline, and it broke builds across several projects. I posted 'my bad' in the channel, fixed it quickly by scoping it properly, then designed the per-pipeline flag and rollback plan for the remaining stages, which I should have had from the start."

### "How do you decide what to work on?" (the pet-project trap; answer it head-on)
> "Customer and business priority first. This year that was SMS onboarding and Drip Campaigns, both roadmap features that customers and Sales were asking for. I do invest in platform work, but only when it has a number attached and doesn't compete with the roadmap. For example, our frontend builds ran on hand-maintained agents, so every toolchain upgrade was an infra ticket. I've been moving them to Docker in the gaps, and the first stage made the deploy package build about 40% faster. If it ever competes with a customer feature, the feature wins."

### "How do you know your work had impact?"
> Use `interview/impact-metrics-playbook.md`: one adoption number, one cost or time number, one quality number (incidents/regressions ≈ 0).

---

## 4. Next 6 months: work that closes the gap (pick 2, not 4)

The fastest way to fix the feedback is to **have** the stories, not just tell old ones better. These are aimed at Nov 2026 → May 2027.

| Priority | Initiative | Why it fixes the gap | How you'll measure it | First step this week |
|---|---|---|---|---|
| ⭐ 1 | **Ask to be the named tech lead for SMS Checkpoints 2–3** (UK/AU sender IDs, **Infobip → Twilio migration for ~250 customers**) | Turns "de-facto lead" into a **title on a revenue-adjacent migration** you can describe as "I led". | Customers migrated / 250; legacy provider retired; manual provisioning requests at 0; registration rejection rate | Tell your EM: "I'd like to own SMS through migration as tech lead. Here's a one-page plan." |
| ⭐ 2 | **"Drip Campaigns: 90 days later" impact readout** | Senior ICs own outcomes after launch. Pull adoption (your `SendingAgentType` column + Amplitude), write a one-page readout with the PM, and propose which of the ~22 orphaned fast-follow tickets (e.g. segments as root recipient) to fund. | Accounts using drip; drip sends; incidents; the follow-up the PM funds | Run the adoption query; book 30 min with the PM |
| 3 | **Ship Brand Hub 1A and measure it** | Recent, customer-requested, end-to-end. | % of kits edited; colour-correction support requests falling | Agree the success metric with the PM *before* launch and put it in the epic |
| 4 | **Finish JC-411 with a before/after dashboard** (time-box: **no more than 20% of your time**) | Converts the "pet project" into a cross-team win with a number. | PR push → green time; agent-hours/yr; package build median | Flip canary; re-pull TeamCity stats in 3 weeks |
| Bonus | **Fill the Journeys TL gap** | The handover doc says *"There is no named successor tech lead"* for Journeys, and you're named as a key knowledge holder. An org with a named gap is an invitation. | — | Raise it with your EM alongside #1 |

**Rule of thumb:** for every hour of platform/tooling work, there should be roughly four hours on roadmap features you can name a customer for.

---

## 5. Language upgrades (say this, not that)

| ❌ Undersells | ✅ Senior |
|---|---|
| "I worked on the SMS embed." | "I led the technical side of SMS onboarding." |
| "We decided to go sales-led." | "I documented the sales-led-first plan and made sure we staged it, because the registration's irreversible." |
| "I built some endpoints." | "I designed the provisioning API so a retry can never buy a second number." |
| "I helped with the launch." | "I owned go-live: dashboards, alerts, runbook. I told SRE when it was live." |
| "I upgraded the build to Docker." | "I cut the deploy package build by ~40%, and I'm making toolchain upgrades a code change instead of an infra ticket." |
| "The PR got merged." | "It's been live since October on every plan, and ⟨N⟩ accounts use it." |
| "It was a team effort." | "The team built it; my piece was X, and the call I made was Y." (Credit others *and* claim your part.) |
