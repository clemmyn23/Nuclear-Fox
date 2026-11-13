# JIRA Projects observed in Clement Ng's PRs

JIRA cloud: campaignmonitor.atlassian.net (cloudId `59e46053-3fb0-480c-87e9-04a5aa68a8b9`).

Project metadata was retrieved by sampling one ticket per prefix from JIRA (the `getVisibleJiraProjects` endpoint was not authorized in this session, so per-project descriptions and leads could not be pulled in bulk — fields where data is unavailable are marked `n/a`).

PR counts cover Clement Ng (cng@campaignmonitor.com / cng@meetmarigold.com) across `git.campmon.com`, drawn from `authored-prs.csv` and `reviewed-prs.csv` in this folder.

| Prefix | Project name | Description | Lead | PRs (authored / reviewed) |
|---|---|---|---|---|
| AJ | Boole | Journeys / Boole team — workflows, journey builder, custom-field steps, conditions, wait-until, complex series, subscriber profile, agency status, pre-built journeys | n/a | 117 / 150 |
| SMS | SMS | SMS Campaigns — earliest usable product for SMS sends, tech debt and feature work | n/a | 87 / 44 |
| CA | Campaigns | Campaign creation, A/B testing, sign-up forms, validation, snapshot/report pages | n/a | 61 / 39 |
| UX1 | UX Refresh 1 | Subscriber management UX refresh — list/segment/subscriber screens, recipient surfaces | n/a | 50 / 23 |
| MER | Merchant | CM eCommerce — Shopify receipt journeys, merchant integrations | n/a | 49 / 19 |
| ED | Email Designer | Email Designer (drag-and-drop email builder) | n/a | 13 / 2 |
| BTB | (Obsolete) Bloom - The Bootstrappers | Bloom / The Bootstrappers — Slice 0 discovery + planning (project now obsolete) | n/a | 5 / 4 |
| CL | Customer Love | Customer Love week / small customer-impact fixes | n/a | 4 / 2 |
| UX3 | UX Refresh (UX3) | Subsequent UX-refresh project — not found via API in this session (likely renamed/archived) | n/a | 2 / 0 |
| JC | JC (project not accessible) | Could not retrieve project metadata (no permission or renamed) | n/a | 1 / 3 |
| CAS | CAS (project not accessible) | Could not retrieve project metadata (no permission or renamed) | n/a | 1 / 1 |
| PLAT | Platform | Platform team — infra, datastore moves (Redis → Couchbase), service-level concerns | n/a | 0 / 7 |
| EL | Elevate | Campaign reporting UI refresh and follow-ons | n/a | 0 / 41 |
| PP | Pricing and Packaging | Paddle/Chargify investigation, agency billing/markup, 3DS2, plan upgrades | n/a | 0 / 21 |
| SE | Send And Evaluate | Send and Evaluate team tooling/setup | n/a | 0 / 10 |
| SRE | SRE | Site Reliability — infra, observability, incident-related work | n/a | 0 / 8 |
| COM | COM (project not accessible) | Could not retrieve project metadata | n/a | 0 / 7 |
| ZUSE | Zuse | Zuse team onboarding work | n/a | 0 / 6 |
| STRK | Strikeforce Porpoise | Migrating internal services into CmAPI.ContentManagement project | n/a | 0 / 5 |
| HOP | HOPPER | Hopper — account setup / experiment enrolment flakiness | n/a | 0 / 4 |
| SHARE | SHARE (project not directly fetched) | Sharing surface — not sampled this session | n/a | 0 / 3 |
| LSK | Liskov | Liskov team — not sampled this session | n/a | 0 / 3 |
| CONV | Conversions | Experiments enrichment, Amplitude/Segment instrumentation | n/a | 0 / 3 |
| AML | AML | Anti-money-laundering / GRPC endpoints work | n/a | 0 / 2 |
| TUR | Turing | Turing — website builder monolith scaffolding | n/a | 0 / 1 |
| CD | Change Day | Change Day initiative — small customer wins (e.g. merging subscriber lists) | n/a | 0 / 1 |

## Notes

- Lead names and project descriptions were not available because the `getVisibleJiraProjects` MCP tool was denied permission in this session — only `getJiraIssue` was usable, which returns per-issue project name but not the project lead. The descriptions above are inferred from one sampled ticket per project.
- A handful of prefixes (`UX3`, `JC`, `CAS`, `COM`) returned 404/permission errors when sampled with `<PREFIX>-1`. They may still exist (renumbered start key or archived); the PR titles confirm those keys *did* exist at the time of the PR.
- PR counts under "authored" are unique JIRA keys parsed from PR titles by prefix; one PR contributes one count per project. "Reviewed" likewise counts unique review PRs whose title started with that prefix.
