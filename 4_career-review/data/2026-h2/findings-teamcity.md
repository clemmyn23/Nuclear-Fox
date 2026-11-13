# TeamCity build stats (pulled 2026-11-10, read-only, window 2026-08-10 → 2026-11-10 ≈ 90 days)

> ⚠️ **Superseded:** see [portfolio/docker-frontend-builds-results-2026-11.md](../../portfolio/docker-frontend-builds-results-2026-11.md) §9. The "FE merge check" rows below are the **Docker** checks, not the Windows ones. TeamCity kept ~10 days of history, not 90, so the run counts and "~1,900 pushes/yr" are wrong. The 41% package figure holds like-for-like.

| Job | Runs (90d) | Median | p90 | Agent-hours (90d) |
|---|---:|---:|---:|---:|
| FE merge check — Validate JS (app) | 475 | 41 s | 61 s | 7.0 |
| FE merge check — Validate JS (shared) | 476 | 21 s | 90 s | 4.8 |
| FE merge check — Build images & CSS | 470 | 31 s | 52 s | 5.4 |
| FE merge check — Build JS (Closure) | 463 | 60 s | 160 s | 9.2 |
| FE merge check — Build JS (Webpack) | 457 | 180 s | 240 s | 24.0 |
| **5 FE merge checks combined** | ~470 pushes | ~333 s summed | — | **~50.4 h** |
| Monolith Deploy — Web Package Javascript (legacy agent) | 409 | 495 s | 532 s | 56.9 |
| Monolith Deploy — Front End Deploy Build & Test | 478 | 885 s | 1032 s | 95.6 |
| **Monolith Deploy — Web Package Javascript (Docker)** — JC-413/414, first run 2026-11-09 | 20 | **290 s** | 405 s | 1.5 |

Takeaways (early, n=20 Docker runs):
- Dockerised Web Package JS median 290 s vs legacy 495 s → **~41% faster (~3.4 min saved per package build)**. Early sample — re-measure after 2–4 weeks.
- ~470 FE merge-check pushes / 90 days ≈ **~1,900 pushes/yr**. JC-411 comment: Docker deps-layer cache saves ~5–9 min agent time per push → **~160–285 agent-hours/yr** if it holds across all merge checks (projection, not measured).
- Package-build volume ~409/90d ≈ 1,650/yr × 3.4 min ≈ **~94 agent-hours/yr** on Web Package JS alone (projection).
- Canary and Hotfix Docker package jobs exist but have 0 runs yet (Stage 3 not rolled out there).
