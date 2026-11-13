# JS-Crew Review Activity — who you reviewed, where, when, what you said

This file analyses your reviewer footprint based on PR metadata + actual review comment text.

For the **JS-crew authority signals in Slack** (cross-team interventions, intra-crew chats about frontend architecture, hiring-screen reviews) see [13-slack-architecture-discussions.md](13-slack-architecture-discussions.md). Key Slack moments include:
- **2026-01-22 #js-crew-members** — The JS-crew teammate tagged you to step into a team's PR cleanup before context-provider sprawl got worse.
- **2025-10-30 #js-crew-members** — The squad product lead asked for Campaign Series module-placement guidance; you offered the SMS-style two-app split based on prior work.
- **2025-07-02 #js-crew-members** — Vite-vs-Webpack migration strategic framing during the JS-crew teammate's Node 18 trench session.
- **2025-10-09 #dev-recruitment** — mid-level engineering technical screen with hire/no-hire call.

## Totals
- **558 PRs reviewed** for other authors (excluding self-reviews)
- **55 distinct teammates** whose work you've reviewed
- **31 distinct repos** you've reviewed in
- **466 review comments** authored — captured across **187 PRs**
- **187 of 558 reviewed PRs had ≥1 review comment from you** (33%)
  - (The other 371 PRs you reviewed but only with approval/no-comment.)

## Review comments by year

| Year | PRs reviewed | PRs with your comments | Total comments | Avg comments per PR-with-comments |
|---|---:|---:|---:|---:|
| Y1 | 87 | 33 | 70 | 2.1 |
| Y2 | 116 | 39 | 97 | 2.5 |
| Y3 | 90 | 34 | 112 | 3.3 |
| Y4 | 84 | 23 | 45 | 2.0 |
| Y5 | 159 | 51 | 130 | 2.5 |
| Y6 | 22 | 7 | 12 | 1.7 |

## Where the comments land — file extension breakdown

Shows the technologies you spend reviewing time on.

| Extension | Count | Notes |
|---|---:|---|
| `.tsx` | 272 | React component files — the dominant surface |
| `.ts` | 80 | TypeScript modules, API clients, utilities |
| `.cs` | 61 | C# backend (CmAPI, services, datastores) |
| `.scss` | 19 | Sass styling |
| `.js` | 15 | Legacy JS, scripts, lambda |
| `.json` | 4 | Config / package.json |
| `.yaml` | 4 | SegmentTrackingPlan event definitions |
| `.tf` | 3 | Terraform infra |
| `.config` | 2 | .NET app.config |
| `.sql` | 2 | Stored procs |
| `(no ext)` | 1 |  |
| `.md` | 1 | README / docs |
| `.Master` | 1 | Master pages (legacy ASP.NET) |
| `.lock` | 1 | Lockfiles |

## Top PR authors by your review-comment count (lifetime)

These are the people whose code you spent the most time engaging with in review:

| Author | Total comments | PRs reviewed (lifetime) |
|---|---:|---:|
| junior engineer | 57 | 45 |
| engineer | 45 | 15 |
| engineer | 40 | 20 |
| engineer | 36 | 54 |
| junior engineer | 30 | 10 |
| engineer | 28 | 23 |
| engineer | 24 | 42 |
| engineer | 18 | 42 |
| engineer | 18 | 28 |
| engineer | 13 | 2 |
| engineer | 13 | 22 |
| senior engineer | 12 | 7 |
| engineer | 12 | 3 |
| engineer | 11 | 15 |
| engineer | 11 | 9 |
| junior engineer | 10 | 16 |
| engineer | 8 | 38 |
| engineer | 8 | 18 |
| engineer | 8 | 5 |
| engineer | 8 | 3 |

## Top files / paths by comment count

| Path | Comments |
|---|---:|
| `srcfrontend/app/audience/components/Lists/ConfirmBulkDeleteModal.tsx` | 7 |
| `srcfrontend/app/audience/components/CustomFields/CustomFieldsTable.tsx` | 7 |
| `srcfrontend/app/automation/components/CheckWorkflowRecipeStatus/CheckWorkflowRecipeStatus.tsx` | 7 |
| `lambda/index.js` | 7 |
| `srcfrontend/app/campaigns/components/NewSequence/NewSequence.tsx` | 7 |
| `srcfrontend/app/campaignreport/components/Snapshot/MachineClicksBanner/MachineClicksBanner.tsx` | 6 |
| `app/CampMon.Data.NetStandard/Crm/CrmLiteRepository.cs` | 6 |
| `srcfrontend/app/audience/components/CrmLite/CrmLiteApi.ts` | 6 |
| `srcfrontend/app/smscampaigncreationchecklist/components/SmsFromStep/SmsFromStep.tsx` | 5 |
| `srcfrontend/app/smscampaigncreationchecklist/components/SmsMessageStep/SmsComplianceToggles/SmsComplianceToggles.tsx` | 5 |
| `srcfrontend/app/campaignreport/components/ShareDialog/ShareDialog.tsx` | 5 |
| `app/CampMon.CmAPI/Endpoints/CrmLite/CrmLiteService.cs` | 5 |
| `TrackingPlan/events.yaml` | 4 |
| `srcfrontend/app/smscampaigncreationchecklist/components/SmsMessageStep/SmsMessageStep.tsx` | 4 |
| `srcfrontend/app/smscampaigncreationchecklist/SmsDataProvider.tsx` | 4 |
| `srcfrontend/app/commercesettings/components/CommerceStoreRegistration/CommerceStoreRegistration.tsx` | 4 |
| `shared/components/managecard/Card/AddBraintreeCard.tsx` | 4 |
| `srcfrontend/app/components/Integrations/IntegrationMigrationDialog/variants/ShopifyPostSunsetIntegrationMigrationDialogVariant.tsx` | 4 |
| `srcfrontend/app/twofactormanagement/api.ts` | 4 |
| `srcfrontend/app/commercesettings/pages/ShopifyMigrationStatusAgency/LegacyShopifyIntegrationContextProvider.tsx` | 4 |

## Reviewer pattern by year

| Year | Reviewed | Distinct authors | Distinct repos | JIRA projects |
|---|---:|---:|---:|---:|
| Y1 | 87 | 11 | 4 | 6 |
| Y2 | 116 | 29 | 12 | 8 |
| Y3 | 90 | 23 | 11 | 11 |
| Y4 | 84 | 20 | 8 | 7 |
| Y5 | 159 | 26 | 17 | 13 |
| Y6 | 22 | 9 | 6 | 4 |

## Top reviewed authors per year

### Year 1

| Author | Reviewed PRs |
|---|---:|
| engineer | 23 |
| engineer | 17 |
| engineer | 14 |
| engineer | 12 |
| engineer | 7 |
| engineer | 5 |
| engineer | 3 |
| engineer | 2 |
| engineer | 2 |
| engineer | 1 |

### Year 2

| Author | Reviewed PRs |
|---|---:|
| engineer | 26 |
| engineer | 14 |
| engineer | 12 |
| engineer | 7 |
| engineer | 6 |
| engineer | 6 |
| engineer | 5 |
| engineer | 5 |
| senior engineer | 4 |
| engineer | 3 |

### Year 3

| Author | Reviewed PRs |
|---|---:|
| engineer | 12 |
| engineer | 10 |
| engineer | 10 |
| engineer | 8 |
| senior engineer | 7 |
| engineer | 7 |
| engineer | 6 |
| senior engineer | 5 |
| engineer | 3 |
| engineer | 3 |

### Year 4

| Author | Reviewed PRs |
|---|---:|
| engineer | 21 |
| engineer | 9 |
| engineer | 9 |
| engineer | 7 |
| engineer | 5 |
| engineer | 4 |
| engineer | 4 |
| engineer | 4 |
| engineer | 3 |
| engineer | 3 |

### Year 5

| Author | Reviewed PRs |
|---|---:|
| junior engineer | 38 |
| engineer | 25 |
| engineer | 18 |
| junior engineer | 11 |
| engineer | 10 |
| engineer | 9 |
| junior engineer | 8 |
| engineer | 6 |
| engineer | 5 |
| engineer | 5 |

### Year 6

| Author | Reviewed PRs |
|---|---:|
| junior engineer | 7 |
| junior engineer | 5 |
| junior engineer | 2 |
| senior engineer | 2 |
| engineer | 2 |
| engineer | 1 |
| engineer | 1 |
| engineer | 1 |
| engineer | 1 |

## Cross-team review breadth

Top JIRA projects reviewed per year:

| Year | Top JIRA projects (reviewed) |
|---|---|
| Y1 | CA (35), UX1 (23), CAS (1), ED (1), SE (1), SMS (1) |
| Y2 | SMS (41), EL (13), SE (8), MER (6), PP (5), CONV (3), PLAT (3), CA (2) |
| Y3 | EL (19), PP (15), MER (13), AJ (3), SMS (2), CL (2), CA (2), SE (1) |
| Y4 | AJ (31), EL (9), BTB (4), ZUSE (4), JC (2), COM (2), PP (1) |
| Y5 | AJ (100), SRE (7), HOP (4), COM (4), STRK (4), PLAT (3), SHARE (3), ZUSE (2) |
| Y6 | AJ (16), STRK (1), COM (1), LSK (1) |

## Reviewer-to-author ratio over time

Higher ratio means more reviewing per authored PR — a senior-IC pattern.

| Year | Authored | Reviewed | Ratio |
|---|---:|---:|---:|
| Y1 | 159 | 87 | 0.55x |
| Y2 | 131 | 116 | 0.89x |
| Y3 | 84 | 90 | 1.07x |
| Y4 | 66 | 84 | 1.27x |
| Y5 | 77 | 159 | 2.06x |
| Y6 | 15 | 22 | 1.47x |

---

**See also:** [12-review-comment-patterns.md](12-review-comment-patterns.md) for thematic analysis of your actual review-comment text — what kinds of feedback you give, what you push back on, what you praise.