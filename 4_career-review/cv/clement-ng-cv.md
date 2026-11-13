# Clement Ng

**Senior Software Engineer · Full-stack (TypeScript / React / .NET) · Sydney**

[cng@meetmarigold.com](mailto:cng@meetmarigold.com) · GitHub: [cng](https://git.campmon.com/cng) · LinkedIn: _(add)_ · _(add: phone)_

---

## Summary

Senior full-stack engineer with five years' tenure at Campaign Monitor (acquired by Marigold), progressing from frontend developer through to **feature tech lead** on a tribe of ~10 engineers. Has shipped 532 PRs spanning 25+ repositories across six product domains — UX refresh, Campaign Authoring, SMS, Commerce/Shopify, Automation Recipes, and Journeys/CRM. Equally comfortable owning a vertical slice through React UIs, .NET Core services, gRPC protobuf contracts, and SQL Server schema design — and writing the Confluence design doc that gets it through architecture review. Recognised internally as the "JS Crew" reviewer of record for the createsend.com monolith.

---

## Core skills

- **Frontend:** TypeScript, React (16 → 18 + concurrent mode), Redux, react-beautiful-dnd, Sass, CMDS (in-house design system), Webpack (4 → 5), Vite, esbuild, Prettier/ESLint toolchains, Jest, Cypress, micro-frontends.
- **Backend:** C# / .NET Framework → .NET Core → .NET 9, ASP.NET Core, gRPC, SQL Server (stored procs, schema design, DBA collaboration), Kafka, AWS Lambda, DynamoDB, Couchbase, Redis.
- **Platform & infra:** Protobuf contracts, microservices on AWS ECS/Fargate, Terraform, Docker / Docker Compose, AWS Cognito, AWS SQS/SNS/SSM, Sentry, Datadog, Graylog, Segment, Amplitude.
- **Practice:** LDR / RFC authoring, multi-repo coordinated changes, feature-flagged release, GDPR-aware design, code review at scale, bug-bash coordination, technical screening for hiring.

---

## Experience

### Campaign Monitor / Marigold — Software Engineer → Senior Software Engineer / Feature Tech Lead
*Sydney, Australia · April 2021 – May 2026*

Email marketing SaaS used by tens of thousands of businesses. Shipped product features and platform work across the createsend.com monolith and its surrounding microservice mesh.

#### Selected achievements

**CRM Lite — Subscriber Profile (Q1 2026, feature tech lead)**
Owned the end-to-end design and delivery of CRM-Lite, a new "single customer view" surfacing each subscriber's data across all the lists they appear on. Drove pre-design DBA negotiations to land an `IsMasterList` column on `SU_Lists` instead of widening `CL_Clients`. Authored the [Architecture-space LDR](https://campaignmonitor.atlassian.net/wiki/spaces/arc/pages/1593835523/) covering protobuf contracts, Kafka event design, SQS queueing, and the scaling math (10M subscribers ≈ 84 min at 2k/s throughput). Personally drove GDPR race-condition handling with the platform team. Coached two junior engineers through their delivery; ran the [Bug Bash for the Subscriber Profile](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/1897562113/); owned the [prod-enablement flip](https://git.campmon.com/Freshview/createsend.com/pull/22680).

**Campaign Series v1 → v2 (Q4 2025 – Q2 2026)**
Designed and built the schema, backend service, and UI for Campaign Series — a new product feature allowing scheduled collections of campaigns distinct from per-subscriber journeys. Shipped the v1 backend → frontend → segment-tracking instrumentation in 8 separately-scoped sub-PRs, then took over the Complex Campaign Series v2 evolution (`CS_ComplexSequenceNodeTree` schema, tree-rendering backend, gRPC-fed condition types).

**Agency Partnership Status page (Q3 2025)**
Built a customer-facing status page for agency partner billing, including a new .NET 9 cron agent (`AgencyPerformanceReportAgent`) computing agency annual revenue. Delivered the backend + UI + bug-bash fixes + eligibility checks for `AJ-727`.

**WorkflowLookupService gRPC migration (Q2 2025)**
Designed a new `GetWorkflowStatusForWorkflowId` RPC, then migrated the WorkflowLookupService from the .NET Framework monolith into a netcore service. Three sequential revert-and-retry cycles to land cleanly under production load — demonstrates tenacity on hard platform changes. Spanned `platform/cm.protobuf` + the monolith + `runnerservice.core`.

**Journeys feature platform (2024 – 2025)**
Delivered four sequential journey-step features on the Audience-Journeys tribe: **UCF Advanced Expressions** (calc editor + plan-tier gating + FF rollout + cleanup); **Wait-Until step** (DB schema + persistence + cross-DB copy for journey clone + CAL/GDPR scrubbing); **Send-a-Test for journey email** (cm-api refactor + click tracking); **Condition Path Swap** (feature-flagged UI + monolith endpoint + GDPR-audited CAL logging). Each shipped across both the monolith and the workflow-builder microservice repos.

**Bloom Bootstrap greenfield prototype (Sept 2024)**
Bootstrapped a new product prototype from zero — docker compose with watch mode, AWS Cognito server + React-client auth, change-password flow, gobot Slack integration. Two-week burst that established DevX for the team. Acted as tech-lead reviewer for two teammates on the prototype.

**Commerce / Shopify Migration Assistant (2023, primary engineer)**
Owned the Shopify migration assistant frontend, the new Commerce Management landing pages, the cross-service reimport flow, and the automation recipes feature. Touched the monolith, `cm.protobuf`, `ThirdPartyListImporter`, `campmon.hex`, and the workflowcontext copy-service family in coordinated multi-repo changes. Delivered cross-service permission checks for email-template copy (`MER-665`) landing across four services in one PR set.

**SMS Product end-to-end (2022, primary engineer)**
72 SMS-tagged PRs across 9 repos in 12 months: full-stack delivery of SMS sends, reporting (link tracking, clicks, bounces), geo expansion (country add/remove, phone-number lookup), hosted/copypaste signup forms, and preference-center consent. Designed and landed the SMS link-tracking topic taxonomy across `cm.protobuf`, `kafka-acls`, `jvm-libs`, and `TrackingServices`.

**createsend.com JS toolchain modernisation (2022 – 2026, JS Crew)**
Led the createsend.com frontend modernisation as a recurring secondary thread of work: yarn workspaces (2022), Vite change-day (2022), esbuild-loader for dev builds (2022), Node 16 LTS bump with Windows agents (2022), TypeScript 4 upgrade (2022), Prettier 2.7 rollout in three-PR batches (2022 ×2), React 18 bundle-by-bundle concurrent-mode migration (2025), Node 22→18.20.8 LTS dance (2025), Webpack 5 upgrade (2026). Maintained the JS-crew Confluence reference docs for Node bumps.

**Customer Lifecycle — async subscriber export streaming (2023)**
Implemented async stream-writer-based subscriber export behind FF 838 — performance-aware backend work at scale.

**Client Overview UX Refresh (2021, onboarding feature)**
Year 1 feature lead on the UX1 client-overview redesign. Built Bulk Delete Lists (FF 538), drag-and-drop custom-fields table (contributing back to the in-house CMDS design system), delete-custom-field dependency checking. Coordinated four-repo QA-hook changes (`UX1-490`) across CMDS, createsend.com, TestingCore, and TestAutomation in a single week.

#### Operating signals

- **Code review at scale:** 558 PRs reviewed for 128 distinct teammates; 466 substantive review comments captured. The reviewer-to-author ratio crossed 2.0× by Year 5 — the senior-IC indicator.
- **Design-doc-first practice:** Authored 21 Confluence pages including an LDR in the Architecture space; contributed to 44 more (the architects' LDR template, the JS-crew toolchain refs, multiple SRE playbooks).
- **Cross-functional coordination:** Drove DBA, GDPR, SRE, platform, and product conversations *before* publishing implementation plans. Confluence docs are the artifact of the prior chats.
- **Hiring:** Acted as technical screener for mid-level engineering candidates. Made hire/no-hire calls on take-home code samples.
- **Production response:** Late-night P2 debugging (Feb 2026 enterprise-customer incident; Oct 2024 Insights/Matillion outage), with structured walkups posted to team channels.

---

## Selected open-source / design-system contributions

- **CMDS (in-house React design system):** Multiple contributions over five years including [Table Tr ref passthrough](https://git.campmon.com/CMDS/cmds/pull/1895), [RowAtionsData interface export](https://git.campmon.com/CMDS/cmds/pull/1875), CM-Header QA hooks, dialog z-index fixes. Type-utility contributions to `@cmds/cm-utils` (isNil, isNullOrEmpty type fixes).

---

## Tooling and methodology

- **Internal:** LDR (Lightweight Design Review) v2.0 framework — contributor to the template itself. Bug-bash QA coordination — ran 4 squad bug bashes between 2024 and 2026.
- **Industry:** TypeScript-strict, BEM, hooks-first React, GDPR-by-design, feature-flag-gated releases, observability via Sentry + Datadog + Graylog + Segment tracking plans.

---

## Education

_(add)_

## Languages

_(add)_

---

*Source data underlying this CV: 532 authored PRs + 558 reviewed PRs + 466 review comments + 21 Confluence design docs + Slack discussion mining (May 2026 review). Full dataset and analysis at [career-review/](../README.md).*
