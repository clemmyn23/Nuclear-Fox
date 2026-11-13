# Notable PRs — a curated highlight reel across 5 years

These are the PRs that best represent your trajectory — biggest features, multi-repo coordinations, tooling milestones, and the bonus "interesting in retrospect" entries.

**For full context, many of these PRs are accompanied by Confluence design docs ([14-confluence-design-docs.md](14-confluence-design-docs.md)) and Slack design conversations ([13-slack-architecture-discussions.md](13-slack-architecture-discussions.md)).** Cross-references are noted inline where relevant.

## Year 1

### 2021-04-08 — First PR — onboarding work
[UX1-400 Add recipients column to Recently sent campaigns](https://git.campmon.com/Freshview/createsend.com/pull/9381)

_Your first PR on the company GitHub. Small but real product change._

### 2021-05-17 — First feature ownership
[UX1-437 Bulk Delete Lists (rest of the owl)](https://git.campmon.com/Freshview/createsend.com/pull/9755)

_A multi-week feature you owned end-to-end including the feature flag. The PR title "the rest of the owl" is a classic — the whole feature in one PR after the prep work._

### 2021-05-28 — First design-system contribution
[UX1-474 Table Tr ref passthrough](https://git.campmon.com/CMDS/cmds/pull/1895)

_First PR contributing back to the in-house design system. Signal that your work was trusted beyond your immediate squad._

### 2021-05-31 — End-to-end drag-and-drop
[UX1-474-b Drag Drop table for custom fields](https://git.campmon.com/Freshview/createsend.com/pull/9899)

_Required upgrading react-beautiful-dnd + design-system PR + the actual feature. Multi-PR coordination._

### 2021-06-22 — Cross-component dependency check
[UX1-519 Delete custom fields dialog dependency checks](https://git.campmon.com/Freshview/createsend.com/pull/10096)

_Workflow-aware deletion — knew which workflows used a field before allowing deletion. Sophisticated UX._

### 2021-08-09 — First cross-app analytics
[UX1-580 Extend WorkflowInitiationContext for page referrer](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/68)

_First PR outside the monolith. Cross-app tracking instrumentation._

## Year 2

### 2022-04-19 — Build system overhaul begins
[Setup yarn workspaces](https://git.campmon.com/Freshview/createsend.com/pull/12692)

_Kicked off the multi-quarter JS toolchain modernisation._

### 2022-05-12 — Vite change-day
[[Change-day] Vite build 1](https://git.campmon.com/Freshview/createsend.com/pull/12854)

_Big infrastructure change requiring whole-team coordination._

### 2022-06-17 — First protobuf contract
[SMS-155 Add SMS link tracking topics](https://git.campmon.com/platform/cm.protobuf/pull/588)

_First time landing changes in the platform protobuf repo — designing the contract for a feature you'd then implement everywhere else._

### 2022-07-04 — Node 16 LTS upgrade
[Update Node.js to 16.15.1 LTS](https://git.campmon.com/Freshview/createsend.com/pull/13212)

_Whole-codebase runtime upgrade. Also patched the Windows CI agents in [aws.stack.build#83](https://git.campmon.com/operations/aws.stack.build/pull/83). **Also wrote the [JS-crew Node bump reference doc](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/238686695/) the same week** — every Node bump after refers back to it._

### 2022-08-26 — esbuild dev mode
[Use esbuild-loader for development JS builds](https://git.campmon.com/Freshview/createsend.com/pull/13540)

_Made local dev faster for everyone._

### 2022-10-18 — TypeScript 4 upgrade
[Typescript 4 - upgrade and fix](https://git.campmon.com/Freshview/createsend.com/pull/13877)

_Whole-codebase TS upgrade. Big diff, careful work._

## Year 3

### 2023-06-01 — Commerce Management landing
[MER-394-a Commerce Management landing page for new customers](https://git.campmon.com/Freshview/createsend.com/pull/15434)

_First customer-facing page in the new Commerce experience._

### 2023-06-29 — Shopify reimport across services
[MER-536 Rerun shopify list import](https://git.campmon.com/Freshview/createsend.com/pull/15631)

_Touched monolith + cm.protobuf + ThirdPartyListImporter + campmon.hex coordinated._

### 2023-08-11 — Subscriber export streaming behind FF
[CL-9-f Implement FF 838 SubscriberExport](https://git.campmon.com/Freshview/createsend.com/pull/15938)

_Async stream-writers behind feature flag — performance work at scale._

### 2023-09-18 — Cross-service permission contract
[MER-665 Permission check on email-template copy (service)](https://git.campmon.com/Engineering/workflowcontext.copyworkflowservice.core/pull/19)

_Three-repo coordinated permission change: monolith + service + datastores. **Spawned the [CopyWorkflowService Confluence walkthrough](https://campaignmonitor.atlassian.net/wiki/spaces/JO/pages/238699043/) six months later** — having mapped the queue topology to land this PR, you wrote the doc that onboards new AJ engineers to the codebase._

### 2024-03-11 — AJ tribe debut
[AJ-194-a Enable save only when custom-field form values change](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/191)

_First PR in the AJ tribe codebase — sets up Years 4 and 5._

## Year 4

### 2024-05-07 — UCF Advanced Expressions UI
[AJ-311-a Custom field advanced expressions UI](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/208)

_First major AJ tribe feature — multi-PR delivery culminating in FF cleanup._

### 2024-07-16 — Wait-Until step backend
[AJ-400-a Save workflow wait-until step data into db](https://git.campmon.com/Freshview/createsend.com/pull/17852)

_DB schema + persistence + action/config models. Backend chops on display._

### 2024-08-08 — Infra with PITR + deletion protection
[AJ-369-a Upgrade terraform and enable dynamodb backups](https://git.campmon.com/Engineering/workflowbuildercontext.sampleeventpageservice.core/pull/24)

_Terraform + DynamoDB PITR + deletion protection. Senior-IC infra-aware work._

### 2024-09-13 — Bloom greenfield kickoff
[BTB-09-a Hook up aws cognito for server](https://git.campmon.com/Deprecated/bloom-app/pull/6)

_Started a project from zero — AWS Cognito server-side auth. Demonstrated greenfield muscle._

### 2024-11-12 — Create segment from campaign report
[AJ-494-a Create segment from campaign report](https://git.campmon.com/Freshview/createsend.com/pull/18413)

_Cross-cutting feature touching reports, lists, worldview, A/B reports, templates. **Companion Confluence pages** captured the product rationale ([Create segment from campaign report page](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/847052808/)) and the pre-release [Bug Bash coordination](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/847446022/) — first of the four squad bug bashes you organised._

### 2025-01-14 — Condition path swap with GDPR audit
[AJ-488 Swap condition paths](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/280)

_Feature-flagged UI + monolith endpoint + CAL logging with GDPR audit verifying internals weren't leaked._

### 2025-02-17 — Failure-reason RPC contract
[AJ-575 Add WorkflowFailureReason to ClientTimezoneFromWorkflowResponse](https://git.campmon.com/platform/cm.protobuf/pull/796)

_Three-repo gRPC change: protobuf + runner service + monolith._

## Year 5

### 2025-04-02 — WorkflowLookupService RPC design
[AJ-603 Add rpc GetWorkflowStatusForWorkflowId](https://git.campmon.com/platform/cm.protobuf/pull/814)

_Started the WorkflowLookupService gRPC migration that defined Q2 2025._

### 2025-05-08 — Third-try platform migration
[AJ-603-b Migrate workflow lookup service to netcore [Third try]](https://git.campmon.com/Freshview/createsend.com/pull/19811)

_After two reverts, landed the netcore migration. Tenacity in the diffs._

### 2025-07-18 — Compute agency annual revenue
[AJ-691/699 Compute agency annual revenue](https://git.campmon.com/Freshview/createsend.com/pull/20317)

_Cron agent on .NET 9 computing agency revenue — backend chops for a customer-impact feature._

### 2025-08-22 — Agency Partnership Status page
[AJ-727 Agency partnership status page - part 1](https://git.campmon.com/Freshview/createsend.com/pull/20598)

_Customer-facing status page end-to-end including eligibility checks and bug-bash fixes._

### 2025-10-31 — Campaign Series backend kickoff
[AJ-891-a Campaign sequence - Backend part 1](https://git.campmon.com/Freshview/createsend.com/pull/21140)

_Started the Campaign Series v1→v2 workstream that ran through Q4 2025._

### 2026-01-30 — CRM Lite list population
[AJ-1039-b Start crm list population process on feature opt-in](https://git.campmon.com/Freshview/createsend.com/pull/22099)

_Bootstrap of the new CrmLite list-population pipeline — first PR of the CRM Lite Subscriber Profile feature. **Implements the [LDR - CRM-lite initial list population](https://campaignmonitor.atlassian.net/wiki/spaces/arc/pages/1593835523/)** published two days earlier in the Architecture space — the doc preceded the code. The schema decisions in this PR are the outcome of [Slack DBA negotiations with a DBA](https://campaignmonitor.slack.com/archives/D03V82VP47R/p1763094094937379) and [Slack GDPR design discussions with a platform engineer](https://campaignmonitor.slack.com/archives/D03LTAWLFL2/p1768884819587579) from Nov 2025–Jan 2026._

### 2026-02-17 — CRM Subscriber Profile frontend
[AJ-1063-a CRM Subscriber profile page frontend - part 1](https://git.campmon.com/Freshview/createsend.com/pull/22291)

_Three-part frontend delivery for the CRM Lite Subscriber Profile._

### 2026-03-27 — Prod enablement flip
[AJ-crm-release-prod Turn on contactmanagementscheduledagent in prod](https://git.campmon.com/Freshview/createsend.com/pull/22680)

_Owned the actual production enablement — the moment the feature is live for customers. Two weeks earlier you ran the [Bug Bash for the Subscriber Profile](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1897562113/) to validate the feature before flip._

## Year 6

### 2026-04-13 — Complex Campaign Series backend
[AJ-1115-b Implement complex campaign series backend](https://git.campmon.com/Freshview/createsend.com/pull/22857)

_Currently in flight — the v2 evolution of Campaign Series._

### 2026-05-28 — Most recent PR
[AJ-1196-d Pass IsJourneyReportingEnabled feature flag to workflow ui](https://git.campmon.com/Freshview/createsend.com/pull/23356)

_Your latest PR as of this review._

---

## Cross-source: where the design lived before the code

Many of the most substantial PRs above have a **Confluence design doc that preceded them** and a **Slack thread that informed the design**. The triple-source view:

| PR | Confluence | Slack |
|---|---|---|
| `Node 16 LTS` ([#13212](https://git.campmon.com/Freshview/createsend.com/pull/13212)) | [Upgrading Node.JS on build agents](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/238686695/) (same week) | — |
| `MER-665 perm checks` ([#19](https://git.campmon.com/Engineering/workflowcontext.copyworkflowservice.core/pull/19)) | [CopyWorkflowService and how it works](https://campaignmonitor.atlassian.net/wiki/spaces/JO/pages/238699043/) (6mo later) | — |
| `AJ-494 Create segment` ([#18413](https://git.campmon.com/Freshview/createsend.com/pull/18413)) | [Create segment page](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/847052808/) + [Bug bash](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/847446022/) | — |
| `Onboarding rework AJ-783-era` | [Tech audit](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1362067562/) + [Tech investigation](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1368588295/) + [Technical approach](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1389854769/) | [Onboarding stats request](https://campaignmonitor.slack.com/archives/C028YGQLACS/p1758519199984599) (Sep 2025) |
| `AJ-985/1039 CRM-Lite list pop.` ([#22099](https://git.campmon.com/Freshview/createsend.com/pull/22099)) | **[LDR in Architecture space](https://campaignmonitor.atlassian.net/wiki/spaces/arc/pages/1593835523/)** | [DBA negotiation](https://campaignmonitor.slack.com/archives/D03V82VP47R/p1763094094937379) + [GDPR design](https://campaignmonitor.slack.com/archives/D03LTAWLFL2/p1768884819587579) + [DBA release plan](https://campaignmonitor.slack.com/archives/D07T8R5SYUA/p1770682795839669) |
| `AJ-1044 list-pop status` (multi-PR) | [Updating CRM list population job status](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1819312139/) | [Distributed-work completion design debate](https://campaignmonitor.slack.com/archives/C028VG4K5TP/p1771368788702119) |
| `AJ-1063 Subscriber Profile FE` (multi-PR) | [Bug Bash — Subscriber profile](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1897562113/) | [Figma reviews with Yuri](https://campaignmonitor.slack.com/archives/D0B2B3DAHLM/p1778204426277409) |

The Year 5 CRM-Lite row is the densest — three different Slack DMs across DBA / GDPR-platform / DBA-DB feeding into a single LDR which then drives ~15 PRs.

---

## 🆕 2026-H2 highlight reel (Jun–Nov 2026)

| PR | Why it's notable |
|---|---|
| [createsend.com#25046](https://git.campmon.com/Freshview/createsend.com/pull/25046) COM-1700 | **Idempotent SMS provisioning**: create customer → buy/reuse toll-free number; client-derived requestId; region check before purchase; typed upstream errors; "Decisions worth a look" section; 1,957 tests green |
| [createsend.com#25080](https://git.campmon.com/Freshview/createsend.com/pull/25080) COM-1701 | **Merged 3 duplicate provisioning flows into one service**; known-gaps section; 2,264 tests green |
| [createsend.com#25163](https://git.campmon.com/Freshview/createsend.com/pull/25163) COM-1733 | Australian alphanumeric sender IDs; concurrent-init handling |
| [createsend.com#23545](https://git.campmon.com/Freshview/createsend.com/pull/23545) AJ-1186 | **Schema decision with an audit**: new `SendingAgentType` column (7 additive files vs 20–30 incl. hot send procs); debt logged separately |
| [createsend.com#23585](https://git.campmon.com/Freshview/createsend.com/pull/23585) AJ-1149-a | Killed your own timeline-gutter design early, with the reason written down |
| [createsend.com#23711](https://git.campmon.com/Freshview/createsend.com/pull/23711) AJ-1149-d | Drip canvas scheduled date/time/GMT offset; tree-utils restructure (+1,007/−464) |
| [createsend.com#25020](https://git.campmon.com/Freshview/createsend.com/pull/25020) JC-412 | Frontend build in Docker with byte-level parity; caught Closure exiting 0 on errors |
| [createsend.com#25593](https://git.campmon.com/Freshview/createsend.com/pull/25593) JC-414 | Per-pipeline flag rollout + **disaster-recovery section** (draft) |
| [updatecustomfield#73](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/73) COM-1625 | Cross-team regression root-caused; DLQ follow-ups; "great detective work" |
| [GitHubTeamManagement#7](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/7) | Escaped user content in Slack notifications after restoring the org-wide bot |
| [createsend.com#24483](https://git.campmon.com/Freshview/createsend.com/pull/24483) | Hex resource-ownership page: "the less manual SQL I execute against prod dbs, the better" |
| BrandHubServices #81–86 | AI-DLC Node→C# port (+16.4k; 307/307 + 72/72 tests), **deliberately not shipped** |
