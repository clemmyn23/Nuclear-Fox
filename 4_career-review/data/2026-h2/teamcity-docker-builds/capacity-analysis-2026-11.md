# Build-agent capacity: Windows → Docker (pulled 10 Nov 2026)

Companion to [`portfolio/docker-frontend-builds-results-2026-11.md`](../../../portfolio/docker-frontend-builds-results-2026-11.md). The Slack draft for devops/platform is in [§6](#6-slack-draft-for-devopsplatform).

## 1. The fleets (from Terraform, not TeamCity)

| | Windows (`apse2c-bld-*`) | Docker (`apse2c-dok-*`, Sydney) |
|---|---|---|
| Terraform | `Engineering/windows-teamcity-build-agents` → `deployments/terraform/env/corp/ap-southeast-2/main.tf` | `data-tribe/build-agents` → `environments/corp-ap-southeast-2/main.tf` |
| Size knob | `number_of_teamcity_agents = 26` | `instance_count = 11` |
| Instance | m6id.2xlarge, Windows (8 vCPU / 32 GB) | m6a.2xlarge, Linux (8 vCPU / 32 GB) |
| Schedule | Always on. Sydney's off-peak reduction is hard-coded to 0% "to keep every agent available" | Always on. `enable_off_peak_schedules = false`; the module can cut 70% weekday 20:30–05:20 and at weekends |
| On-demand $/h (AWS Pricing API, Sydney) | **$0.9644** | **$0.432** |
| 1-yr RI, no upfront, $/h | $0.7437 | $0.2858 |
| $/month at 24/7, on-demand | $704 per agent; **$18,304** fleet | $315 per agent; **$3,469** fleet |
| TeamCity projects sharing the pool | 256 | 422 |

- **One Windows agent costs about 2.2 Docker agents on-demand**, or 2.6 on RIs.
- **Option A (§5) nets about −$460/month either way:**
  - On-demand: +$946 Docker, −$1,408 Windows.
  - RI: +$626 Docker, −$1,086 Windows.
- **Neither fleet autoscales.** TeamCity has no cloud profiles. Both are fixed ASGs sized in Terraform. (An earlier note said the Windows pool "autoscales 22–40 agents a day". That was instance replacement after a Terraform apply on 2 Nov.)

### What the read-only `dev` AWS profile shows (account 891719040994)

- **Readable:**
  - EC2 and ECS describe.
  - CloudWatch metrics.
  - Cost Explorer: the dev account cost ~$57.5k in October.
  - The Pricing API.
- **The build agents are not in this account.** Both Terraform configs pin the **corp** account (654951736321), so their utilisation and cost need a corp read-only profile.
- **The container-service hosts are reserved, not used.** These are ECS-on-EC2 clusters in dev, 14 days of hourly CloudWatch data:

| Cluster | Hosts | CPU reserved | CPU used, mean (max) | Memory reserved | Memory used | $/month on-demand |
|---|---|---:|---:|---:|---:|---:|
| `campmon` | 9 × r5.xlarge (4 vCPU / 32 GB) | 87% | 7.6% (12%) | 30% | 15% | ~$1,984 |
| `contacts-and-segments` | 6 × m5.xlarge (4 vCPU / 16 GB) | 62% | 14% (27%) | 56% | 41% | ~$1,051 |
| `platform-ecs` | 3 | 83% | 3.6% (4%) | 36% | 12% | – |

  These hosts are sized by **task CPU reservations about 10× actual use**. Right-sizing those reservations could free roughly half of them (rough: memory reservations would become the limit). That is a separate dev-account saving.
- **Not a home for build agents:** they are 4-vCPU hosts in a different account, and TeamCity agents need their own Docker daemon. Mixing CI bursts with dev services would also reintroduce noisy-neighbour queues.
- **Neither fleet autoscales.** TeamCity has no cloud profiles. Both are fixed ASGs sized in Terraform. (An earlier note said the Windows pool "autoscales 22–40 agents a day". That was instance replacement after a Terraform apply on 2 Nov.)

## 2. Data and method

- **Data:**
  - Every finished build on both pools, 13 Oct – 10 Nov (server-wide pull, filtered by agent name).
  - Per-build TeamCity statistics for all 18,228 builds from 2–10 Nov.
  - Each build's time "waiting for an idle compatible agent" comes from `queueWaitReason:There_are_no_idle_compatible_agents_which_can_run_this_build`.
- **Retention limit:** TeamCity keeps ~14 days of merge-check history. Baselines use **28–30 Oct**; anything earlier is undercounted.
- **Simulator:**
  - Replays the real 2–10 Nov Docker-pool arrivals: ready time = start − agent wait, and the measured durations.
  - Models a FIFO queue over N identical agents, with an optional peak/off-peak schedule.
  - "Push → all-green" is measured per PR commit: from the first of the five FE checks queued to the last one finished, for pushes made Mon–Fri 08:00–19:00.
- **Calibration at today's size:**

| | Push → green p50 | Push → green p90 | All-build wait p90 |
|---|---:|---:|---:|
| Docker, 11 agents, actual | 502 s | 1,819 s | 1,145 s |
| Docker, 11 agents, simulated | 522 s | 1,716 s | 1,119 s |
| Windows, 26 agents, actual | – | – | 303 s |
| Windows, 26 agents, simulated | – | – | 275 s |

  The simulator is slightly optimistic at the tail; Windows p99 is optimistic, 966 vs 1,495 s, so only p90 is used there. Hence one agent of margin in the recommendations.
- **Scripts:** `scripts/teamcity-docker-builds/` (`trace.py`, `sim.py`, `sweep.py`, `sweepwin.py`, `b1`–`b7.py`). Raw sweep output: `sweep_out.txt`, `sweepwin_out.txt` next to this file.

## 3. How much capacity moved

| Work | Before, on Windows (agent-h per weekday) | After, on Docker (agent-h per weekday) |
|---|---:|---:|
| Five FE PR checks (moved 6 Nov) | 21.5–23.1 | 6.3–7.4 |
| FE deploy package (moves with JC-414) | 2.5 (17.9 runs × 495 s) | ~1.5 (17.9 × ~305 s) |
| **Total** | **~25** | **~9** |

| Concurrency, Mon–Fri 09:00–18:00 | Windows, FE work | Docker, FE work |
|---|---:|---:|
| Mean busy agents | 1.9–2.4 | 0.6–0.7 (+~0.1 package after JC-414) |
| p99 busy agents | 10–12 | 4 |

- **The same work needs ~65% fewer agent-hours.** At list prices it's ~85% cheaper per unit of work: about $24 → $4 of agent time per weekday. Because both fleets are fixed, no money moves unless fleet sizes change.

## 4. Why a small move caused a big queue

- **The Docker pool was already full at peak before the move.** On 28–30 Oct it averaged 6.5 busy agents, with all 11 busy at p90 and p99.
- **Its business-hours load is now 60–98%** (median ~72%).
- **The FE checks arrive as bursts of five per push** into a pool near 100%.
- **Effect on other teams' builds, Mon–Fri 08:00–19:00 (simulated):**

| Docker agents | Other teams' wait p90, without FE checks | With FE checks |
|---:|---:|---:|
| 11 | 561 s | 986 s (measured: 951 s) |
| 14 | 102 s | 243 s |

  So the FE checks **nearly doubled other teams' wait**. At 14 agents, everyone waits less than before the migration.
- **The freed Windows capacity is already absorbed.** Two new Windows merge checks, *Web Back End V2* and *StyleCop (Core)*, first ran on 31 Oct. Together they use ~31 agent-h per weekday, more than the ~25 the FE work freed. The Windows pool is still fully busy (all 26) at p90.
- **Docker non-FE load is also growing:** +13% from 28–30 Oct to November (MCP Server merge checks, CmAPI.NetCore image builds).

## 5. Sizing results (2–10 Nov load, plus the JC-414 package builds)

**Target:** match the Windows era (27 Oct – 6 Nov): push → green **p90 827 s (13.8 min)**, median 327 s.

### Docker, always on

| Agents | Push → green p50 | Push → green p90 | All-build wait p90 (business hours) | $/month | Δ vs today |
|---:|---:|---:|---:|---:|---:|
| 11 (today) | 556 s | 1,811 s | 1,157 s | $3,469 | – |
| 12 | 366 s | 1,218 s | 760 s | $3,784 | +$315 |
| 13 | 304 s | 905 s | 526 s | $4,100 | +$631 |
| **14** | **255 s** | **729 s** | **374 s** | **$4,415** | **+$946** |
| 15 | 224 s | 591 s | 273 s | $4,730 | +$1,261 |
| 16 | 198 s | 526 s | 201 s | $5,046 | +$1,577 |

- JC-414 adds only ~+35 s to p90 at 14 agents (694 s → 729 s).
- 14 is the smallest size that meets the target with margin. 15 adds headroom for growth and simulator optimism.

### Docker with the off-peak schedule (weekdays 05:50–20:30 full size, otherwise reduced)

| Peak / off-peak agents | Push → green p90 | Off-peak wait p90 / p99 | $/month |
|---|---:|---:|---:|
| 14 / 5 (module's built-in 70% cut) | 729 s | 328 s / 1,009 s | $2,858 |
| 14 / 8 | 729 s | 0 s / 321 s | **$3,377 (≈ today)** |
| 15 / 8 | 591 s | 0 s / 321 s | $3,519 |

- Today's off-peak wait is p90 0 s, p99 ~112 s.
- An off-peak floor of 8 needs a small Terraform change: `num_instances_off_peak_reduction` is a hard-coded local (0.70 for ap-southeast-2).
- Scale-in at 20:30 needs agent draining, or it can kill builds still running.

### Windows after JC-414 (no FE work left)

| Agents | Wait p90 (business hours) | Wait p99 | $/month | Δ vs today |
|---:|---:|---:|---:|---:|
| 26 (today, with FE work until 6 Nov) | 275 s simulated (303 s actual) | 966 s simulated | $18,304 | – |
| 26, without FE work | 145 s | 504 s | $18,304 | – |
| **24** | **225 s** | **587 s** | **$16,896** | **−$1,408** |
| 22 | 321 s | 769 s | $15,488 | −$2,816 |

- Off-peak scaling on Windows isn't recommended: weekday 20:00–21:00 bursts reach 21 busy agents, which would push off-peak p90 waits above 6 minutes.

### Combined options

| Option | Docker | Windows | Net $/month | Push → green p90 |
|---|---|---|---:|---:|
| **A (recommended)** | 14 always on | 24 | **−$462** | 729 s |
| A+ | 15 always on | 24 | −$147 | 591 s |
| B (Docker only) | 14 peak / 8 off-peak | 26 | −$92 | 729 s |
| C (cheapest) | 14 peak / 5 off-peak | 26 | −$611 | 729 s, slower off-peak |

**Caveats:**
- On-demand list prices only: no RIs or savings plans, EBS excluded.
- The simulator assumes interchangeable agents and FIFO order, and replays fixed arrival times. It can't model chained builds starting earlier when upstream builds finish sooner.
- Load is growing on both pools. Re-run after JC-414 lands and again in about four weeks.
- JC-428 (one checkout/image per push) and JC-430 (registry layer cache) will cut FE Docker load further.

## 6. Slack draft for devops/platform

> *Docker build agents (Sydney `apse2c-dok`): proposal to add 3 agents, paid for by 2 Windows agents*
>
> Hi team 👋 On 6 Nov the five `app/` frontend PR checks moved from the Windows agents to the Docker agents (JC-411/JC-414). They now use ~65–70% fewer agent-hours: ~25 Windows agent-h per weekday became ~9 Docker agent-h. But the Sydney Docker pool is now the bottleneck, and PR feedback got slower:
> • *Push → all frontend checks green, p90:* ~14 min on Windows (27 Oct–6 Nov) → *~30 min* on Docker (2–10 Nov)
> • *It's not just our builds:* every Docker build waits p90 ~19 min for an agent in business hours. Other teams' builds went from ~9 to ~16 min p90 once our checks landed.
> • *Why:* the pool (11 × m6a.2xlarge, always on) was already full at peak before we moved. All 11 agents were busy at p90 on 28–30 Oct. Our checks add only ~0.7 agents on average and ~4 at peak, but bursts of five checks per push into a full pool turn into long queues.
>
> *Modelling:* I replayed 7 weekdays (2–10 Nov) of real Docker-pool builds, 9,312 builds with their actual agent-wait times, through a queue simulator. It includes the package builds JC-414 moves over next. At 11 agents it reproduces today: 1,716 s p90 simulated vs 1,819 s actual.
> ```
> Docker agents   push→green p90   all-builds wait p90   $/month (on-demand)
> 11 (today)          30 min             19 min              $3,469
> 13                  15 min              9 min              $4,100
> 14                  12 min              6 min              $4,415
> 15                  10 min            4.5 min              $4,730
> target (Windows era) 14 min
> ```
> *Ask:*
> 1. `data-tribe/build-agents` → `environments/corp-ap-southeast-2/main.tf`: `instance_count` 11 → *14*, or 15 for headroom. Cost: +$946/mo, or +$1,261/mo for 15.
> 2. Once JC-414 has moved the package builds off Windows: `windows-teamcity-build-agents` → `deployments/terraform/env/corp/ap-southeast-2/main.tf`: `number_of_teamcity_agents` 26 → *24*. Saves $1,408/mo. With no FE work left, the simulator puts Windows business-hours wait p90 at ~4 min with 24 agents, vs ~5 min today with 26.
> *Net: about −$460/mo* (−$150/mo with 15 Docker agents), and PR p90 drops back to ~12 min.
>
> *Docker-only alternative:* keep Windows at 26 and enable the Docker module's off-peak schedule at 14 peak agents. With a night floor of 8 it costs $3,377/mo, about today, with off-peak p99 wait ~5 min. That needs the 70% reduction exposed as a variable, plus agent draining at 20:30 scale-in. The built-in 70% cut (14 → 5) is $2,858/mo, but off-peak builds would wait p99 ~17 min.
>
> *Caveats:* prices are from the AWS Pricing API, Sydney on-demand. With 1-yr RIs the net is the same, about −$460/mo. EBS is excluded. The model assumes interchangeable agents and is a little optimistic at the tail, hence 14–15 rather than 13. Load is still growing: Web Back End V2 and StyleCop Core on Windows since 31 Oct (~31 agent-h per weekday), and MCP Server checks on Docker. JC-428 and JC-430 will cut our Docker load further. Happy to re-run the numbers in a month and to pair on the change. Full method and numbers: ⟨link⟩
