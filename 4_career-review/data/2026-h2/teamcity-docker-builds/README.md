# TeamCity raw data: Docker vs Windows frontend builds (pulled 2026-11-10)

Analysis and portfolio copy: [`portfolio/docker-frontend-builds-results-2026-11.md`](../../../portfolio/docker-frontend-builds-results-2026-11.md).

## `builds.csv`: one row per finished build (6,320 rows)

| `series` | TeamCity build configuration | Retained window |
|---|---|---|
| `pr_<check>_win` | `CreatesendCom_StaticAssetValidation`, `…_ValidateJavascriptShared`, `CreatesendCom_BuildValidateCss`, `CreatesendCom_BuildJavascriptClosure`, `CreatesendCom_BuildJavascriptWebpack` (Windows, paused 6 Nov) | 27 Oct – 6 Nov |
| `pr_<check>_dock` | `CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_*` (Docker) | 31 Oct – 10 Nov |
| `deploy_legacy` | `CreatesendCom_MonolithDeploy_WebPackageJavascript` (Windows, ships to prod) | 9 Oct – 10 Nov |
| `deploy_docker` | `CreatesendCom_MonolithDeploy_FrontendPackageDocker_WebPackageJavascript` (shadow) | 9 – 10 Nov |
| `deploy_backend_control` | `CreatesendCom_MonolithDeploy_WebPackageBackend` (unchanged control) | 9 Oct – 10 Nov |

Columns:
- **Times:** `queued_utc` / `started_utc` / `finished_utc` are TeamCity timestamps. `duration_s` = finish − start.
- **`queue_s`:** TeamCity's `TimeSpentInQueue`.
- **`checkout_s`:** `buildStageDuration:sourcesUpdate`.
- **`step_durations_s`:** JSON of `buildStep<RUNNER_ID>` → seconds.

Windows runner IDs:

| Runner | Step |
|---|---|
| `RUNNER_967` / `RUNNER_965` | npm install |
| `RUNNER_996` | types |
| `RUNNER_595` | lint |
| `RUNNER_302` | jest |
| `RUNNER_1368` | legacy TS |
| `RUNNER_1357` | closure |
| `RUNNER_1354` | webpack / CSS build |
| `RUNNER_1366` | lint CSS |
| `RUNNER_1375` | images |
| `RUNNER_670` | `yarn run build` |
| `RUNNER_674` | NuGet pack |
| `RUNNER_677` | NuGet push |

Docker runner IDs:
- `RUNNER_1` is `tasks.sh <task>`. In the package job, `RUNNER_1` is the compare check and `RUNNER_2` is `tasks.sh build`.

## Not saved here

- **Per-agent pool history:** used for the queue and utilisation analysis, re-pull with `scripts/teamcity-docker-builds/pull_pool.sh`.
- **Per-build statistics JSON:** 6,325 files, re-pull with `stats.py`.

The analysis and portfolio docs use roles rather than names. This file holds TeamCity IDs and PR branch numbers only.
