# Docker frontend builds: measured results (JC-411, pulled 10 Nov 2026)

> **Ticket note:** the work is **JC-413** (Stage 2, package publishing) under epic **JC-411**, with JC-412 (Stage 1, build in Docker) and JC-414 (per-chain switch). There is no JSC-413.
>
> **Status on 10 Nov:** the five frontend **PR merge checks are switched**: Docker only since 6 Nov, Windows checks paused. The **deploy package build is in shadow mode**: the Docker job builds next to the Windows job, but the package that ships still comes from Windows ([#25051](https://git.campmon.com/Freshview/createsend.com/pull/25051) pack/push and [#25593](https://git.campmon.com/Freshview/createsend.com/pull/25593) flag switch are still open).
>
> Supersedes the TeamCity numbers in [`data/2026-h2/findings-teamcity.md`](../data/2026-h2/findings-teamcity.md); see [§9 Corrections](#9-corrections-to-earlier-numbers).

---

## TL;DR: the numbers you can use

| | Before (Windows agents) | After (Docker) | Change | Level |
|---|---:|---:|---:|---|
| **Agent time per PR push** (5 FE checks summed, same commits) | 1,109 s (18.5 min) | 348 s (5.8 min) | **−69%**, faster on **233 / 233** commits | ✅ |
| **Slowest check run** (the floor for PR feedback) | 319 s | 180 s | **−44%**, faster on 230 / 233 | ✅ |
| Validate JS (shared) | 179 s | 21 s | **8.5× faster** | ✅ |
| Validate JS (app) | 228 s | 41 s | **5.6× faster** | ✅ |
| Build images & CSS | 166 s | 31 s | 5.4× faster | ✅ |
| Build JS (Closure) | 207 s | 60 s | 3.5× faster | ✅ |
| Build JS (Webpack) | 319 s | 180 s | 1.8× faster | ✅ |
| **Fleet agent-hours for FE checks** (same 6-day window) | 18.4 h/day | 5.1 h/day | **−72%** | ✅ |
| Check runs (same window) | 1,810 | 1,401 | −23%; 209 commits no longer checked needlessly | ✅ |
| **Deploy package build** (same build numbers, shadow) | 523 s | 290 s | **−44%**, faster in 17 / 17 | ✅ early, n=17 |
| Deploy package, like-for-like (checkout + install + build) | 459 s | 273 s | **−41%** | ✅ early |
| Annualised agent-hours saved, FE checks | | | **~4,850 h/yr** | 📐 projection |
| Annualised agent-hours saved, deploy package (once live) | | | ~285 h/yr | 📐 projection |
| **Push → all 5 checks green** (developer wait) | 327 s median, p90 827 s | 488 s median, p90 2,052 s | **worse**: queueing, see §5 | ✅ (honest caveat) |

✅ measured · 📐 projection from measured rates · 🔍 still to measure

**One sentence:** I cut the frontend PR checks' compute by about 70%, with the same tests on the same hardware class, by removing checkout and `npm install` overhead. Measuring the developer-facing result then showed the bottleneck had moved to the shared Docker pool, which was already full at peak. I modelled the fix: +3 Docker agents, paid for by −2 Windows agents.

---

## 1. What changed, when (AEDT)

| Date | Event |
|---|---|
| 8 Oct | Epic JC-411 + 24 child tickets created; Stage 1 PR [#25020](https://git.campmon.com/Freshview/createsend.com/pull/25020) opened (+946/−21, 27 files) |
| 12 Oct | #25020 merged: `app/` frontend builds in Docker, toolchain pinned in one Dockerfile |
| 31 Oct 12:22 | Docker PR checks start running **alongside** the Windows checks on every PR (shadow) |
| 6 Nov 12:24 | [#25501](https://git.campmon.com/Freshview/createsend.com/pull/25501) merged (one DSL for pr/deploy/canary/hotfix chains) → 47-min settings break (§7) |
| 6 Nov ~13:50 | **Windows FE merge checks paused**: Docker checks are now the only frontend PR checks |
| 9 Nov | Docker deploy-package job's first run (shadow, build-only); [#25593](https://git.campmon.com/Freshview/createsend.com/pull/25593) per-chain flag opened |
| 10 Nov | Data pulled. #25051 (pack/push, 9 reviews) and #25593 (7 reviews) still open |

## 2. Method

- **Source:** TeamCity REST API (read-only), 6,325 finished builds + per-build statistics (stage durations, queue wait reasons, tests). Raw rows: [`data/2026-h2/teamcity-docker-builds/builds.csv`](../data/2026-h2/teamcity-docker-builds/builds.csv). Scripts: [`scripts/teamcity-docker-builds/`](../scripts/teamcity-docker-builds/).
- **Retention limits:** TeamCity keeps ~10 days of merge-check history (Windows checks: 27 Oct – 6 Nov) and ~30 days of deploy-package history (from 9 Oct). No longer baseline exists.
- **Paired comparison (the strong evidence):** from 31 Oct to 6 Nov both runtimes checked the **same PR commits**. Matching on (branch, revision) gives 233 commits where all 10 checks passed. Deploy package: paired on build number (same commit), n=17.
- **Fairness checks:**
  - **Hardware:** both are 8 vCPU / 32 GB (Linux `m6a.2xlarge` vs Windows `m6id.2xlarge`).
  - **Tests:** the same jest suites (183 app tests, 130 shared tests) ran in both.
  - **Control:** the deploy chain's *Web Package Backend* job did not change (1,306 s → 1,293 s), so there was no general fleet speed-up.

## 3. Where the time went (why it's faster)

Median seconds per stage on Windows, compared with the single Docker step:

| Check | Windows checkout | Windows `npm install` | Windows real work | **Windows total** | Docker checkout | Docker step (cached deps + work) | **Docker total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Validate JS (app) | 66 | 78 | 43 | 228 | 1 | 36 | 41 |
| Validate JS (shared) | 56 | 70 | 19 | 179 | 1 | 18 | 21 |
| Images & CSS | 37 | 70 | 29 | 166 | 1 | 24 | 31 |
| Closure | 45 | 70 | 60 | 207 | 1 | 51 | 60 |
| Webpack | 39 | 70 | 177 | 319 | 1 | 169 | 180 |

- **54% of all Windows agent time was overhead:** checkout plus `npm install`, repeated five times on every push (~600 s of the 1,109 s).
- **The real work runs at about the same speed:** webpack 177 s vs 169 s. The win is architectural, not a faster compiler:
  - The Docker `deps` layer is cached per agent until a lockfile changes.
  - Checkout is 1 s because the Linux VCS root uses no auto-CRLF and a server-side checkout.
- **Headroom still to unlock:** webpack is now about half of Docker agent time (180 of 348 s per push). JC-411's spikes (webpack warm cache 62.5 → 3.5 s, Closure → esbuild 13.7 → 0.35 s, TS7 tsc 4.8 → 0.46 s) target exactly that. A toolchain upgrade is now a Dockerfile change, not an agent-image change.

## 4. Fewer wasted runs

- In the same 6-day window, Windows checked **481** PR commits and Docker **281**.
- I sampled 8 of the 209 commits only Windows checked. All 8 changed only `srcfrontend/` (a different frontend with its own checks) or C# files. **None could change a check's result.**
- Docker's VCS trigger rules are scoped to the inputs the checks read, so about **4 in 10 of the commits the Windows checks ran on were waste** (209 of 481).

## 5. The new bottleneck: agent-pool queueing (the honest part)

- **Developer wait did not improve.** During the overlap, push → all-green was 341 s on Windows vs 373 s on Docker (median), with Docker faster on 61% of commits. After the switch, Docker-only is 488 s median and p90 34 min. Windows over its whole period was 327 s / p90 827 s.
- **Cause: queue time, not build time.** 99.9% of Docker queue time is "no idle compatible agents". Median queue per check rose from 0 s (Windows) to ~200 s (Docker), with a p90 of ~25 min.
- **A full pool, tipped over:**
  - The Sydney Docker pool (11 × m6a.2xlarge, always on, shared by 422 projects) was **already fully busy at p90 before the move**: all 11 agents on 28–30 Oct.
  - The FE checks add only ~0.7 busy agents on average (~4 at peak, 4–8% of business-hours capacity). But they arrive as bursts of five per push.
  - Simulated, that **nearly doubled other teams' p90 wait**, from ~9 to ~16 min. Measured: 951 s.
  - The busiest day so far: 10 Nov, **98% busy**.
- **Structural difference:** both fleets are fixed-size ASGs, with no autoscaling. Windows has **26 agents** at $0.96/h; Docker has **11** at $0.43/h. The freed Windows capacity was absorbed straight away by two new Windows merge checks, started 31 Oct (~31 agent-h per weekday).
- **Achievable result once capacity is fixed:** with zero queue, PR feedback is bounded by the slowest check, **319 s → 180 s (−44%)**.
- **Sizing (trace-driven queue simulation, calibrated to within ~6% at today's size; see [capacity analysis](../data/2026-h2/teamcity-docker-builds/capacity-analysis-2026-11.md)):**
  - **14 Docker agents** brings p90 push → green to ~12 min, below the Windows era's 14 min, including the JC-414 package builds.
  - That's +$946/mo, more than paid for by **26 → 24 Windows agents** (−$1,408/mo) once JC-414 lands.
  - At 14 agents, other teams wait less than before the migration (p90 ~4 min).

## 6. Deploy package build (shadow, n=17 paired)

| Stage (median s) | Windows | Docker |
|---|---:|---:|
| Checkout | 59 | 5 |
| `npm install` | 109 | (inside the build step, cached layer) |
| JS build | 293 | 268 (install + build in container) |
| NuGet pack + push | 13 | not yet: #25051 |
| Artifact publishing | 33 | 10 |
| **Total** | **523** | **290** |

- **~41–44% faster** like-for-like. Adding ~13 s for pack and push keeps it at ~42%.
- The same 183 tests pass in both.
- **It doesn't shorten deploys:** `Ready to deploy` also waits on *Web Package Backend* (~21.5 min), so the FE package is not the long pole. The win is agent time (~285 h/yr 📐) and the toolchain being code-owned. Don't claim faster deploys.
- **Watch item:** the Windows package job's `npm install` drifted from 70 s to ~105 s on 9–10 Nov. A possible cause is colder Windows caches now that the PR checks have left. Not confirmed (n=49).
- The Docker job publishes a 91 MB artifact vs 0.5 MB on Windows, yet artifact publishing still takes 10 s against 33 s. Its 3 cancellations are the intended "nothing to compare → cancel, don't fail" path.

## 7. Reliability

| | Windows (3,106 runs) | Docker (2,376 runs) |
|---|---:|---:|
| Genuine failures (lint / types / tests) | 3 | 15 |
| Self-caused DSL break, 6 Nov 12:39–13:26 | – | **60 runs, 8 PRs, 47 min** |
| Artifact-upload flakes ("gave up after 4 attempts") | 0 | 7 (0.3%) |
| Cancelled / VCS | 0 | 2 |

- **The DSL break, quantified:**
  - The first and last failing builds both required settings from #25501's merge commit `6f282b78`.
  - The error, in the Frontend Merge Checks project: `Unknown DSL context parameter chain="<placeholder-1>". Use pr or one of [deploy, canary, hotfix]`.
  - Cause: that project's `chain` context parameter resolved to a placeholder when the shared `settings.kts` ran.
  - Impact: 8 PRs got failing checks over 47 minutes, owned and fixed the same day.
  - This is STAR story #20's missing number.
- **Stricter by design:**
  - Linux is case-sensitive on imports.
  - The Docker Closure step fails when the compiler prints `ERROR -`. The Windows step exits 0 and can ship an incomplete bundle.
  - Docker checks read the full frontend tree.
- **New failure mode:** 7 artifact-upload flakes are worth a retry or a smaller artifact (🔍).

## 8. Cache behaviour

- **9–14% of Docker check runs are cold**, at +100–120 s each. For example, validate-shared runs 20 s warm and 140 s cold.
- Cold runs are spread across commits (only 1 of 466 commits was cold on all five checks). So they come from per-agent cache misses, not lockfile changes.
- **Next action:** pushing the toolchain/deps image to ECR as a shared layer cache (JC-413's optional Stage 5) would remove most of the p90 tail.

## 9. Corrections to earlier numbers

`data/2026-h2/findings-teamcity.md` (written earlier today) has three errors:

1. The "FE merge checks (not yet Dockerised)" rows **were the Docker checks**. Their medians (41/21/31/60/180 s) match exactly.
2. "Runs (90d)" was really **~10 days** of retained history. So "~470×/90 days ≈ 1,900 pushes/yr" is wrong by about 9×: the Docker checks trigger on ~46 PR commits a day.
3. The JC-411 baseline of **1,066 s per push**, flagged as "don't quote", **holds up**: I measured 1,109 s. The "~5–9 min saved per push" estimate was **conservative**: the measured saving is **12 min** of agent time per push (paired median 725 s).

The "~41% faster" package claim survives the like-for-like check (41%). Stop pairing it with "1,900 pushes/yr".

These files still quote the old figures:
- `06-year6-current.md` Ch.6
- `interview/star-story-bank.md` #21
- `interview/impact-metrics-playbook.md` §3
- `growth/brag-doc-promo-packet.md`
- `cv/clement-ng-resume-2026-11.md`

---

## 10. Portfolio copy

> Your own guidance ([ownership-and-decisions.md](../interview/ownership-and-decisions.md)) still applies: this is the **depth coda**, not the headline. The upgrade is that it is now a finished, measured result with a diagnosis, not "early, n=20".

### Résumé bullets (choose one)

- **IC/Senior:** Moved the monolith's frontend CI from hand-maintained Windows agents to Docker. **PR-check compute fell 69% per push** (18.5 → 5.8 agent-min, same tests, same hardware class), and **~72% fewer agent-hours** fleet-wide (~4,850 h/yr). Verified byte-level output parity; rolled out per pipeline with shadow runs and a rollback flag.
- **Staff/platform:** Led a 24-ticket CI migration: checks run 1.8–8.5× faster, and toolchain upgrades became a code change. Measured the developer-facing result, found the bottleneck had moved to a shared agent pool that was already full at peak, and sized a cost-neutral fix with a trace-driven queue simulation: +3 Docker / −2 Windows agents, PR p90 30 → 12 min, −$460/mo.
- **Short:** Dockerised frontend CI: −69% compute per PR push, −44% on the slowest check, −41% deploy package build.

### STAR #21, upgraded (replaces the "early" version)

- **S:** The frontend toolchain was baked into hand-maintained Windows build agents. Every PR push spent 18.5 agent-minutes across five checks, and more than half of that was checkout and `npm install` repeated five times.
- **T:** Make toolchain upgrades a code change and cut the waste, without risking the production package.
- **A:**
  - Containerised the build with byte-level parity checks across 6,106 files. Found that the Closure compiler exits 0 on errors.
  - Ran Docker and Windows checks side by side on the same PRs for six days, then switched.
  - Staged the deploy package behind a per-chain flag with a rollback plan.
- **R:**
  - **69% less compute per push** (233/233 commits faster); individual checks 1.8–8.5× faster; ~4,850 agent-h/yr; deploy package 41% faster in shadow.
  - Then I measured what developers actually wait for. It hadn't improved: the shared Docker pool was already full at peak, and my checks' bursts pushed it into long queues for every team.
  - I replayed a week of real builds through a queue simulator, calibrated to within ~6% of the measured queue.
  - It showed 14 Docker agents (from 11) gets PR p90 back under the Windows era's 14 min. Dropping 2 Windows agents more than pays for it (−$460/mo net).
- **Decision:** I chose a parallel shadow run over a cut-over, because it gave a paired, same-commit comparison and a free rollback.
- **Reflection:** "Measure the outcome the user feels, not the metric you optimised. The build got 3× cheaper, and the wait didn't move until we fixed the queue."

### Interview soundbites

- "Most of the CI time wasn't building, it was setup: 54% of agent time was checkout plus `npm install`, five times a push. Docker's layer cache took that to about a second."
- "I didn't stop at the green dashboard. Developer wait got worse after the switch, so I pulled the queue data. The Docker pool was already full at peak. My checks were only about 7% of its time, but they nearly doubled everyone's wait. So I modelled it: three more Linux agents, paid for by two fewer Windows agents."
- "Our own outage was 47 minutes and 8 PRs. A shared DSL evaluated for a project that hadn't set its context parameter. That's why the deploy chains move behind a per-chain flag."

---

## 11. Next steps (to make this a complete win)

| # | Action | Turns into | Re-measure |
|---|---|---|---|
| 1 | Docker 11 → 14 agents, Windows 26 → 24 after JC-414 ([capacity analysis](../data/2026-h2/teamcity-docker-builds/capacity-analysis-2026-11.md)) | PR p90 ~30 → ~12 min, −$460/mo | Median and p90 push → green, queue p90 |
| 2 | Land #25051 + #25593; flip Canary → Hotfix → Deploy | "Deploy package build 41% faster **in production**" | Paired again on live chains; ~285 agent-h/yr |
| 3 | ECR layer cache for the deps image | Cut the cold-run tail (9–14% of runs, +100–120 s) | Docker check p90 |
| 4 | Webpack warm cache / esbuild spikes (JC-411) | Webpack is about half of Docker check time | Webpack check median (now 180 s) |
| 5 | Retry or shrink artifact publishing | Removes the 0.3% upload flakes | Failure rate |

## 12. Reproduce

```bash
cd ~/career-review/scripts/teamcity-docker-builds
python3 pull.py <dir> && python3 pull2.py <dir> && python3 stats.py <dir>   # ~7 min, read-only API
bash pull_pool.sh <dir>                      # Docker-pool history, for a4.py / a5.py
TCD=<dir> python3 a2.py    # per-commit paired comparison (the headline numbers)
TCD=<dir> python3 a4.py    # pool utilisation (the queueing diagnosis)
```
