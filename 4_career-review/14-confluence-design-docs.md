# Confluence — design docs and planning pages

Mined from Campaign Monitor Confluence (campaignmonitor.atlassian.net) for design documents, architecture writeups, technical investigations, and planning pages authored or significantly contributed to by Clement Ng (Atlassian accountId `6080d2f12ad11c0072b8a1ba`).

**Captured:** 21 pages authored, 44 pages contributed to (where he was an editor/major contributor but not the original author).

## What stands out about Clement's Confluence presence

1. **The only person from his squad with pages in the `arc` (Architecture) space.** The LDR for CRM-Lite initial list population is in the Architecture space — the dedicated space for engineering's lightweight design reviews.
2. **He authors the canonical reference doc for every system he touches.** Whether it's SMS link tracking enrichment, Signup Forms, Onboarding service, CopyWorkflowService, or Campaign Series — he leaves behind a "how it works" document so the next engineer can pick up the codebase.
3. **He runs the squad's Bug Bash sessions.** Four separate "Bug Bash -" pages for major features: Subscriber Profile (2026), Subscriber Notes / CRM-lite (2025), Remove Subscribers step (2025), Create Segment from Campaign Report (2024). Indicates ownership of cross-functional pre-release QA coordination.
4. **JS Crew steward via Confluence too.** "Upgrading Node.JS on build agents" (Jul 2022) is the canonical JS-crew reference for Node bumps — published the same week he landed the actual Node 16 LTS PR.

## Pages authored — chronological with summaries

### 2022 — onboarding into JS Crew / SMS year

#### [Running JSONToProtoTrackEnricher locally for sms link tracking development](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/238686665/) — *2022-06-29, Compose space*
**Type:** Local-dev setup reference
**Summary:** Walked through the local dev setup required to develop on SMS link-tracking enrichment. Adapted from a teammate's earlier guide. Sits alongside the SMS-155 protobuf + Kafka + monolith work he was shipping at the time.
**Relevance:** Shows that when he was learning a service, he wrote down the path so the next person didn't have to repeat it.

#### [Upgrading Node.JS on build agents](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/238686695/) — *2022-07-08, Compose space*
**Type:** JS-crew operational reference
**Summary:** The three places to bump the Node version (`scrfrontend/Dockerfile.jsbuild`, `scrfrontend/tasks.sh`, `aws.stack.build/roles/campmon.windows-agent/tasks/main.yml`) plus notes on Node 17 OpenSSL engine changes.
**Relevance:** Pure JS-crew steward output. Published the same week he landed [createsend.com#13212 Node 16 LTS](https://git.campmon.com/Freshview/createsend.com/pull/13212). This document is what other engineers refer to next time they bump Node.

#### [Signup forms functional and technical audit](https://campaignmonitor.atlassian.net/wiki/spaces/DEV/pages/240617940/) — *2022-12-21, Engineering space*
**Type:** Application audit / architectural reference
**Summary:** Frontend + backend walkthrough of the Signup Forms feature — how primary fields are wired to `GrowYourAudienceBase.cs`, how custom fields are handled, how permission checkboxes are added (requires both FE payload + `HostedSubscribeFormSettingsShared.cs` change), translations only apply to primary fields, and the GrowYourAudienceUpdater service agent's refresh cycle.
**Relevance:** Came out of the SMS signup-form work (`SMS-396`, `SMS-451`, `SMS-477`). Doubled as a feature audit and a how-to-extend guide for adding new field types. Still in the Engineering space as of 2026.

### 2023 — Commerce / Recipes / Automation year

#### [Running ThirdPartyListImport.UI locally](https://campaignmonitor.atlassian.net/wiki/spaces/CMC/pages/239943596/) — *2023-05-04, Commerce space*
**Type:** Local-dev setup reference (revised)
**Summary:** Updated an earlier teammate's previous "Running ThirdpartyListImporter locally" entry to account for the okta-getsts → aws sso migration. Covers `aws sso configure`, SSM parameter errors, dev-power profile setup, AWS SSO credential refresh.
**Relevance:** The "I notice the old doc is stale, I rewrite it" pattern. Came from the Shopify Migration Assistant work (`MER-401`, `MER-536`) which exercised this codebase.

#### [Adding and verifying DMARC for a custom domain in CMC](https://campaignmonitor.atlassian.net/wiki/spaces/CMC/pages/309166216/) — *2023-12-19, Commerce space*
**Type:** Customer-success operational runbook
**Summary:** Step-by-step DMARC setup walkthrough — adding a custom domain in CMC, configuring DNS records, verifying via Mailgun. Annotated with multiple screenshots for each step.
**Relevance:** Cross-functional support content — a developer-written operational guide for the Customer Success team to follow when assisting clients. Shows he wrote for non-engineer audiences too.

### 2024 — Operational and Journeys-onboarding year

#### [CopyWorkflowService and how it works](https://campaignmonitor.atlassian.net/wiki/spaces/JO/pages/238699043/) — *2024-03-20, Journeys space*
**Type:** Multi-service architectural reference
**Summary:** Numbered 13-step walkthrough of the journey-copy flow — frontend POST → CmAPI WorkflowRecipesController → Core WorkflowCopyService → Reckless queue → CopyWorkflowService module → SaveCopyWorkflowJob to local DB → CloneWorkflowDefinitionCommand → WorkflowCloneConsumer → CloneWorkflowDefinitionResponseHandler (with branches for email content, condition content, custom-field action content) → SendCopyEmailContentHandler → CopyEmailContentResponseHandler → WorkflowConditionContentCopyConsumer → CopyConditionContentResponseHandler → publish CopyWorkflowCompletedEvent.
**Relevance:** One of the densest internal architecture documents in the Journeys space. Came out of `MER-665` / `MER-668` / `MER-713` permission-check work which forced him to map the whole CopyWorkflowService topology. Used as onboarding material for new AJ-tribe engineers.

#### [Insights Matillion upgrade 20 Oct 2024](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/775421959/) — *2024-10-24, Audience and Journeys space*
**Type:** Operational runbook / postmortem
**Summary:** Documented the failed Matillion upgrade attempt — EBS snapshot ID, EC2/EBS volume IDs, the AMI-not-found error from AWS Marketplace, what couldn't be completed in the maintenance window, "what can be done better for next time" (launch the AMI ahead of the window, check Matillion subscription contract status). Tied to the on-call playbook for Insights as a Service.
**Relevance:** Postmortem-style ops write-up. Co-authored with a DBA. Shows he documents failures honestly.

#### [Jenkins access tracking](https://campaignmonitor.atlassian.net/wiki/spaces/CMC/pages/352190511/) — *2024-10-24, Commerce space*
**Type:** Internal-tooling tracker
**Summary:** Table of whitelisted IPs allowed through the "Jenkins" firewall config on DigitalOcean — explains why it exists (avoid full-public exposure), lists each IP with label (ssh, wework barangaroo, github IP ranges, etc).
**Relevance:** Practical security hygiene. "Since there's no labelling function on DigitalOcean's firewall configurator" — solving the gap by maintaining the doc.

#### [Bug bash - Create segment from campaign report](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/847446022/) — *2024-11-22, Audience and Journeys space*
**Type:** Bug-bash coordination page
**Summary:** Linked the feature epic, response submission form, Lucidchart design, FF 1010 setup notes, and what to test.
**Relevance:** First of his bug-bash organizer pages. Owned the pre-release QA coordination for `AJ-494`.

#### [Create segment from campaign report page](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/847052808/) — *2024-11-22, Audience and Journeys space*
**Type:** Feature spec / planning page
**Summary:** Documented the product rationale and design for AJ-494 — "We often have dead ends in our application, we have completed X so what is next?"
**Relevance:** Companion to the bug-bash page; captured the "why" alongside the "what" for the feature.

### 2025 — Senior IC / Boole tribe year

#### [Bug Bash - Remove subscribers step](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1161592854/) — *2025-05-22, Audience and Journeys space*
**Type:** Bug-bash coordination page (FF 1032 `JourneyRemoveSubscribersStep`)
**Summary:** Same bug-bash template — epic link, response form, response sheet, E2E testing sheet, "what we are testing" sections for frontend UI and backend.
**Relevance:** Second bug-bash he organised. Pattern established: he runs them for major features.

#### [Onboarding service | Getting started | Welcome Guide - tech audit](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1362067562/) — *2025-09-24, Audience and Journeys space*
**Type:** Application tech audit
**Summary:** Mapped the full Onboarding service surface — Frontend (React app at `createsend.com/srcfrontend/apps/welcome`), Backend microservice (PUT/GET endpoints, gRPC server, Kafka `accountonboardingcompleted` event, DynamoDB + management-reporting db storage), Backend monolith (`SignupStep2Controller-ChooseCustomerType`, MSSQL writes), CM.Protobuf (`OnboardingService.proto`'s `GetAccountOnboardingData` RPC consumed by Setup Guide).
**Relevance:** The grounding doc for the larger Onboarding rework. Necessary before deciding which slice to ship.

#### [Onboarding service tech investigation](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1368588295/) — *2025-10-08, Audience and Journeys space*
**Type:** Multi-option tech investigation / design exploration
**Summary:** Decision matrix comparing three options — P1 "Build on existing", P2 "Fresh start", P3 "MVP (remove onboarding)" — across every affected layer: Marketing site, Frontend, Createsend monolith, CMAPI, MSG (cm.protobuf), Microservices (OnboardingService, KafkaToLookerService, SetupGuideService, dr2-analytics-reporting, conversion-scorer), DB Management Reporting, DB Postgres analytics-reporting, DB DynamoDB, SRE playbook, Segment tracking. Each cell shows what work is required. Effort sum, gains, and cons rows close the matrix.
**Relevance:** Classic senior-IC investigation document. The structure makes it possible for product + management to make a slicing decision. Stayed referenced into Jan 2026 when a junior engineer was picking up follow-up work ("I am reading *Onboarding rework technical approach* at the moment").

#### [Onboarding rework technical approach](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1389854769/) — *2025-10-09, Audience and Journeys space*
**Type:** Technical approach / implementation design
**Summary:** Two-stage MVP approach: Stage 1 adjusts marketing site question + monolith signup endpoint + monolith routing to bypass the existing survey; Stage 2 adds a new frontend app + monolith MSSQL `AccountOnboardingSurvey` table. Documents the CMAPI design (GET/PUT survey response, POST industry-guessing), the monolith MSSQL schema (`AccountOnboardingSurvey` columns), DR2 / GDPR considerations, monitoring (DataDog/Graylog), instrumentation (Segment tracking plan `users.yml`).
**Relevance:** "We've received the OK from architects for the new table and the overall CMAPI-CRUD architecture" — i.e. this is *post-architect-review* approved design. Showed he negotiates with the architecture function before publishing the implementation plan.

#### [Bug Bash - Subscriber Notes (CRM-lite)](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1420099702/) — *2025-10-20, AJ space*
**Type:** Bug-bash coordination page (FF 1090 `SubscriberNotes`)
**Summary:** Form submissions link, "test in production" setup, what to test.

### 2026 — CRM-Lite / Campaign Series feature-lead year

#### [LDR - CRM-lite initial list population](https://campaignmonitor.atlassian.net/wiki/spaces/arc/pages/1593835523/) — *2026-01-28, Architecture space* ⭐
**Type:** Lightweight Design Review (LDR) in the official Architecture space
**Summary:**
- **Problem:** Populate the master CRM list with all subscribers in the client; stretch goal — populate by list priority.
- **Data Structure / Flow / Messaging Contracts:** CMAPI sets opt-in flag → sends `InitiateCrmLiteListPopulation` protobuf command → CrmLiteService consumes → grabs all listIds in client → raises `PopulateCrmLiteListPaged` SQS messages (1000-per-page chunks) → builds `RawContactDefined-BulkOperations` Kafka events with `client_id, list_id (= crm_list_id), current_email_address, changed_via (new value crm_init), event_date_utc, contact_details.custom_fields, contact_details.name` → contact pipeline consumes and dedupes by email → contact inserted into crm list. Includes the actual protobuf message shapes for both commands.
- **Scaling:** Contact finaliser throughput 3k/s – 10k/s; 10M subs at 2k/s = 84 minutes.
- **Privacy by Design:** PII deletion on client GDPR delete; GDPR retrieval (list export) deferred to future iteration.
- **Decisions:** List ordering priority not strictly required (customer can reupload), 30 days to fulfil GDPR, dedup by email handled by contact pipeline, set custom fields upfront for fewer round trips.

**Relevance:** This is THE document. Published in the Architecture space (not the team space) means it went through the architecture LDR process. Every CRM-Lite PR he shipped in Q1 2026 traces back to this design.

#### [Updating CRM list population job status on completion](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1819312139/) — *2026-02-23, AJ space*
**Type:** Schema change / design proposal (status: complete, impact: high)
**Summary:** Proposed renaming `CL_ClientCRM` columns for clarity (`PopulateStatus` → `PopulateJobStatus`, `PopulateStatusDateUTC` → `PopulateJobDateUpdatedUTC`), introduced a new `Finalising` enum value between `InProgress` and `Completed`, defined the formula for estimated job completion time (`average wait time in queue + number of subscribers × contact pipeline throughput + buffer time`), and laid out the disaster-recovery handling (5-iteration limit + DLQ + dev notification on processing failure).

**Relevance:** Direct response to the team Slack debate about polling-vs-event-based completion detection (see file 13). The document is the resolution of that thread.

#### [Playbook - Campaign series](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1575780371/) — *2025-12-22, AJ space*
**Type:** Operational playbook
**Summary:** Explains the difference between Campaign Series and Journeys ("journeys are triggered per subscriber - each subscriber gets its own workflow instance. Whereas campaign series campaigns are functionally identical to normal campaigns"), glossary ("Campaign sequence - internal development term... Drip campaigns - initial product name"), feature flag (1110), link to the LDR, Datadog alert link.
**Relevance:** Onboarding doc for anyone joining the Campaign Series feature mid-flight.

#### [Bug Bash - Subscriber profile](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1897562113/) — *2026-03-13, AJ space*
**Type:** Bug-bash coordination page
**Summary:** Pre-release QA for the AJ-941 Subscriber Profile epic. Links to the response submission form.

## Pages he significantly contributed to (selected)

44 total. Notable ones:

- **[Engagement Score - CRM Lite Single Customer View](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1618739202/)** (the squad product lead, Mar 2026) — LDR-style page for the engagement-score addition to CRM-Lite. SQL team approved the approach. Clement was a contributor.
- **[Journeys Cheat Sheet / Playbook](https://campaignmonitor.atlassian.net/wiki/spaces/JO/pages/238698940/)** (a Journeys tribe engineer, multi-year edits, last Mar 2026) — The Journeys tribe's main internal playbook covering microservice architecture, single unified diagram, dashboards. Clement was a contributor.
- **[SRE Playbook - UpdateCustomField](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/318439606/)** (a teammate, Nov 2025) — UCF SRE playbook with the Slice 2: Referential addendum (Feb 2024) showing the gRPC-to-monolith arrow. Clement was a contributor (and the original UCF feature author).
- **[How to create a new CmAPI Domain Outpost](https://campaignmonitor.atlassian.net/wiki/spaces/EP/pages/1301512194/)** (a senior engineer, Jan 2026) — engineering productivity guide for standing up new CmAPI domain services. Clement contributed.
- **[Feature Flags (900 and onwards)](https://campaignmonitor.atlassian.net/wiki/spaces/DEV/pages/382566401/)** (a senior engineer, ongoing) — the central feature-flag registry. Clement contributed entries for every FF he added.
- **[Setup and run monolith locally](https://campaignmonitor.atlassian.net/wiki/spaces/DEV/pages/240617160/)** (a teammate, Jan 2026) — the canonical monolith setup guide. Clement contributed.
- **[GitHub Build Status Checks](https://campaignmonitor.atlassian.net/wiki/spaces/DEV/pages/531071038/)** (a senior engineer, Jun 2025) — how to wire TeamCity status checks into PRs. Clement contributed.
- **[Writing an LDR v2.0 (2025 edition)](https://campaignmonitor.atlassian.net/wiki/spaces/arc/pages/1400930327/)** (an architect, Dec 2025) — the LDR template itself. Clement contributed.

## Themes — what kinds of design problems does Clement gravitate toward?

1. **Schema/contract changes that touch many services** — every long-form authored doc involves at least one protobuf, MSSQL column, or Kafka topic decision.
2. **Coordination with platform / DBA / GDPR / SRE** before code is written — Confluence docs are the artifact of these prior conversations.
3. **"How does this whole system work?"** audit-style documents — Onboarding service, Signup Forms, CopyWorkflowService, ThirdPartyListImporter all got the treatment.
4. **Pre-release QA coordination** via bug bash pages — formalised the squad process.
5. **Operational/runbook contributions** — DMARC verification, Jenkins access tracking, Matillion upgrade postmortem, Node.JS upgrade guidance — non-feature work that keeps the team functional.

## Cross-reference notes

- The LDR ([arc/1593835523](https://campaignmonitor.atlassian.net/wiki/spaces/arc/pages/1593835523/)) corresponds to the PR cluster `AJ-985 / AJ-1019 / AJ-1030 / AJ-1039 / AJ-1115` and the bulk of the [createsend.com#22099 onwards](https://git.campmon.com/Freshview/createsend.com/pull/22099) work.
- The Onboarding tech investigation ([AJ/1368588295](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1368588295/)) corresponds to AJ-783-era epics. By Jan 2026 the lookback discussion in Slack (file 13) shows the project manager consulting it to confirm which option was taken.
- The CopyWorkflowService doc ([JO/238699043](https://campaignmonitor.atlassian.net/wiki/spaces/JO/pages/238699043/)) was a direct outcome of the MER-665 permission-check refactor in 2023.

---

## 🆕 2026-H2 pages (Jun–Nov 2026)
Full detail: [data/2026-h2/findings-confluence.md](data/2026-h2/findings-confluence.md).

| Page | Space | Role | Why it matters |
|---|---|---|---|
| [SMS: Twilio compliance embeddable](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/2451767325) | COMPOSE | **Author** | Tech audit + breakdown: scope (TFN in, sender ID blocked, 10DLC out), **sales-led-first decision**, no-rollback risk → staged rollout, 11-task plan, 7–11 day re-estimate. Credited on the PM's References page; adopted as Checkpoint 1 in the PM's Proposal |
| [Playbook: Drip campaigns (complex campaign series)](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/2350841928) | AJ | **Author** | Launch runbook: architecture, 7 metrics, 7 anomaly runbooks, instrumentation gaps. Outgoing TL: "the best playbook in either space; use it as the template" |
| [Creating a spoofed sales-led account for development](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/2471461091) | COMPOSE | **Author** | Unblocked SMS dev without Salesforce access; later scripted by a teammate |
| Playbook: CRM Lite data population error queues | AJ | Contributor | Ops follow-through on CRM Lite |
| Journeys Context Handover | AJ | **Named knowledge holder** | One of four people to book time with; Journey Designer + Commerce journeys expert |
| Engineering Teams | DEV | Member, Team Mitnick | Confirms the Boole → Mitnick merge |
