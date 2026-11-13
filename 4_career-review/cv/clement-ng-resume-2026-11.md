<!--
RÉSUMÉ — 2026-11 refresh. Supersedes clement-ng-resume-2page-verified.md (Jun 2026) as the base.
What changed and why:
  • Rebuilt around the interview feedback ("show ownership & decisions; lead with feature work, not pet projects").
    CM bullets now lead with customer-facing projects you LED, each with role + decision + outcome.
  • Tooling/build work kept but demoted to one bullet with a measured number.
  • New since June: SMS onboarding (technical lead), Drip Campaigns launch, Brand Hub V2, Docker builds, incidents.
  • 2026-11-10 condense: CM section cut from 9 bullets (~620 words) to 6 (~330). Staffing split, partner-API change,
    US/CA/AU scope and the ~250-customer migration moved out of the résumé; they live in star-story-bank #13–15.
Placeholders: ⟨…⟩ = a real number to fill from interview/impact-metrics-playbook.md before sending. If you can't
get the number, delete the clause. Don't guess.
Every claim traces to data/2026-h2/ or the earlier career-review files.
-->

# Clement Ng

**Senior Software Engineer · Director of IT**, Sydney, Australia
+61 413-424-888 · clementng23@gmail.com · [linkedin.com/in/clemchowder](https://www.linkedin.com/in/clemchowder/)

Senior full-stack engineer (**8+ years**) who leads customer-facing features from discovery through delivery at a global email-marketing SaaS. I scope the work, drive the architecture and rollout decisions, bring product, design and partner teams with me, and own launch readiness. Hands-on across React/TypeScript, C#/.NET, gRPC/Kafka and SQL. I also run IT for one of Australia's largest pop-culture conventions as **Director of IT**, leading a 25-person team for 45,000+ attendees.

---

## Experience

### Software Engineer — Campaign Monitor (Marigold) · Apr 2021 – Present · Sydney
Global email-marketing SaaS; .NET monolith plus a gRPC/Kafka microservice mesh.

- **Led SMS onboarding (technical lead in practice)**, one of Product's highest priorities: replaced a manual, support-run registration process with an in-app Twilio flow. Wrote the plan the PM adopted, staged the rollout because carrier registrations can't be undone, built an **idempotent provisioning API** so retries never buy a duplicate number, and merged three provisioning code paths into one. Dev-complete in 2 months; testing with real customers since Nov 2026. ⟨N customers registered⟩
- **Owned the builder canvas and launch readiness for Drip Campaigns** (branching email sequences), shipped to **every plan** in Oct 2026. Defended the send-pipeline schema change with an impact audit (7 files vs ~20–30) and wrote the launch runbook the outgoing tech lead named as the template. ⟨N accounts / M campaigns⟩
- **Feature tech lead, CRM Lite (single customer view):** took the design through architecture review, settled schema and GDPR-deletion decisions with DBAs and the platform team, and delivered a SQS→Kafka backfill pipeline sized for 20-million-contact lists.
- **Also shipped:** Brand Hub V2 colour editing (sole frontend owner; the most common customer request), and earlier SMS sending (React → gRPC → Kafka), Shopify migration tooling, Journeys automation steps, and a .NET Core gRPC service extracted from the monolith under production load.
- **Production and platform:** resolved four production incidents end-to-end in 2026, including a customer's broken RSS campaign (root cause in under 2 hours, automation paused, fixed send verified) and a cross-team dead-letter-queue regression. Initiated the Docker migration of frontend CI (**~70% less compute per pull request**, deploy package build ~40% faster); earlier modernised the frontend toolchain (Vite/esbuild, TypeScript 5, React 18).
- **Multiplier:** authored ~590 and reviewed ~620 pull requests across 120+ engineers; mentor and technical interviewer. Ran the build phase of an AI-assisted service migration whose evidence led leadership *not* to adopt it (~2× the code, ~3× the maintenance).

*Tech: C#/.NET (Framework → .NET 9), TypeScript/React 18, React Query, gRPC + protobuf, Kafka, SQS, MSSQL, Redis, DynamoDB, Docker, Terraform, AWS, Datadog, TeamCity; AI-assisted development (Claude Code).*

### Associate Software Developer — WiseTech Global · May 2019 – Mar 2021 · Sydney
Global logistics-software platform (CargoWise).
- **Sole owner of the AIS ship-tracking system** (React, TypeScript, Google Maps) delivering real-time vessel visibility to all CargoWise customers, a responsibility above my title.
- Maintained and extended the **MAWB air-cargo automation system** ingesting airline/carrier data (C#, MSSQL); UI enhancements to the in-house PAVE task platform.

### Software Engineer — EdApp LMS (Creative Licence Digital) · Feb 2018 – May 2019 · Sydney
- Built peer-authoring templates and mobile features (React Native, Backbone.js, Cordova); audit logging for push notifications; 24/7 on-call, CI/CD, automated testing.

---

## Engineering Leadership (Volunteer)

### Director of IT — Sydney Manga and Anime Show (SMASH!) Inc. · Nov 2025 – Present
- **Lead IT across Engineering, Systems and Support: 25 volunteers, 3 leads.** Set IT strategy with the Board and Executive; own a multi-year roadmap (cost, infrastructure scaling, internal systems, volunteer engineering operations).
- Accountable for **ticketing, access control, networking and on-site incident response for 45,000+ attendees.**

### Assistant IT Director · Jan 2020 – Nov 2025 · Software Developer · Nov 2018 – Jan 2020
- **Founding engineer (team of 5):** designed and built the integrated ticketing and mobile-scanning system for 40,000+ attendees and vendors.
- Grew the team from 5 engineers; planned, delegated and reviewed work; **delivered 5 consecutive conventions with zero critical IT failures.**

---

## Education · Speaking · Skills
**B.Sc. Computer Science**, University of New South Wales (2014–2017)
**Talk:** "Preparing IT Infrastructure for an Anime Convention", Campaign Monitor engineering-wide retreat, Jun 2025 · [youtube.com/watch?v=bBZFJ9uXrbU](https://www.youtube.com/watch?v=bBZFJ9uXrbU)

- **Languages:** TypeScript, JavaScript, C#, Java, SQL
- **Frontend:** React, React Query, Vite, Webpack, Jest
- **Backend & data:** .NET, gRPC, Kafka, SQS, MSSQL, PostgreSQL, Redis, DynamoDB
- **Infra & delivery:** AWS, Docker, Terraform, TeamCity, GitHub Actions, Datadog, feature-flagged staged rollouts

<!--
LENGTH: ~1.5–1.7 pages A4 after the 2026-11-10 condense. Don't add bullets back; add detail in interviews instead.
If you need one page: drop EdApp to a line, cut "Also shipped" to Brand Hub only, and drop the SMASH "Assistant IT Director" block to one line.

BEFORE SENDING:
 [ ] Fill or delete every ⟨…⟩ (impact-metrics-playbook §1, §2).
 [ ] "one of Product's highest priorities" is quoted from your lead (Slack, 28 Sep).
 [ ] "~70% less compute" = PR merge checks, 1,109 s → 348 s agent time per push, same commits (TeamCity, 10 Nov). It is compute, not wait time: push → green hasn't improved yet (shared agent-pool queue). If asked, say so.
 [ ] "~40% faster" is the deploy Web Package JS job, like-for-like 459 → 273 s, still in shadow (n=17). Re-pull once the chains flip. Source: portfolio/docker-frontend-builds-results-2026-11.md.
 [ ] "~2× code / 3× maintenance": from the no-go rationale (16k lines to replace 8k; "roughly triples the maintenance footprint").
 [ ] "Technical lead" for SMS: your role in practice (discovery owner, plan author, architecture, staffing call adopted).
     It was never a formal title. If a reference check might be literal, use "Led SMS onboarding (technical lead in practice)".
-->
