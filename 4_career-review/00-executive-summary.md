# Executive Summary — 5 Years at Campaign Monitor

> ## 🆕 2026-11 update: the six months since the last review
> **Short version:** the work shifted from *senior reviewer and toolchain steward* to **the engineer the team hands its top-priority ambiguous feature.**
> - **Jun–Oct, Drip Campaigns:** owned the branching-campaign builder frontend and the **go-live** (dashboards, alerts, runbook; told SRE "live on all prod DBs" on 27 Jul). Shipped to **every plan** on 1 Oct. Made and defended the send-pipeline schema call.
> - **Aug–Sep, org change:** the Boole TL left with "no named successor", and **Boole merged into Team Mitnick** on 1 Sep. You were named one of four key Journeys knowledge holders.
> - **Sep–Nov, SMS onboarding (Twilio compliance embed):** asked by the EM to own discovery; became **technical lead in practice**. Wrote the plan the PM adopted, documented the sales-led-first rollout and staged approach, had your staffing proposal adopted, designed the idempotent provisioning API, got a partner team to change its API, and merged 3 provisioning paths into 1. PM: *"in full glory! Great work Clem, Alexis!!"*
> - **AI-DLC experiment:** ran the build phase (307/307 + 72/72 tests). Your evidence became leadership's no-go (~2× code, ~3× maintenance).
> - **Docker frontend builds:** created a 24-ticket epic; first measurement shows the **deploy package build ~41% faster**.
> - **4 incidents** resolved end-to-end; **Brand Hub V2** frontend owner (Brand Hub's most common customer request).
> - **Interview-readiness:** see [interview/ownership-and-decisions.md](interview/ownership-and-decisions.md) and [cv/clement-ng-resume-2026-11.md](cv/clement-ng-resume-2026-11.md).

## The arc in one paragraph

Clement joined Campaign Monitor in April 2021 as a frontend engineer on the **UX1** client-overview refresh squad. Over the next five years he progressed through five distinct product domains — UX refresh → Campaign Authoring → SMS → Commerce/Recipes → Journeys/CRM — accumulating breadth across **25 distinct repositories** and **26 JIRA projects**. By Year 5 he was the dominant reviewer on the Audience/Journeys tribe (181 reviews/year, double his own authoring volume), routinely owning multi-repo gRPC migrations and bottom-to-top features like CRM Lite Subscriber Profile. His tooling-steward side — yarn workspaces (Y2), TS upgrades (Y2 + Y5), Prettier rollouts (Y2), Node LTS bumps (Y2 + Y5), Vite/esbuild (Y2), React 18 migration (Y5), webpack 5 (Y6) — shows up every year as a consistent secondary identity: he ships product *and* takes responsibility for the infra everyone else depends on. Beneath the PR record, a second signal: **21 Confluence pages authored (1 LDR in the Architecture space) and substantive Slack-chat engineering writing that drives design decisions before code is written** — DBA negotiations, GDPR design conversations, distributed-work-completion debates that resolve into the published docs.

## Sources behind this review

| Source | Captured |
|---|---|
| GitHub PRs authored | **532** (87% merged) — see [data/authored-prs.csv](data/authored-prs.csv) |
| GitHub PRs reviewed (for others) | **558** across 128 distinct authors — see [data/reviewed-prs.csv](data/reviewed-prs.csv) |
| PR review comments authored | **466** across 187 PRs — see [data/review-comments.csv](data/review-comments.csv) and [12-review-comment-patterns.md](12-review-comment-patterns.md) |
| JIRA tickets | 535+ keys referenced; **67 enriched** (mostly AJ); 26 JIRA projects mapped — see [08-jira-projects.md](08-jira-projects.md) |
| Confluence pages authored | **21** (incl. CRM-Lite LDR in `arc` space); **44** contributed to — see [14-confluence-design-docs.md](14-confluence-design-docs.md) |
| Slack discussions captured | ~25 high-signal threads across 9 channels — see [13-slack-architecture-discussions.md](13-slack-architecture-discussions.md) |
| Tenure | 2021-04-08 → present (5 years, 7 months at 2026-11-10) |
| 2026-H2 refresh | GitHub, Jira, Confluence, Slack and **TeamCity** re-mined for Jun–Nov 2026 — see [data/2026-h2/](data/2026-h2/) |

## At-a-glance table

| Year | Window | Authored | Merged | Reviewed | Repos | Confluence | Primary JIRA projects | Squad | One-line theme |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2021-04 → 2022-03 | 159 | 151 | 87 | 9 | 0 | CA (58), UX1 (50), SMS (15) | UX1 → CA | Client-Overview refresh, custom-fields drag-drop; transition to Campaign Authoring. |
| 2 | 2022-04 → 2023-03 | 131 | 113 | 116 | 12 | 3 | SMS (72), ED (3), CA (3) | SMS + JS infra | SMS product end-to-end; led yarn workspaces, Vite, Node 16, TS 4, Prettier 2.7. **First Confluence pages** (Node-bump guide, signup-forms audit). |
| 3 | 2023-04 → 2024-03 | 84 | 74 | 90 | 14 | 3 | MER (49), CL (4), AJ (2) | Commerce + Recipes | Shopify migration assistant, Commerce Management, Automation Recipes. **CopyWorkflowService deep-dive doc** still used to onboard new AJ engineers. |
| 4 | 2024-04 → 2025-03 | 66 | 52 | 84 | 13 | 4 | AJ (47), BTB (5) | Journeys (AJ) | UCF Advanced Expressions, Wait-Until, Send-a-Test; Bloom prototype. **First bug-bash organising** + Matillion postmortem. |
| 5 | 2025-04 → 2026-03 | 77 | 64 | 159 | 7 | 9 | AJ (55), JC (1) | Platform IC | WorkflowLookupService gRPC migration, Agency Partnership, Campaign Series, CRM Lite. **LDR in Architecture space**; in-chat design lead. |
| 6 | 2026-04 → 2026-11 *(in progress)* | 71 | 53 | 84 | 9 | 3 | AJ (→Aug), **COM (Sep→)**, JC | Boole → **Mitnick** | **Drip Campaigns** builder + go-live (all plans, Oct); team merge; **SMS onboarding technical lead**; AI-DLC no-go; Docker builds epic (−41% package build); Brand Hub V2; 4 incidents. |

## Squad / product-area journey

```
2021    2022    2023    2024    2025    2026
  │       │       │       │       │       │ 
  ├─UX1───┤                                    Client Overview refresh
          ├─CA───┤                             Campaign Authoring checklist
          ├──────SMS──────┤                    SMS product end-to-end
                   ├─MER──────────┤            Commerce / Shopify integration
                          ├─CL─┤               Subscriber export streaming
                              ├─────AJ──────────────────────────────────┤
                                          ├─BTB┤  Bloom Bootstrap prototype
```

Transitions are clean — each squad change shows a few weeks of overlap then a clean handover. No half-finished work trailing behind.

## What the volume looks like over time

Per-month authored + reviewed counts (a quick visual sense of intensity):

```
2021-04  A: 5 R: 0  █████
2021-05  A:18 R: 4  ██████████████████░░░░
2021-06  A:14 R:14  ██████████████░░░░░░░░░░░░░░
2021-07  A:13 R: 9  █████████████░░░░░░░░░
2021-08  A:11 R: 4  ███████████░░░░
2021-09  A:12 R: 7  ████████████░░░░░░░
2021-10  A:10 R: 7  ██████████░░░░░░░
2021-11  A:20 R:12  ████████████████████░░░░░░░░░░░░
2021-12  A: 9 R: 1  █████████░
2022-01  A:11 R: 6  ███████████░░░░░░
2022-02  A:16 R:15  ████████████████░░░░░░░░░░░░░░░
2022-03  A:20 R: 8  ████████████████████░░░░░░░░
2022-04  A:18 R:15  ██████████████████░░░░░░░░░░░░░░░
2022-05  A:15 R: 9  ███████████████░░░░░░░░░
2022-06  A:14 R: 9  ██████████████░░░░░░░░░
2022-07  A: 9 R:10  █████████░░░░░░░░░░
2022-08  A:15 R:16  ███████████████░░░░░░░░░░░░░░░░
2022-09  A:14 R:16  ██████████████░░░░░░░░░░░░░░░░
2022-10  A:11 R:11  ███████████░░░░░░░░░░░
2022-11  A: 6 R: 6  ██████░░░░░░
2022-12  A: 5 R: 5  █████░░░░░
2023-01  A:11 R: 5  ███████████░░░░░
2023-02  A: 5 R: 4  █████░░░░
2023-03  A: 8 R:10  ████████░░░░░░░░░░
2023-04  A: 3 R: 5  ███░░░░░
2023-05  A:11 R: 4  ███████████░░░░
2023-06  A:17 R: 8  █████████████████░░░░░░░░
2023-07  A:11 R: 8  ███████████░░░░░░░░
2023-08  A:13 R:16  █████████████░░░░░░░░░░░░░░░░
2023-09  A:12 R:12  ████████████░░░░░░░░░░░░
2023-10  A: 7 R: 4  ███████░░░░
2023-11  A: 3 R: 6  ███░░░░░░
2023-12  A: 1 R: 6  █░░░░░░
2024-01  A: 1 R:15  █░░░░░░░░░░░░░░░
2024-03  A: 5 R: 6  █████░░░░░░
2024-04  A: 5 R:11  █████░░░░░░░░░░░
2024-05  A: 5 R: 5  █████░░░░░
2024-06  A: 6 R: 8  ██████░░░░░░░░
2024-07  A:10 R:12  ██████████░░░░░░░░░░░░
2024-08  A: 5 R: 6  █████░░░░░░
2024-09  A: 8 R:11  ████████░░░░░░░░░░░
2024-10  A: 3 R: 4  ███░░░░
2024-11  A: 5 R: 7  █████░░░░░░░
2024-12  A: 1 R: 3  █░░░
2025-01  A: 7 R: 5  ███████░░░░░
2025-02  A: 5 R: 6  █████░░░░░░
2025-03  A: 6 R: 6  ██████░░░░░░
2025-04  A:10 R:11  ██████████░░░░░░░░░░░
2025-05  A:10 R:14  ██████████░░░░░░░░░░░░░░
2025-06  A: 2 R:10  ██░░░░░░░░░░
2025-07  A: 8 R: 5  ████████░░░░░
2025-08  A: 4 R: 4  ████░░░░
2025-09  A: 4 R:21  ████░░░░░░░░░░░░░░░░░░░░░
2025-10  A: 6 R:18  ██████░░░░░░░░░░░░░░░░░░
2025-11  A: 4 R:14  ████░░░░░░░░░░░░░░
2025-12  A:11 R:13  ███████████░░░░░░░░░░░░░
2026-01  A: 3 R:13  ███░░░░░░░░░░░░░
2026-02  A: 3 R:15  ███░░░░░░░░░░░░░░░
2026-03  A:12 R:21  ████████████░░░░░░░░░░░░░░░░░░░░░
2026-04  A: 5 R:11  █████░░░░░░░░░░░
2026-05  A:10 R:11  ██████████░░░░░░░░░░░
```

**Reading the chart:** `█` = authored, `░` = reviewed.
- Authoring volume peaks early (2021-05, 2021-11, 2022-03) when ramping on new domains.
- Review volume grows steadily — Year 5 (Oct 2025 onwards) shows the senior-IC pattern where reviews dominate authoring.
- The June 2024–March 2025 dip in authoring corresponds to the Bloom Bootstrap pivot and AJ tribe ramp-up.
