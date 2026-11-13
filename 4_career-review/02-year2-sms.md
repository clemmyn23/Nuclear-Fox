# Year 2 — SMS product + JS toolchain steward

**Window:** 2022-04 → 2023-03
**Authored:** 131 PRs (113 merged, 18 closed-without-merge / open)
**Reviewed:** 116 PRs
**JIRA projects (authored):** SMS (72), ED (3), CA (3)
**Top repos (authored):** Freshview/createsend.com (103), Freshview/campmon.hex (10), Engineering/SegmentTrackingPlan (4), platform/cm.protobuf (4), Engineering/contentbuildercontext.staticresourceservice.core (2)
**Top reviewed authors:** engineer (26), engineer (14), engineer (12), engineer (7), engineer (6), engineer (6), engineer (5), engineer (5)

## The story of Year 2 (Apr 2022 — Mar 2023)

The **SMS product squad** year. 72 SMS-tagged PRs in twelve months touching the **whole stack** — UI, CMAPI endpoints, gRPC services, protobufs, Kafka ACLs, JVM libs, the HEX admin tool, and analytics tracking. This is where you graduated from "good frontend engineer" to "engineer who can ship a vertical slice through any layer."

Three threads to call out:

**1. The full-stack SMS build-out.** SMS reporting end-to-end (link tracking SMS-155 across [cm.protobuf#586](https://git.campmon.com/platform/cm.protobuf/pull/586), [cm.protobuf#588](https://git.campmon.com/platform/cm.protobuf/pull/588), [TrackingServices#73](https://git.campmon.com/platform/TrackingServices/pull/73), [createsend.com#13257](https://git.campmon.com/Freshview/createsend.com/pull/13257); clicks page SMS-162 a/b/c/d/e/f; bounces SMS-89), geo expansion (country add/remove SMS-266, phone-number lookup SMS-313, signup-form mobile field SMS-396/398), preference-center consent (SMS-543/583). This is huge surface area for one engineer in one year.

**2. The JS-toolchain modernisation.** You ran a multi-quarter rebuild of the createsend.com JS stack:
- Yarn workspaces ([#12692](https://git.campmon.com/Freshview/createsend.com/pull/12692), April)
- Vite change-day ([#12854](https://git.campmon.com/Freshview/createsend.com/pull/12854), May)
- esbuild-loader for dev ([#13540](https://git.campmon.com/Freshview/createsend.com/pull/13540), August)
- Node 16 LTS ([#13212](https://git.campmon.com/Freshview/createsend.com/pull/13212), July) — also covered windows agents in [aws.stack.build#83](https://git.campmon.com/operations/aws.stack.build/pull/83)
- TypeScript 4 upgrade ([#13877](https://git.campmon.com/Freshview/createsend.com/pull/13877), October)
- Prettier 2.7 + ESLint upgrade in three-PR batches (config → auto-fix → manual cleanups, repeated twice in Oct + Dec)

You weren't just shipping product, you were steering the platform underneath. This is the year the "JS-crew steward" identity is most visible.

**3. Reviewer footprint widens.** 116 reviews across 29 distinct authors — more than the 87 of Year 1, and spread over more squads. Your reviews now cover Subject Line / Feature Feedback Widget (SE-), Client Settings / API key UI (EL-), Shopify Merchant integration (MER-), plan-selection / setup-guide (CONV-), payments (PP- Braintree), and snapshot/machine-clicks (PLAT-). The first signs of "JS-crew polyglot" — trusted across products, not just within your own squad.

## Confluence — first design-doc presence

Three pages authored this year — the start of the "I wrote the doc for the system I just learned" pattern that recurs every year after.

- **2022-06-29 — [Running JSONToProtoTrackEnricher locally for sms link tracking development](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/238686665/)** *(Compose space)* — local-dev setup reference for SMS link-tracking enrichment, adapted from a teammate's earlier guide. Co-evolved with the [SMS-155 protobuf + Kafka + monolith work](https://git.campmon.com/platform/cm.protobuf/pull/588) shipping the same week.
- **2022-07-08 — [Upgrading Node.JS on build agents](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/238686695/)** *(Compose space, JS-crew operational reference)* — the three places to bump the Node version (`Dockerfile.jsbuild`, `tasks.sh`, `aws.stack.build/roles/campmon.windows-agent`) plus notes on Node 17's OpenSSL engine change. Published the same week as [createsend.com#13212 Node 16 LTS](https://git.campmon.com/Freshview/createsend.com/pull/13212). **This document is what the team refers to for every Node bump after.**
- **2022-12-21 — [Signup forms functional and technical audit](https://campaignmonitor.atlassian.net/wiki/spaces/DEV/pages/240617940/)** *(Engineering space)* — frontend + backend walkthrough of the Signup Forms feature: how primary fields wire to `GrowYourAudienceBase.cs`, how custom fields and permission checkboxes are added, translations, and the GrowYourAudienceUpdater service-agent refresh cycle. Came out of the [SMS-396 / SMS-451 / SMS-477](https://git.campmon.com/Freshview/createsend.com/pull/14288) signup-form work. Still in the Engineering space as of 2026.

**Slack discussions captured:** none from this period in the curated set — the engineering-writing surface in chat became prominent from Year 4 onwards. See [13-slack-architecture-discussions.md](13-slack-architecture-discussions.md) for the curated list across all years.

## All 131 authored PRs

| Date | Repo | # | JIRA | State | Title |
|---|---|---|---|---|---|
| 2022-04-06 | Engineering/localdev-tools | [#50](https://git.campmon.com/Engineering/localdev-tools/pull/50) | — | ✅ | Update star.localcreatesend cert |
| 2022-04-07 | Engineering/SegmentTrackingPlan | [#299](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/299) | [SMS-109](https://campaignmonitor.atlassian.net/browse/SMS-109) | 🔴 | SMS-109-a Add SMS page load tracking |
| 2022-04-08 | Engineering/SegmentTrackingPlan | [#300](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/300) | [SMS-109](https://campaignmonitor.atlassian.net/browse/SMS-109) | ✅ | SMS-109-a Add SMS page load tracking (remake) |
| 2022-04-11 | createsend.com | [#12631](https://git.campmon.com/Freshview/createsend.com/pull/12631) | [SMS-109](https://campaignmonitor.atlassian.net/browse/SMS-109) | ✅ | SMS-109-b SMS page tracking |
| 2022-04-12 | createsend.com | [#12647](https://git.campmon.com/Freshview/createsend.com/pull/12647) | [SMS-109](https://campaignmonitor.atlassian.net/browse/SMS-109) | ✅ | SMS-109-c Tracking page load - list of suppressed mobiles |
| 2022-04-12 | createsend.com | [#12653](https://git.campmon.com/Freshview/createsend.com/pull/12653) | [SMS-77](https://campaignmonitor.atlassian.net/browse/SMS-77) | ✅ | SMS-77-b ManageSmsCampaigns localized loading spinners |
| 2022-04-13 | createsend.com | [#12661](https://git.campmon.com/Freshview/createsend.com/pull/12661) | [SMS-77](https://campaignmonitor.atlassian.net/browse/SMS-77) | ✅ | SMS-77-c ManageSmsCampaigns - Moving a lot of files and cleanups |
| 2022-04-19 | createsend.com | [#12684](https://git.campmon.com/Freshview/createsend.com/pull/12684) | [SMS-112](https://campaignmonitor.atlassian.net/browse/SMS-112) | ✅ | SMS-112-a Show toast when sms campaign creation error |
| 2022-04-19 | createsend.com | [#12692](https://git.campmon.com/Freshview/createsend.com/pull/12692) | — | ✅ | Setup yarn workspaces |
| 2022-04-20 | createsend.com | [#12707](https://git.campmon.com/Freshview/createsend.com/pull/12707) | [SMS-91](https://campaignmonitor.atlassian.net/browse/SMS-91) | ✅ | SMS-91 SMS Reports - Adjust mobile preview widths |
| 2022-04-20 | createsend.com | [#12708](https://git.campmon.com/Freshview/createsend.com/pull/12708) | — | ✅ | SendApiUpdate Fetch csrf token on page load only |
| 2022-04-21 | createsend.com | [#12714](https://git.campmon.com/Freshview/createsend.com/pull/12714) | — | ✅ | SendApiUpdate 2 - Fix potential test failures |
| 2022-04-22 | createsend.com | [#12717](https://git.campmon.com/Freshview/createsend.com/pull/12717) | — | 🔴 | Upgrade typescript 4.6.3 latest |
| 2022-04-27 | createsend.com | [#12745](https://git.campmon.com/Freshview/createsend.com/pull/12745) | [SMS-121](https://campaignmonitor.atlassian.net/browse/SMS-121) | ✅ | SMS-121 Sms log sent metrics to datadog |
| 2022-04-27 | createsend.com | [#12748](https://git.campmon.com/Freshview/createsend.com/pull/12748) | — | ✅ | JS: Copy more files to docker container for build |
| 2022-04-27 | createsend.com | [#12749](https://git.campmon.com/Freshview/createsend.com/pull/12749) | — | ✅ | JS: Update dockerignore |
| 2022-04-27 | createsend.com | [#12751](https://git.campmon.com/Freshview/createsend.com/pull/12751) | — | ✅ | JS: update yarn lockfile |
| 2022-04-29 | createsend.com | [#12779](https://git.campmon.com/Freshview/createsend.com/pull/12779) | [SMS-121](https://campaignmonitor.atlassian.net/browse/SMS-121) | ✅ | SMS-121-b SMS sent campaign metrics fix |
| 2022-05-03 | Engineering/contentbuildercontext.staticresourceservice.core | [#763](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/763) | [ED-1257](https://campaignmonitor.atlassian.net/browse/ED-1257) | ✅ | ED-1257 Keyboard shortcuts |
| 2022-05-06 | createsend.com | [#12824](https://git.campmon.com/Freshview/createsend.com/pull/12824) | [SMS-126](https://campaignmonitor.atlassian.net/browse/SMS-126) | ✅ | SMS-126-a Move PrepareToSend sub-steps code into own directories |
| 2022-05-10 | createsend.com | [#12843](https://git.campmon.com/Freshview/createsend.com/pull/12843) | [SMS-126](https://campaignmonitor.atlassian.net/browse/SMS-126) | ✅ | SMS-126-b SMS Show delivery cost on prepare to send dialog |
| 2022-05-10 | Engineering/SegmentTrackingPlan | [#310](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/310) | [ED-1257](https://campaignmonitor.atlassian.net/browse/ED-1257) | ✅ | ED-1257-b Add keyboard shortcut tracking property |
| 2022-05-11 | Engineering/contentbuildercontext.staticresourceservice.core | [#765](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/765) | [ED-1257](https://campaignmonitor.atlassian.net/browse/ED-1257) | ✅ | ED-1257-b Tracking keyboard shortcuts |
| 2022-05-12 | createsend.com | [#12854](https://git.campmon.com/Freshview/createsend.com/pull/12854) | — | 🔴 | [Change-day] Vite build 1 |
| 2022-05-16 | createsend.com | [#12860](https://git.campmon.com/Freshview/createsend.com/pull/12860) | — | ✅ | Add polyfill String.prototype.matchAll for Safari 12 |
| 2022-05-17 | createsend.com | [#12877](https://git.campmon.com/Freshview/createsend.com/pull/12877) | [CA-1309](https://campaignmonitor.atlassian.net/browse/CA-1309) | ✅ | CA-1309 Fix stuck campaign when fallback email has whitespace |
| 2022-05-20 | CMDS/cm-utils | [#96](https://git.campmon.com/CMDS/cm-utils/pull/96) | [CA-1309](https://campaignmonitor.atlassian.net/browse/CA-1309) | ✅ | CA-1309-b Spaces in front of fallbacks in sender email address cause stuck campaigns |
| 2022-05-20 | createsend.com | [#12902](https://git.campmon.com/Freshview/createsend.com/pull/12902) | [CA-1309](https://campaignmonitor.atlassian.net/browse/CA-1309) | ✅ | CA-1309-c Bump is-personalized-email  |
| 2022-05-23 | createsend.com | [#12915](https://git.campmon.com/Freshview/createsend.com/pull/12915) | — | ✅ | Upgrade eslint packages |
| 2022-05-23 | createsend.com | [#12918](https://git.campmon.com/Freshview/createsend.com/pull/12918) | — | ✅ | Eslint fixes scrfrontend |
| 2022-05-24 | platform/cm.protobuf | [#578](https://git.campmon.com/platform/cm.protobuf/pull/578) | [SMS-137](https://campaignmonitor.atlassian.net/browse/SMS-137) | ✅ | SMS-137 Add contact_id to SMS bounce and opt-out |
| 2022-05-26 | createsend.com | [#12951](https://git.campmon.com/Freshview/createsend.com/pull/12951) | — | ✅ | Pin lerna version in jsbuild dockerfile |
| 2022-05-27 | Engineering/SmsSendingServices | [#34](https://git.campmon.com/Engineering/SmsSendingServices/pull/34) | [SMS-137](https://campaignmonitor.atlassian.net/browse/SMS-137) | ✅ | SMS-137-c Add contact_id to bounces/ opt-out proto |
| 2022-06-02 | Engineering/SmsSendingServices | [#35](https://git.campmon.com/Engineering/SmsSendingServices/pull/35) | — | ✅ | Bump cm.protobuf 1.0.1002 |
| 2022-06-03 | createsend.com | [#13012](https://git.campmon.com/Freshview/createsend.com/pull/13012) | — | ✅ | Eslint fixes app, shared |
| 2022-06-08 | createsend.com | [#13037](https://git.campmon.com/Freshview/createsend.com/pull/13037) | [SMS-167](https://campaignmonitor.atlassian.net/browse/SMS-167) | ✅ | SMS-167 Redirect away checklist when sms campaign is sent.  |
| 2022-06-10 | createsend.com | [#13067](https://git.campmon.com/Freshview/createsend.com/pull/13067) | [SMS-178](https://campaignmonitor.atlassian.net/browse/SMS-178) | ✅ | SMS-178 Prevent sms edit when delivered or deleted |
| 2022-06-15 | platform/cm.protobuf | [#586](https://git.campmon.com/platform/cm.protobuf/pull/586) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-a Setup ContactClickedLinkInSmsMailing |
| 2022-06-16 | platform/TrackingServices | [#73](https://git.campmon.com/platform/TrackingServices/pull/73) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-b SMS link tracking clientid enrichment |
| 2022-06-17 | platform/cm.protobuf | [#588](https://git.campmon.com/platform/cm.protobuf/pull/588) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | 🔴 | SMS-155-b Add SmsMailingLookupServiceGrpc.GetClientIdForSmsMailingId |
| 2022-06-17 | platform/cm.protobuf | [#589](https://git.campmon.com/platform/cm.protobuf/pull/589) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-c GetSmsMailingOwner grpc  |
| 2022-06-21 | createsend.com | [#13115](https://git.campmon.com/Freshview/createsend.com/pull/13115) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-d Upgrade cm.protobufs 1.0.1009 |
| 2022-06-21 | createsend.com | [#13125](https://git.campmon.com/Freshview/createsend.com/pull/13125) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-e Implement grpc GetSmsMailingOwner |
| 2022-06-24 | platform/kafka-acls | [#85](https://git.campmon.com/platform/kafka-acls/pull/85) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-f  Add sms link tracking topics |
| 2022-06-24 | Engineering/jvm-libs | [#114](https://git.campmon.com/Engineering/jvm-libs/pull/114) | [SMS-155](https://campaignmonitor.atlassian.net/browse/SMS-155) | ✅ | SMS-155-g Protobuf builders SmsMailingId SmsMailingLinkId |
| 2022-06-29 | createsend.com | [#13196](https://git.campmon.com/Freshview/createsend.com/pull/13196) | — | ✅ | Revert "Upgrade eslint packages" |
| 2022-06-30 | createsend.com | [#13199](https://git.campmon.com/Freshview/createsend.com/pull/13199) | — | ✅ | Update node 16 lts |
| 2022-07-01 | createsend.com | [#13207](https://git.campmon.com/Freshview/createsend.com/pull/13207) | — | 🔴 | Eslint upgrade. Second try.  |
| 2022-07-04 | createsend.com | [#13212](https://git.campmon.com/Freshview/createsend.com/pull/13212) | — | ✅ | Remove "95% emitting" message |
| 2022-07-08 | operations/aws.stack.build | [#83](https://git.campmon.com/operations/aws.stack.build/pull/83) | — | ✅ | Update Nodejs to 16.15.1 LTS in windows agents |
| 2022-07-08 | createsend.com | [#13250](https://git.campmon.com/Freshview/createsend.com/pull/13250) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-a Sms report - snapshot page changes |
| 2022-07-11 | createsend.com | [#13254](https://git.campmon.com/Freshview/createsend.com/pull/13254) | — | ✅ | ChartStatistic - Change label from p to div |
| 2022-07-11 | createsend.com | [#13257](https://git.campmon.com/Freshview/createsend.com/pull/13257) | — | ✅ | Eslint upgrade. The other second try.  |
| 2022-07-12 | createsend.com | [#13264](https://git.campmon.com/Freshview/createsend.com/pull/13264) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-b smscampaignreport Link tracking changes part 2 |
| 2022-07-25 | createsend.com | [#13343](https://git.campmon.com/Freshview/createsend.com/pull/13343) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-c Sms reports clicks page part c |
| 2022-07-27 | createsend.com | [#13359](https://git.campmon.com/Freshview/createsend.com/pull/13359) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-d Sms link tracking - clicks page integration.  |
| 2022-08-01 | createsend.com | [#13382](https://git.campmon.com/Freshview/createsend.com/pull/13382) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-d SMS reports clicks page cmapi integration |
| 2022-08-04 | createsend.com | [#13395](https://git.campmon.com/Freshview/createsend.com/pull/13395) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-e Sms reports clicks breakdown link to contacts page  |
| 2022-08-08 | createsend.com | [#13410](https://git.campmon.com/Freshview/createsend.com/pull/13410) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-f SMS Reports - show minutes in sms clicks history graph |
| 2022-08-11 | createsend.com | [#13443](https://git.campmon.com/Freshview/createsend.com/pull/13443) | [SMS-206](https://campaignmonitor.atlassian.net/browse/SMS-206) | ✅ | SMS-206-a SMS checklist - CMAPI Save selected segments  |
| 2022-08-17 | createsend.com | [#13480](https://git.campmon.com/Freshview/createsend.com/pull/13480) | [SMS-206](https://campaignmonitor.atlassian.net/browse/SMS-206) | ✅ | SMS-206-b SMS-checklist Show selected segments |
| 2022-08-18 | createsend.com | [#13494](https://git.campmon.com/Freshview/createsend.com/pull/13494) | [SMS-206](https://campaignmonitor.atlassian.net/browse/SMS-206) | ✅ | SMS-206-c SMS-checklist - Bug fixes |
| 2022-08-19 | createsend.com | [#13501](https://git.campmon.com/Freshview/createsend.com/pull/13501) | [SMS-199](https://campaignmonitor.atlassian.net/browse/SMS-199) | ✅ | SMS-199-a - Add SmsListsAndSegmentsRepository |
| 2022-08-22 | createsend.com | [#13504](https://git.campmon.com/Freshview/createsend.com/pull/13504) | [SMS-206](https://campaignmonitor.atlassian.net/browse/SMS-206) | ✅ | SMS-206-d SMS-checklist-segments - More bugfixes |
| 2022-08-24 | createsend.com | [#13526](https://git.campmon.com/Freshview/createsend.com/pull/13526) | [SMS-199](https://campaignmonitor.atlassian.net/browse/SMS-199) | ✅ | SMS-199-b Register SmsListsAndSegmentsRepository singleton for dotnetcore services |
| 2022-08-24 | createsend.com | [#13528](https://git.campmon.com/Freshview/createsend.com/pull/13528) | [SMS-199](https://campaignmonitor.atlassian.net/browse/SMS-199) | ✅ | SMS-199-c SMS-checklist - Recipient count support for segments.  |
| 2022-08-25 | createsend.com | [#13536](https://git.campmon.com/Freshview/createsend.com/pull/13536) | — | ✅ | SMS checklist - Increase dialog width to 1200px to match email |
| 2022-08-26 | createsend.com | [#13540](https://git.campmon.com/Freshview/createsend.com/pull/13540) | — | ✅ | Use esbuild-loader for development js builds.  |
| 2022-08-30 | createsend.com | [#13555](https://git.campmon.com/Freshview/createsend.com/pull/13555) | [SMS-199](https://campaignmonitor.atlassian.net/browse/SMS-199) | ✅ | SMS-199-d Add empty check for SMS segments |
| 2022-08-30 | createsend.com | [#13556](https://git.campmon.com/Freshview/createsend.com/pull/13556) | — | 🔴 | JS build - Remove old yarn lockfile |
| 2022-08-30 | createsend.com | [#13557](https://git.campmon.com/Freshview/createsend.com/pull/13557) | — | ✅ | JS build - Enable localdev esbuild for most scrfrontend apps |
| 2022-09-07 | createsend.com | [#13598](https://git.campmon.com/Freshview/createsend.com/pull/13598) | [SMS-266](https://campaignmonitor.atlassian.net/browse/SMS-266) | ✅ | SMS-266-b Add and remove sms country |
| 2022-09-09 | campmon.hex | [#693](https://git.campmon.com/Freshview/campmon.hex/pull/693) | [SMS-266](https://campaignmonitor.atlassian.net/browse/SMS-266) | ✅ | SMS-266-a SMS client add and remove regions |
| 2022-09-09 | campmon.hex | [#694](https://git.campmon.com/Freshview/campmon.hex/pull/694) | — | 🔴 | Update cm packages |
| 2022-09-09 | campmon.hex | [#695](https://git.campmon.com/Freshview/campmon.hex/pull/695) | — | ✅ | Update cm packages |
| 2022-09-12 | createsend.com | [#13632](https://git.campmon.com/Freshview/createsend.com/pull/13632) | — | ✅ | JS build - Remove old yarn lockfile b |
| 2022-09-13 | campmon.hex | [#696](https://git.campmon.com/Freshview/campmon.hex/pull/696) | — | ✅ | Add dropdown entry 'login via localcreatesend' |
| 2022-09-13 | campmon.hex | [#697](https://git.campmon.com/Freshview/campmon.hex/pull/697) | [SMS-266](https://campaignmonitor.atlassian.net/browse/SMS-266) | ✅ | SMS-266-c Update confirm-SMS-country dialog styling |
| 2022-09-13 | campmon.hex | [#698](https://git.campmon.com/Freshview/campmon.hex/pull/698) | — | ✅ | HEX - Remove email domain check for login-via-localcreatesend |
| 2022-09-13 | createsend.com | [#13647](https://git.campmon.com/Freshview/createsend.com/pull/13647) | [SMS-251](https://campaignmonitor.atlassian.net/browse/SMS-251) | ✅ | SMS-251-a SMS Show cross-sale for externally billed AUS customers |
| 2022-09-26 | createsend.com | [#13733](https://git.campmon.com/Freshview/createsend.com/pull/13733) | [SMS-256](https://campaignmonitor.atlassian.net/browse/SMS-256) | ✅ | SMS-256-a Add table column SMS_Campaign.IncludeUnsubscribeInstruction |
| 2022-09-27 | createsend.com | [#13742](https://git.campmon.com/Freshview/createsend.com/pull/13742) | [SMS-243](https://campaignmonitor.atlassian.net/browse/SMS-243) | 🔴 | SMS-243-a Add CmSmsClient model and endpoint |
| 2022-09-28 | createsend.com | [#13757](https://git.campmon.com/Freshview/createsend.com/pull/13757) | [SMS-243](https://campaignmonitor.atlassian.net/browse/SMS-243) | ✅ | SMS-243-b Method to update sms client message prefix |
| 2022-09-29 | campmon.hex | [#705](https://git.campmon.com/Freshview/campmon.hex/pull/705) | — | ✅ | Upgrade cm packages |
| 2022-09-30 | campmon.hex | [#706](https://git.campmon.com/Freshview/campmon.hex/pull/706) | [SMS-243](https://campaignmonitor.atlassian.net/browse/SMS-243) | ✅ | SMS-243-d HEX Display and edit SMS organization prefix |
| 2022-10-05 | campmon.hex | [#707](https://git.campmon.com/Freshview/campmon.hex/pull/707) | [SMS-243](https://campaignmonitor.atlassian.net/browse/SMS-243) | ✅ | SMS-243-e HEX Hide edit button when client does not sms |
| 2022-10-06 | createsend.com | [#13793](https://git.campmon.com/Freshview/createsend.com/pull/13793) | [SMS-313](https://campaignmonitor.atlassian.net/browse/SMS-313) | ✅ | SMS-313-a Phone number geo lookup utility |
| 2022-10-12 | createsend.com | [#13841](https://git.campmon.com/Freshview/createsend.com/pull/13841) | [SMS-313](https://campaignmonitor.atlassian.net/browse/SMS-313) | 🔴 | SMS-313-b1 SMS country filtering 1 |
| 2022-10-12 | createsend.com | [#13842](https://git.campmon.com/Freshview/createsend.com/pull/13842) | [SMS-313](https://campaignmonitor.atlassian.net/browse/SMS-313) | ✅ | SMS-313-b2 SMS country filter 2 |
| 2022-10-14 | createsend.com | [#13857](https://git.campmon.com/Freshview/createsend.com/pull/13857) | — | 🔴 | Prettier update 2.7 and eslint changes |
| 2022-10-14 | createsend.com | [#13858](https://git.campmon.com/Freshview/createsend.com/pull/13858) | — | 🔴 | Prettier 2.7 and formatting changes |
| 2022-10-17 | createsend.com | [#13866](https://git.campmon.com/Freshview/createsend.com/pull/13866) | — | 🔴 | Prettier update - the auto fixable stuff |
| 2022-10-18 | createsend.com | [#13876](https://git.campmon.com/Freshview/createsend.com/pull/13876) | — | 🔴 | Prettier update - the manual cleanups |
| 2022-10-18 | createsend.com | [#13877](https://git.campmon.com/Freshview/createsend.com/pull/13877) | — | ✅ | Typescript 4 |
| 2022-10-24 | createsend.com | [#13910](https://git.campmon.com/Freshview/createsend.com/pull/13910) | — | ✅ | SMS Add sentry monitoring to sms apps |
| 2022-10-25 | createsend.com | [#13926](https://git.campmon.com/Freshview/createsend.com/pull/13926) | [SMS-364](https://campaignmonitor.atlassian.net/browse/SMS-364) | ✅ | SMS-364 Add FF 750 SmsSignupFormOptions |
| 2022-11-03 | createsend.com | [#13994](https://git.campmon.com/Freshview/createsend.com/pull/13994) | — | ✅ | [Change Day][ponte-vecchio] Segments builder changes 1 |
| 2022-11-04 | createsend.com | [#14003](https://git.campmon.com/Freshview/createsend.com/pull/14003) | — | 🔴 | [Change day][ponte vecchio] Copy segments (master)  |
| 2022-11-11 | createsend.com | [#14054](https://git.campmon.com/Freshview/createsend.com/pull/14054) | — | 🔴 | SMS Subscriber form WIP to be deleted |
| 2022-11-15 | createsend.com | [#14066](https://git.campmon.com/Freshview/createsend.com/pull/14066) | [SMS-396](https://campaignmonitor.atlassian.net/browse/SMS-396) | 🔴 | SMS-396-a SMS signup builder - show mobile field |
| 2022-11-15 | createsend.com | [#14075](https://git.campmon.com/Freshview/createsend.com/pull/14075) | [SMS-396](https://campaignmonitor.atlassian.net/browse/SMS-396) | ✅ | SMS-396-a2 SMS signup builder - show mobile field |
| 2022-11-22 | createsend.com | [#14129](https://git.campmon.com/Freshview/createsend.com/pull/14129) | [SMS-398](https://campaignmonitor.atlassian.net/browse/SMS-398) | ✅ | SMS-398-a Sms Signup form changes 1  |
| 2022-12-13 | createsend.com | [#14288](https://git.campmon.com/Freshview/createsend.com/pull/14288) | — | ✅ | Prettier-eslint update a2 - Config changes  |
| 2022-12-13 | createsend.com | [#14296](https://git.campmon.com/Freshview/createsend.com/pull/14296) | — | ✅ | Prettier-eslint update b2 - The auto fix stuff |
| 2022-12-13 | createsend.com | [#14298](https://git.campmon.com/Freshview/createsend.com/pull/14298) | — | ✅ | Prettier-eslint update c2 - The manual fixes |
| 2022-12-21 | createsend.com | [#14367](https://git.campmon.com/Freshview/createsend.com/pull/14367) | [SMS-451](https://campaignmonitor.atlassian.net/browse/SMS-451) | ✅ | SMS-451-a Mobile number signup form submission fixes |
| 2022-12-30 | createsend.com | [#14399](https://git.campmon.com/Freshview/createsend.com/pull/14399) | [SMS-477](https://campaignmonitor.atlassian.net/browse/SMS-477) | ✅ | SMS-477-a Signup form builder SMS design updates |
| 2023-01-10 | createsend.com | [#14435](https://git.campmon.com/Freshview/createsend.com/pull/14435) | [SMS-477](https://campaignmonitor.atlassian.net/browse/SMS-477) | ✅ | SMS-477-b Signup form prefill defaultMobileCountry based on account.  |
| 2023-01-12 | createsend.com | [#14450](https://git.campmon.com/Freshview/createsend.com/pull/14450) | [SMS-477](https://campaignmonitor.atlassian.net/browse/SMS-477) | ✅ | SMS-477-c Signup form SMS fixes and styling updates |
| 2023-01-13 | createsend.com | [#14456](https://git.campmon.com/Freshview/createsend.com/pull/14456) | [SMS-401](https://campaignmonitor.atlassian.net/browse/SMS-401) | ✅ | SMS-401-a Copy-paste signup form mobile input functionality |
| 2023-01-23 | createsend.com | [#14508](https://git.campmon.com/Freshview/createsend.com/pull/14508) | — | ✅ | Hosted form - Replace array.prot.find() to support ie11 |
| 2023-01-24 | createsend.com | [#14517](https://git.campmon.com/Freshview/createsend.com/pull/14517) | — | ✅ | Hosted form - Replace array.prot.find() to support ie11 2 |
| 2023-01-24 | createsend.com | [#14519](https://git.campmon.com/Freshview/createsend.com/pull/14519) | [SMS-510](https://campaignmonitor.atlassian.net/browse/SMS-510) | ✅ | SMS-510-a Change loading spinner to loading submit button |
| 2023-01-27 | createsend.com | [#14550](https://git.campmon.com/Freshview/createsend.com/pull/14550) | [SMS-500](https://campaignmonitor.atlassian.net/browse/SMS-500) | ✅ | SMS-500-a Hosted signup forms - Change SMS marketing consent checkbox to conditionally required |
| 2023-01-27 | createsend.com | [#14551](https://git.campmon.com/Freshview/createsend.com/pull/14551) | [SMS-510](https://campaignmonitor.atlassian.net/browse/SMS-510) | ✅ | SMS-510-b Copypaste forms - Fix css keyframes rule breaking copypaste form genenerator |
| 2023-01-30 | createsend.com | [#14561](https://git.campmon.com/Freshview/createsend.com/pull/14561) | [SMS-500](https://campaignmonitor.atlassian.net/browse/SMS-500) | ✅ | SMS-500-b Copypaste forms - Change SMS marketing consent checkbox to conditionally required |
| 2023-01-31 | createsend.com | [#14567](https://git.campmon.com/Freshview/createsend.com/pull/14567) | — | ✅ | Force https on all js and css assets |
| 2023-01-31 | createsend.com | [#14576](https://git.campmon.com/Freshview/createsend.com/pull/14576) | [SMS-416](https://campaignmonitor.atlassian.net/browse/SMS-416) | ✅ | SMS-416-a Singup-forms - Add translations for mobile fields |
| 2023-02-01 | createsend.com | [#14585](https://git.campmon.com/Freshview/createsend.com/pull/14585) | — | 🔴 | Force https only when request scheme is http |
| 2023-02-01 | createsend.com | [#14589](https://git.campmon.com/Freshview/createsend.com/pull/14589) | — | ✅ | Force hosted form js css https assets |
| 2023-02-27 | createsend.com | [#14780](https://git.campmon.com/Freshview/createsend.com/pull/14780) | — | ✅ | Revert "Force hosted form js css https assets" |
| 2023-02-27 | createsend.com | [#14782](https://git.campmon.com/Freshview/createsend.com/pull/14782) | — | 🔴 | Force hosted form js css https assets 2 |
| 2023-02-27 | createsend.com | [#14784](https://git.campmon.com/Freshview/createsend.com/pull/14784) | — | ✅ | Force hosted form js css https 2 |
| 2023-03-01 | createsend.com | [#14804](https://git.campmon.com/Freshview/createsend.com/pull/14804) | — | ✅ | Copy-paste form - Handle ie11 misfiring input events.  |
| 2023-03-13 | Engineering/SegmentTrackingPlan | [#358](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/358) | [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) | ✅ | SMS-543-a Add new event 'Changed Preference Center Field Settings' |
| 2023-03-14 | createsend.com | [#14872](https://git.campmon.com/Freshview/createsend.com/pull/14872) | [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) | ✅ | SMS-543-b Track preference center field changes |
| 2023-03-17 | createsend.com | [#14896](https://git.campmon.com/Freshview/createsend.com/pull/14896) | [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) | ✅ | SMS-543-c Add CAL category and logging 'ClientPreferenceCenterFieldVisibilitySettingsChanged' |
| 2023-03-21 | campmon.hex | [#752](https://git.campmon.com/Freshview/campmon.hex/pull/752) | [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) | ✅ | SMS-543-d Update CM packages |
| 2023-03-24 | createsend.com | [#14945](https://git.campmon.com/Freshview/createsend.com/pull/14945) | [SMS-583](https://campaignmonitor.atlassian.net/browse/SMS-583) | ✅ | SMS-583-a Preference center - SMS consent asterisk when not required |
| 2023-03-29 | createsend.com | [#14975](https://git.campmon.com/Freshview/createsend.com/pull/14975) | [SMS-583](https://campaignmonitor.atlassian.net/browse/SMS-583) | ✅ | SMS-583-b Preference center - Fix some field titles visible when fields are hidden |
| 2023-03-29 | createsend.com | [#14978](https://git.campmon.com/Freshview/createsend.com/pull/14978) | [SMS-543](https://campaignmonitor.atlassian.net/browse/SMS-543) | ✅ | SMS-543-c Fix Capitalization For Tracking Property Values |

## All 116 reviewed PRs

| Date | Author | Repo | # | JIRA | State | Title |
|---|---|---|---|---|---|---|
| 2022-04-04 | engineer | createsend.com | [#12574](https://git.campmon.com/Freshview/createsend.com/pull/12574) | [SMS-88](https://campaignmonitor.atlassian.net/browse/SMS-88) | ✅ | SMS-88: Unsubscribes link should go to unsubscribes tab of recipient activity |
| 2022-04-04 | engineer | createsend.com | [#12577](https://git.campmon.com/Freshview/createsend.com/pull/12577) | [SMS-107](https://campaignmonitor.atlassian.net/browse/SMS-107) | ✅ | SMS-107 prevent re-sending an SMS campaign |
| 2022-04-05 | engineer | createsend.com | [#12587](https://git.campmon.com/Freshview/createsend.com/pull/12587) | [EL-469](https://campaignmonitor.atlassian.net/browse/EL-469) | ✅ | EL-469 Get and rotate client api key |
| 2022-04-11 | engineer | createsend.com | [#12632](https://git.campmon.com/Freshview/createsend.com/pull/12632) | [CONV-951](https://campaignmonitor.atlassian.net/browse/CONV-951) | ✅ | CONV-951 Obsolete ChoosePlanIntroductionContentRefresh |
| 2022-04-11 | engineer | createsend.com | [#12636](https://git.campmon.com/Freshview/createsend.com/pull/12636) | [SMS-76](https://campaignmonitor.atlassian.net/browse/SMS-76) | ✅ | SMS-76-c SMS preview followup improvements |
| 2022-04-12 | engineer | Engineering/SegmentTrackingPlan | [#301](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/301) | [SMS-111](https://campaignmonitor.atlassian.net/browse/SMS-111) | ✅ | SMS-111: Add "Created Sms Campaign" event |
| 2022-04-12 | engineer | createsend.com | [#12650](https://git.campmon.com/Freshview/createsend.com/pull/12650) | [CONV-969](https://campaignmonitor.atlassian.net/browse/CONV-969) | ✅ | CONV-969 Re-order feature list for table expansion |
| 2022-04-12 | engineer | createsend.com | [#12651](https://git.campmon.com/Freshview/createsend.com/pull/12651) | [EL-559](https://campaignmonitor.atlassian.net/browse/EL-559) | ✅ | EL-559b Add hash routing to url |
| 2022-04-12 | engineer | createsend.com | [#12652](https://git.campmon.com/Freshview/createsend.com/pull/12652) | [SE-348](https://campaignmonitor.atlassian.net/browse/SE-348) | ✅ | SE-348 - Add feature feedback widget to the 'Latest Subject Line' |
| 2022-04-13 | engineer | createsend.com | [#12665](https://git.campmon.com/Freshview/createsend.com/pull/12665) | [SMS-124](https://campaignmonitor.atlassian.net/browse/SMS-124) | ✅ | SMS-124: Beginnings of usage of SmsBillingAccess |
| 2022-04-15 | engineer | createsend.com | [#12681](https://git.campmon.com/Freshview/createsend.com/pull/12681) | — | ✅ | Sms 110 b track sent sms campaign |
| 2022-04-20 | engineer | createsend.com | [#12703](https://git.campmon.com/Freshview/createsend.com/pull/12703) | — | ✅ | Sms 89 a sms report bounce refactor |
| 2022-04-20 | engineer | createsend.com | [#12709](https://git.campmon.com/Freshview/createsend.com/pull/12709) | — | ✅ | Sms 89 b sms report bounce count |
| 2022-04-27 | engineer | createsend.com | [#12750](https://git.campmon.com/Freshview/createsend.com/pull/12750) | — | ✅ | Sms 115 b delete sms |
| 2022-04-29 | engineer | createsend.com | [#12782](https://git.campmon.com/Freshview/createsend.com/pull/12782) | [PLAT-3051](https://campaignmonitor.atlassian.net/browse/PLAT-3051) | ✅ | PLAT-3051: Adjusted export on campaign snapshot. |
| 2022-05-02 | engineer | createsend.com | [#12791](https://git.campmon.com/Freshview/createsend.com/pull/12791) | [PLAT-3051](https://campaignmonitor.atlassian.net/browse/PLAT-3051) | ✅ | PLAT-3051 Add option to exclude machine clicks as checkbox |
| 2022-05-06 | engineer | createsend.com | [#12825](https://git.campmon.com/Freshview/createsend.com/pull/12825) | [SMS-125](https://campaignmonitor.atlassian.net/browse/SMS-125) | ✅ | SMS-125-c show SMS credits in checklist below preview |
| 2022-05-09 | engineer | Engineering/contentbuildercontext.staticresourceservice.core | [#764](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/764) | [CONV-974](https://campaignmonitor.atlassian.net/browse/CONV-974) | ✅ | CONV-974 - Implement unsplash alternative |
| 2022-05-10 | engineer | createsend.com | [#12846](https://git.campmon.com/Freshview/createsend.com/pull/12846) | [SE-402](https://campaignmonitor.atlassian.net/browse/SE-402) | ✅ | SE-402 - Use polyfill for ResizeObserver |
| 2022-05-17 | engineer | createsend.com | [#12876](https://git.campmon.com/Freshview/createsend.com/pull/12876) | [SMS-115](https://campaignmonitor.atlassian.net/browse/SMS-115) | ✅ | SMS-115-e fix delete dialog title plural |
| 2022-05-20 | engineer | createsend.com | [#12900](https://git.campmon.com/Freshview/createsend.com/pull/12900) | [CA-1302](https://campaignmonitor.atlassian.net/browse/CA-1302) | ✅ | CA-1302: Show preview on iOS |
| 2022-05-23 | senior engineer | createsend.com | [#12912](https://git.campmon.com/Freshview/createsend.com/pull/12912) | [MER-16](https://campaignmonitor.atlassian.net/browse/MER-16) | ✅ | MER-16 - add page to install shopify app from |
| 2022-05-24 | engineer | createsend.com | [#12925](https://git.campmon.com/Freshview/createsend.com/pull/12925) | — | ✅ | Ca 1311 b emoji picker for subject line |
| 2022-05-31 | engineer | Engineering/contentbuildercontext.staticresourceservice.core | [#767](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/767) | [MER-26](https://campaignmonitor.atlassian.net/browse/MER-26) | ✅ | MER-26: Add product list content type |
| 2022-06-06 | engineer | createsend.com | [#13015](https://git.campmon.com/Freshview/createsend.com/pull/13015) | [SMS-132](https://campaignmonitor.atlassian.net/browse/SMS-132) | ✅ | SMS-132: Update README.md |
| 2022-06-06 | engineer | createsend.com | [#13021](https://git.campmon.com/Freshview/createsend.com/pull/13021) | — | ✅ | Sms 148 link trailing slash |
| 2022-06-09 | engineer | createsend.com | [#13048](https://git.campmon.com/Freshview/createsend.com/pull/13048) | — | ✅ | SMS-bug-bash-fix-estimated-delivery-time |
| 2022-06-21 | engineer | createsend.com | [#13127](https://git.campmon.com/Freshview/createsend.com/pull/13127) | — | ✅ | Sms 38 a refactor sms message parser |
| 2022-06-24 | engineer | createsend.com | [#13161](https://git.campmon.com/Freshview/createsend.com/pull/13161) | — | ✅ | JS - Update yarn lock |
| 2022-06-27 | engineer | createsend.com | [#13166](https://git.campmon.com/Freshview/createsend.com/pull/13166) | — | ✅ | JS - Update testing library |
| 2022-06-27 | engineer | createsend.com | [#13168](https://git.campmon.com/Freshview/createsend.com/pull/13168) | [SMS-171](https://campaignmonitor.atlassian.net/browse/SMS-171) | ✅ | SMS-171 sms failed to delete |
| 2022-06-29 | engineer | createsend.com | [#13192](https://git.campmon.com/Freshview/createsend.com/pull/13192) | — | ✅ | Checklist: Minor follow up, removed an empty div |
| 2022-06-29 | engineer | createsend.com | [#13194](https://git.campmon.com/Freshview/createsend.com/pull/13194) | [SE-458](https://campaignmonitor.atlassian.net/browse/SE-458) | ✅ | SE-458 Reduce flicker of pill and form. |
| 2022-07-05 | engineer | createsend.com | [#13224](https://git.campmon.com/Freshview/createsend.com/pull/13224) | [SE-474](https://campaignmonitor.atlassian.net/browse/SE-474) | ✅ | SE-474 Remove open rate; remove "Create a campaign" button for cross-sell |
| 2022-07-05 | engineer | platform/kafka-acls | [#89](https://git.campmon.com/platform/kafka-acls/pull/89) | [SMS-158](https://campaignmonitor.atlassian.net/browse/SMS-158) | ✅ | SMS-158: Allow InsightsKafkaConsumer to consume ContactClickedLinkInSmsMailing |
| 2022-07-05 | engineer | createsend.com | [#13232](https://git.campmon.com/Freshview/createsend.com/pull/13232) | [EL-713](https://campaignmonitor.atlassian.net/browse/EL-713) | ✅ | EL-713.Client setting dropdown menu changes, refresh cm header and and new api and integration page |
| 2022-07-07 | engineer | createsend.com | [#13243](https://git.campmon.com/Freshview/createsend.com/pull/13243) | [SE-462](https://campaignmonitor.atlassian.net/browse/SE-462) | ✅ | SE-462 Simplify SMS Cross Sell endpoint calls |
| 2022-07-11 | engineer | data-tribe/insights-web-api | [#55](https://git.campmon.com/data-tribe/insights-web-api/pull/55) | [SMS-159](https://campaignmonitor.atlassian.net/browse/SMS-159) | ✅ | SMS-159-2-a: Update README for local development |
| 2022-07-13 | engineer | createsend.com | [#13272](https://git.campmon.com/Freshview/createsend.com/pull/13272) | [MER-43](https://campaignmonitor.atlassian.net/browse/MER-43) | ✅ | MER-43b - Show success/error banner based on querystring |
| 2022-07-15 | engineer | createsend.com | [#13289](https://git.campmon.com/Freshview/createsend.com/pull/13289) | — | ✅ | [CONV-924] Remove ClickMetrics endpoints and calls - they don't do anything |
| 2022-07-25 | engineer | createsend.com | [#13336](https://git.campmon.com/Freshview/createsend.com/pull/13336) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-snapshot-cm-api Util for calling CM API for clicks over time,… |
| 2022-07-27 | engineer | Engineering/TestAutomation | [#231](https://git.campmon.com/Engineering/TestAutomation/pull/231) | [CA-1327](https://campaignmonitor.atlassian.net/browse/CA-1327) | ✅ | CA-1327-m: Convert SendCampaignWithDynamicContentEmailBuilderSections to use checklist |
| 2022-07-28 | engineer | createsend.com | [#13367](https://git.campmon.com/Freshview/createsend.com/pull/13367) | [SMS-161](https://campaignmonitor.atlassian.net/browse/SMS-161) | ✅ | SMS-161-b: Links Details and Contact Clicks endpoints |
| 2022-08-01 | engineer | createsend.com | [#13384](https://git.campmon.com/Freshview/createsend.com/pull/13384) | [SMS-161](https://campaignmonitor.atlassian.net/browse/SMS-161) | ✅ | SMS-161-c: Add in encrypted ContactId to Contact-Clicks |
| 2022-08-02 | engineer | createsend.com | [#13389](https://git.campmon.com/Freshview/createsend.com/pull/13389) | — | ✅ | Sms 162 report snapshot polishing |
| 2022-08-05 | engineer | createsend.com | [#13398](https://git.campmon.com/Freshview/createsend.com/pull/13398) | [EL-749](https://campaignmonitor.atlassian.net/browse/EL-749) | ✅ | EL-749 Client settings custom access bug fixes |
| 2022-08-08 | engineer | createsend.com | [#13402](https://git.campmon.com/Freshview/createsend.com/pull/13402) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-chart-tooltip-style use custom tooltip for SMS report |
| 2022-08-08 | engineer | createsend.com | [#13403](https://git.campmon.com/Freshview/createsend.com/pull/13403) | [SMS-162](https://campaignmonitor.atlassian.net/browse/SMS-162) | ✅ | SMS-162-remove-dup-fetch-link Keep only one util for SMS links |
| 2022-08-08 | engineer | createsend.com | [#13406](https://git.campmon.com/Freshview/createsend.com/pull/13406) | [EL-746](https://campaignmonitor.atlassian.net/browse/EL-746) | ✅ | EL-746-b Client settings miscellaneous bug fixes |
| 2022-08-09 | engineer | createsend.com | [#13417](https://git.campmon.com/Freshview/createsend.com/pull/13417) | [EL-753](https://campaignmonitor.atlassian.net/browse/EL-753) | ✅ | EL-753 Text related updates |
| 2022-08-09 | engineer | createsend.com | [#13420](https://git.campmon.com/Freshview/createsend.com/pull/13420) | [SMS-208](https://campaignmonitor.atlassian.net/browse/SMS-208) | ✅ | SMS-208-a: Make it so that we have a feature flagged version of the SmsToStep |
| 2022-08-09 | engineer | createsend.com | [#13424](https://git.campmon.com/Freshview/createsend.com/pull/13424) | [SE-432](https://campaignmonitor.atlassian.net/browse/SE-432) | ✅ | SE-432 ClickOutside not working for subject recommendations when clicking outside of subject section |
| 2022-08-09 | engineer | createsend.com | [#13430](https://git.campmon.com/Freshview/createsend.com/pull/13430) | [SMS-208](https://campaignmonitor.atlassian.net/browse/SMS-208) | ✅ | SMS-208-c: Display segments |
| 2022-08-17 | engineer | createsend.com | [#13472](https://git.campmon.com/Freshview/createsend.com/pull/13472) | — | ✅ | [CONV-925] New plan selection page - more jank than previously |
| 2022-08-22 | engineer | createsend.com | [#13503](https://git.campmon.com/Freshview/createsend.com/pull/13503) | [SMS-239](https://campaignmonitor.atlassian.net/browse/SMS-239) | ✅ | SMS-239 - SMS Adding feature flag for UI for geographical expansion |
| 2022-08-29 | engineer | CMDS/cmds | [#2375](https://git.campmon.com/CMDS/cmds/pull/2375) | — | ✅ | CSS-Internal: separate out utilities from tokens to reduce build noise in monolith |
| 2022-08-29 | engineer | createsend.com | [#13543](https://git.campmon.com/Freshview/createsend.com/pull/13543) | [PLAT-3316](https://campaignmonitor.atlassian.net/browse/PLAT-3316) | ✅ | PLAT-3316 Implement machine clicks info banner on campaign snapshot page |
| 2022-08-30 | engineer | createsend.com | [#13549](https://git.campmon.com/Freshview/createsend.com/pull/13549) | — | ✅ | JS - Remove the now deleted yarn lock from docker config |
| 2022-08-31 | engineer | createsend.com | [#13563](https://git.campmon.com/Freshview/createsend.com/pull/13563) | — | ✅ | JS - Update yarn lock |
| 2022-09-02 | engineer | createsend.com | [#13570](https://git.campmon.com/Freshview/createsend.com/pull/13570) | — | 🔴 | Sms 187 b javascript changes to prevent sending and display tooltips and unverified status while not verified |
| 2022-09-06 | engineer | createsend.com | [#13586](https://git.campmon.com/Freshview/createsend.com/pull/13586) | — | ✅ | JS - Fail tests on console errors  |
| 2022-09-08 | engineer | createsend.com | [#13617](https://git.campmon.com/Freshview/createsend.com/pull/13617) | — | ✅ | Sms 188 a add a verified flag when the user is verified.  |
| 2022-09-09 | engineer | Engineering/SmsSendingServices | [#43](https://git.campmon.com/Engineering/SmsSendingServices/pull/43) | — | ✅ | Update README.md |
| 2022-09-18 | engineer | createsend.com | [#13690](https://git.campmon.com/Freshview/createsend.com/pull/13690) | [SMS-251](https://campaignmonitor.atlassian.net/browse/SMS-251) | ✅ | SMS-251-ra-b: Use config to get cut off date by country |
| 2022-09-19 | engineer | createsend.com | [#13693](https://git.campmon.com/Freshview/createsend.com/pull/13693) | [SMS-251](https://campaignmonitor.atlassian.net/browse/SMS-251) | ✅ | SMS-251: Make sms cross sell work off UTC time instead of (what could be) Sydney time |
| 2022-09-19 | engineer | createsend.com | [#13694](https://git.campmon.com/Freshview/createsend.com/pull/13694) | [SMS-251](https://campaignmonitor.atlassian.net/browse/SMS-251) | ✅ | SMS-251: Remove this keyword from unit test |
| 2022-09-19 | engineer | createsend.com | [#13697](https://git.campmon.com/Freshview/createsend.com/pull/13697) | [SMS-278](https://campaignmonitor.atlassian.net/browse/SMS-278) | ✅ | SMS-278-a refactor personalization util |
| 2022-09-20 | engineer | createsend.com | [#13705](https://git.campmon.com/Freshview/createsend.com/pull/13705) | [SE-595](https://campaignmonitor.atlassian.net/browse/SE-595) | ✅ | SE-595 - Add Ada support to Feature Feedback Widget |
| 2022-09-21 | engineer | createsend.com | [#13719](https://git.campmon.com/Freshview/createsend.com/pull/13719) | — | ✅ | Update CMDS Toggle to version 7 |
| 2022-09-21 | engineer | Engineering/integrationstorecontext.managerservice.core | [#64](https://git.campmon.com/Engineering/integrationstorecontext.managerservice.core/pull/64) | [MER-110](https://campaignmonitor.atlassian.net/browse/MER-110) | ✅ | MER-110 - Hide abandoned cart from those pesky app reviewers |
| 2022-09-26 | engineer | createsend.com | [#13730](https://git.campmon.com/Freshview/createsend.com/pull/13730) | [EL-683](https://campaignmonitor.atlassian.net/browse/EL-683) | ✅ | EL-683 Change div to fix issue with regression tests |
| 2022-09-27 | engineer | platform/cm.protobuf | [#605](https://git.campmon.com/platform/cm.protobuf/pull/605) | [SMS-305](https://campaignmonitor.atlassian.net/browse/SMS-305) | ✅ | SMS-305 add bounce type MESSAGE_BOUNCE_TYPE_UNSUPPORTED_REGION |
| 2022-09-27 | engineer | createsend.com | [#13751](https://git.campmon.com/Freshview/createsend.com/pull/13751) | — | ✅ | Sms 240-a Server changes to separate client properties from CmSmsMailing into CmSmsClient |
| 2022-09-27 | engineer | createsend.com | [#13752](https://git.campmon.com/Freshview/createsend.com/pull/13752) | [SMS-240](https://campaignmonitor.atlassian.net/browse/SMS-240) | ✅ | SMS-240 frontend changes to to separate out CmSmsMailing into two separate classes |
| 2022-09-29 | engineer | createsend.com | [#13767](https://git.campmon.com/Freshview/createsend.com/pull/13767) | [EL-868](https://campaignmonitor.atlassian.net/browse/EL-868) | ✅ | EL-868 Dynamically populate country field |
| 2022-10-06 | engineer | createsend.com | [#13796](https://git.campmon.com/Freshview/createsend.com/pull/13796) | — | ✅ | Sms 241 b frontend changes for toggles, updating saving toggle info to database |
| 2022-10-09 | senior engineer | createsend.com | [#13809](https://git.campmon.com/Freshview/createsend.com/pull/13809) | [MER-135](https://campaignmonitor.atlassian.net/browse/MER-135) | ✅ | MER-135 - change Shopify OAuth flow to meet requirements |
| 2022-10-13 | engineer | createsend.com | [#13846](https://git.campmon.com/Freshview/createsend.com/pull/13846) | [EL-875](https://campaignmonitor.atlassian.net/browse/EL-875) | ✅ | EL-875 Add confirmation dialog for rotating API key |
| 2022-10-17 | engineer | createsend.com | [#13864](https://git.campmon.com/Freshview/createsend.com/pull/13864) | — | ✅ | [CONV-1023] Client Overview Setup Guide - im not sure the "hasCompletedSetupGuide" value in the database is getting set |
| 2022-10-17 | engineer | createsend.com | [#13867](https://git.campmon.com/Freshview/createsend.com/pull/13867) | — | ✅ | Sms 242-b apply frontend changes to preview and report, sync back end to send messages.  |
| 2022-10-19 | engineer | createsend.com | [#13882](https://git.campmon.com/Freshview/createsend.com/pull/13882) | [SMS-311](https://campaignmonitor.atlassian.net/browse/SMS-311) | ✅ | SMS-311: SMS campaign search front end changes |
| 2022-10-19 | engineer | createsend.com | [#13890](https://git.campmon.com/Freshview/createsend.com/pull/13890) | — | ✅ | Sms 242 b fixed spelling mistakes which ruined character count |
| 2022-10-20 | engineer | createsend.com | [#13893](https://git.campmon.com/Freshview/createsend.com/pull/13893) | [SMS-355](https://campaignmonitor.atlassian.net/browse/SMS-355) | ✅ | SMS-355: Add new app alias to front end |
| 2022-10-21 | engineer | Engineering/integrationstorecontext.managerservice.core | [#67](https://git.campmon.com/Engineering/integrationstorecontext.managerservice.core/pull/67) | — | ✅ | [MER-148] Link Shopify integration tile to Shopify settings page |
| 2022-10-21 | engineer | createsend.com | [#13906](https://git.campmon.com/Freshview/createsend.com/pull/13906) | [SMS-242](https://campaignmonitor.atlassian.net/browse/SMS-242) | ✅ | SMS-242 fixes as per requests. |
| 2022-10-24 | engineer | createsend.com | [#13908](https://git.campmon.com/Freshview/createsend.com/pull/13908) | [SMS-311](https://campaignmonitor.atlassian.net/browse/SMS-311) | ✅ | SMS-311: Fix for sms search term on show all links |
| 2022-11-07 | engineer | createsend.com | [#14013](https://git.campmon.com/Freshview/createsend.com/pull/14013) | [EL-798](https://campaignmonitor.atlassian.net/browse/EL-798) | ✅ | EL-798 Instrumentation - Tax information pages |
| 2022-11-10 | engineer | createsend.com | [#14035](https://git.campmon.com/Freshview/createsend.com/pull/14035) | — | ✅ | sms-fix-use-recipient-data make sure fetch recursively works |
| 2022-11-11 | engineer | createsend.com | [#14051](https://git.campmon.com/Freshview/createsend.com/pull/14051) | [SMS-394](https://campaignmonitor.atlassian.net/browse/SMS-394) | ✅ | SMS-394-a remove the use of feature flag SmsSegments to reduce clutter |
| 2022-11-11 | engineer | createsend.com | [#14055](https://git.campmon.com/Freshview/createsend.com/pull/14055) | [SMS-394](https://campaignmonitor.atlassian.net/browse/SMS-394) | ✅ | SMS-394-b Use real SMS send throughput |
| 2022-11-17 | engineer | createsend.com | [#14096](https://git.campmon.com/Freshview/createsend.com/pull/14096) | [EL-862](https://campaignmonitor.atlassian.net/browse/EL-862) | ✅ | EL-862 ClientSettingsForPersons TaxInformation page |
| 2022-11-25 | engineer | Engineering/SegmentTrackingPlan | [#337](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/337) | [SMS-425](https://campaignmonitor.atlassian.net/browse/SMS-425) | ✅ | SMS-425: Add segment copy page event |
| 2022-12-20 | engineer | createsend.com | [#14361](https://git.campmon.com/Freshview/createsend.com/pull/14361) | — | ✅ | El 975 - Client Person bug bash |
| 2022-12-20 | senior engineer | createsend.com | [#14365](https://git.campmon.com/Freshview/createsend.com/pull/14365) | [PP-41](https://campaignmonitor.atlassian.net/browse/PP-41) | ✅ | PP-41 Surfacing a visual indicator for SMS campaigns denied sending due to billing |
| 2022-12-21 | engineer | createsend.com | [#14375](https://git.campmon.com/Freshview/createsend.com/pull/14375) | [SMS-452](https://campaignmonitor.atlassian.net/browse/SMS-452) | ✅ | SMS-452: Removed unused feature flag reference to SmsSelfServiceCrossSell |
| 2022-12-22 | engineer | createsend.com | [#14381](https://git.campmon.com/Freshview/createsend.com/pull/14381) | [EL-977](https://campaignmonitor.atlassian.net/browse/EL-977) | ✅ | EL-977b - Fixed merged conflict in srcfrontend |
| 2022-12-30 | engineer | createsend.com | [#14402](https://git.campmon.com/Freshview/createsend.com/pull/14402) | [SMS-469](https://campaignmonitor.atlassian.net/browse/SMS-469) | ✅ | SMS-469 use ContactId for SmsSubscriberDeliveryResult |
| 2023-01-16 | senior engineer | campmon.hex | [#729](https://git.campmon.com/Freshview/campmon.hex/pull/729) | [PP-40](https://campaignmonitor.atlassian.net/browse/PP-40) | ✅ | PP-40 Upgrading CampMon packages plus fixing issues with subscribe form abuse and currencies |
| 2023-01-18 | engineer | createsend.com | [#14480](https://git.campmon.com/Freshview/createsend.com/pull/14480) | [SMS-491](https://campaignmonitor.atlassian.net/browse/SMS-491) | ✅ | SMS-491: Attempt to join feature flag check on SmsSignupFormOptions with SmsAccess feature check |
| 2023-01-23 | engineer | createsend.com | [#14503](https://git.campmon.com/Freshview/createsend.com/pull/14503) | — | ✅ | Sms report rename case |
| 2023-01-23 | engineer | createsend.com | [#14509](https://git.campmon.com/Freshview/createsend.com/pull/14509) | — | ✅ | SMS-report-rename-case-2 rename css imports |
| 2023-01-31 | engineer | createsend.com | [#14578](https://git.campmon.com/Freshview/createsend.com/pull/14578) | [SMS-500](https://campaignmonitor.atlassian.net/browse/SMS-500) | ✅ | SMS-500-c: Allow no mobile when mobile number is optional on the back end |
| 2023-02-01 | engineer | createsend.com | [#14586](https://git.campmon.com/Freshview/createsend.com/pull/14586) | — | ✅ | Sms 513 Fix cursor skipping to end of line when editing the mobile number |
| 2023-02-22 | engineer | createsend.com | [#14745](https://git.campmon.com/Freshview/createsend.com/pull/14745) | [SMS-538](https://campaignmonitor.atlassian.net/browse/SMS-538) | ✅ | SMS-538 add javascript to attach events to format mobile in pattern based on country |
| 2023-02-27 | engineer | createsend.com | [#14788](https://git.campmon.com/Freshview/createsend.com/pull/14788) | [SMS-538](https://campaignmonitor.atlassian.net/browse/SMS-538) | ✅ | SMS-538 add wobble for invalid mobile number and/or consent not selected… |
| 2023-02-27 | senior engineer | createsend.com | [#14789](https://git.campmon.com/Freshview/createsend.com/pull/14789) | [PP-155](https://campaignmonitor.atlassian.net/browse/PP-155) | ✅ | PP-155 New component for Braintree card authorisation with hosted fields |
| 2023-03-01 | engineer | createsend.com | [#14809](https://git.campmon.com/Freshview/createsend.com/pull/14809) | [SMS-417](https://campaignmonitor.atlassian.net/browse/SMS-417) | ✅ | SMS-417-c: Bring language translations to the UI |
| 2023-03-05 | engineer | createsend.com | [#14841](https://git.campmon.com/Freshview/createsend.com/pull/14841) | [MER-336](https://campaignmonitor.atlassian.net/browse/MER-336) | ✅ | MER-336 signup form ui fix: styled form, close btn, scroll to published |
| 2023-03-06 | engineer | campmon.hex | [#745](https://git.campmon.com/Freshview/campmon.hex/pull/745) | [PP-124](https://campaignmonitor.atlassian.net/browse/PP-124) | ✅ | PP-124 - Tooling for data migration import |
| 2023-03-14 | engineer | createsend.com | [#14873](https://git.campmon.com/Freshview/createsend.com/pull/14873) | [SMS-552](https://campaignmonitor.atlassian.net/browse/SMS-552) | ✅ | SMS-552: Sms Self Service Data Provider and link refactor |
| 2023-03-15 | engineer | Engineering/workflowbuildercontext.uiservice.core | [#156](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/156) | — | ✅ | [MER-335a] Time Filter Select Component refinements |
| 2023-03-21 | engineer | createsend.com | [#14912](https://git.campmon.com/Freshview/createsend.com/pull/14912) | [EL-1064](https://campaignmonitor.atlassian.net/browse/EL-1064) | ✅ | EL-1064 linting |
| 2023-03-22 | engineer | createsend.com | [#14927](https://git.campmon.com/Freshview/createsend.com/pull/14927) | [SMS-558](https://campaignmonitor.atlassian.net/browse/SMS-558) | ✅ | SMS-558 apply geolocation to get default Country Code |
| 2023-03-24 | engineer | Engineering/contentbuildercontext.staticresourceservice.core | [#838](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/838) | [SE-762](https://campaignmonitor.atlassian.net/browse/SE-762) | ✅ | SE-762 Identify if a URL is pointing to a document |
| 2023-03-25 | senior engineer | createsend.com | [#14950](https://git.campmon.com/Freshview/createsend.com/pull/14950) | [PP-117](https://campaignmonitor.atlassian.net/browse/PP-117) | ✅ | PP-117 Braintree React component to show card type validations |
| 2023-03-27 | engineer | campmon.hex | [#756](https://git.campmon.com/Freshview/campmon.hex/pull/756) | — | ✅ | Fix Back Url from client details page |
