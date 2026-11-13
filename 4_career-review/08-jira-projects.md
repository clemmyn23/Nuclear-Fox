# JIRA project journey — every project you've touched

Combines authored + reviewed PRs by JIRA project prefix. Project metadata sourced from the JIRA enrichment (see `data/jira-tickets.csv` for the 67 tickets we successfully fetched and `data/jira-projects-summary.md` for the full project map).

**Cloud:** campaignmonitor.atlassian.net
**Total unique JIRA keys observed:** ~535 across authored + reviewed PRs

## Quick map — projects ranked by total interaction

| Prefix | Project | Authored | Reviewed | First touched | Last touched | Relevance |
|---|---|---:|---:|---|---|---|
| **AJ** | Boole | 117 | 150 | 2023-11-08 | 2026-05-28 | primary |
| **SMS** | SMS Campaigns | 87 | 44 | 2022-03-03 | 2023-06-13 | primary |
| **CA** | Campaigns | 61 | 39 | 2021-08-18 | 2024-03-14 | primary |
| **UX1** | UX Refresh 1 | 50 | 23 | 2021-04-08 | 2021-08-19 | primary |
| **MER** | Merchant | 49 | 19 | 2022-05-23 | 2023-12-18 | primary |
| **EL** | Elevate | 0 | 41 | 2022-04-05 | 2024-10-04 | reviewer |
| **PP** | Pricing and Packaging | 0 | 21 | 2022-12-20 | 2024-04-22 | reviewer |
| **ED** | Email Designer | 13 | 2 | 2021-11-29 | 2024-01-15 | secondary |
| **SE** | Send And Evaluate | 0 | 10 | 2022-02-07 | 2023-06-08 | reviewer |
| **BTB** | (Obsolete) Bloom - The Bootstrappers | 5 | 4 | 2024-09-11 | 2024-09-20 | secondary |
| **SRE** | SRE | 0 | 8 | 2023-08-14 | 2026-02-18 | reviewer |
| **PLAT** | Platform | 0 | 7 | 2022-04-29 | 2025-09-11 | reviewer |
| **COM** | COM | 0 | 7 | 2024-07-30 | 2026-05-04 | reviewer |
| **CL** | Customer Love | 4 | 2 | 2023-07-25 | 2023-08-11 | tangential |
| **ZUSE** | Zuse | 0 | 6 | 2024-10-17 | 2026-03-03 | reviewer |
| **STRK** | Strikeforce Porpoise | 0 | 5 | 2025-11-11 | 2026-05-04 | reviewer |
| **JC** | JC | 1 | 3 | 2024-07-23 | 2025-04-08 | tangential |
| **HOP** | HOPPER | 0 | 4 | 2025-04-07 | 2025-11-12 | tangential |
| **CONV** | Convert | 0 | 3 | 2022-04-11 | 2022-05-09 | tangential |
| **SHARE** | Share | 0 | 3 | 2025-09-11 | 2025-11-05 | tangential |
| **LSK** | LSK | 0 | 3 | 2025-09-30 | 2026-05-04 | tangential |
| **CAS** | CAS | 1 | 1 | 2021-06-08 | 2021-07-23 | tangential |
| **UX3** | UX Refresh 3 | 2 | 0 | 2021-09-22 | 2021-09-22 | tangential |
| **AML** | Audience Multi-List? | 0 | 2 | 2026-01-30 | 2026-03-24 | tangential |
| **CD** | Continuous Delivery | 0 | 1 | 2025-08-14 | 2025-08-14 | tangential |
| **TUR** | TUR | 0 | 1 | 2026-01-14 | 2026-01-14 | tangential |

## Detailed view by project

### AJ — Boole
_Journeys / Boole team — workflows, journey builder, custom-field steps, conditions, wait-until, complex series, subscriber profile, agency status, pre-built journeys_

**Authored:** 117 PRs from 2024-03-11 to 2026-05-28
**Reviewed:** 150 PRs from 2023-11-08 to 2026-05-28

**Sample authored PRs:**

- 2024-03-11 — [AJ-194](https://campaignmonitor.atlassian.net/browse/AJ-194) — [workflowbuildercontext.uiservice.core#191](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/191) — AJ-194-a Only enable save button when custom field form values are changed from initial. 
- 2024-03-19 — [AJ-223](https://campaignmonitor.atlassian.net/browse/AJ-223) — [workflowcontext.copyworkflowservice.core#25](https://git.campmon.com/Engineering/workflowcontext.copyworkflowservice.core/pull/25) — AJ-223 Update readme - copy custom field
- 2024-04-04 — [AJ-226](https://campaignmonitor.atlassian.net/browse/AJ-226) — [TestAutomation#416](https://git.campmon.com/Engineering/TestAutomation/pull/416) — AJ-226-a Add tests for journey copy custom fields 
- 2024-04-11 — [AJ-247](https://campaignmonitor.atlassian.net/browse/AJ-247) — [workflowcontext.updatecustomfield#49](https://git.campmon.com/Engineering/workflowcontext.updatecustomfield/pull/49) — AJ-247-a Improve UCF logging
- 2024-04-18 — [AJ-234](https://campaignmonitor.atlassian.net/browse/AJ-234) — [workflowbuildercontext.uiservice.core#200](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/200) — AJ-234 Adjust UCF step note styling
- 2024-04-18 — [AJ-234](https://campaignmonitor.atlassian.net/browse/AJ-234) — [workflowbuildercontext.uiservice.core#201](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/201) — AJ-234-b Update UCF step styling 2
- 2026-05-14 — [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) — [createsend.com#23200](https://git.campmon.com/Freshview/createsend.com/pull/23200) — AJ-1140-a Campaign series - fix enum inconsistency
- 2026-05-20 — [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) — [createsend.com#23243](https://git.campmon.com/Freshview/createsend.com/pull/23243) — AJ-1140-c Complex sequence - Add campaign nodes to tree
- 2026-05-22 — [AJ-1140](https://campaignmonitor.atlassian.net/browse/AJ-1140) — [createsend.com#23265](https://git.campmon.com/Freshview/createsend.com/pull/23265) — AJ-1140-e Complex sequence - Add campaign nodes to tree
- 2026-05-25 — [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) — [workflowcontext.runnerservice.core#147](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/147) — AJ-1196-a Add feature flag client
- 2026-05-28 — [AJ-1206](https://campaignmonitor.atlassian.net/browse/AJ-1206) — [workflowcontext.runnerservice.core#153](https://git.campmon.com/Engineering/workflowcontext.runnerservice.core/pull/153) — AJ-1206-a Migrate to GrpcClient v2
- 2026-05-28 — [AJ-1196](https://campaignmonitor.atlassian.net/browse/AJ-1196) — [createsend.com#23356](https://git.campmon.com/Freshview/createsend.com/pull/23356) — AJ-1196-d Pass IsJourneyReportingEnabled feature flag to workflow ui
- … (105 more in [data/authored-prs.csv](data/authored-prs.csv))

---

### SMS — SMS Campaigns
_SMS product end-to-end — sends, reporting, link tracking, geo expansion, signup forms, preference center_

**Authored:** 87 PRs from 2022-03-03 to 2023-03-29
**Reviewed:** 44 PRs from 2022-03-30 to 2023-06-13

**Sample authored PRs:**

- 2022-03-03 — [SMS-16](https://campaignmonitor.atlassian.net/browse/SMS-16) — [SmsSendingServices#8](https://git.campmon.com/Engineering/SmsSendingServices/pull/8) — SMS-16 Implement fetching bounces from shared services
- 2022-03-04 — [SMS-16](https://campaignmonitor.atlassian.net/browse/SMS-16) — [SmsSendingServices#9](https://git.campmon.com/Engineering/SmsSendingServices/pull/9) — SMS-16 Setup SharedServicesConfig and terraform stuff
- 2022-03-08 — [SMS-56](https://campaignmonitor.atlassian.net/browse/SMS-56) — [cm.protobuf#546](https://git.campmon.com/platform/cm.protobuf/pull/546) — SMS-56 Extending interface for bounced recipient data. 
- 2022-03-14 — [SMS-56](https://campaignmonitor.atlassian.net/browse/SMS-56) — [SmsSendingServices#11](https://git.campmon.com/Engineering/SmsSendingServices/pull/11) — SMS-56 Add bounced_at_date_utc column to mailing_recipient_bounce_type
- 2022-03-16 — [SMS-56](https://campaignmonitor.atlassian.net/browse/SMS-56) — [SmsSendingServices#14](https://git.campmon.com/Engineering/SmsSendingServices/pull/14) — SMS-56-b Send bounced data on recipient summary
- 2022-03-17 — [SMS-56](https://campaignmonitor.atlassian.net/browse/SMS-56) — [createsend.com#12408](https://git.campmon.com/Freshview/createsend.com/pull/12408) — SMS-56-c SMS reporting - Update new bounced properties
- 2023-03-14 — [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) — [createsend.com#14872](https://git.campmon.com/Freshview/createsend.com/pull/14872) — SMS-543-b Track preference center field changes
- 2023-03-17 — [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) — [createsend.com#14896](https://git.campmon.com/Freshview/createsend.com/pull/14896) — SMS-543-c Add CAL category and logging 'ClientPreferenceCenterFieldVisibilitySettingsChanged'
- 2023-03-21 — [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) — [campmon.hex#752](https://git.campmon.com/Freshview/campmon.hex/pull/752) — SMS-543-d Update CM packages
- 2023-03-24 — [SMS-583](https://campaignmonitor.atlassian.net/browse/SMS-583) — [createsend.com#14945](https://git.campmon.com/Freshview/createsend.com/pull/14945) — SMS-583-a Preference center - SMS consent asterisk when not required
- 2023-03-29 — [SMS-583](https://campaignmonitor.atlassian.net/browse/SMS-583) — [createsend.com#14975](https://git.campmon.com/Freshview/createsend.com/pull/14975) — SMS-583-b Preference center - Fix some field titles visible when fields are hidden
- 2023-03-29 — [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) — [createsend.com#14978](https://git.campmon.com/Freshview/createsend.com/pull/14978) — SMS-543-c Fix Capitalization For Tracking Property Values
- … (75 more in [data/authored-prs.csv](data/authored-prs.csv))

---

### CA — Campaigns
_Campaign creation, A/B testing, sign-up forms, validation, snapshot/report pages, checklist flow_

**Authored:** 61 PRs from 2021-08-18 to 2022-05-20
**Reviewed:** 39 PRs from 2021-08-29 to 2024-03-14

**Sample authored PRs:**

- 2021-08-18 — [CA-982](https://campaignmonitor.atlassian.net/browse/CA-982) — [createsend.com#10680](https://git.campmon.com/Freshview/createsend.com/pull/10680) — CA-982 Improved efficiency of re-importing HTML
- 2021-08-23 — [CA-982](https://campaignmonitor.atlassian.net/browse/CA-982) — [createsend.com#10723](https://git.campmon.com/Freshview/createsend.com/pull/10723) — CA-982-b Add missing prop in mock
- 2021-08-25 — [CA-1077](https://campaignmonitor.atlassian.net/browse/CA-1077) — [createsend.com#10757](https://git.campmon.com/Freshview/createsend.com/pull/10757) — CA-1077 Send test emails dialog typeahead improvements. 
- 2021-09-07 — [CA-1089](https://campaignmonitor.atlassian.net/browse/CA-1089) — [createsend.com#10851](https://git.campmon.com/Freshview/createsend.com/pull/10851) — CA-1089 Campaigns checklist recipient-step changes (opp 2)
- 2021-09-14 — [CA-1089](https://campaignmonitor.atlassian.net/browse/CA-1089) — [createsend.com#10899](https://git.campmon.com/Freshview/createsend.com/pull/10899) — CA-1089-b Fix cypress test 
- 2021-09-14 — [CA-1088](https://campaignmonitor.atlassian.net/browse/CA-1088) — [createsend.com#10901](https://git.campmon.com/Freshview/createsend.com/pull/10901) — CA-1088 Show campaign name in inclusion dialog header
- 2022-02-10 — [CA-1241](https://campaignmonitor.atlassian.net/browse/CA-1241) — [createsend.com#12019](https://git.campmon.com/Freshview/createsend.com/pull/12019) — CA-1241-b [SMS] Reports UI - Fetch summary and recipient activity
- 2022-02-15 — [CA-1242](https://campaignmonitor.atlassian.net/browse/CA-1242) — [createsend.com#12054](https://git.campmon.com/Freshview/createsend.com/pull/12054) — CA-1242 [SMS] Monolith - SendCampaign permissions for sms pages
- 2022-02-17 — [CA-1250](https://campaignmonitor.atlassian.net/browse/CA-1250) — [createsend.com#12092](https://git.campmon.com/Freshview/createsend.com/pull/12092) — CA-1250-a Update @cmds/dialog
- 2022-05-17 — [CA-1309](https://campaignmonitor.atlassian.net/browse/CA-1309) — [createsend.com#12877](https://git.campmon.com/Freshview/createsend.com/pull/12877) — CA-1309 Fix stuck campaign when fallback email has whitespace
- 2022-05-20 — [CA-1309](https://campaignmonitor.atlassian.net/browse/CA-1309) — [cm-utils#96](https://git.campmon.com/CMDS/cm-utils/pull/96) — CA-1309-b Spaces in front of fallbacks in sender email address cause stuck campaigns
- 2022-05-20 — [CA-1309](https://campaignmonitor.atlassian.net/browse/CA-1309) — [createsend.com#12902](https://git.campmon.com/Freshview/createsend.com/pull/12902) — CA-1309-c Bump is-personalized-email 
- … (49 more in [data/authored-prs.csv](data/authored-prs.csv))

---

### UX1 — UX Refresh 1
_Subscriber management UX refresh — list/segment/subscriber screens, custom fields, client overview_

**Authored:** 50 PRs from 2021-04-08 to 2021-08-19
**Reviewed:** 23 PRs from 2021-05-06 to 2021-08-11

**Sample authored PRs:**

- 2021-04-08 — [UX1-400](https://campaignmonitor.atlassian.net/browse/UX1-400) — [createsend.com#9381](https://git.campmon.com/Freshview/createsend.com/pull/9381) — UX1-400 Add recipients column to Recently sent campaigns
- 2021-04-14 — [UX1-323](https://campaignmonitor.atlassian.net/browse/UX1-323) — [createsend.com#9435](https://git.campmon.com/Freshview/createsend.com/pull/9435) — UX1-323 Backfilling thumbnail screenshots
- 2021-04-21 — [UX1-428](https://campaignmonitor.atlassian.net/browse/UX1-428) — [createsend.com#9524](https://git.campmon.com/Freshview/createsend.com/pull/9524) — UX1-428 Fix fetched thumbnails flashing when lists are refreshed. 
- 2021-04-29 — [UX1-414](https://campaignmonitor.atlassian.net/browse/UX1-414) — [TestAutomation#149](https://git.campmon.com/Engineering/TestAutomation/pull/149) — UX1-414 Test changes for client-overview page refresh
- 2021-04-30 — [UX1-337](https://campaignmonitor.atlassian.net/browse/UX1-337) — [createsend.com#9608](https://git.campmon.com/Freshview/createsend.com/pull/9608) — UX1-337 fix empty-list state being shown when changing filter
- 2021-05-03 — [UX1-410](https://campaignmonitor.atlassian.net/browse/UX1-410) — [createsend.com#9622](https://git.campmon.com/Freshview/createsend.com/pull/9622) — UX1-410 move filter button in supressions list
- 2021-08-09 — [UX1-580](https://campaignmonitor.atlassian.net/browse/UX1-580) — [workflowbuildercontext.uiservice.core#68](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/68) — UX1-580-b Extend WorkflowInitiationContext for page referrer tracking
- 2021-08-10 — [UX1-580](https://campaignmonitor.atlassian.net/browse/UX1-580) — [SegmentTrackingPlan#246](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/246) — UX1-580 Update tracking plan 
- 2021-08-10 — [UX1-580](https://campaignmonitor.atlassian.net/browse/UX1-580) — [createsend.com#10603](https://git.campmon.com/Freshview/createsend.com/pull/10603) — UX1-580-c Client overview tracking changes
- 2021-08-16 — [UX1-580](https://campaignmonitor.atlassian.net/browse/UX1-580) — [createsend.com#10653](https://git.campmon.com/Freshview/createsend.com/pull/10653) — UX1-580-d Monolith Add client overview initiation context properties for journeys
- 2021-08-18 — [UX1-580](https://campaignmonitor.atlassian.net/browse/UX1-580) — [createsend.com#10690](https://git.campmon.com/Freshview/createsend.com/pull/10690) — UX1-580-e Re-add enum WorkflowInitiationContext.CreateModal for compat
- 2021-08-19 — [UX1-580](https://campaignmonitor.atlassian.net/browse/UX1-580) — [createsend.com#10694](https://git.campmon.com/Freshview/createsend.com/pull/10694) — UX1-580-f Adjust WorkflowInitiationContext enum 
- … (38 more in [data/authored-prs.csv](data/authored-prs.csv))

---

### MER — Merchant
_CM eCommerce — Shopify migration assistant, Commerce Management pages, Automation Recipes, merchant integrations_

**Authored:** 49 PRs from 2023-04-14 to 2023-12-18
**Reviewed:** 19 PRs from 2022-05-23 to 2023-11-10

**Sample authored PRs:**

- 2023-04-14 — [MER-366](https://campaignmonitor.atlassian.net/browse/MER-366) — [createsend.com#15064](https://git.campmon.com/Freshview/createsend.com/pull/15064) — MER-366-a Commerce settings - Shopify migration FAQ page
- 2023-04-26 — [MER-375](https://campaignmonitor.atlassian.net/browse/MER-375) — [createsend.com#15140](https://git.campmon.com/Freshview/createsend.com/pull/15140) — MER-375-a Shopify migration progress page (frontend) 
- 2023-04-28 — [MER-375](https://campaignmonitor.atlassian.net/browse/MER-375) — [ThirdPartyListImporter.UI#48](https://git.campmon.com/Engineering/ThirdPartyListImporter.UI/pull/48) — MER-375-b Get status endpoint
- 2023-05-18 — [MER-401](https://campaignmonitor.atlassian.net/browse/MER-401) — [createsend.com#15308](https://git.campmon.com/Freshview/createsend.com/pull/15308) — MER-401-a Add feature flag 805. Refactor commercesettings router
- 2023-05-22 — [MER-401](https://campaignmonitor.atlassian.net/browse/MER-401) — [createsend.com#15341](https://git.campmon.com/Freshview/createsend.com/pull/15341) — MER-401-b New commerce management page
- 2023-05-24 — [MER-413](https://campaignmonitor.atlassian.net/browse/MER-413) — [SegmentTrackingPlan#372](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/372) — MER-413 Add commerce management events
- 2023-10-06 — [MER-713](https://campaignmonitor.atlassian.net/browse/MER-713) — [workflowcontext.copyworkflowservice-datastores#4](https://git.campmon.com/Engineering/workflowcontext.copyworkflowservice-datastores/pull/4) — MER-713-b Add 'IsRecipe' column to CloneEmailContentJob
- 2023-10-06 — [MER-713](https://campaignmonitor.atlassian.net/browse/MER-713) — [workflowcontext.copyworkflowservice.core#21](https://git.campmon.com/Engineering/workflowcontext.copyworkflowservice.core/pull/21) — MER-713-c Add isRecipe property
- 2023-10-06 — [MER-713](https://campaignmonitor.atlassian.net/browse/MER-713) — [createsend.com#16332](https://git.campmon.com/Freshview/createsend.com/pull/16332) — MER-713-e Skip email design copy for recipe when limited user permissions 
- 2023-11-08 — [MER-723](https://campaignmonitor.atlassian.net/browse/MER-723) — [createsend.com#16568](https://git.campmon.com/Freshview/createsend.com/pull/16568) — MER-723-a Remove shopify migration banner and dialog
- 2023-11-14 — [MER-750](https://campaignmonitor.atlassian.net/browse/MER-750) — [createsend.com#16595](https://git.campmon.com/Freshview/createsend.com/pull/16595) — MER-750-a Integrations - Prepend clientid in URL for integration page uplift
- 2023-12-18 — [MER-792](https://campaignmonitor.atlassian.net/browse/MER-792) — [CommerceServices#47](https://git.campmon.com/Engineering/CommerceServices/pull/47) — MER-792 Support Shopify POS orders
- … (37 more in [data/authored-prs.csv](data/authored-prs.csv))

---

### EL — Elevate
_Campaign reporting UI refresh and follow-ons_

**Reviewed:** 41 PRs from 2022-04-05 to 2024-10-04

---

### PP — Pricing and Packaging
_Paddle/Chargify investigation, agency billing/markup, 3DS2, plan upgrades_

**Reviewed:** 21 PRs from 2022-12-20 to 2024-04-22

---

### ED — Email Designer
_Drag-and-drop email builder — keyboard shortcuts, tracking_

**Authored:** 13 PRs from 2021-11-29 to 2022-05-11
**Reviewed:** 2 PRs from 2021-12-13 to 2024-01-15

**Sample authored PRs:**

- 2021-11-29 — [ED-1247](https://campaignmonitor.atlassian.net/browse/ED-1247) — [contentbuildercontext.staticresourceservice.core#715](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/715) — ED-1247 Superscript and subscript functionality
- 2021-11-30 — [ED-1247](https://campaignmonitor.atlassian.net/browse/ED-1247) — [SegmentTrackingPlan#282](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/282) — ED-1247 Tracking for superscript and subscript text formatting
- 2021-11-30 — [ED-1247](https://campaignmonitor.atlassian.net/browse/ED-1247) — [createsend.com#11594](https://git.campmon.com/Freshview/createsend.com/pull/11594) — ED-1247 Tracking for superscript subscript text formatting
- 2021-12-02 — [ED-1248](https://campaignmonitor.atlassian.net/browse/ED-1248) — [SegmentTrackingPlan#286](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/286) — ED-1248 Tracking properties for strikethrough formatting
- 2021-12-02 — [ED-1248](https://campaignmonitor.atlassian.net/browse/ED-1248) — [createsend.com#11612](https://git.campmon.com/Freshview/createsend.com/pull/11612) — ED-1248 Tracking properties for strikethrough formatting
- 2021-12-02 — [ED-1248](https://campaignmonitor.atlassian.net/browse/ED-1248) — [contentbuildercontext.staticresourceservice.core#723](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/723) — ED-1248 Implement strikethrough text formatting
- 2021-12-13 — [ED-1247](https://campaignmonitor.atlassian.net/browse/ED-1247) — [contentbuildercontext.staticresourceservice.core#741](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/741) — ED-1247 Can only have either superscript or subscript enabled at one time
- 2021-12-14 — [ED-1256](https://campaignmonitor.atlassian.net/browse/ED-1256) — [contentbuildercontext.staticresourceservice.core#742](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/742) — ED-1256 Add "title" attributes to formatting toolbar buttons
- 2022-01-24 — [ED-1252](https://campaignmonitor.atlassian.net/browse/ED-1252) — [contentbuildercontext.staticresourceservice.core#757](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/757) — ED-1252 open up segment section when 'who should see' clicked
- 2022-05-03 — [ED-1257](https://campaignmonitor.atlassian.net/browse/ED-1257) — [contentbuildercontext.staticresourceservice.core#763](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/763) — ED-1257 Keyboard shortcuts
- 2022-05-10 — [ED-1257](https://campaignmonitor.atlassian.net/browse/ED-1257) — [SegmentTrackingPlan#310](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/310) — ED-1257-b Add keyboard shortcut tracking property
- 2022-05-11 — [ED-1257](https://campaignmonitor.atlassian.net/browse/ED-1257) — [contentbuildercontext.staticresourceservice.core#765](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/765) — ED-1257-b Tracking keyboard shortcuts
- … (1 more in [data/authored-prs.csv](data/authored-prs.csv))

---

### SE — Send And Evaluate
_Send and Evaluate team tooling/setup_

**Reviewed:** 10 PRs from 2022-02-07 to 2023-06-08

---

### BTB — (Obsolete) Bloom - The Bootstrappers
_Greenfield prototype — discovery + planning, AWS Cognito, docker compose, change password flow_

**Authored:** 5 PRs from 2024-09-11 to 2024-09-19
**Reviewed:** 4 PRs from 2024-09-16 to 2024-09-20

**Sample authored PRs:**

- 2024-09-11 — [BTB-4](https://campaignmonitor.atlassian.net/browse/BTB-4) — [bloom-app#2](https://git.campmon.com/Deprecated/bloom-app/pull/2) — BTB-4 Update readme, add docker compose
- 2024-09-13 — [BTB-09](https://campaignmonitor.atlassian.net/browse/BTB-09) — [bloom-app#6](https://git.campmon.com/Deprecated/bloom-app/pull/6) — BTB-09-a Hook up aws cognito for server
- 2024-09-13 — [BTB-09](https://campaignmonitor.atlassian.net/browse/BTB-09) — [bloom-app#9](https://git.campmon.com/Deprecated/bloom-app/pull/9) — BTB-09-b Set up aws cognito for server
- 2024-09-16 — [BTB-13](https://campaignmonitor.atlassian.net/browse/BTB-13) — [bloom-app#12](https://git.campmon.com/Deprecated/bloom-app/pull/12) — BTB-13-a Docker compose watch
- 2024-09-19 — [BTB-21](https://campaignmonitor.atlassian.net/browse/BTB-21) — [bloom-app#19](https://git.campmon.com/Deprecated/bloom-app/pull/19) — BTB-21-a Change password functionality

---

### SRE — SRE
_Site Reliability — infra, observability, incident-related_

**Reviewed:** 8 PRs from 2023-08-14 to 2026-02-18

---

### PLAT — Platform
_Platform team — infra, datastore moves (Redis → Couchbase), service-level concerns_

**Reviewed:** 7 PRs from 2022-04-29 to 2025-09-11

---

### COM — COM
_Project metadata not retrievable_

**Reviewed:** 7 PRs from 2024-07-30 to 2026-05-04

---

### CL — Customer Love
_Customer Love week / small customer-impact fixes — subscriber export streaming_

**Authored:** 4 PRs from 2023-07-25 to 2023-08-11
**Reviewed:** 2 PRs from 2023-07-25 to 2023-07-26

**Sample authored PRs:**

- 2023-07-25 — [CL-9](https://campaignmonitor.atlassian.net/browse/CL-9) — [createsend.com#15773](https://git.campmon.com/Freshview/createsend.com/pull/15773) — CL-9-a Implement subscribers export
- 2023-07-25 — [CL-9](https://campaignmonitor.atlassian.net/browse/CL-9) — [createsend.com#15783](https://git.campmon.com/Freshview/createsend.com/pull/15783) — CL-9-b Implement async subscriber export stream writers
- 2023-08-02 — [CL-9](https://campaignmonitor.atlassian.net/browse/CL-9) — [createsend.com#15853](https://git.campmon.com/Freshview/createsend.com/pull/15853) — CL-9-d Export subscribers improvements
- 2023-08-11 — [CL-9](https://campaignmonitor.atlassian.net/browse/CL-9) — [createsend.com#15938](https://git.campmon.com/Freshview/createsend.com/pull/15938) — CL-9-f Implement feature flag 838 SubscriberExport

---

### ZUSE — Zuse
_Zuse team onboarding_

**Reviewed:** 6 PRs from 2024-10-17 to 2026-03-03

---

### STRK — Strikeforce Porpoise
_Migrating internal services into CmAPI.ContentManagement project_

**Reviewed:** 5 PRs from 2025-11-11 to 2026-05-04

---

### JC — JC
_Project metadata not retrievable in this session_

**Authored:** 1 PRs from 2025-04-08 to 2025-04-08
**Reviewed:** 3 PRs from 2024-07-23 to 2025-04-08

**Sample authored PRs:**

- 2025-04-08 — [JC-406](https://campaignmonitor.atlassian.net/browse/JC-406) — [createsend.com#19365](https://git.campmon.com/Freshview/createsend.com/pull/19365) — JC-406-c Migrate bundles to react 18

---

### HOP — HOPPER
_Hopper — account setup / experiment enrolment_

**Reviewed:** 4 PRs from 2025-04-07 to 2025-11-12

---

### CONV — Convert
_Conversion / setup-guide / plan-selection_

**Reviewed:** 3 PRs from 2022-04-11 to 2022-05-09

---

### SHARE — Share
_Sharing / collaboration_

**Reviewed:** 3 PRs from 2025-09-11 to 2025-11-05

---

### LSK — LSK
_Project metadata not retrievable_

**Reviewed:** 3 PRs from 2025-09-30 to 2026-05-04

---

### CAS — CAS
_Project metadata not retrievable in this session_

**Authored:** 1 PRs from 2021-07-23 to 2021-07-23
**Reviewed:** 1 PRs from 2021-06-08 to 2021-06-08

**Sample authored PRs:**

- 2021-07-23 — [CAS-2156](https://campaignmonitor.atlassian.net/browse/CAS-2156) — [createsend.com#10444](https://git.campmon.com/Freshview/createsend.com/pull/10444) — CAS-2156 Hide field required checkbox for MultiSelectMany on copypaste forms

---

### UX3 — UX Refresh 3
_Subsequent UX-refresh project (likely renamed/archived)_

**Authored:** 2 PRs from 2021-09-22 to 2021-09-22

**Sample authored PRs:**

- 2021-09-22 — [UX3-773](https://campaignmonitor.atlassian.net/browse/UX3-773) — [SegmentTrackingPlan#262](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/262) — UX3-773 Add Email Builder Content Types Used property values
- 2021-09-22 — [UX3-773](https://campaignmonitor.atlassian.net/browse/UX3-773) — [createsend.com#10963](https://git.campmon.com/Freshview/createsend.com/pull/10963) — UX3-773 Add Email Builder Content Types Used property values

---

### AML — Audience Multi-List?
_Audience-side work_

**Reviewed:** 2 PRs from 2026-01-30 to 2026-03-24

---

### CD — Continuous Delivery
_CD pipeline work_

**Reviewed:** 1 PRs from 2025-08-14 to 2025-08-14

---

### TUR — TUR
_Project metadata not retrievable_

**Reviewed:** 1 PRs from 2026-01-14 to 2026-01-14

---

---

## 🆕 2026-H2 projects (Jun–Nov 2026)
Full detail: [data/2026-h2/findings-jira.md](data/2026-h2/findings-jira.md).

| Project / epic | Team | Your share | Notes |
|---|---|---|---|
| **AJ-1111** Advanced Drip Campaigns – Branching | Boole | 10 of 68 assigned; frontend owner | Done 9 Oct; all plans 1 Oct |
| AJ-1158 Simple Drip UI / AJ-1250 fast-follows | Boole | 1 / 3 | ~22 fast-follows left in backlog after the merge |
| AJ-1192 Journey Reporting innovation sprint | Boole | 2 | Not productionised by you |
| AJ-961 Graylog → Datadog | Boole | 3 | Done 17 Sep |
| **COM-1620** SMS Twilio Compliance Embeddable (Sales Led) | **Mitnick** | **16 of 28 reported, 8 assigned** | De-facto technical lead |
| COM-1629 Brand Hub V2 1A | Mitnick | 3 (entire frontend) | In flight |
| COM-1673 AI-DLC Stream A build | Mitnick | 1 (whole build phase) | No-go 3 Nov |
| COM-1625 UCF alerts | Mitnick | Investigation owner | Cross-team regression |
| **JC-411** createsend web app build improvements | JS Crew | **Epic creator + all 24 children** | Stage 1 done; stages 2–3 in flight |
| JC-436 CM-GITHUB bot outage | JS Crew | Reporter + fixer | ~9h40m outage, RCA |

**New project keys since May:** COM (Team Mitnick, after the 1 Sep merge) and JC (as epic owner, not just member).
