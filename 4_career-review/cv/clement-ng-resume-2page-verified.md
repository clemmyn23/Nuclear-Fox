# Clement Ng

**Senior Software Engineer · Director of IT** — Sydney, Australia
+61 413-424-888 · clementng23@gmail.com · [linkedin.com/in/clemchowder](https://www.linkedin.com/in/clemchowder/)

Full-stack software engineer with **8+ years** across SaaS platforms, real-time systems, and event-scale IT infrastructure. Owns features end-to-end through React/TypeScript front ends, .NET/C# services, and gRPC/Kafka messaging — and the design docs that get them through architecture review. For 7+ years has helped build and now leads the IT function for one of Australia's largest pop-culture conventions — from founding engineer to Director of IT (45,000+ attendees, 25-person team). Known for translating messy real-world constraints into reliable systems and for being the engineer teams defer to across a large codebase.

---

## Experience

### Software Engineer — Campaign Monitor (Marigold) · Apr 2021 – Present · Sydney
Email-marketing SaaS. Shipped product and platform work across the createsend.com monolith and its surrounding microservice mesh; worked across **six product domains** (Audience UX, Campaign Authoring, SMS, Commerce, Automation Recipes, Journeys/CRM).

- **Feature tech lead for CRM Lite (single-customer-view).** Authored the design (LDR reviewed by the architecture function), brokered schema decisions with DBAs and privacy-by-design decisions with the platform team, then delivered the feature end-to-end — protobuf contracts, a paged SQS/Kafka backfill pipeline sized for 20-million-contact client lists, the subscriber-profile UI, and the production rollout.
- **Built the SMS product as a vertical slice through the entire stack** — React UI, CmAPI endpoints, gRPC services, and the link-tracking topic taxonomy spanning protobuf, Kafka ACLs, and shared messaging libraries. Extended to geo expansion (country/phone-number handling), hosted sign-up forms, and preference-center consent.
- **Led front-end build/toolchain modernisation for the org as a JavaScript Crew member** — yarn workspaces, Vite/esbuild dev builds, Node LTS upgrades (incl. CI agents), TypeScript 4→5, Prettier/ESLint rollouts, React 18 concurrent-mode migration, and Webpack 5. Reviewed JS merges and maintained shared libraries and build tooling across the front-end engineering org.
- **Drove multi-repo, contract-first changes** as a default mode — e.g. permission-checking and failure-handling features landing across 3–4 repositories (monolith + protobuf + microservices + datastores) in a single coordinated set.
- **Migrated a workflow-lookup service from the .NET-Framework monolith to a standalone .NET Core gRPC service**, persisting through multiple production-load iterations to land it cleanly.
- **Delivered the Journeys/Automation step library** — advanced custom-field expressions, a Wait-Until step (schema, persistence, cross-DB clone, GDPR-audited activity logging), send-a-test, and condition-path swapping — each feature-flag-gated across monolith and microservice.
- **Shipped Commerce / Shopify** — the migration assistant, Commerce Management pages, and automation recipes, coordinating contract changes across the monolith, protobuf, the third-party importer service, and the admin tool.
- Authored **20+ architecture and reference docs** (system walkthroughs still used to onboard new engineers); organised pre-release bug-bash sessions for major features; **screened mid-level engineering candidates** and mentored junior engineers.
- Across the tenure: **authored 530+ and reviewed 550+ pull requests across entire engineering department.**

*Tech: C#/.NET (Framework → Core → 9), TypeScript/React (16→18), gRPC + protobuf, Kafka, MSSQL, DynamoDB, Terraform, AWS.*

### Associate Software Developer — WiseTech Global · May 2019 – Mar 2021 · Sydney
Global logistics-software platform (CargoWise).

- **Sole owner of the AIS ship-tracking system** (React, TypeScript, Google Maps) delivering real-time cargo visibility to all CargoWise customers — responsibility above the title.
- Maintained and extended the **MAWB air-cargo automation system**, ingesting airline/carrier data for near-real-time cargo visibility (C#, MSSQL).
- Delivered UI enhancements to **PAVE**, WiseTech's in-house task-management platform.

*Tech: C#, MSSQL, React, JavaScript/TypeScript.*

### Software Engineer — EdApp LMS (formerly Creative Licence Digital) · Feb 2018 – May 2019 · Sydney
Mobile-first learning-management platform.

- Built peer-authoring templates and mobile features across React Native, Backbone.js, and Cordova.
- Implemented logging and audit trails for the push-notification system.
- Participated in 24/7 on-call support, CI/CD pipelines, and automated testing.

*Tech: CoffeeScript/JavaScript, MongoDB, React, C#, PostgreSQL, Jenkins, React Native.*

---

## Engineering Leadership (Volunteer)

### Director of IT — Sydney Manga and Anime Show (SMASH!) Inc. · Nov 2025 – Present
One of Australia's largest pop-culture conventions.

- **Lead IT across Engineering, Systems, and Support — 25 volunteers and 3 leads.**
- Partner with the Board and Executive to **set IT strategy** aligned with growth, risk, and live-event constraints.
- Accountable for **ticketing, access control, networking, and on-site incident response for 45,000+ attendees**.
- Leading a **multi-year IT strategy and roadmap** — cost monitoring, infrastructure scaling, internal systems, and volunteer engineering operations.

### Assistant IT Director — SMASH! Inc. · Jan 2020 – Nov 2025
- Coordinated cross-team delivery across IT, Ticketing, and Operations; managed ticket allocations for all exhibitors and guest performers.
- Planned, delegated, and reviewed work for a team of engineers building and maintaining event systems; **grew the team from 5 engineers**.
- **Delivered 5 consecutive conventions with zero critical IT failures**; ran on-site technical setup and live operations under peak load.

### Software Developer — SMASH! Inc. · Nov 2018 – Jan 2020
- **Designed and built an integrated ticketing and mobile-scanning system** supporting 40,000+ attendees and vendors, as one of a founding team of 5 engineers.
- Managed on-site technical setup and live operations under peak load.

---

## Education

**B.Sc. (Computer Science)** — University of New South Wales · 2014 – 2017

## Speaking & Extras

- **"Preparing IT Infrastructure for an Anime Convention"** — engineering-wide company-retreat talk (Campaign Monitor) on the DevOps, hardware, software, and personnel behind running a major live event. Jun 2025 · [youtube.com/watch?v=bBZFJ9uXrbU](https://www.youtube.com/watch?v=bBZFJ9uXrbU)

## Technical Skills

- **Languages:** JavaScript, TypeScript, C#, Java
- **Frameworks:** React, .NET, Express.js, Jest, NUnit
- **Data:** MSSQL, MySQL, PostgreSQL, Redis, DynamoDB
- **Messaging / Infra:** gRPC, Kafka, AWS, Azure, Terraform
- **CI/CD & Tooling:** TeamCity, GitHub Actions, Git, Jira, Vite, Webpack
