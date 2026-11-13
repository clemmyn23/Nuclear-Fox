# Slack — architecture and planning discussions

Mined from the **campaignmonitor.slack.com** workspace for substantive engineering conversations Clement Ng (`@blacksmith`, user_id `U01SKCA6MHC`, email `cng@campaignmonitor.com`) initiated or significantly drove. These complement the PR/comment records by showing the **planning, design, and technical-decision work that happened in chat** rather than in code.

The search was scoped to messages by Clement using phrases that surface engineering writing (`RFC`, `proposal`, `we should`, `architecture`, `design`, `approach`, `investigate`). What follows is a curated selection of the conversations that show senior-IC engineering judgment.

## Top channels mined

| Channel | Engagement type | Notes |
|---|---|---|
| `#cm-team-boole-dev` | Daily squad engineering channel | Where most CRM Lite / Campaign Series / Workflow technical-decision threads happened |
| `#cm-team-boole-eng-prod` | Squad production-issues channel | Incident response, follow-ups, ownership clarifications |
| `#cm-team-boole` | Wider Boole tribe | Cross-squad pings; "you have most context in this area" lookups |
| `#js-crew-members` | JS-crew internal | Frontend architecture, code-quality interventions, tooling migrations |
| `#boole-ai-log` | Innovation Sprint AI work log | Documented his own AI tool usage during the May 2026 Innovation Sprint |
| `#dev-recruitment` | Engineering hiring | Technical screening of mid-level engineering candidates |
| `#html-css`, `#cm-product-design` | Cross-team design coordination | Pointed teammates to the right forums for UX/design questions |
| DMs with DBAs and a platform engineer | Pre-design DBA negotiation | Where CRM-Lite schema decisions were brokered before LDR write-up |
| DMs with the squad product lead | Product-eng coordination | Feature scoping, designer reviews, sprint planning |
| DMs with peers and junior engineers | Per-PR / per-design pairings | One-to-one technical reviews and pair sessions |

## Discussions by theme

### 1. Architecture / design decisions

#### **CRM-Lite database schema negotiation with DBA** *(2025-11-14, DM with a DBA)*
Initiated by Clement during pre-LDR investigation. Proposed a new nullable `CrmListID` foreign key column on `CL_Clients`. The DBA objected — argued a flag on `SU_Lists` was preferable to widening an already-wide table. Clement listened, then negotiated to an `IsMasterList` column on `SU_Lists`. Showed willingness to:

> "we decided to go with a hack for the first iteration - so rather than having a `isCrmList` column on the lists table, we are just gonna set the crm list to `isDeleted=1 isVisible=0` to get something out in 2 weeks"
> "we can still add in the `isCrmList` column into the list table, but that list will still have the `isDeleted=1 isVisible=0` flags checked as a start"

Outcome: agreed `IsMasterList` on `SU_Lists` + ship the hack to meet the deadline, then layer the proper column later. This is the textbook pragmatic-senior-IC move — get clean architecture *and* hit the deadline by carrying both forward. [Permalink](https://campaignmonitor.slack.com/archives/D03V82VP47R/p1763094094937379)

#### **GDPR delete race condition during CRM-Lite init** *(2026-01-20, DM with a platform engineer)*
Identified a race condition between GDPR deletes and the CRM-Lite list-population job. Floated a specific design option (modify the "check for subs deactivator status" step in the AWS Step Function to also query the monolith `CL_ClientCRM` table) and explicitly asked whether it was OK from an architecture stand point. The platform engineer redirected to a Zoom: "GDPR is a bit more complicated than you think ;)". Clement absorbed the complexity, then later updated the published LDR with the resolved approach. [Permalink](https://campaignmonitor.slack.com/archives/D03LTAWLFL2/p1768884819587579)

#### **Distributed-work completion detection — design debate** *(2026-02-18, #cm-team-boole-dev)*
After a teammate suggested a polling-based completion detector, Clement weighed in publicly:

> "Yes it can work. I personally don't like the idea of polling db tables on a schedule to do work. We should add index to the status column if we go with this solution. Performance - probably the same for both implementations. Easier to understand? Arguably yea. Either way it'll probably be the first time we are solving this problem (marking a piece of distributed work of non-fixed size as done) at CM. Import csv is similar, except with csv we know the work size at the start whereas list size can change on a whim (ppl can import new contacts while crm list population is happening) for us. Decision? which one do we go with? idk maybe discuss at standup"

Pure senior-IC commentary: stated preference, acknowledged downsides, contextualised the problem against prior CM patterns, and deferred decision to standup. [Permalink](https://campaignmonitor.slack.com/archives/C028VG4K5TP/p1771368788702119)

#### **CRM-Lite count-query design call with a junior engineer** *(2026-02-04, DM with a junior engineer)*
The junior engineer proposed `COUNT(DISTINCT s.EmailAddress)` to dedupe subscriber counts across multiple CRM lists. Clement caught the misconception in two messages:

> "It breaks the base assumption that a client will only ever have one crm list, and thus it breaks all the system design"
> "Pls don't do that" *(re: enabling CRM Lite on 2 lists to test)*

Then explained the model: "One email. One crm list. Multiple normal lists. Dropdown is for selecting one of the normal lists from the multiple". Closed with "But it's a good QA mindset you have" — coaching mode rather than just correcting. [Permalink](https://campaignmonitor.slack.com/archives/D09UX9Q0AUQ/p1770182178452369)

#### **CRM-Lite endpoint-error contract design** *(2026-04-09, #cm-team-boole-dev)*
The junior engineer asked whether the `crm-enabled` endpoint should return 400 or `200 {hasAccess: false}`. Clement responded with a full design proposal:

> "The end goal for this is to reduce noise in cmapi logs. So I see two approaches:
> 1. Modify every crm endpoint return model to be something like `{hasAccess: false} | {hasAccess: true, data: ...}`
> 2. Go through all cmapi calls in the frontend, and make sure all calls to crm endpoints are called only when the has-crm-enabled call returns true."

Followed up with explicit guidance: "either cache the response on the frontend or refactor the app to only fire those requests after the check call." the junior engineer implemented option 2. [Permalink](https://campaignmonitor.slack.com/archives/C028VG4K5TP/p1775710296065669)

#### **Campaign Series module-placement debate** *(2025-10-30, #js-crew-members)*
The squad product lead asked where the new Campaign Series feature should live (in `campaigns.tsx` vs. a new module). Clement suggested an SMS-style two-app split:

> "either that or you can approach it like sms with two apps: managesmscampaigns and smscampaigncreateionchecklist"

A JS-crew teammate weighed in supporting the chunky-app approach. The squad product lead ultimately went with the unified module. Clement's prior experience designing the SMS module split was the reference. [Permalink](https://campaignmonitor.slack.com/archives/G740DCZA5/p1761780501955639)

#### **Frontend code-quality intervention** *(2026-01-22, #js-crew-members)*
The JS-crew teammate tagged Clement: "we might need to step in sooner rather than later and clean some of this up before it gets away from us?" Context: a team had been adding too many React Context providers to their PRs, with one PR merged before JS-crew approval. Clement responded:

> "That's my team / the squad product lead's team. I've been in system design land I haven't been looking closely at the PRs"

Took ownership, escalated to the squad product lead at the same time. Crew authority on display. [Permalink](https://campaignmonitor.slack.com/archives/G740DCZA5/p1769063429582639)

### 2. Project planning / kickoff

#### **Onboarding rework — 3-option investigation** *(2025-09-24, link to LDR threads)*
Initiated by Clement asking a teammate whether onboarding survey conversion stats had been collected:

> "Have you done any work yet on collecting statistics on the existing onboarding survey data? Stuff like - per question attempt rates, how many made it to page 2, number of sign ups vs completed onboarding surveys (drop off rates)"
> "Wanted to make sure we have the stats before I propose to wipe the old database :elmofire: Might not happen but good to be prepared."

The teammate replied with the famous "Clem has gone mad with power after becoming feature lead". Output: the Confluence page [Onboarding service tech investigation](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1368588295/) with the 3-option comparison matrix. [Permalink](https://campaignmonitor.slack.com/archives/C028YGQLACS/p1758519199984599)

#### **CRM-Lite release-plan DBA consultation** *(2026-02-10, DM with a DBA)*
Pre-release planning kicked off with the DBA:

> "I am drafting up the release plan for the CRM-lite feature.
> The problem we might have is that when a client opts into the feature, we start a copy job that essentially copies all subscribers in the client into a special CRM list. It's batched in 1000s but we would like to be cautious.
> From the DBA side, do you foresee any problems with this? And do you reckon we should put in some constraints in place (eg. only enable the opt-in for accounts with less than x subs)?"

The DBA followed up with a Zoom — Clement walked him through the system end-to-end. [Permalink](https://campaignmonitor.slack.com/archives/D07T8R5SYUA/p1770682795839669)

#### **Onboarding slicing decision lookback** *(2026-01-08, DM with the project manager)*
Project manager came back to him asking which option from his tech-investigation matrix had been selected:

> "do you remember which option we ended up going with in [spreadsheet] as written up in [Onboarding rework technical approach]?"

Clement was honest:

> "tbh I don't remember. they look the same"
> "I think overall the project tasks are very doable in parallel so splitting into 2 parts can have less ppl working in parallel and free up some capacity. Both approaches take 2 sprints"

Showed continued ownership of the project context even months after the original investigation. [Permalink](https://campaignmonitor.slack.com/archives/D02UZBV5L83/p1767851778026359)

### 3. Post-incident / retro

#### **Insights/Matillion production debugging with a DBA** *(2024-10-24, DM)*
Wrote up a complete diagnostic walkthrough for the on-call channel:

> "Insights call with teammate:
> • The teammate noticed the insights - engagement - RefreshA job wasn't running.
>     ◦ Everything was late in <http://insights-monitoring.campmon.com/updatestatus>
>     ◦ Restarting Matillion didn't help
> • Going by the architecture diagram here [Restore-Refresh Cycle]
>     ◦ We checked the database and figured it is preparing the data as expected
>     ◦ Matillion is running
>     ◦ SQS is running but nothing was being inserted
>     ◦ Eventually figured out InsightsEventsService was stalling.
> • InsightsEventsService is the service that polls the databases every 10 seconds to check for data readiness, then inserts a message into sqs for matillion to pick up and start a job.
> • Restarted InsightsEventsService and looks like the RefreshA job is being scheduled properly now."

Posted to both DM and `#cm-team-boole-dev`. Classic problem-isolation walkthrough — system diagram → confirm each subsystem → identify the breaker. [Permalink](https://campaignmonitor.slack.com/archives/D07T8R5SYUA/p1729744878980699)

#### **Enterprise-customer P2 — late-night journey debugging** *(2026-02-19/20, #cm-team-boole-dev)*
After being roped in by a teammate at 11pm:

> "a teammate and I have been looking at this from 11pm -> 1am
> *Problem* Client has been firing 800/min API requests to update a single subscriber, but strangely the same email. Probably a bug on their side. We can refresh the page and see the subscriber name updating in real time lol.
> The list is attached to 10 active journeys.
> This created a big backlog so journey activity is very delayed."

This was the incident that became the postmortem published in a teammate's Confluence space ([2026-02-20 - P2 - On Subscription Journeys stopped triggering](https://campaignmonitor.atlassian.net/wiki/spaces/~712020050cc2bb540c4f6da8df0b75b17479b4/pages/2032697352/)). [Permalink](https://campaignmonitor.slack.com/archives/C028VG4K5TP/p1771510509542259)

### 4. Technical investigations / spike conclusions

#### **Stored-procedure index advice from DBA** *(2025-07-23, #cm-team-boole-dev)*
Chatted with the DBA about a giant query for agency-revenue computation; came back with a concrete index recommendation and shared it back to the team:

> "okie chatted with the DBA, he is very helpful yes yes :excited:
> 1. Giant query and approach looks ok.
> 2. Suggested new index - 'I would change the index to look like this as it would be more useful to other queries as well. I believe this to be a valid index that should be added.'"
> `CREATE NONCLUSTERED INDEX ... ON [dbo].[AD_TransactionProcessing] ([DateAdded],[UserID]) INCLUDE ([Amount],[Currency],[BaseCost])`

Followed-up with: "also looks like the currency='US' currency='USD' thing is an existing issue in prod and deploy so we are stuck with the workaround." [Permalink](https://campaignmonitor.slack.com/archives/C028VG4K5TP/p1753227346624899)

#### **Workflow-failure investigation — March 2026** *(2026-03-19, #cm-team-boole-eng-prod)*
After the project manager pulled him in: "Hey @blacksmith you probably have most context in this area - what do think?" Clement walked through:

> "a teammate's post does not match his PR description"
> "All I know is that these `autoresponderabusecheck` `autoresponderqueuecheck` and `autoresponderqueuecheckterminations` agents exist and sit somewhere just before the workflow trigger service."

Identified the agents involved without code-diving. [Permalink](https://campaignmonitor.slack.com/archives/C028YGQLACS/p1774398743095879)

### 5. Tooling / process improvements

#### **Vite vs Webpack migration strategy** *(2025-07-02, #js-crew-members)*
A JS-crew teammate was deep in the trenches of a Node 18 + Webpack 5 migration. Clement provided strategic framing:

> "we should still move away from webpack at some point but yes"

Earlier in the year (May 2026) followed through and shipped the actual Webpack 5 upgrade (PR #23354) using AI assistance documented in `#boole-ai-log`. [Permalink](https://campaignmonitor.slack.com/archives/G740DCZA5/p1751419259817729)

#### **Feature-flag hygiene reminder** *(2025-09-05, #cm-team-boole-dev)*
Casual one-liner that becomes the team's tech-debt agenda:

> "we should probably clean up some of our old feature flags :sweat_smile:"

David replied "There's a ff cleanup ticket somewhere". This is how team backlogs get nudged. [Permalink](https://campaignmonitor.slack.com/archives/C028VG4K5TP/p1757047787862369)

#### **AI work-log entries during Innovation Sprint** *(2026-05-27 to 28, #boole-ai-log)*
During a company-wide Innovation Sprint, Clement filed structured AI-tool-use reports — including a Webpack 5 upgrade with time-delta estimates ("~1 day with AI vs. ~1 week manually"), a `RunnerService` gRPC v2 migration, and code-reviews-with-AI. Demonstrates both willingness to use new tools and discipline in measuring their actual impact. Sample:

> ":clipboard: Task: Migrate all GrpcClient usages in RunnerService to the V2 API across the repo.
> :arrows_counterclockwise: Default Approach: Manually audit every gRPC service file, update client call signatures, and replace NuGet packages one by one — a tedious, error-prone process across a large codebase.
> :robot_face: AI Approach: Used AI to systematically go through every gRPC service in the repo, identify V1 usages, migrate the code to the V2 service API, and update-replace the corresponding NuGet packages.
> :stopwatch: Time Delta: ~1–2 hrs with AI vs. ~half a day manually (estimated).
> :link: Evidence: [runnerservice.core#153](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/153)"

[Permalink](https://campaignmonitor.slack.com/archives/C0B4TN4N8H5/p1779950748238719)

### 6. Hiring + people leadership

#### **Mid-level engineering screen** *(2025-10-09, #dev-recruitment)*
A senior engineer handed off a candidate's take-home; Clement reviewed the code-samples:

> "did they read the spec properly?"
> "Tbh it looks like junior code. the responses are missing..... finesse"
> "I see stuff like... Unused variables, using `let` but not reassigning, the `groupBy` question solution not to spec. I would expect more finesse from a mid level."

Closed with: "the senior engineer let's fail for mid". Decisive, well-reasoned hire/no-hire call. [Permalink](https://campaignmonitor.slack.com/archives/G0F5DVCUQ/p1759991953792449)

#### **Kairos all-hands summary** *(2025-10-02, #cm-team-boole-eng-prod)*
After the post-Zeta-acquisition all-hands, Clement summarised the CEO's video into a structured Executive-Summary-style writeup with sections for Vision, Delivery Philosophy, Quality & Discipline, Leadership Commitments, and Team Call to Action. Even noted: "so I got copilot to summarise the transcript for the CEO's video :stuck_out_tongue:". Useful evidence of his ability to digest strategic messaging and re-broadcast for the team. [Permalink](https://campaignmonitor.slack.com/archives/C028YGQLACS/p1759385747170749)

## Notable individual messages (longform writeups)

These are the longform Clement messages where a substantive engineering decision is captured in a single message. Useful as standalone artifacts of his thinking.

1. **Distributed-work-completion design opinion** — 2026-02-18 — see "Architecture / design decisions §3"
2. **CRM-Lite count-query coaching** — 2026-02-04 — see §4
3. **CRM-Lite endpoint contract proposal** — 2026-04-09 — see §5
4. **Enterprise-customer P2 problem framing** — 2026-02-20 — see "Post-incident §2"
5. **Insights/Matillion debugging walkthrough** — 2024-10-24 — see "Post-incident §1"
6. **Kairos strategy summary** — 2025-10-02 — see "Hiring §2"
7. **CRM-Lite list-population status-detection proposal** — 2026-02-19 (engineering channel)
8. **Onboarding survey stats request** — 2025-09-22 — see "Planning §1"

## Observations

- The "engineering writing" surface in Slack is dominated by **CRM-Lite design work** (Nov 2025 – Mar 2026). This was the period he was most clearly acting as **feature tech lead** — driving DBA consultations, GDPR design, downstream consumer impact analysis, release-plan reviews. The conversations also show repeated handoffs back to him from product/PM ("you have most context in this area — what do think?").
- **Tone**: warm, self-deprecating, uses emoji liberally — but the engineering content underneath is tight and decisive. Stops to coach junior engineers (a junior engineer, a junior engineer, a junior engineer) without losing scope.
- **Cross-team operating style**: comfortable starting DMs with DBAs, platform engineers, designers, and product leads to pre-bake decisions before publishing the formal LDR. The Confluence LDR (file 14) is the *output* of these chats, not the start of the conversation.
- **Engineering hiring** participation is a non-PR signal of the trust placed in him — code-screen review with hire/no-hire judgment was delegated to him by another senior engineer.
- **Strategic engagement**: even outside his technical role, the Kairos all-hands summary shows he absorbs and amplifies company-strategic context for the team.

---

## 🆕 2026-H2 threads (Jun–Nov 2026)
Full detail: [data/2026-h2/findings-slack.md](data/2026-h2/findings-slack.md). Teammates by role.

| Date | Channel | Thread | Why it matters |
|---|---|---|---|
| 06-15 | team / on-call | Trigger-service healthcheck: "Leader election was dropped in the .core port, so all 6 instances run the heartbeat" | Root cause from prod Consul; advised against restart; stopgap + fix |
| 06-17→19 | DM / #c-sharp | Drip schema: "Let's make the column non-null… drop the constraint… this pattern is not used anywhere else"; "We don't think reusing the column is a good idea." | Design call made with the senior DB reviewer |
| 07-22→27 | #cm-sre | "Drip campaigns… is now live on all prod DBs. Playbook… DD Dashboard" | You owned the go-live announcement |
| 09-01 | DM (EM) | "Would you be up for taking the discovery piece of this work on for our team" | Handed the top-priority project |
| 09-02→04 | team | UCF DLQ: 3 options, "too tired to be touching prod", "an actual bug in the contact attribute service", fixes "6 of the 8" | Cross-team incident, judgment |
| 09-07→15 | team / PM | Twilio embed "black box" risk; "Have we applied for early access?"; "CM does not support A2P 10DLC numbers"; discovery DONE + tasks created | Discovery leadership |
| 09-28 | DM (lead) | Staffing recommendation → "we'll go with what you've recommended!" | Decision adopted |
| 09-28 | team | "Claude has been going back and forth… 2.5 business days" → "Such a great call out" | AI judgment |
| 10-07→08 | #cm-thompson-support | "chicken-egg problem" → partner team makes `registrationInfo` optional next day | Influence without authority |
| 10-09 | eng | GitHub bot outage timeline → "We are back!" | Org-wide tooling restored same day |
| 11-04 | team | PM: "SMS Compliance Embeddable in full glory! Great work Clem, Alexis!!" | Public credit |
| 11-06 | eng | "I didn't think it would affect everything, my bad" | Owned a mistake |
