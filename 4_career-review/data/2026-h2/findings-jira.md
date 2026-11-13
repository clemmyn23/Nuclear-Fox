# Jira findings: Clement Ng (accountId 6080d2f12ad11c0072b8a1ba), 2026-05-28 → 2026-11-10

Source: campaignmonitor.atlassian.net, read-only JQL plus issue reads (descriptions, comments, links, remote links). Nothing was edited.
Legend: **[Fact]** is stated in Jira. **[Inference]** is my reading and is not stated in Jira.

## 0. Context: teams and projects

| Project key | Project / team name (Jira) | Clement's work there |
|---|---|---|
| AJ | **Boole** (Audience & Journeys) | Drip Campaigns (Advanced/Simple), Journey Reporting innovation sprint, Graylog→Datadog, journeys on-call fixes. Ran to about 1 Sep 2026 |
| COM | **Mitnick** | SMS Twilio Compliance Embed (Sep–Oct), AI-DLC Stream A (Sep–Oct), Brand Hub V2 1A (Nov), UCF alert investigation |
| JC | **Javascript Crew** (guild-style) | Docker frontend builds and build-speed epic JC-411 (Oct), CM-GITHUB bot outage |

**Why AJ → COM?** Jira has no explicit reorg ticket. Evidence:
- [Fact] AJ-1305 "Document Journeys context handover (last day 27 Aug)" (Samantha Crome, Boole). The handover says: "**There is no named successor tech lead.** Flagged in the document as the biggest structural risk in the handover; the decision sits with the Engineering Manager." It also says Journey Reporting "is stalled, not in progress" and the WorkflowContext prod-account migration "is on hold".
- [Fact] Clement's first COM ticket is COM-1619 (SMS Compliance Embeddable Discovery), created 2026-09-01 by Karthik Ramaswamy Iyengar (the SMS PM on COM). COM-1625 (UCF alerts, journeys infrastructure) was also filed in COM on 2026-09-04, so Mitnick appears to have taken over journeys operational support as well.
- [Fact] COM-1749 says "Mitnick has inherited the [Brand Hub] codebase from Zuse." Fan Li (also ex-Boole) moved to COM Brand Hub work too.
- [Fact] AJ-1333 (Drip admin-only pilot flag) was cancelled 2026-09-25 by PM Jarrod Taylor: "No longer required as we will release to all agency/MT users at once." Jarrod later appears as PM on Brand Hub (COM-1629).
- **[Inference]** Boole was wound down or merged into Mitnick around late Aug / early Sep 2026. The likely trigger is the tech lead (Samantha Crome) leaving on 27 Aug, with Drip Campaigns shipped and Journey Reporting stalled. Mitnick seems to have absorbed Boole's engineers and PM, and possibly its journeys support duties. Confirm this with the EM or Slack.
- [Fact] Team labels in use: "Boole" on AJ tickets, "Mitnick" on COM Brand Hub tickets, and "Team Thompson" (Shared Services: Tim Cranfield and others) owns the SMS backend and CM-API side, per COM-1619 and COM-1808.

## 1. Epic narratives

### 1.1 Advanced Drip Campaigns – Branching (AJ-1111), "Complex Campaign Series"
- **Epic:** [AJ-1111](https://campaignmonitor.atlassian.net/browse/AJ-1111). Reporter Shenny Mackie (EM/delivery lead, inferred). Created 2026-03-23, **Done 2026-10-09**. No fixVersions. Remote links: Confluence "LDR - Complex Series Campaigns" (pageId 1891401732) and "Inception: Complex Series branching" (pageId 2015232040). Figma "Campaign-series---slice-2". Related epics AJ-1158, AJ-925, AJ-866.
- **What it is:** branching drip/series campaigns. Campaign nodes and condition nodes (Yes/No) form a tree, and subscribers are routed into **cohorts** that are evaluated at send time. "Complex series" was renamed "Drip Campaigns (Advanced)" during the work (AJ-1236).
- **Size and people:** 68 child tickets (66 Done, 2 Cancelled). By assignee: Fan Li 22, Sharareh Lotfi 11, **Clement Ng 10**, Samantha Crome 8, Alex Zissis 6, Christopher Luong 6, Yuri Fontes (design) 2. PM / product decisions: Tom Evans (AJ-1246 decisions, AJ-1254 help doc). Jarrod Taylor was PM on the fast-follow/rollout decisions.
- **Clement's role: owned the whole Advanced Drip frontend canvas.**
  - AJ-1115 (Mar–May 8): tree API contract (`sequenceTree`, `ComplexSeriesTreeNodeType`, `ComplexSequenceEdgeType`) plus the first tree rendering. It blocks AJ-1114, AJ-1116 and AJ-1117, so it was on the critical path.
  - AJ-1139 (→ May 21): zoomable, pannable canvas, URL-driven node focus. Ticket note: "We will not be sharing components from journeys. We will be copying/creating our own versions in the monolith repo."
  - AJ-1140 (→ Jun 12): "+" add-step, Email/Condition dropdown, node limit banner, hard-block interactions while saving ("no queuing mechanism… unlike Journeys"). Clement's comments: "Flag added / Paused for innovation week" and PR createsend.com#23265.
  - AJ-1149: timeline display. The design changed "due to scaling concerns."
  - **AJ-1190 (self-created 2026-05-19 → Jul 16): "Complex sequence – Design and function alignment."** This was the final UX polish before release, and Clement reframed the card himself: "This card is now used for the final design alignment and ux polishing work before we release the final product." (2026-06-16). He added the follow-up items (plain-text nodes block conditions, status-pill anchoring). Yuri Fontes (design) addressed him directly with panel redesign requests.
  - AJ-1186: backend C# change. It stamps `SendingAgentType = ComplexSequence` at campaign creation so the dedicated ComplexSequenceAgent claims those campaigns. Design: Confluence "MailingSendServiceAgent Workflow and Potential Blocking Issue Solution".
  - **AJ-1155 (→ Jul 27): Monitoring and alerting** for complex series: dashboards, cohort-population stuck alerts, a weak-point review and a playbook. Shenny: "Ideally done before release." [Inference] The "Playbook - Drip campaigns" page in the AJ space, which AJ-1305 calls "the model to copy", may be related. Not confirmed who wrote it.
  - AJ-1249 (grey out condition after plain-text email). This came from the product decision on AJ-1246 ("no, grey out the condition", Tom Evans) and was delivered inside AJ-1190-b (PR #23903).
  - AJ-1254: help doc "Learn more" links (help.campaignmonitor.com/s/article/drip-campaigns). AJ-1257: nodes-overlap fix, self-reported and fixed within a day.
  - Reported AJ-1231 (lock recipients at create time for complex-sequence campaigns), a product-correctness rule he raised.
- **Timeline:** bug bash AJ-1153 (Done Jul 20). Mini bug bash AJ-1232. E2E testing AJ-1154 (Jul 20). Performance/load test AJ-1270 (Jul 30): Christopher Luong records a concurrency issue, "10 lists of 50k subscribers + 1 real email all fail to send", analysed by Fan. Amplitude instrumentation AJ-1176 (Jul 28). [Inference] Release to customers was around late July / Aug 2026. Bugs filed against "Production" from 2026-07-17 (AJ-1262, AJ-1265) suggest it was live behind a flag by mid-July. The epic closed 2026-10-09.
- **Rollout:** [Fact] AJ-1333 was an interim plan for "a small, closed pilot group of trusted agency and multi-team customers". It was cancelled 2026-09-25: "we will release to all agency/MT users at once" (Jarrod Taylor). Feature flag FF 1136 is `CampaignSequenceForAllAccountTypes`.
- **Post-launch bugs (AJ-1250 fast follows):** AJ-1238 (second-level child campaigns fail to send, no cohort resolved, Fan), AJ-1239, AJ-1258 (cancel downstream when a send fails), AJ-1259 (cohort race condition can send to the wrong cohort, Backlog), AJ-1260. Clement fixed AJ-1262 (thumbnail not rendering) and AJ-1265 (zoom resets). He closed AJ-1243 after analysis: "Cannot replicate. Might be fixed by Fan's work on changing the sending state styling. Or fixed by sherry's work on the sidebar."

### 1.2 Simple Drip Campaigns UI Update (AJ-1158) and Advanced Drip Fast Follows (AJ-1250)
- AJ-1158: 5 tickets, Done 2026-10-09 (Samantha 2, Jay Chen 2, **Clement 1**). Clement's **AJ-1161 "Accordion list of campaigns (big)"** (→ Aug 31) is the main stage of the redesigned simple series page: date/status ordering, focus by URL, deep links, revert on a missing campaign. It is gated by the AJ-1165 flag.
- AJ-1250: 35 tickets (11 Done, 22 Backlog). Clement owned 3 (AJ-1243, AJ-1262, AJ-1265). The backlog includes "Segments as root recipient" (AJ-1317–1322, Boole) and a draft state. [Inference] These were left unfinished when the team moved.

### 1.3 Journey Reporting – Innovation Sprint (AJ-1192) and productionisation (AJ-1215)
- AJ-1192 goal [Fact]: "prove the data layer works, demonstrate a compelling UI, and establish the handler pattern — all behind a feature flag… This is not a production release." 20 tickets, all Done except 1. **Clement owned 2:** AJ-1196 (feature-flag gRPC client in RunnerService plus a monolith flag, Done May 29) and AJ-1195 (subscriber activity feed UI, a "30-day activity history… so that [support] can diagnose issues without needing to query the database directly", Done Jun 9).
- Fan Li's merge plan (2026-08-31) flags AJ-1196: PR #147 added the tests and #152 deleted them, so "net effect is the client ships with no test coverage. Disclose in the PR body and raise a follow-up."
- Clement reported **AJ-1206** (tech debt: migrate to the V2 gRPC client) after review feedback: "Might actually be a decent candidate to use AI for… Should do before we merge to master though." PR runnerservice#153.
- AJ-1215 (productionisation) is gated on the datastore hosting decision. It was stalled per the AJ-1305 handover. AJ-1213 (mock data from Datadog/Graylog logs) is still assigned to Clement in Backlog.

### 1.4 Graylog → Datadog migration for Journeys (AJ-961)
- Rationale [Fact]: "We are moving away from graylog and will be using datadog as a logging tool going forward… with minimal disruptions." Epic Done 2026-09-17. 20 tickets: Christopher Luong 5, Jay Chen 4, Fan Li 4, **Clement 3**, Russell Abedin 2, Alexis Tzanos 1.
- Clement: AJ-971 DefinitionService ("Repo has zero references to Graylog. No work needed. Datadog agent is already set up"). AJ-980 metric service ("logs are in prod DD!", Sep 8). AJ-1292 workflowcontext.updatecustomfield follow-up (PR updatecustomfield#72, Sep 15).
- Related: **JC-436 CM-GITHUB Slack bot outage (Oct 9)**. Clement restored the bot by moving it off decommissioned Graylog to Datadog and bumping the fargate module. His detailed RCA comment covers the outage window ("down from 2026-10-08 18:35 UTC to 2026-10-09 04:15 UTC"), honest unknowns ("the fix can't be attributed to one of them") and follow-ups (pin the Datadog agent image instead of `:latest`).

### 1.5 SMS – Twilio Compliance Embeddable (Sales Led) (COM-1620): toll-free verification
- **Epic** [COM-1620](https://campaignmonitor.atlassian.net/browse/COM-1620), reporter and PM Karthik Ramaswamy Iyengar. Created 2026-09-01, In Progress. No fixVersion, no remote links. References: Google slide deck and walkthrough video, Confluence `wiki/x/EoA5i`, and a Shared Services estimate page "Toll-Free Verification Twilio Compliance Embeddable Implementation Estimate CM Emma" (SS space 2285469714). The engineering doc **"SMS Twilio compliance embeddable" (COMPOSE space, page 2451767325)** was written by Clement: "Initial work breakdown doc" (his COM-1619 comment, 2026-09-15).
- **Business rationale [Fact]:** "Twilio offers Compliance Embeddable, an iframe experience for us to onboard our customers on SMS." The scope is "Sales Led Direct, Agency and Multiteam Customers… new and existing customers who need SMS". Self-serve is excluded (it depends on SMS credits in ChargeBee), and so are customers on Infobip. COM-1619 says one goal is "to provide that UI to the end customer to complete all the details required for Registration (and reduce human error)". Covers TFN, 10DLC and alphanumeric sender IDs. COM-1702 describes the manual process it replaces: "Today a person flips `SMS_Client.SendApprovalStatus` to `Allowed` in Hex". **No carrier/regulatory deadline, customer count or revenue number appears in Jira.** [Inference] US/CA toll-free verification is a carrier requirement, so this matters for compliance, but Jira does not state a date.
- **Clement's role: technical lead / DRI (inferred, strongly supported).** He did the discovery (COM-1619), wrote the breakdown doc, and on 2026-09-15 **created the 11-ticket work breakdown** (COM-1646–1656) with effort estimates. On 2026-10-08 he created the CmAPI breakdown (COM-1699–1702). He **reported 16 of the 28 epic tickets and was assignee on 8**. Alexis Tzanos was assignee on 14 (frontend), Karthik on 2 (testing and status sync).
- **Clement's tickets:**
  - COM-1646: feature flag and routing gate (US/CA to the embed, AU/UK unchanged).
  - COM-1648: provisioning-endpoint spike. He proposed the API shape: init returns the Twilio token; get-session returns "Not available | In progress | Available" plus a 24 h session token.
  - COM-1699: status and gating (`GetSmsComplianceEmbedStatusAsync`, agency support). He removed the `isDirect` param.
  - **COM-1700: `POST compliance-embed-init` and the GET session endpoint.** Design decisions in it: a deterministic `requestId` derived from the client "so retries never buy a second number"; "Don't return Shared Services DTOs directly from CmAPI"; a documented open decision on GET semantics (re-call `compliance_inquiry` or cache in Redis for less than 24 h); AC "Calling init twice for the same client never buys a second number."
  - COM-1701: monolith side effects (SMS access, workflow type, SMS_Account, compliance Slack post, analytics). AC "Re-running init… doesn't duplicate rows, posts or log entries."
  - COM-1654: per-brand theming, with two ThemeSetIds (Direct purple, Agency green) configured in deploy and prod.
  - COM-1733: alphanumeric sender support (AU/UK).
- **Scope decisions by Clement:** COM-1653 resume/resubmit closed with "We get this for free." COM-1652 status display closed with "Merged into COM-1651." COM-1702 was parked until Twilio and Shared Services provided event streams: "Wait for webhook / event-stream work on twilio and shared services side." It was later closed as no work needed.
- **Risk call-out (COM-1699, 2026-10-13):** "Follow-up: provisioning hard-failed for a client, with no retry available". This covers Failed/Deleted numbers that leave customers at a dead end. He proposed an escalation-to-support process and named the engineering decisions needed. "Not blocking COM-1699: no real customers use the embed yet."
- **Status at window end:** COM-1656 testing closed 2026-11-06. Karthik: "Internal tests are complete. I have requested Greg and team to test in Production and with a real customer." Late scope changes, mostly by Alexis: remove US/CA (COM-1746, 1800) and UK (COM-1807) from the region selector, and provision AU alphanumeric through Twilio instead of Infobip (COM-1765). [Inference] By November the launch scope appears to have narrowed toward AU alphanumeric plus TFN through Twilio, with production validation against a real customer pending.

### 1.6 Brand Hub V2 | 1A: Correct the Kit (COM-1629)
- Epic reporter and PM Jarrod Taylor, design Yuri Fontes. Created 2026-09-07, To Do. Links: 1A spec (ProdMgmgt 2561605696), Tech Discovery QA (2561638420), Brand Hub V2 PRD (2310864939), Figma.
- **Business rationale [Fact]:** "Brand Hub V1 is view-only, so customers can't correct inaccurate collection results. **Colour corrections are the most common request (three of four customers in CMPD-475).** Removing unwanted images is next." COM-1749 calls it "the most common customer request (CMPD-475)". Russell Abedin (COM-1685): "Editing brand hub assets is our priority… customer-requested work."
- 14 tickets: Fan Li 5 (backend, plus the discovery COM-1749), **Clement 3 (the entire 1A frontend)**, 6 unassigned. COM-1792 frontend data layer (3 pts, Done Nov 6). COM-1793 colour edit-mode UI (5 pts, Done Nov 10). COM-1794 logo/image delete UI (3 pts, In Progress). The work uses stale-row protection (kit id sent on Save, 409 handling), a 15-colour cap and duplicate-colour validation.

### 1.7 AI-DLC (AWS workshop) Stream A: Brand Hub Services Node→C# migration (COM-1673 / COM-1684)
- [Fact] COM-1673 "Finish stream A AI-DLC build phase" was assigned to Clement (Shenny Mackie reported it; 2026-09-23 → Done 2026-10-02). Its output was the stacked PRs BrandHubServices #80 (AI-DLC config harness) and #81–#85 (**AIDLC-A-1…A-5**, units 1–6), plus #86 (build fixes across all 6 units). COM-1685 lists them and calls COM-1673 the "Originating task". So the AIDLC-A-1..5 keys are PR/branch names, not Jira keys.
- Follow-on epic COM-1684 (Russell Abedin) planned review → dev → prod. **Decision 2026-11-03 (Russell, COM-1685): "we're not proceeding with the C# migration of AIBrandScraper at this time."** Reasons quoted: "It was a worthwhile experiment. It showed how far AI-DLC can take a large, multi-unit change". The stack "adds about 16k lines to replace a service of about 8k". "We'd lose LLM observability" (no Datadog LLM Obs SDK for .NET). Migration 007 can't be cleanly reversed. "With Claude doing most of our development, working in Node is no longer a significant barrier." It would also delay customer-requested editing work. The branches are kept and tagged. The idea of versioned brand kits may be reused.
- [Inference] For a career review this is experimental leadership that produced a clear no-go decision, which is a valid outcome. Shenny's COM-1749 analysis of Stream A (rules for building 1A now, medium rework risk) relied directly on the Stream A branches `aidlc-a-1` to `aidlc-a-6`.

### 1.8 createsend web app build improvements: Docker frontend builds (JC-411)
- **Epic created and owned by Clement** (2026-10-08, To Do, no assignee). Goal [Fact]: "Dockerise every TeamCity build that runs the `createsend.com/app` frontend toolchain… so upgrading it is a code change and no longer an agent/AMI change." He scoped in-scope pipelines and listed stale pipelines to retire.
- Clement created **all 24 child tickets** (JC-412–JC-435) in two days. Stage tickets: JC-412 Done, JC-413 In Progress, JC-414–416 To Do. Build-speed tickets: JC-417–JC-435.
- **JC-412 (Done 2026-10-13):** merged in createsend.com #25020 (24f90c49d6) on 2026-10-12, approved by francois-naude and matthewn. Parity check: 6,106 files. Fixes needed: Linux case-sensitivity bugs, and the discovery that "Closure only prints `ERROR -` and exits 0, so those bundles would ship incomplete." `steps.sh` now fails on closure errors.
- **JC-413:** an end-to-end artifact-flow investigation covering TeamCity, Octopus and Nexus. Key finding: "Canary does consume a TeamCity build artifact directly." PR #25051 is open. Sha Kong-Brooks's board audit: "the work is Clement Ng's."
- **Headline metrics (Clement's JC-411 comments):** goal "about 10 min → about 2 min". 5 merge checks per PR push = **1,066 s** today. The cached Docker deps layer saves "about 5–9 minutes of agent time" per PR push. Spikes: warm webpack cache **62.5 s → 3.5 s**; Closure → esbuild **13.7 s → 0.35 s**; TS 5.6 → TS 7 **4.8 s → 0.46 s**; Node 24 webpack −20%. The fe package is 165 MB / 6,106 files. Babel targets "IE 10/11, BlackBerry 7, Opera Mini". Estimated target: "about 1–1.5 min" warm, 2–2.5 min cold. He recorded the caveat that nothing has run on the dok agents yet.
- Also closed old JC-389 (local proxy webpack 5) and JC-367 (Change-day Vite, superseded by JC-422).

### 1.9 Operational / on-call ownership
- **AJ-1233** (self-reported 2026-06-26): prod trigger service health check. He found that the 6 scaled instances fire the blackhole-email health check simultaneously, which leads to 429 "Subscriber was added too many times too quickly." He weighed two options (vary the email vs leader election), took the C# crew's recommendation, and opened PR triggerservice.core#66.
- **COM-1625** (Sep 4–9): recurring UpdateCustomField alerts across multiple customer accounts (3 named client IDs). The ticket states: "Clement Ng investigated each occurrence". He reconstructed Redis cache keys, found the entries missing while the DLQ entries remained, and judged redrive safe because the operations are idempotent SETs. Follow-ups: COM-1666 (completed steps land in the DLQ permanently when an ECS task dies) and COM-1667 (runbooks direct on-call to redrive already-completed work).


## 2. Clement's notable comments (verbatim, short)
- AJ-1190 (2026-06-16): "This card is now used for the final design alignment and ux polishing work before we release the final product."
- AJ-1140 (2026-05-22): "Flag added / Paused for innovation week"
- AJ-1243 (2026-07-29): "Cannot replicate. Might be fixed by Fan's work on changing the sending state styling."
- AJ-1206 (description): "Might actually be a decent candidate to use AI for, but not as high in priority. Should do before we merge to master though."
- AJ-1233 (2026-06-26): "Personally I like the per-instance healthchecks so maybe I'll ask platform for opinion."
- AJ-971 (2026-09-02): "Repo has zero references to Graylog. No work needed."
- AJ-980 (2026-09-08): "logs are in prod DD!"
- COM-1619 (2026-09-15): "Initial work breakdown doc" → COMPOSE page 2451767325
- COM-1648 (2026-10-02): proposed endpoints ("initial sms account provisioning… get current session + status… Not available | In progress | Available")
- COM-1702 (2026-10-12): "Wait for webhook / event-stream work on twilio and shared services side."
- COM-1699 (2026-10-13): "Follow-up: provisioning hard-failed for a client, with no retry available… Proposed: set up a company process to escalate these clients to customer service"
- COM-1653 (2026-10-19): "We get this for free."
- COM-1652 (2026-10-20): "Merged into COM-1651"
- COM-1654 (2026-10-21): "Styling working. Theme set is tied to session."
- JC-436 (2026-10-09): "Root cause. Logging, jvm-libs and the Terraform module all changed in the same deploy, so the fix can't be attributed to one of them."
- JC-411 (2026-10-09): "Build speed findings: app/ and shared/ (goal: about 10 min → about 2 min)… Nothing has been tested on the dok agents yet."

## 3. Business rationale and metrics (every number found)
| Area | Number / statement | Source |
|---|---|---|
| Brand Hub 1A | "Colour corrections are the most common request (three of four customers in CMPD-475)" | COM-1629 |
| Brand Hub 1A | max 15 colours per kit; hard-delete with no restore | COM-1629 |
| AI-DLC Stream A | "adds about 16k lines to replace a service of about 8k"; "maintenance footprint would roughly triple" | COM-1685 (Russell) |
| SMS Embed | Scope: Sales-led Direct, Agency, Multiteam; excludes self-serve and Infobip customers | COM-1620 |
| SMS Embed | Manual process replaced: staff flip `SendApprovalStatus` in Hex | COM-1702 |
| SMS Embed | Session token expires after 24 h; init idempotent (never buys a second number) | COM-1700 |
| SMS Embed | Effort estimates per ticket (0.5–3 d), e.g. COM-1700 2–3 d, COM-1701 1–1.5 d | COM-1646…1701 |
| SMS Embed | "no real customers use the embed yet" (13 Oct); prod test with a real customer requested 6 Nov | COM-1699, COM-1656 |
| SMS Embed (Twilio roadmap) | Short codes ~2027; RCS Q4 2026 / early 2027 | COM-1619 |
| Drip rollout | pilot for "small, closed pilot group of trusted agency and multi-team customers" dropped → "release to all agency/MT users at once" | AJ-1333 |
| Drip load test | concurrency failure with "10 lists of 50k subscribers + 1 real email" | AJ-1270 |
| Drip email limit | "You've hit the limit of X emails allowed per series" (limit banner) | AJ-1140 |
| Journey Reporting | 30-day subscriber activity history for support | AJ-1195 |
| Trigger service | scaled to 6 instances → duplicate health-check emails → 429 | AJ-1233 |
| UCF alerts | Redis TTL ~3 days; multiple customer accounts affected | COM-1625 |
| CM-GITHUB bot | outage 2026-10-08 18:35 → 2026-10-09 04:15 UTC (~9h40m) | JC-436 |
| Build speed | 5 merge checks/PR = 1,066 s; install 69–77 s per build; Web Package JS 483 s median | JC-411, JC-412 |
| Build speed | Docker deps cache saves ~5–9 min agent time per PR push | JC-412 |
| Build speed | webpack warm cache 62.5→3.5 s; closure 13.7→0.35 s; tsc 4.8→0.46 s; jest 12.4→7.2 s | JC-411 |
| Build speed | goal ~10 min → ~2 min (est. 1–1.5 min warm) | JC-411 |
| Build artefact | createsend.com.fe 165 MB / 6,106 files; Docker image 2.34 GB | JC-411 |

**Not found in Jira:** ARR or revenue, support-ticket volumes, adoption/usage numbers for Drip Campaigns, OKRs, a carrier or regulatory deadline for toll-free verification, fixVersions/releases (none set on any of these epics), or story points (the custom field isn't populated; COM-179x put "Size: N points" in the description). Explicit "tech lead"/"DRI" titles weren't found either. AJ-1305 says Boole had "no named successor tech lead" after 27 Aug.

## 4. Ownership tallies per epic
| Epic | Total children | Clement assignee | Clement reporter | Others (top) |
|---|---|---|---|---|
| AJ-1111 Advanced Drip – Branching | 68 | 10 | 3 (AJ-1190, AJ-1231, AJ-1257) | Fan Li 22, Sharareh 11, Samantha 8 |
| AJ-1158 Simple Drip UI | 5 | 1 | 0 | Samantha 2, Jay 2 |
| AJ-1250 Drip Fast Follows | 35 | 3 | 0 | Fan 7, 21 unassigned |
| AJ-1192 Journey Reporting sprint | 20 | 2 | 0 | Fan 5, Samantha 4 |
| AJ-961 Graylog→Datadog | 20 | 3 | 0 | Christopher 5, Jay 4, Fan 4 |
| COM-1620 SMS Compliance Embed | 28 | 8 | 16 | Alexis 14, Karthik 2 |
| COM-1629 Brand Hub 1A | 14 | 3 (all frontend) | 0 | Fan 5 |
| JC-411 Docker builds | 24 | 0 assigned (work is his per audit) | 25 incl. epic | — |
| COM-1673 AI-DLC Stream A build | 1 | 1 | 0 | — |

## 5. Full ticket table (Clement assignee or reporter, active in window)
Note: AJ-648 appears because Clement is its reporter (2025). AJ-846 is a stale 2025 To Do. AJ-1115 and AJ-1139 (Drip tree, resolved 8 and 21 May) fall just before the window but set up the Drip work.

| Epic | Key | Type | Status | Assignee | Reporter | Created | Resolved | Summary |
|---|---|---|---|---|---|---|---|---|
| AJ-1111 | [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) | Task | Done | Clement Ng | Samantha Crome | 2026-04-17 | 2026-06-12 | Complex sequence create campaign frontend - make it work |
| AJ-1111 | [AJ-1149](https://campaignmonitor.atlassian.net/browse/AJ-1149) | Task | Done | Clement Ng | Samantha Crome | 2026-04-17 | — | Timeline display |
| AJ-1111 | [AJ-1155](https://campaignmonitor.atlassian.net/browse/AJ-1155) | Task | Done | Clement Ng | Samantha Crome | 2026-04-17 | 2026-07-27 | Monitoring and Alert check/creation |
| AJ-1111 | [AJ-1186](https://campaignmonitor.atlassian.net/browse/AJ-1186) | Task | Done | Clement Ng | Fan Li | 2026-05-18 | — | ComplexSequenceAgent: stamp SendingAgentType at complex sequence campaign creation |
| AJ-1111 | [AJ-1190](https://campaignmonitor.atlassian.net/browse/AJ-1190) | Task | Done | Clement Ng | Clement Ng | 2026-05-19 | 2026-07-16 | Complex sequence - Design and function alignment |
| AJ-1111 | [AJ-1231](https://campaignmonitor.atlassian.net/browse/AJ-1231) | Task | Done | Samantha Crome | Clement Ng | 2026-06-22 | — | Complex sequence campaigns - lock recipients |
| AJ-1111 | [AJ-1249](https://campaignmonitor.atlassian.net/browse/AJ-1249) | Bug | Done | Clement Ng | Shenny Mackie | 2026-07-13 | 2026-07-20 | Grey out condition to prevent selection after a plain text email in an advanced series |
| AJ-1111 | [AJ-1254](https://campaignmonitor.atlassian.net/browse/AJ-1254) | Task | Done | Clement Ng | Tom Evans | 2026-07-15 | 2026-07-20 | Help doc update |
| AJ-1111 | [AJ-1257](https://campaignmonitor.atlassian.net/browse/AJ-1257) | Bug | Done | Clement Ng | Clement Ng | 2026-07-16 | 2026-07-17 | Fix nodes overlapping in some cases |
| AJ-1158 | [AJ-1161](https://campaignmonitor.atlassian.net/browse/AJ-1161) | Task | Done | Clement Ng | Samantha Crome | 2026-04-20 | 2026-08-31 | Accordion list of campaigns (big) |
| AJ-1192 | [AJ-1195](https://campaignmonitor.atlassian.net/browse/AJ-1195) | Task | Done | Clement Ng | Samantha Crome | 2026-05-25 | 2026-06-09 | Build subscriber activity feed UI (mock data) |
| AJ-1192 | [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) | Task | Done | Clement Ng | Samantha Crome | 2026-05-25 | 2026-05-29 | Add feature flag gRPC client to RunnerService and monolith feature flag for journey reporting UI |
| AJ-1192 | [AJ-648](https://campaignmonitor.atlassian.net/browse/AJ-648) | Task | Done | Yuri Fontes | Clement Ng | 2025-05-14 | 2026-05-29 | Journey reporting UI design |
| AJ-1215 | [AJ-1206](https://campaignmonitor.atlassian.net/browse/AJ-1206) | Task | Backlog | — | Clement Ng | 2026-05-27 | — | [tech debt] Migrate to use V2 GRPC client in runnerservice.  |
| AJ-1215 | [AJ-1213](https://campaignmonitor.atlassian.net/browse/AJ-1213) | Task | Backlog | Clement Ng | Sharareh Lotfi | 2026-06-03 | — | Generate mock journey data in Postgres from Datadog journey logs |
| AJ-1250 | [AJ-1243](https://campaignmonitor.atlassian.net/browse/AJ-1243) | Bug | Cancelled | Clement Ng | Samantha Crome | 2026-07-03 | 2026-07-30 | Full page error on tree/sequence page when state changes to sending/sent |
| AJ-1250 | [AJ-1262](https://campaignmonitor.atlassian.net/browse/AJ-1262) | Bug | Done | Clement Ng | Samantha Crome | 2026-07-17 | 2026-08-07 | New campaign thumbnail doesn't render until page refresh |
| AJ-1250 | [AJ-1265](https://campaignmonitor.atlassian.net/browse/AJ-1265) | Bug | Done | Clement Ng | Samantha Crome | 2026-07-17 | 2026-08-03 | Zoom level resets whenever a new campaign is added to a Drip flow |
| AJ-48 | [AJ-1233](https://campaignmonitor.atlassian.net/browse/AJ-1233) | Bug | Done | Clement Ng | Clement Ng | 2026-06-26 | — | Investigate and fix healthcheck for workflowcontext.triggerservice.core |
| AJ-826 | [AJ-846](https://campaignmonitor.atlassian.net/browse/AJ-846) | Task | To Do | Clement Ng | Samantha Crome | 2025-10-01 | — | Set up sending domain |
| AJ-961 | [AJ-1292](https://campaignmonitor.atlassian.net/browse/AJ-1292) | Task | Done | Clement Ng | Jay Chen | 2026-08-10 | 2026-09-15 | Graylog migration: workflowcontext.updatecustomfield follow up |
| AJ-961 | [AJ-971](https://campaignmonitor.atlassian.net/browse/AJ-971) | Task | Done | Clement Ng | Samantha Crome | 2025-12-11 | 2026-09-02 | Update DefinitionService (C#) |
| AJ-961 | [AJ-980](https://campaignmonitor.atlassian.net/browse/AJ-980) | Task | Done | Clement Ng | Samantha Crome | 2025-12-11 | 2026-09-08 | Update metric service |
| COM-1620 | [COM-1619](https://campaignmonitor.atlassian.net/browse/COM-1619) | Task | Done | Clement Ng | Karthik Ramaswamy Iyengar | 2026-09-01 | 2026-09-15 | SMS - Compliance Embeddable Discovery |
| COM-1620 | [COM-1646](https://campaignmonitor.atlassian.net/browse/COM-1646) | Task | Done | Clement Ng | Clement Ng | 2026-09-15 | 2026-10-06 | SMS Embed: Feature flag + routing gate for TFV embed path |
| COM-1620 | [COM-1647](https://campaignmonitor.atlassian.net/browse/COM-1647) | Task | Done | Alexis Tzanos | Clement Ng | 2026-09-15 | 2026-10-01 | SMS Embed: Spike — custom pre-provisioning form & validate prior FE scaffolding (Rusty/Mitnick) |
| COM-1620 | [COM-1648](https://campaignmonitor.atlassian.net/browse/COM-1648) | Task | Done | Clement Ng | Clement Ng | 2026-09-15 | 2026-10-12 | SMS Embed: Spike — new CmAPI SMS provisioning endpoint |
| COM-1620 | [COM-1649](https://campaignmonitor.atlassian.net/browse/COM-1649) | Task | Done | Alexis Tzanos | Clement Ng | 2026-09-15 | 2026-10-08 | SMS Embed: Build embed container component (TwilioComplianceEmbed) |
| COM-1620 | [COM-1650](https://campaignmonitor.atlassian.net/browse/COM-1650) | Task | Done | Alexis Tzanos | Clement Ng | 2026-09-15 | 2026-10-22 | SMS Embed: Token-fetch integration with CmAPI |
| COM-1620 | [COM-1651](https://campaignmonitor.atlassian.net/browse/COM-1651) | Task | Cancelled | Alexis Tzanos | Clement Ng | 2026-09-15 | 2026-11-03 | SMS Embed: Lifecycle wiring (onInquirySubmitted/onCancel/onError) |
| COM-1620 | [COM-1652](https://campaignmonitor.atlassian.net/browse/COM-1652) | Task | Cancelled | — | Clement Ng | 2026-09-15 | 2026-10-20 | SMS Embed: Status display (approved/pending/rejected) |
| COM-1620 | [COM-1653](https://campaignmonitor.atlassian.net/browse/COM-1653) | Task | Cancelled | — | Clement Ng | 2026-09-15 | 2026-10-19 | SMS Embed: Resume/resubmit path |
| COM-1620 | [COM-1654](https://campaignmonitor.atlassian.net/browse/COM-1654) | Task | Done | Clement Ng | Clement Ng | 2026-09-15 | 2026-10-21 | SMS Embed: Per-brand theming (ThemeSetId) |
| COM-1620 | [COM-1655](https://campaignmonitor.atlassian.net/browse/COM-1655) | Task | Backlog | — | Clement Ng | 2026-09-15 | — | SMS Embed: Clean up US/CA branches in legacy wizard |
| COM-1620 | [COM-1656](https://campaignmonitor.atlassian.net/browse/COM-1656) | Task | Done | Karthik Ramaswamy Iyengar | Clement Ng | 2026-09-15 | 2026-11-06 | SMS Embed: Testing (happy path, resume, flag routing) |
| COM-1620 | [COM-1699](https://campaignmonitor.atlassian.net/browse/COM-1699) | Task | Done | Clement Ng | Clement Ng | 2026-10-08 | 2026-10-21 | SMS Embed CMAPI : Compliance embed status and gating |
| COM-1620 | [COM-1700](https://campaignmonitor.atlassian.net/browse/COM-1700) | Task | Done | Clement Ng | Clement Ng | 2026-10-08 | 2026-10-19 | SMS Embed CMAPI : compliance-embed-init and session endpoints |
| COM-1620 | [COM-1701](https://campaignmonitor.atlassian.net/browse/COM-1701) | Task | Done | Clement Ng | Clement Ng | 2026-10-08 | 2026-10-21 | SMS Embed CMAPI : Monolith side effects on Toll-free provisioning |
| COM-1620 | [COM-1702](https://campaignmonitor.atlassian.net/browse/COM-1702) | Task | Done | Karthik Ramaswamy Iyengar | Clement Ng | 2026-10-08 | 2026-11-05 | SMS Embed CMAPI : Verification status sync |
| COM-1620 | [COM-1733](https://campaignmonitor.atlassian.net/browse/COM-1733) | Task | Done | Clement Ng | Clement Ng | 2026-10-19 | 2026-10-23 | SMS Embed CMAPI: Alphanumeric number support |
| COM-1629 | [COM-1792](https://campaignmonitor.atlassian.net/browse/COM-1792) | Task | Done | Clement Ng | Fan Li | 2026-11-02 | 2026-11-06 | Brand Hub 1A: frontend data layer for edits |
| COM-1629 | [COM-1793](https://campaignmonitor.atlassian.net/browse/COM-1793) | Task | Done | Clement Ng | Fan Li | 2026-11-02 | 2026-11-10 | Brand Hub 1A: colour edit mode UI |
| COM-1629 | [COM-1794](https://campaignmonitor.atlassian.net/browse/COM-1794) | Task | In Progress | Clement Ng | Fan Li | 2026-11-02 | — | Brand Hub 1A: logo and image delete mode UI |
| JC-388 | [JC-389](https://campaignmonitor.atlassian.net/browse/JC-389) | Task | Done | Clement Ng | Clement Ng | 2024-05-30 | 2026-10-08 | [Local Proxy] Upgrade to Webpack 5 (or Vite) |
| JC-411 | [JC-412](https://campaignmonitor.atlassian.net/browse/JC-412) | Task | Done | — | Clement Ng | 2026-10-08 | 2026-10-13 | Stage 1: Build the app/ frontend in Docker |
| JC-411 | [JC-413](https://campaignmonitor.atlassian.net/browse/JC-413) | Task | In Progress | — | Clement Ng | 2026-10-08 | — | Stage 2: Frontend package artifact publishing for prod deployment |
| JC-411 | [JC-414](https://campaignmonitor.atlassian.net/browse/JC-414) | Task | To Do | — | Clement Ng | 2026-10-08 | — | Stage 3: Migrate each app/ frontend TeamCity pipeline to Docker |
| JC-411 | [JC-415](https://campaignmonitor.atlassian.net/browse/JC-415) | Task | To Do | — | Clement Ng | 2026-10-08 | — | Stage 4: Test and verify dockerised app/ frontend builds |
| JC-411 | [JC-416](https://campaignmonitor.atlassian.net/browse/JC-416) | Task | To Do | — | Clement Ng | 2026-10-08 | — | Stage 5: Cleanup and follow-ups for app/ frontend build dockerisation |
| JC-411 | [JC-417](https://campaignmonitor.atlassian.net/browse/JC-417) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Decide whether webpack should stop transpiling node_modules |
| JC-411 | [JC-418](https://campaignmonitor.atlassian.net/browse/JC-418) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Replace the Java-based closure compiler build so the frontend toolchain needs no JRE |
| JC-411 | [JC-419](https://campaignmonitor.atlassian.net/browse/JC-419) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: persist the webpack filesystem cache between CI builds |
| JC-411 | [JC-420](https://campaignmonitor.atlassian.net/browse/JC-420) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: compile the webpack bundles in parallel instead of one at a time |
| JC-411 | [JC-421](https://campaignmonitor.atlassian.net/browse/JC-421) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: stop transpiling app/ bundles for IE 10/11 and other dead browsers |
| JC-411 | [JC-422](https://campaignmonitor.atlassian.net/browse/JC-422) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: choose a faster bundler for app/ (Rspack 2 vs Vite 8) |
| JC-411 | [JC-423](https://campaignmonitor.atlassian.net/browse/JC-423) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: upgrade app/ and shared/ type checking to TypeScript 7 (native tsc) |
| JC-411 | [JC-424](https://campaignmonitor.atlassian.net/browse/JC-424) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: replace the legacy gulp-typescript step (2 files) |
| JC-411 | [JC-425](https://campaignmonitor.atlassian.net/browse/JC-425) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: run app/ and shared/ jest tests in parallel with a faster transform |
| JC-411 | [JC-426](https://campaignmonitor.atlassian.net/browse/JC-426) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: upgrade the app/ and shared/ toolchain from Node 18 to Node 24 LTS |
| JC-411 | [JC-427](https://campaignmonitor.atlassian.net/browse/JC-427) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: run independent steps of the package build in parallel and skip repeated validation |
| JC-411 | [JC-428](https://campaignmonitor.atlassian.net/browse/JC-428) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: share one checkout and image across the app/ merge checks |
| JC-411 | [JC-429](https://campaignmonitor.atlassian.net/browse/JC-429) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: cut VCS checkout time for the app/ builds |
| JC-411 | [JC-430](https://campaignmonitor.atlassian.net/browse/JC-430) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: share the Docker dependency layer across agents through a registry cache |
| JC-411 | [JC-431](https://campaignmonitor.atlassian.net/browse/JC-431) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: replace yarn 1 + lerna 4 with pnpm workspaces |
| JC-411 | [JC-432](https://campaignmonitor.atlassian.net/browse/JC-432) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: package only the files the site serves in createsend.com.fe |
| JC-411 | [JC-433](https://campaignmonitor.atlassian.net/browse/JC-433) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: modernise the app/ CSS and image pipeline |
| JC-411 | [JC-434](https://campaignmonitor.atlassian.net/browse/JC-434) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Build speed: skip app/ and shared/ build tasks whose inputs have not changed |
| JC-411 | [JC-435](https://campaignmonitor.atlassian.net/browse/JC-435) | Task | To Do | — | Clement Ng | 2026-10-09 | — | Put the createsend.com Monolith TeamCity projects under versioned Kotlin DSL settings |
| — | [COM-1625](https://campaignmonitor.atlassian.net/browse/COM-1625) | Bug | Done | Clement Ng | Shenny Mackie | 2026-09-04 | 2026-09-09 | Investigate recurring UpdateCustomField (UCF) alerts in #cm-ucf-alerts |
| — | [COM-1673](https://campaignmonitor.atlassian.net/browse/COM-1673) | Task | Done | Clement Ng | Shenny Mackie | 2026-09-23 | 2026-10-02 | Finish stream A AI-DLC build phase |
| — | [JC-367](https://campaignmonitor.atlassian.net/browse/JC-367) | Task | Done | Clement Ng | Clement Ng | 2022-05-13 | 2026-10-13 | [Change day] Vite webpack replacement |
| — | [JC-411](https://campaignmonitor.atlassian.net/browse/JC-411) | Epic | To Do | — | Clement Ng | 2026-10-08 | — | createsend web app build improvements |
| — | [JC-436](https://campaignmonitor.atlassian.net/browse/JC-436) | Bug | Done | — | Clement Ng | 2026-10-09 | 2026-10-12 | CM-GITHUB slack bot is down! |
