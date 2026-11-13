<!--
RAW: impact quantification, run 2026-11-12. Sources: Amplitude (CM Production, project 226438),
Datadog (dashboards + metrics), git.campmon.com API. Re-run instructions per section.
Window focus: Nov 2025 → Nov 2026 (CADD window).
-->

# Impact numbers — measured, 2026-11-12

The numbers the résumé ⟨placeholders⟩ and the interview playbook were waiting for. Everything below
was pulled live from Amplitude/Datadog/GitHub on 12 Nov 2026.

## 1. Advanced Drip Campaigns — adoption is real and growing

Amplitude events went live with the 27 Jul all-prod-DBs release (your go-live). Since then
(27 Jul → 12 Nov, CM Production project 226438):

| Metric | Value | Source |
|---|---:|---|
| **Drip campaigns created (all types)** | **1,212** | `Created Drip Campaign` totals (chart `8mkurue3`) |
| **Unique users creating drips** | **713** | same, UNIQUES |
| **Distinct client accounts adopting** | **688** | property_count on `Client Id` (chart `jo0zdfay`) |
| **Advanced (branching) drips created** | **446** | filter `Drip Type = Advanced` (chart `oidz1zyb`) |
| **Unique users creating Advanced drips** | **289** | same, UNIQUES |
| **Distinct accounts using Advanced drips** | **282** | property_count on `Client Id` (chart `32v8a0xa`) |
| Campaigns added into drips | 2,917 events | `Added Campaign To Drip Campaign` taxonomy volume |
| Conditions (branching!) added | 220 events | `Added Condition To Drip Campaign` — the advanced feature you built |
| Deletions | 181 | `Deleted Drip Campaign` — net creation strongly positive |

**The GA effect (your 1 Oct every-plan launch):** weekly unique creators averaged ~34/week in the
Direct-only period (27 Jul–28 Sep) and **~88/week after all-plans GA** (5 Oct onward; peak 100) —
a **~2.6× step change**. Weekly drips created: ~48/week → ~119/week. Advanced-only shows the same
shape: ~14 creators/week pre-GA → ~31/week post-GA (**~2.2×**), and Advanced is **37% of all drips
created** (446 of 1,212) despite being the newer, more complex option. The branching feature itself
is exercised: 220 `Added Condition To Drip Campaign` events (conditions exist only on Advanced).

**Repeat usage (retention, chart `u70u0fem`):** 16.2% of all creators come back and create another
drip in week 1-or-later (unbounded). The launch cohort (w/c 27 Jul, n=49) shows **35% eventual
repeat creation** and was still ~10% active at week 13. Interpretation for the review: drip
creation is naturally episodic (you build a sequence, it runs); a sixth of creators making *more*
sequences within weeks is genuine repeat adoption, not a one-off toy.

**Operational health:** your launch dashboard
([a3b-9pp-efn](https://app.datadoghq.com/dashboard/a3b-9pp-efn)) tracks cohort-convergence
failures (alert threshold > 0), lock-contention retries/exhaustions, lock-hold p95 and queue depth —
the instrumentation you specified in the AJ-1155 playbook, since reused as the launch template.

**One-liner:** *"Drip Campaigns: 688 client accounts created 1,212 branching campaigns in the first
15 weeks; adoption rate ~2.6×'d when we took it from Direct-only to every plan in October."*

## 2. SMS compliance embed — first customers measured; funnel instrumentation to own

- **The embed IS partially instrumented** (code crawl: `SmsComplianceEmbedClientSetupService.cs`
  fires `Set Up SMS` with `Number Type` + `Countries Enabled` when a customer is provisioned).
  **First live data, w/c 2 Nov 2026: 3 customers provisioned through the embed — 2 Alphanumeric
  (AU) + 1 Toll Free (US/CA)** (chart `v09sn1tp`), in the feature's first week with real customers.
  Baseline before this: 0 self-serve — every provision was a manual, single-person support task.
- Cleanest embed-only count for the readout: SQL `CL_ActivityLog` where
  `Category='SmsClientAccessEnabled' AND Description LIKE '%Enabled by: Compliance embed%'`.
- No Datadog dashboard or custom metric for the embed yet; request volume is visible via APM on
  `compliance-embed-init|session|status` (service `campmon.cmapi.netcore-http-server`). Monitoring
  today = #sms-compliance-alerts + a per-customer Slack post.
- **Funnel gaps you can own** (see [findings-instrumentation-hooks.md](findings-instrumentation-hooks.md)):
  no event for "inquiry submitted" (the TODO is literally in `SmsRegistrationNew.tsx`) and none for
  Twilio approval/rejection.
- Status timeline (Slack): dev-complete 2 Nov; PM demo "in full glory" 4 Nov; cleared for real
  customers 5 Nov; "a few customer requests" in flight pending Twilio approval 9 Nov.
- **Metrics to agree with the PM before Checkpoint 2** (put these in the epic):
  1. Registrations started / completed per month (vs. ~0 self-serve baseline — all manual before).
  2. Time from customer request → SMS-enabled (baseline: support round-trips over days, single
     person dependency: "None of us other than Greg have done provisioning").
  3. Manual provisioning requests to support (target 0 for US/CA TFN + AU alphanumeric).
  4. Registration rejection rate (Twilio verification outcomes).
  5. Foundation value: ~250 Infobip customers to migrate in 2027.

## 3. Brand Hub V2 — baseline exists, feature too new to measure

- `BrandHubV2` flag in prod 6 Nov; colour editing is days old. No edit events instrumented yet —
  same instrumentation gap, same opportunity.
- Baseline you inherit: `Started Brand Collection` 2,199 events / `Completed Brand Collection`
  4,231 events since the Aug Brand Hub launch (team-level numbers, not yours — use as denominator).
- Metric to agree pre-GA: % of kits with a colour correction applied, and colour-correction
  support-ticket volume ("three of four customers" ask for it — that's the baseline to beat).

## 4. Docker frontend builds — already measured (TeamCity, 10 Nov)

See [portfolio/docker-frontend-builds-results-2026-11.md](../../portfolio/docker-frontend-builds-results-2026-11.md):
PR-check compute **−69%/push** (1,109s → 348s, faster on 233/233 same-commit pairs); checks
1.8–8.5× faster; **~4,850 agent-hours/yr** projected saving (−72%); deploy package −41% in shadow
(n=17). Caveat stands: push→all-green median not yet improved due to shared-pool queueing.

## 5. Code volume, CADD window (1 Nov 2025 → 12 Nov 2026, git.campmon.com)

| Metric | Value |
|---|---:|
| PRs authored | **106** (86 merged, 81%) |
| PRs reviewed for others | **163** |
| Mentees with measured growth arcs | 4 (see [findings-mentorship.md](findings-mentorship.md)) |
| Production incidents closed end-to-end | 4 (+1 self-caused CI break, owned + fixed) |

## 5b. New evidence channel: meeting notes
Gemini meeting notes (Drive + Gmail) cover 39 Mitnick standups since Sep, daily Thompson SU, JS Crew,
Weekly Tech Meeting and the SMS/Brand Hub project meetings — per-person recaps of verbal
contributions not visible in Slack/PR mining. See [findings-meeting-notes.md](findings-meeting-notes.md).

## 6. How to refresh these numbers
- Amplitude (project 226438): charts `8mkurue3` (weekly uniques/totals), `jo0zdfay` (distinct
  Client Id count), `u70u0fem` (retention). Events: `Created Drip Campaign`,
  `Added Campaign To Drip Campaign`, `Added Condition To Drip Campaign`.
- Datadog: dashboard `a3b-9pp-efn`; metrics `campmon.mailingsendservice.complexsequence.*`.
- GitHub: `gh api "search/issues?q=type:pr+author:cng+created:2025-11-01..2026-11-12"` etc. with
  `GH_HOST=git.campmon.com`.

## 7. Instrumentation hooks found in code
Full detail with file:line references, SQL recipes, flag IDs and the instrument-next list:
[findings-instrumentation-hooks.md](findings-instrumentation-hooks.md). Headlines:
- Drip is well measured (Amplitude `Drip Type` split + SQL `CS_Sequence.SequenceType=1` /
  `CS_Campaign.SendingAgentType=1` — your schema column doubles as the adoption counter).
- SMS embed: provisioning measured (`Set Up SMS`), submission/approval funnel not — small PRs close it.
- Brand Hub V2 editing: zero instrumentation today; `brand_kit.version` (append-only) is the proxy.
- **No shared adoption dashboard was found in the org for any of the three features** — defining one
  is an open seat to take.
  - Clem's correction (13 Nov): PMs do monitor Drip adoption routinely in Amplitude (project
    226438 — the §6 charts are the likely artefacts). The verified claim stays narrow: no shared
    dashboard found. Do not claim "nobody watches adoption" or "numbers live only in a private file".
