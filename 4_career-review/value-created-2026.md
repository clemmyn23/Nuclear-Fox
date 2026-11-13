# What your 2026 was worth in dollars — a defensible model (Nov 2026)

> **Read this first.** No honest analyst can give you one true number — anyone who does is selling
> something. What I can give you is a **model with every assumption exposed**, three scenarios, and
> a per-row confidence label, anchored to the measured numbers in
> [findings-impact-numbers.md](data/2026-h2/findings-impact-numbers.md). Use the ⭐ hard-measured
> rows out loud in negotiations; use the totals only as "directional, order-of-magnitude".
> Window: Nov 2025 → Nov 2026 (CADD window). All AUD.

## Shared assumptions (tweak these and the model moves)
| Assumption | Value | Basis |
|---|---:|---|
| Your fully-loaded cost to the company | ~$160k/yr | $133k base + ~20% super/overheads |
| Loaded engineer rate (yours & peers') | **$85/hr** | $160k ÷ 1,880 productive hrs |
| Senior contractor market rate (replacement lens) | $140–170/hr | Sydney market |
| CM email ARPU (blended) | $75–150/mo | assumption — replace with a real number if you can get one |
| SMS credits spend per enabled customer | $100–300/mo, ~35% margin | assumption — Product/Finance would know |
| Windows CI agent cost | $0.60–1.20/agent-hr | EC2 Windows on-demand ballpark |

---

## Lens 1 — Replacement cost: what buying your output would cost
The simplest honest lens: 106 PRs authored (86 merged, including two flagship features + launch
ownership), 163 reviews, 4 incident resolutions, discovery/tech-audit/design work, 4 engineers
coached. Buying that from a senior contractor at $140–170/hr for ~1,700 delivered hours:

**≈ $240k – $290k** — vs the ~$160k you cost. That's a 1.5–1.8× markup the company keeps **before
counting any of the value below.** High confidence (it's arithmetic, not attribution).

## Lens 2 — Incremental value created (savings + avoidance + multipliers)
Each row: model × **attribution haircut** (your fair share of shared work). Conservative / Mid.

| # | Contribution | Model (anchors are measured; multipliers are assumptions) | Attribution | Conservative | Mid | Confidence |
|---|---|---|---:|---:|---:|---|
| 1 | ⭐ Docker CI — infra compute | 4,850 agent-hr/yr saved (measured) × $0.60–1.00/hr | 80% | $2.3k | $3.9k | **High** (measured hours) |
| 2 | Docker CI — upgrades become code changes | 3–6 toolchain upgrades/yr × 8–16 staff-hrs saved (coordination + agent/AMI work) × $85 | 80% | $1.6k | $4.9k | Medium |
| 3 | ⭐ SMS — manual provisioning eliminated | 100–250 registrations/yr × 1.5–2.5 staff-hrs each (support+eng round-trips, single-person dependency) × $85 | 70% | $8.9k | $31.2k | Medium (process was real; volume is projected) |
| 4 | SMS — revenue enabled (self-serve + sales-led) | 30–75 incremental SMS customers/yr × $1.2k–2.9k/yr credits × 35% margin | 40% | $5.0k | $21.3k | **Low** (every factor assumed) — directional only |
| 5 | Drip — retention value of adoption | 688 adopted accts (measured) → ~1,200 by yr-1 × $900–1,500 ARPU/yr × 1–2pp churn improvement | 30% | $2.8k | $8.1k | **Low** — adoption measured, churn effect assumed |
| 6 | Incidents — RSS enterprise customer save | 1 enterprise acct $12k–36k ARR × 20–40% churn-risk reduction (customer thanked you via support) | 70% | $1.7k | $7.1k | Medium |
| 7 | Incidents — UCF DLQ, trigger-service, GitHub bot | Escalation + other-team eng time avoided, 60–180 staff-hrs total × $85 | 70% | $3.6k | $10.7k | Medium |
| 8 | ⭐ AI-DLC no-go evidence | Avoided ~2× code / ~3× maintenance (leadership's own numbers): 0.1–0.25 FTE-yr not spent | 60% | $9.6k | $24.0k | Medium-high (decision happened, cited your evidence) |
| 9 | Reviews — 163 PRs (measured) | 0.4–0.8 downstream rework-hrs saved per review × $85 (review-caught defects cost ~10× later) | 100% | $5.5k | $11.1k | Medium |
| 10 | ⭐ Mentoring — 4 engineers (arcs measured) | Chris + Melisa reached review-independence est. 2–5 wks earlier each; Sherry/Gen unblocked ≈ 60–150 hrs | 50% | $8.1k | $23.4k | Medium (arcs measured, acceleration assumed) |
| 11 | Local proxy overhaul | ~25–35 monolith devs × 2–5 hrs each saved getting local dev working post-CmAPI move (quote: "you will need the updated version… Which Clem overhauled") | 90% | $4.6k | $11.5k | Medium |
| 12 | Hex lookup + TeamCity audit + CVE flag + Graylog migrations | Lookups replacing prod-SQL remoting (5–15 min × 300–800 uses/yr) + dead-project clutter + CVE expected-loss avoidance (counted $0 — unquantifiable, could dwarf everything) | 90% | $2.5k | $7.7k | Low-medium |
| | **Lens 2 total** | | | **≈ $56k** | **≈ $165k** | |

An aggressive scenario (top of every range, lighter haircuts) lands ≈ **$350–400k** — quote it
never; it's the ceiling that makes the mid credible.

## Lens 3 — What's deliberately NOT counted
- **Core feature revenue** (Drip's and SMS's actual revenue) — that belongs to the product and the
  whole team; Lens 2 rows 4–5 only claim thin, haircut slivers.
- **Future value already in motion:** ~250-customer Infobip→Twilio migration (2027); Docker
  push-to-green potential (~800 dev-hrs/yr ≈ $60–70k **if** the pool queue is fixed — measured as
  not yet realised, so $0 today); Closure→esbuild / TS7 benchmarks (62.5→3.5s etc.).
- **The CVE catch and the 4 incidents' tail risk** beyond modest staffing costs — expected-loss
  maths on security/outage events is where these models become fiction.
- **Bus-factor insurance**: Journeys knowledge-holder, SMS no longer single-person. Real, uncashable.

## The punchline (use this framing, not a single number)
> "On replacement cost alone my output ran $240–290k against my ~$160k cost. On top of that, the
> measurable side-effects — CI savings, the provisioning process I deleted, the AI-DLC decision,
> the mentoring arcs — model out to roughly **$55k conservative / $165k mid per year** of
> incremental value, with the two revenue rows deliberately haircut to slivers. By any lens the
> company clears a healthy multiple on my $133k."

## Rules of use
1. **Say the ⭐ rows as facts** (they anchor to measured numbers); say everything else as "modeled,
   assumptions on request".
2. Never defend the total — defend a row. If someone attacks row 4, concede it instantly ("that's
   the most assumed row, strike it") — the case barely moves.
3. The number this document is *really* for: the comp conversation in
   [comp/pay-gap-brief-2026-11.md](comp/pay-gap-brief-2026-11.md). Value-created ≫ cost is the
   backdrop; the ask itself stays anchored on market + scope.
4. Refresh row anchors quarterly (impact-numbers doc has the queries); swap assumed ARPUs for real
   ones if a friendly PM or Finance person will give them to you.
