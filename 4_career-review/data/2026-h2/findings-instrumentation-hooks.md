<!--
RAW: code crawl of /Users/clementng/dev clones, 2026-11-12 (createsend.com on COM-1794 branch,
47 behind master; BrandHubServices on aidlc-a-6). Condensed from an agent sweep of track calls,
StatsD metrics, flags and schema. Full query recipes included so numbers can be re-pulled.
-->

# Instrumentation hooks — how each feature's adoption is (and isn't) measurable

**Analytics pipeline:** Segment Track → Amplitude. Backend constants in
`CampMon.Core.NetStandard/Metrics/SegmentAnalytics/SegmentAnalyticsEvents.cs`; frontend constants in
`shared/cm-api/utils/analyticsEvents.ts` (generated from events.yaml); wrapper
`analyticsUtils.ts` (`trackAnalyticsEvent`, `trackClientUIEvent` → generic "Interacted With UI").
Datadog via `CampMon.Util.NetStandard/Logging/Stats.cs` (DogStatsD).

## Advanced Drip — well instrumented
- `Created Drip Campaign` (`SequenceAnalyticsService.cs:23`, fired from `SequenceMailingService.cs:595`)
  carries **`Drip Type` = Advanced|Basic**, `Client Id`, `Drip Campaign Id` → the adoption split.
- `Added Campaign To Drip Campaign` carries `Branch` (Unconditional/Yes/No — advanced only);
  `Added/Updated/Deleted Condition…` events = branching usage (`Condition Type` values: Was opened /
  Had any link clicked / Was opened with no links clicked / Was not opened).
- `Sent Campaign` has `Is In Drip Campaign` (bool) but **not** the type, and misses accounts flagged
  only via `CampaignSequenceForAllAccountTypes` → for sends, use SQL instead.
- **SQL:** `CS_Sequence.SequenceType=1` (complex) → `SELECT COUNT(DISTINCT ClientID)…` per shard;
  `CS_Campaign.SendingAgentType=1` (set in `SequenceCampaignRepository.cs:222`) = advanced-drip
  campaigns actually sent — your schema column doubling as the adoption counter, as designed.
  `CS_ComplexSequenceNodeTree` gives depth/branching complexity per sequence.
- Flags for exposure: `ComplexCampaignSequence=1169`, `CampaignSequence=1110`,
  `CampaignSequenceForAllAccountTypes=1136`, `BasicCampaignSequenceUIRefresh=1216` (`F_FeatureUsers`).
- Datadog `mailingsendservice.complexsequence.*` = operational health only (your dashboard a3b-9pp-efn).

## SMS compliance embed — partly instrumented
- `Set Up SMS` (`SmsSetupAnalyticsService.cs:37`, fired from
  `SmsComplianceEmbedClientSetupService.cs:69,84`) fires when the embed initialises a customer
  (number provisioned / inquiry started / access granted as Verifying). Properties: **`Number Type`
  (Toll Free = unambiguously the embed; Alphanumeric is shared with the legacy flow)**, `Countries Enabled`.
  **First live data: w/c 2 Nov 2026 — 2 Alphanumeric + 1 Toll Free.**
- Cleanest embed-specific SQL: `CL_ActivityLog` where `Category='SmsClientAccessEnabled' AND
  Description LIKE '%Enabled by: Compliance embed%'` (logged at `SmsComplianceEmbedClientSetupService.cs:76`).
- Per-customer Slack post to the SMS compliance channel ("…created through the compliance embed").
- Datadog APM request volume: `campmon.cmapi.netcore-http-server` resources
  `compliance-embed-status|init|session` (`SmsSetupController.cs:25-41`). Info-level logs in
  `SmsComplianceEmbedService.cs:402,449,503,519` mark provisions/starts/resumes per ClientId.
- **Gaps you can own:** no event for Twilio inquiry *submitted* (frontend
  `SmsRegistrationNew.tsx:34` has a literal `// TODO: Used for tracking later`;
  `onInquirySubmitted` updates UI state only), and no event for approval/rejection (that status
  lives in Shared Services `ProvisioningStatusType`, read in `SmsComplianceEmbedService.cs:30`).
- Flag: `SmsTwilioComplianceEmbed=1228`. Theming is config (`TwilioEmbeddableThemeSetIdForDirect/ForAgency`), not a flag.

## Brand Hub V2 — editing not instrumented at all
- Exists today: page view `Brand Hub`; `Started Brand Collection` (frontend,
  `brandTrackingUtils.ts:11`, props `Location`/`Collection Type`/`Is Recollection`);
  `Completed/Failed Brand Collection` from the Node AIBrandScraper (`analytics.ts:12`,
  `pipeline.ts:301,349` — props incl. `Number Of Colors`). ⚠️ the C# replacement pipeline emits no
  analytics, so these may stop at cutover.
- **V2 editing (colour edits, asset deletes, 409 conflicts): zero events or metrics.** The editing
  components have no track calls; the only proxy is APM on `PUT …/brand/colors` with
  `http.status_code:409` on the ContentManagement service.
- SQL (BrandHub Postgres): `brand_kit.version` is append-only — one row per save
  (`BrandKitRepository.cs:78-100`) → versions-per-kit ≈ edit count once V2 lands, but there is no
  "manually edited" marker; `jobs` table gives collection counts per client.
- Flags: `BrandHubV2=1236`, `BrandHub=1207`, agency `ClientFeature.BrandHub=5`; gate in
  `BrandHubAccessService.cs:39` (excludes `GenAiOptOut`).

## No adoption dashboards exist anywhere
Datadog-as-code (`terraform/environment/global/cmapi_netcore_datadog/`) is generic APM health; no
Amplitude dashboards configured. → The "define success metrics before launch" ask in the CADD/HR
form is backed by this: the org genuinely has no adoption dashboards for these features.

## Instrument-next list (small PRs, high leverage for the TL case)
1. `Submitted Compliance Inquiry` + `Compliance Registration Approved/Rejected` events (close the
   SMS funnel; the TODO is already in the code).
2. `Edited Brand Kit Colors` / `Deleted Brand Asset` / 409-conflict counter for V2 — agree the
   "% kits corrected" metric with the PM before GA.
3. A `Drip Type` property on `Sent Campaign` (or a small SQL job off `SendingAgentType=1`) so send
   volume per drip type is chartable without shard queries.
