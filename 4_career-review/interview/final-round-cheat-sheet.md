<!--
FINAL-ROUND CHEAT SHEET: one page to skim 15 minutes before a hiring-manager / culture-fit / values round.
Source of truth: star-story-bank.md (stories), ownership-and-decisions.md (decisions), impact-metrics-playbook.md (numbers).
Fill the ⟨⟩ once you have measured numbers.
-->

# Final-Round Cheat Sheet (2026-11)

## My positioning in one line
> **"Senior full-stack engineer who gets handed the ambiguous, high-priority feature, makes the calls, and owns it through launch. Plus seven years in SMASH! IT on the side, now leading its 25-person team."**

## The 3 projects I lead with (in this order)
| # | Project | My role (say it plainly) | The decision I own | Outcome / number |
|---|---|---|---|---|
| 1 | **SMS onboarding** (Twilio compliance embed), Sep–Nov 2026 | Led the technical side: discovery, plan, CmAPI architecture, staffing proposal | **Staged rollout** (irreversible registration); **idempotent API** (never double-buy a number) | Manual, single-person process → in-app; ~2 months to dev-complete; 3 provisioning paths → 1; foundation for ~250-customer migration; ⟨N registered, turnaround before/after⟩ |
| 2 | **Drip Campaigns**, Apr–Oct 2026 | Owner of the builder canvas + launch readiness (TL led overall) | Defended the new `SendingAgentType` column over reuse (7 vs 20–30 files) | Every plan by Oct; my runbook was named the template for others; ⟨N accounts / M campaigns⟩ |
| 3 | **CRM Lite**, 2025–26 | Feature tech lead; LDR through architecture review | DBA schema + GDPR race handling; completion detection | Shipped to prod; pipeline sized for 20M-contact lists |
| + | Brand Hub V2 (in flight) | Sole frontend owner | Optimistic-concurrency saves | Brand Hub's most common customer request (3 of 4 in research) |

## Numbers I can say without blinking
- **~2 months** from discovery to dev-complete on SMS · **16 of 28** epic tickets reported by me · **3 → 1** provisioning paths · **2,264** tests green
- **Every plan** for Drip by 1 Oct · runbook with **7 metrics / 7 runbooks**, reused for the all-plans launch
- **~41% faster** deploy package build (early, n=20) · 24-ticket epic I created
- **307/307 + 72/72** tests on the AI migration that leadership chose *not* to ship (~2× code, ~3× maintenance)
- **4** production incidents resolved end-to-end in 2026 · **~620** PRs reviewed career-wide
- SMASH!: **25** people / **3** leads · **45,000+** attendees · **5** conventions with **zero** critical failures

## Other people's words (use one, never a list)
- Team lead at Drip GA: *"the real heroes behind this… Thank you Clem, Fan and Chris"*
- Boole TL on a CRM Lite customer question: *"I think clem implemented that work, we can have a chat with him"*
- Partner team, reading the SMS code: *"Looks like Clem did this work"*
- RSS customer via Support: *"Thanks for spotting the issues and letting me know"*

## Values-round mapping (Ownership / Customer / Bias for action / Earn trust / Learn)
| They probe | Story | Key line |
|---|---|---|
| Ownership | 13 SMS | "My EM asked me to own discovery; I ended up owning the plan, the rollout staging and the API." |
| Customer obsession | **23 RSS**, 13, D9 | "I paused their automation, explained both problems so they could fix them, and checked the next send went out right." |
| Disagree & commit | 17 schema | "I answered 'do we need this?' with a cost comparison and gave the cleanup its own ticket." |
| Bias for action / judgment | 19 UCF | "I asked for a 👍 before touching prod late at night. Fast doesn't mean reckless." |
| Earn trust / own mistakes | 20 CI break, **24 webpack review** | "'My bad', fixed quickly, then designed the flag so it can't recur." / "I approved a build change that broke a customer feature. Now I review the output, not just the diff." |
| Frugality / simplicity | 18 AI-DLC, D6 | "The cheapest code is the code we correctly didn't write." |
| Influence | 14, 15 | "I proposed the staffing split; my lead took it." / "Partner team changed their API the next day." |
| Learn & be curious | 18 | AI-driven development: what it's good at, where it loops |
| Develop others | junior mentoring, React Query standard | "I championed React Query invalidation in reviews across the team." |

## When they ask "why are you leaving?"
> "I've grown into leading features: discovery, rollout calls, launch. I want a role where that's the job, with the scope and title to match."

## Traps to avoid
- ❌ Opening with tooling (webpack/Vite/TS/Docker) or reviewer stats. That's the "pet project" read.
- ❌ "We decided…" for decisions *I* made. ❌ Claiming I led Drip overall, or that Biome, the webpack 5 monolith build or JS Crew leadership were mine.
- ❌ Stories that end at "it merged". End at **launch + number + reflection**.

## 3 questions to ask them (ownership-flavoured)
1. "What's a decision a senior engineer here made recently that changed the roadmap?"
2. "How do you measure whether a feature succeeded after launch, and who owns that number?"
3. "What would I own in my first 6 months, and what would 'great' look like at the end of it?"
*(More in reverse-interview-questions.md.)*
