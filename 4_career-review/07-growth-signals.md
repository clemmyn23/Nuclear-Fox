# Growth signals — what the data shows about your trajectory

This file synthesises patterns across all 5+ years that don't fit cleanly inside a single yearly write-up.

## 1. Scope per PR grew while count per year shrank

- **Year 1** (159 authored, 87 reviewed)
- **Year 2** (131 authored, 116 reviewed)
- **Year 3** (84 authored, 90 reviewed)
- **Year 4** (66 authored, 84 reviewed)
- **Year 5** (77 authored, 159 reviewed)
- **Year 6** (15 authored, 22 reviewed)

Authoring count is a misleading proxy for productivity. Year 1's 159 PRs include things like *"Move filter button in suppressions list"* and *"Update header to 'Subscription opt-in'"*. Year 5's 92 PRs include *"Migrate WorkflowLookupService to netcore"* (three sequential reverts/retries to land) and *"Implement complex campaign series backend"*. The PR-to-scope ratio has shifted significantly.

## 2. Repo breadth widened then re-focused (peak in Y3)

| Year | Distinct repos (authored) | Distinct repos (reviewed) |
|---|---:|---:|
| Y1 | 9 | 4 |
| Y2 | 12 | 12 |
| Y3 | 14 | 11 |
| Y4 | 13 | 8 |
| Y5 | 7 | 17 |
| Y6 | 2 | 6 |

Year 3 is the peak-breadth year because Shopify integration touched the most surface area (monolith + cm.protobuf + ThirdPartyListImporter + HEX + workflowcontext.copyworkflowservice). Year 5+ has fewer repos but deeper changes inside each.

## 3. Reviewer role grew from peer to anchor

| Year | Authored | Reviewed | Reviewed / Authored |
|---|---:|---:|---:|
| Y1 | 159 | 87 | 0.55x |
| Y2 | 131 | 116 | 0.89x |
| Y3 | 84 | 90 | 1.07x |
| Y4 | 66 | 84 | 1.27x |
| Y5 | 77 | 159 | 2.06x |
| Y6 | 15 | 22 | 1.47x |

Y1–Y3 you reviewed roughly as much as you authored. From Y4 onwards reviewing dominates — Y5 has a 2.0x ratio. This is the unmistakable senior-IC signal: you're a load-bearing reviewer on your tribe.

## 4. The JS-crew steward identity is constant across all 5 years

Every year has a substantial chunk of infra/tooling PRs *not* tied to a feature ticket:

| Year | Notable tooling/infra work | PR count w/o JIRA key |
|---|---|---:|
| Y1 | Drag-drop upgrade for custom fields, UI-UX-Refresh test cleanup, Iso8601 date formatting, force-https assets | 23 |
| Y2 | Yarn workspaces, Vite change-day, esbuild-loader, Node 16 LTS, TypeScript 4, Prettier 2.7 (×2), SMS sentry monitoring | 53 |
| Y3 | React Server Components POC ([teammate]/cm-rsc), cm-nexus HTTPS migration, Lerna pin, Node 18 proxy, Consul docker upgrade | 29 |
| Y4 | Terraform upgrade + DynamoDB PITR, eslint/prettier upgrade in workflowbuildercontext, package vulnerability bumps, build pipeline repairs | 14 |
| Y5 | React 18 bundle-by-bundle migration, Node 22→18.20.8 LTS, openssl legacy fallback, cross-env build:faster, sass-loader migration, .NET 9 upgrade, modernise localdev proxy | 21 |
| Y6 | Webpack 5 upgrade pt 2, GrpcClient v2 migration, pnpm workspace TS pinning, GitHub bot improvements | 2 |

142 of 532 (27%) of your authored PRs have no JIRA prefix. Many of these are tooling/infra changes — this is the part of the work that doesn't get sprint-planned but matters enormously to everyone else.

## 5. Multi-repo coordination is your move

A consistent pattern: when work spans contracts (protobuf) + backend + frontend + tests, you carry it through:

| Year | Multi-repo feature | # repos touched |
|---|---|---:|
| Y1 | `UX1-490` cm-header QA hooks | 4 (CMDS + createsend.com + TestingCore + TestAutomation) |
| Y1 | `UX1-580` page-referrer analytics | 2 (createsend.com + workflowbuildercontext.uiservice.core) |
| Y2 | `SMS-155` SMS link tracking | 5 (cm.protobuf + TrackingServices + kafka-acls + jvm-libs + createsend.com) |
| Y2 | `SMS-137` contact_id on SMS bounce/opt-out | 3 (cm.protobuf + SmsSendingServices + createsend.com) |
| Y3 | `MER-536` Shopify reimport | 4 (createsend.com + cm.protobuf + ThirdPartyListImporter + campmon.hex) |
| Y3 | `MER-665` permission check on email-template copy | 4 (createsend.com + copyworkflowservice.core + copyworkflowservice-datastores ×2) |
| Y4 | `AJ-575` `WorkflowNotFound` failure-reason | 3 (cm.protobuf + runnerservice.core + createsend.com) |
| Y5 | `AJ-603` WorkflowLookupService netcore migration | 2 (cm.protobuf + createsend.com — but multiple sub-PRs) |
| Y6 | `AJ-1196` IsJourneyReportingEnabled FF | 2 (runnerservice.core + createsend.com) |

## 6. Tenacity in the diffs

Three reverts and retries for **AJ-603 WorkflowLookupService netcore migration** ([first try](https://git.campmon.com/Freshview/createsend.com/pull/19409), [Second try](https://git.campmon.com/Freshview/createsend.com/pull/19705), [Third try](https://git.campmon.com/Freshview/createsend.com/pull/19811)) — Y5. Prettier-eslint rollout in three batches (config / auto-fix / manual cleanups) because the first two PRs revealed problems — Y2. Two attempts at SMS hosted-form HTTPS forcing because of edge cases — Y2. The work isn't always linear, and the trace shows you push through rather than abandon.

## 7. Greenfield + brownfield

Bloom Bootstrap (Y4, Sept 2024) was you setting up a project from zero — docker compose with watch mode, AWS Cognito server+client, change-password flow, Slack gobot integration, basic UI. Five PRs in two weeks taking the project from empty to working DevX.

Everything else has been deep-stack changes in existing systems — the Y5 WorkflowLookupService migration is the opposite end: extracting a service from a 15-year-old monolith. Both skill sets are visible.

## 8. Clean squad transitions, every time

| Transition | When | Pattern |
|---|---|---|
| UX1 → CA | Aug–Oct 2021 | First CA-982 PR while still finishing UX1-580. Reviews stay on UX1 partners for a month then shift. |
| CA → SMS | Mar–Apr 2022 | Last CA PR Feb 2022, first SMS PR April 2022. One-month overlap absorbed into infra/tooling work. |
| SMS → MER/CL | Mar–Apr 2023 | SMS-543/583 wraps in March; MER-401 lands in April. Quick switch. |
| MER → AJ | Mar 2024 | First AJ-194 PR while still on MER tail. Reviews already shifted to EL/PP by Q4 2023. |
| AJ + Bloom side-project | Sept 2024 | Two-week prototype burst then back to AJ tribe full-time. |

No half-finished work trailing behind. Each transition shows a few weeks of overlap then a clean handover.

## 9. Languages and stacks crossed

Touched repos suggest these technologies:

- **Frontend:** React (16 through 18), TypeScript (3.x through 5.x), Webpack 4/5, Vite, esbuild, Prettier, ESLint, react-beautiful-dnd, CMDS (in-house design system), eslint configs
- **Monolith backend:** .NET Framework → .NET Core → .NET 9 (Year 5), C#, SQL Server stored procs
- **Microservices:** Java/Kotlin (workflowcontext.* family), gRPC + protobuf, Kafka, AWS Lambda
- **Data:** DynamoDB (PITR), Redis → Couchbase migration in PLAT, SQL Server
- **Infra:** Terraform, Docker + Docker Compose, AWS Cognito, JUnit, Sentry, Datadog, Amplitude/Segment
- **Mobile-adjacent:** Hosted/copypaste signup forms with IE11 polyfills (Year 2 SMS work)

## 10. Design-doc-first practice emerged in Year 2 and matured into Year 5

Confluence-authored pages per year shows a clear arc:

| Year | Pages authored | Notable docs |
|---|---:|---|
| Y1 | 0 | (none — heads-down learning) |
| Y2 | 3 | Node.JS-on-build-agents (JS-crew ref), Signup Forms tech audit |
| Y3 | 3 | CopyWorkflowService deep-dive (still used to onboard new AJ engineers) |
| Y4 | 4 | Bug-bash organising starts; Matillion postmortem |
| Y5 | 9 | **LDR in Architecture space**; onboarding investigation matrix; CRM-Lite design |
| Y6 | 0 | (continuing prior LDRs as live references) |

Year 5 is the inflection: an LDR in the official `arc` Architecture space, an architect-approved technical-approach doc (an architect signed off the Onboarding rework table design), and resolution of in-chat design debates into written form. That's where the senior-IC pattern becomes visible in writing, not just in code. See [14-confluence-design-docs.md](14-confluence-design-docs.md).

## 11. Chat-first design conversations seed the Confluence docs

For Year 5 CRM-Lite specifically, the pattern is: **chat → doc → PR**.

- DBA negotiation in Slack DM with a DBA (Nov 14, 2025) → schema decisions captured in the LDR (Jan 28, 2026).
- GDPR-race-condition discussion in Slack DM with a platform engineer (Jan 20, 2026) → Privacy-by-Design section of the LDR.
- Polling-vs-event-based completion-detection debate in #cm-team-boole-dev (Feb 18, 2026) → "Updating CRM list population job status on completion" doc (Feb 23, 2026).
- Onboarding survey statistics request in #cm-team-boole-eng-prod (Sep 22, 2025) → 3-option Onboarding tech investigation doc (Oct 8, 2025).

The Confluence doc is the *artifact* of the prior conversations, not the start of them. Visible across [13-slack-architecture-discussions.md](13-slack-architecture-discussions.md) ↔ [14-confluence-design-docs.md](14-confluence-design-docs.md).

## 12. Operating signals beyond code

- **Hiring authority** (Y5, Oct 2025) — technical screener for mid-level engineering candidates; made hire/no-hire calls on take-home code samples.
- **Bug-bash organiser** — 4 sessions across Y4–Y6 for major features (Create Segment from Campaign Report, Remove Subscribers, Subscriber Notes, Subscriber Profile).
- **Production-response writeups** — Insights/Matillion outage (Oct 2024), Enterprise-customer P2 (Feb 2026, 11pm–1am with a teammate).
- **Strategic communication** — summarised the VP-Engineering's Kairos all-hands video for the team (Oct 2025); filed structured AI-work-log entries during the May 2026 Innovation Sprint with honest time-delta estimates.

---

## 13. 2026-H2: from steward to owner (added 2026-11-10)

The six months after the May review show the clearest step change since Year 2:

| Signal | Before (Y1–Y5 pattern) | Jun–Nov 2026 |
|---|---|---|
| Who assigns you work | Squad backlog; tooling you chose yourself | **EM hands you the top-priority ambiguous project** ("would you be up for taking the discovery piece") |
| Your role on features | Feature tech lead once (CRM Lite) | De-facto **technical lead** on SMS onboarding; **launch-readiness owner** on Drip Campaigns; sole frontend owner on Brand Hub V2 |
| Decisions | Mostly in review comments and LDRs ratified by architects | **Rollout staging, staffing proposal, API design, scope cuts, schema defence**, written into the plan and adopted |
| Cross-team | Negotiated with DBA/platform inside your own feature | **Changed another team's API** (chicken-egg), traced a regression to another team's PR without blame |
| After launch | Rarely visible | Dashboards, alerts, runbook, "live on all prod DBs" to SRE; runbook reused by others |
| Tooling | Yearly upgrades, no numbers | Cross-team epic **with a measured result** (−41% deploy package build) |
| AI | Time-saving logs | **Judgment about AI**: called out a 2.5-day AI loop; the experiment became a no-go decision |
| Org resilience | Stable team | TL left, team merged, 3 departures. You held Journeys context and took the new team's top priority |

**Read-across to interviews:** this is the evidence that was missing when interviewers said "show ownership". See [interview/ownership-and-decisions.md](interview/ownership-and-decisions.md).

**The remaining gap** is the **title** and the **measured outcome**. You were technical lead in practice, never by title, and adoption numbers aren't yet pulled. Both are fixable in the next 3 months: ask for the named TL role on SMS Checkpoints 2–3 and run the Drip 90-day readout (ownership-and-decisions §4).
