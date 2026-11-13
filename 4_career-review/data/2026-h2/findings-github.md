# GitHub Enterprise findings — `cng`, 2026-05-28 → 2026-11-10
Source: git.campmon.com via `gh api` (read-only). [fact] = visible in GitHub; [inference] = reading. Full PR list: [authored_new.tsv](authored_new.tsv); reviewed: [reviewed_new.tsv](reviewed_new.tsv).

## Headline
- **Authored 59 PRs / 9 repos** (41 in createsend.com). **42 merged (+18,071 / −4,757)**, 7 open (COM-1794 ×3, JC-413 #25051, JC-414 #25593, Hex #24499, runnerservice #153), 10 closed-unmerged (6 AI-DLC, 3 AJ-1149 design pivots, 1 split).
- **Reviewed 63 PRs by 22 authors**; CHANGES_REQUESTED on 3 (#23685, #24396, #24871).
- Sign-offs "LGTM team Boole" → "team Mitnick" from Sep [inference: team move ~early Sep].
- AI-heavy workflow from Sep: "Generated with Claude Code", posts AI self-reviews, replies to every bot finding.

| Workstream | PRs (merged) | LOC | Dates |
|---|---|---|---|
| A Drip campaigns (AJ-1149/1161/1186/1190/1254/1257/1262/1265) | 15 (12) | +4,499/−1,676 | 06-12→08-28 |
| B SMS Twilio Compliance Embed backend (COM-1646/1648/1699/1700/1701/1733) | 9 (8) | +7,756/−1,377 | 09-25→10-22 |
| C Brand Hub V2 1A frontend (COM-1792/1793/1794) | 8 (5) | +3,124/−316 | 11-03→open |
| C′ BrandHubServices AI-DLC C# port (#81–86) | 6 (0) | +16,401/−810 | 09-23→09-25, shelved 11-03 |
| D Docker frontend builds (JC-411–414) + node-notifier | 5 (3) | +1,623/−289 | 10-08→open |
| E Observability + prod fixes | 7 (7) | +499/−177 | 06-16→10-09 |
| F Journey reporting + GrpcClient v2 | 5 (4) | +2,115/−1,040 | 05-28→06-09 |
| G Tooling (Hex, localdev-tools, webpack 5) | 4 (3) | +2,507/−1,232 | 05-28→09-08 |

## A. Drip campaigns (Team Boole) — frontend lead + one key backend schema decision
- Every PR on AJ-1149/1190/1257/1262/1161 is his. Topic search "complex sequence": fan-li 13 (backend agent/cohorts), cng 5, chris-luong 3, samanthac 2. Main JS reviewer for team's drip PRs.
- **AJ-1186-a #23545** — `SendingAgentType` column on `CS_Campaign` so complex-sequence campaigns avoid the regular queue's blocking issue. Reviewer: "Do we really need another column? SendServiceType already exists". **Clement's decision post:** SendServiceType is a claim-state flag reset to 0 → reuse would self-clobber; reuse = "~20–30 files incl. hot send procs, vs 7 additive files for the new column"; "I don't want to pick fight with roadmap deadlines"; "The new column is additive + correct-by-construction, so going with it. Happy to take the Legacy=0 cleanup as separate debt." Made nullable per LDR, re-requested SQL review. 3 approvals.
- **AJ-1149-a #23585 (closed)** — prototyped then killed own "timeline gutter": "too difficult to present multiple campaigns with diff scheduled date on the same X axis." #23666/#23680 superseded.
- **AJ-1149-c2 #23682** — moved sequence-details to React Query, replaced `window.location.reload()` with `invalidateQueries` (canvas updates in place), rename→mutation, load-error banner (previously failed silently).
- **AJ-1149-d #23711** (+1,007/−464, 27 files) — scheduled date/time/GMT offset on nodes, branch backdrops, IANA-tz `getGmtOffset()`, tree-utils restructure ("No import cycles"). Posted own AI self-review against a 13-item peer review.
- **AJ-1190-b #23903** — block adding steps under draft parents, disable conditions after plain-text parents, zoom-scaled toolbars, icon consolidation.
- AJ-1190-c capitalisation per CMDS; AJ-1254 help doc; AJ-1257 node-overlap fix (d3 separation); AJ-1265 fit view; **AJ-1262 #24142** thumbnails — scoped out high-traffic client-overview call sites ("I'll make a separate card").
- **AJ-1161-a/b #24309/#24355** — Simple sequence redesign behind `BasicCampaignSequenceUIRefresh`; CSS report 85/100.

## B. SMS Twilio Compliance Embed (Team Mitnick) — backend owner/architect
- alexis-tzanos built the embed frontend (COM-1649/1650/1740/1745/1747/1765/1783/1800/1807); Clement reviewed it. Every COM-1646/1648/1699/1700/1701/1733 PR is Clement's. Flag `SmsTwilioComplianceEmbed` (1228).
- **#24875 COM-1646-backend** — status enum + ordered eligibility rules; logic moved controller→`SmsAccessService`; fixed client-ID bug + unguarded Shared Services throw; owned mistakes in review ("great catch I copied the wrong thing. This is my bad.").
- **#24882 COM-1646-frontend** — non-dismissable "Register your phone number to send SMS" banner (admin vs non-admin copy), analytics, table-driven tests.
- **#24999 / #25031 COM-1648** — `POST compliance-embed-init`, agencies made eligible, CancellationToken plumbing, theme sets; moved to CmAPI.NetCore on reviewer request.
- **#25046 COM-1700** (+1,252/−320) — end-to-end provisioning (create Shared Services customer → buy/reuse Toll-free number). **Idempotent**: requestId from client; 409 = already exists. CSRF-protected session POST; typed exceptions incl non-JSON 502/504; legacy endpoint removed. **"Decisions worth a look"**: 422 vs 409/501; region check ("a number bought for the wrong region is still paid for"); branding; requestId tied to client. "all 1957 CmAPI.NetCore unit tests pass"; integration tests never buy real numbers. Reviewer: "a lot of work in this".
- **#25079 COM-1699** — `Enabled` status, `CanOpenSmsComplianceEmbed()`, Decisions section; "untested in real world. Impact minimal — no real users yet."
- **#25080 COM-1701** — **merged three duplicate provisioning flows (Hex, legacy self-serve, embed) into one `SmsClientProvisioningService`**; known-gaps section; 113 Core + "all 2264 unit tests pass".
- **#25163 COM-1733** (+1,593/−179) — Australian alphanumeric sender IDs; concurrent-init handling; fixed 6 bot findings (URL escaping, sync SQL → async).

## C. Brand Hub V2 1A (Team Mitnick) — sole frontend author
- #25460 data layer (409 optimistic concurrency "kit changed", 400 field errors, built against mock contract); #25526 `BrandHubV2` flag (1236); #25537 edit-mode layout ("I broke the page two ways… old tests passed against both, the new ones fail"); #25539 edit/add/delete/save (15-colour limit, 409 toasts, page lock, found CMDS ColorPicker selector bug); #25577 contract fix after peer catch; COM-1794 stack #25595–97 open (blocked on backend).

## C′. AI-DLC Stream A — BrandHubServices #81–86 (+16.4k), shelved 2026-11-03
- Port of AIBrandScraper Node→C# via AWS AI-DLC workflow incl. `Cm.CampMonBench.Parity` C#-vs-Node parity bench (#85). Closed: not proceeding — "roughly triples the maintenance footprint", "loses Datadog LLM Observability (no .NET SDK)", migration 007 not cleanly reversible, would delay customer-requested asset editing; kept on `archive/aidlc-stream-a` as "a worthwhile AI-DLC experiment". (Close comment from shared bot account; COM-1685 rationale by tech lead per Jira.)

## D. Docker frontend builds (JC-411) — sole author ("my little pet project")
- **#25020 JC-412** — Dockerfile, tasks.sh, Kotlin DSL; matched Linux output to Windows (casing fixes; Closure prints `ERROR -` and exits 0 → now fails build; dead node_modules regex). "64 Linux bundles differed… 338 B to 29 KB"; byte-by-byte verification.
- **#25051 JC-413** — NuGet pack + idempotent SHA512-deduped push; "We are not touching prod"; 9 feed scenarios tested.
- **#25501 JC-413** — one DSL for pr/deploy/canary/hotfix chains; quantified risk "2 to 10 of every 100 Version builds… p50 111 s, p90 540 s"; rejected agent-side checkout (~700 CRLF diffs); "let's start small and verify my little pet project works first".
- **#25593 JC-414 (draft)** — per-chain flag `frontend.package.docker`, staged Canary→Hotfix→Deploy, "Check, then turn it on" list, **Disaster recovery** section.
- #25500 removed node-notifier + vendored binaries.

## E. Observability / production fixes
- **triggerservice.core #66** — 6 instances firing same healthcheck email → throttled 429s; root cause conflicting RunScheduled vs RunWithLeaderElection.
- **updatecustomfield #73 COM-1625** — traced regression to a platform PR (PLAT-4905); error queue "0–1 through August, then stepped 1→6→8→9 from Sep 2"; Datadog monitor; 10 tests; DLQ semantics follow-ups; tagged team-platform. TL: "great detective work and a really great fix"; platform engineer apologised.
- AJ-980 / AJ-1292 Graylog→Datadog.
- **GitHubTeamManagement #6/#7/#8 (JC-436)** — Slack bot down since 10-08 18:33 UTC after Graylog shutdown; restored same day; #7 escapes `& < >` and triple backticks in user-controlled PR titles/branches/comments (injection fix); fargate 0.88.

## F/G. Journey reporting, tooling
- uiservice #317 subscriber history dialog (mock data, AI self-review); #319/#321 realistic demo mocks; runnerservice #153 GrpcClient v2 (UNTESTED, open/parked).
- **Hex #24483 resource ownership page** — "I got tired of tunneling into prod jump box and manually sql… the less manual SQL I execute against prod dbs, the better." TL: "love seeing you thinking outside the box… enhance our support abilities".
- localdev-tools #76 proxy profiles (stacked on #74 Modernise local proxy, +6.2k/−21.8k, merged 06-25); webpack 5 pt 2 #23354.

## Review highlights (63 reviewed)
- By author: TL 12, backend peer 8, JS-crew peer 6, others.
- Drip: cancel-cascade AJ-1148 #23660 (3 rounds, tested locally), AJ-1258 #23987, #23685 CHANGES_REQUESTED (11 comments).
- Biome-for-ESLint series (#24324/24330/24346/24351/24365/24396) as JS Crew reviewer — #24396 changes requested ("missing the biome.jsonc change").
- **React Query standard he introduced then taught**: "Look into invalidating the react query instead." / "Can you migrate this file / Atlas to use react-query while the scope and impact is still small?" — bot reviewer later "Reinforcing @cng's earlier comment".
- Bugs caught: "I'm gonna veto the earlier change here and insist these needs to be wrapped in `toRem()` so the final transpiled css is actually valid."; class-name collision; unvalidated `new Date()`.
- Standards: "One component per file please."; "Please avoid cross app imports."
- AI hygiene: "Don't really need these token burning comments."; "don't push the robot review to repo" → TL followed up with a fix PR.

## Ownership tells
Decisions sections (#25046, #25079, #25080, #25593); known-gaps sections; rollout + DR plan (#25593); flags created (1228, 1236); alternatives weighed (AJ-1186, AJ-1149, #25501, #25046); cross-team root cause (COM-1625); named follow-ups (AJ-1187, JC-415/416/417, COM-1652/1796/1797); owning mistakes; evidence-based pushback; shelving work with rationale; zero reverts.
