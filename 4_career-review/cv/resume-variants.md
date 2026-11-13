<!--
ROLE-TARGETED RÉSUMÉ VARIANTS — three angles on the same true facts.
Base: cv/clement-ng-resume-2page-draft.md. Does NOT replace any existing draft.
Pick the variant matching the role you're applying to. Shared sections (Earlier Experience / Education / Skills) are repeated in each so any one variant is copy-paste standalone.
No invented metrics. [verify] = real but worth your own gut-check before sending.
-->

# Role-Targeted Résumé Variants

> **🆕 2026-11:** the base is now [clement-ng-resume-2026-11.md](clement-ng-resume-2026-11.md). For any variant, **replace the first two CM bullets with these** (then trim older bullets to fit):
> - **Variant A (Staff/Senior+ IC):** use the SMS technical-lead bullet + the Drip builder/launch bullet verbatim from the 2026-11 base; keep CRM Lite third; collapse JS Crew/toolchain into the Docker-builds bullet (with "~41% faster").
> - **Variant B (EM/Tech Lead):** lead with *"Technical lead, SMS onboarding: wrote the plan, documented the staged rollout, proposed the team split (adopted by the team lead); coordinated PM, design and a partner platform team; dev-complete in ~2 months."* Add *"Held Journeys context through a TL departure and team merge; named the Journey Designer knowledge holder in the handover."*
> - **Variant C (Backend/Platform):** lead with *"Designed an idempotent provisioning API over a third-party compliance provider: client-derived idempotency keys, validate-before-spend, typed upstream errors; consolidated three provisioning paths into one service."* Then the `SendingAgentType` send-pipeline routing decision and the Docker build migration.
> The variants below are the **June 2026** versions.

Three angles, same facts, different emphasis. Use the one that matches the job posting:
- **Variant A — Staff / Senior+ IC** → "Staff Software Engineer", "Senior+/Principal", deep-technical product cos.
- **Variant B — Engineering Manager / Tech Lead** → EM, Tech Lead, Head of Engineering/IT (esp. smaller orgs).
- **Variant C — Backend / Platform Engineer** → backend, platform, distributed-systems, infra-leaning roles.

---
---

# VARIANT A — Staff / Senior+ IC

## Clement Ng
**Staff-track Software Engineer** — Sydney · +61 413-424-888 · clementng23@gmail.com · [linkedin.com/in/clemchowder](https://www.linkedin.com/in/clemchowder/)

Full-stack engineer, 8+ years, who owns features from design doc to production across React/TypeScript, .NET/C#, and gRPC/Kafka. Reviewer-of-record for a large email-marketing monolith; authors the architecture docs other engineers build from; persists through hard multi-repo platform migrations. Also runs the IT function for a 45,000-attendee convention — proof the technical-leadership scope is real, not aspirational.

### Experience

**Software Engineer — Campaign Monitor (Marigold)** · Apr 2021 – Present
*Depth, breadth, and standards-setting across the createsend.com monolith + microservice mesh (6 product domains).*
- **Designed and led CRM Lite (single-customer-view) end-to-end** — wrote the LDR through the architecture-review process, defined the protobuf/Kafka contracts and a paged backfill pipeline sized for multi-million-contact lists, and owned it to production. [verify]
- **Architected multi-repo, contract-first changes** as a default — permission-checking and failure-handling features landing across 3–4 repositories (monolith + protobuf + microservices + datastores) in single coordinated sets.
- **Migrated a workflow-lookup service from the .NET-Framework monolith to a standalone .NET Core gRPC service**, persisting through multiple production-load iterations to land it cleanly.
- **Set front-end engineering standards as a JavaScript Crew member** — reviewed JS merges org-wide, owned shared libraries/build tooling, and drove modernisation: yarn workspaces, Vite/esbuild, Node LTS, TypeScript 4→5, React 18 concurrent mode, Webpack 5.
- **Built the SMS product as a full vertical slice** — React UI → CmAPI → gRPC services → link-tracking topic taxonomy across protobuf, Kafka ACLs, and shared messaging libs.
- Authored **20+ architecture/reference docs** used to onboard engineers; **screened engineering candidates**; mentored juniors. Across the tenure: **authored 530+ and reviewed 550+ PRs across 120+ engineers.** [verify]

*Tech: C#/.NET (Framework→Core→9), TypeScript/React (16→18), gRPC + protobuf, Kafka, MSSQL, DynamoDB, Terraform, AWS.*

### Earlier Experience
**Associate Software Developer — WiseTech Global** · May 2019 – Mar 2021 — Sole owner of the AIS ship-tracking system (React/TS/Google Maps) serving all CargoWise customers; maintained MAWB air-cargo automation (C#, MSSQL).
**Software Engineer — EdApp LMS** · Feb 2018 – May 2019 — Peer-authoring templates and mobile features (React Native/Backbone/Cordova); push-notification audit logging; 24/7 on-call, CI/CD.

### Engineering Leadership (Volunteer)
**Director of IT / Asst. IT Director / Software Developer — SMASH! Inc.** · Nov 2018 – Present — Founding engineer (built the original ticketing + mobile-scanning system for 40,000+) who grew into Director of IT: now lead Engineering/Systems/Support, 25 volunteers/3 leads; set Board-level IT strategy; accountable for ticketing, networking, and incident response for 45,000+ attendees; 5 consecutive conventions, zero critical IT failures.

### Education & Skills
B.Sc. Computer Science, UNSW (2014–2017). · **Skills:** JavaScript, TypeScript, C#, Java · React, .NET, Jest, NUnit · MSSQL, PostgreSQL, Redis, DynamoDB · gRPC, Kafka, AWS, Azure, Terraform · TeamCity, GitHub Actions, Vite, Webpack.

---
---

# VARIANT B — Engineering Manager / Tech Lead

## Clement Ng
**Engineering Leader / Tech Lead** — Sydney · +61 413-424-888 · clementng23@gmail.com · [linkedin.com/in/clemchowder](https://www.linkedin.com/in/clemchowder/)

Engineering leader who has run a 25-person technical organisation for one of Australia's largest conventions — setting Board-level strategy and delivering zero-critical-failure live operations for 45,000+ attendees — while operating as a senior full-stack engineer and feature lead at a global SaaS company. Combines hands-on technical credibility (8+ yrs shipping production software) with proven people leadership, hiring, and multi-year roadmap ownership.

### Leadership Experience

**Director of IT — Sydney Manga and Anime Show (SMASH!) Inc.** · Nov 2025 – Present
- **Lead IT across Engineering, Systems, and Support — 25 volunteers and 3 team leads.**
- **Set IT strategy with the Board and Executive**, aligned to growth, risk, and live-event constraints.
- Own a **multi-year IT strategy and roadmap** — cost monitoring, infrastructure scaling, internal systems, and volunteer engineering operations.
- Accountable for ticketing, access control, networking, and **on-site incident response for 45,000+ attendees**.

**Assistant IT Director — SMASH! Inc.** · Jan 2020 – Nov 2025
- **Grew the engineering team from 5**, planning work, delegating, and reviewing output across IT/Ticketing/Operations.
- **Delivered 5 consecutive conventions with zero critical IT failures**; ran live operations under peak load.

**Software Developer — SMASH! Inc.** · Nov 2018 – Jan 2020
- Founding engineer (team of 5): **designed and built the integrated ticketing + mobile-scanning system** for 40,000+ attendees and vendors — the system the org I now direct was built on.

**Software Engineer / Feature Lead — Campaign Monitor (Marigold)** · Apr 2021 – Present
- **Feature tech lead on CRM Lite** — owned design (architecture-reviewed LDR), cross-functional coordination (DBA, privacy/platform, product), and delivery to production.
- **Set front-end engineering standards** as a JavaScript Crew member — reviewed merges org-wide and owned shared tooling.
- **Screened engineering candidates and mentored junior engineers**; organised cross-functional pre-release bug-bash sessions.
- Reviewed **550+ PRs across 120+ engineers** — the de-facto reviewer-of-record for the team. [verify]
- Technically hands-on across 6 product domains: full-stack feature delivery, multi-repo gRPC/Kafka changes, platform migrations.

### Earlier Experience
**Associate Software Developer — WiseTech Global** (2019–2021) — sole owner of a real-time ship-tracking system for all CargoWise customers. · **Software Engineer — EdApp LMS** (2018–2019) — mobile/LMS features, 24/7 on-call.

### Education, Speaking & Skills
B.Sc. Computer Science, UNSW (2014–2017). · **Talk:** "Preparing IT Infrastructure for an Anime Convention" — company-wide engineering retreat, Jun 2025. · **Technical:** C#/.NET, TypeScript/React, gRPC, Kafka, MSSQL, AWS/Azure, Terraform.

---
---

# VARIANT C — Backend / Platform Engineer

## Clement Ng
**Backend / Platform Software Engineer** — Sydney · +61 413-424-888 · clementng23@gmail.com · [linkedin.com/in/clemchowder](https://www.linkedin.com/in/clemchowder/)

Backend-leaning full-stack engineer, 8+ years, specialising in event-driven services, gRPC/Kafka messaging, and large-scale data pipelines on .NET/C# + MSSQL. Designs the contracts and the failure handling, not just the happy path. Experienced extracting services from a legacy monolith and running real-time systems in production.

### Experience

**Software Engineer — Campaign Monitor (Marigold)** · Apr 2021 – Present
- **Designed CRM Lite's contact-backfill pipeline** — opt-in command → service consumer → paged SQS messages (1,000 records/page) → bulk Kafka contact events → dedup-by-email finalisation; defined the protobuf contracts and a status/disaster-recovery model (DLQ, multi-state job lifecycle) sized for multi-million-contact lists. [verify]
- **Designed event-driven backend services and queue-based processing pipelines**, improving reliability/scalability of asynchronous workflows.
- **Built the SMS link-tracking backbone** across protobuf, Kafka ACLs, JVM messaging libs, and tracking services — contract-first, multi-repo.
- **Extracted a workflow-lookup service from the .NET-Framework monolith into a standalone .NET Core gRPC service**, landed under production load.
- Delivered Journeys/Automation backend steps (schema, persistence, cross-DB clone, GDPR-audited activity logging) and a .NET 9 cron/reporting agent.
- Multi-repo permission/failure-handling changes across monolith + protobuf + microservices + datastores.

*Tech: C#/.NET (Framework→Core→9), gRPC + protobuf, Kafka, MSSQL, DynamoDB, Terraform, AWS; TypeScript/React on the front end.*

**Associate Software Developer — WiseTech Global** · May 2019 – Mar 2021
- Sole owner of the **AIS ship-tracking system** (real-time vessel data) for all CargoWise customers.
- Maintained the **MAWB air-cargo automation system** ingesting airline/carrier data for near-real-time visibility (C#, MSSQL).

**Software Engineer — EdApp LMS** · Feb 2018 – May 2019
- Push-notification system logging/audit; mobile features (React Native); 24/7 on-call, CI/CD, automated testing.

### Leadership (Volunteer) · Education · Skills
**SMASH! Inc.** (Nov 2018–Present) — founding engineer who **designed and built the integrated ticketing + mobile-scanning system** (40,000+ attendees), now Director of IT leading a 25-person org; incident response + networking for 45,000+ attendees; zero critical failures over 5 conventions. · B.Sc. Computer Science, UNSW. · **Skills:** C#, Java, TypeScript, JavaScript · MSSQL, PostgreSQL, MySQL, Redis, DynamoDB · gRPC, Kafka · AWS, Azure, Terraform, TeamCity.

<!--
USAGE NOTES (delete before sending):
- Variants share a fact base; only emphasis/ordering changes. Nothing here is invented.
- [verify]: PR/review counts (532/558/128 → rounded down); "multi-million-contact" reflects your LDR's 10M-@-2k/s capacity figure, not a stated client size — soften to "large client lists" if you prefer.
- For ATS: keep one variant per application; match its keywords to the job description.
- Variant B (EM) is the highest-differentiation play given few senior ICs have a real 25-person leadership record — lead with it for any lead/EM posting.
-->
