# IC Level Assessment

An evidence-based estimate of Clement Ng's engineering IC level, and the progression that led there. Drawn from the full dataset in this review: 532 authored PRs, 558 reviews, 466 review comments, 21 authored Confluence pages, and ~25 Slack discussion threads (2021-04 → 2026-05).

> **Caveat up front:** this is an *artifact-based* estimate. It reads PRs, docs, and chat — it cannot see performance-review calibration, promo packets, comp band, design-review meetings, or verbal incident leadership. Treat it as "what the written record supports," not an HR determination.

---

## Headline

**Current level: Senior Software Engineer (IC3) — operating at the top of the band, with a credible and forming Staff (IC4) case.**

Shorthand: **Senior, Staff-trending.** If you were assembling a promotion packet today, Years 5–6 are the raw material for it — but the scope is still *tribe-bounded* (Boole / Audience-Journeys) rather than *org-bounded*, and the deepest architecture calls are ratified by the architecture function (Lance Smith) rather than owned by you. That's the gap between "strong Senior acting as feature tech lead" and "Staff."

Confidence: **high** that you're solidly Senior; **medium** on exactly how much of the Staff case is already met vs. emerging.

---

## The ladder being mapped against

Generic industry IC ladder (names vary by company):

| Level | Generic name | Scope of impact | Ambiguity owned |
|---|---|---|---|
| IC1 | Engineer I / Junior | Own tasks, well-defined | Low — told what to build |
| IC2 | Engineer II / Mid | Own features, some design | Medium — given a problem |
| **IC3** | **Senior** | **Own features end-to-end + multi-service; uplift the team** | **High — given a goal** |
| IC4 | Staff | Own multi-quarter, cross-team initiatives; org-level technical influence | Very high — given a direction |
| IC5+ | Senior Staff / Principal | Reshape how the org builds | Open-ended |

**Campaign Monitor's actual ladder** (from the [CMC Engineering Team Confluence page](https://campaignmonitor.atlassian.net/wiki/spaces/CMC/pages/239941816/)): "Engineering I / II / III" + "Tech Lead" + EM. So CM "Engineering III" ≈ Senior (IC3), and "Tech Lead" is a role overlay rather than a separate rung. Your Slack profile title reads "Software Engineer"; teammates referred to you as **"feature lead"** in 2025 ("Clem has gone mad with power after becoming feature lead"). You also bookmarked the internal **"Senior Software Engineer" Workday posting** in Dec 2024 — a signal you were tracking the promotion yourself.

---

## Level progression — year by year, with the signals that moved you up

### Year 1 (2021–22) — entered/consolidated at **Mid (IC2)**, ramping fast
**What the record shows:** small UI fixes in week 1 → owning **Bulk Delete Lists** end-to-end (incl. feature flag) by week 6 → **drag-and-drop custom fields** with a design-system contribution by month 3.

**Promotion-relevant signals:**
- Speed from "task-doer" to "feature-owner" was unusually fast — suggests you were *hired in* at mid-level, not entry.
- First **multi-repo coordinated change** (`UX1-490` across 4 repos in one week) — an IC3 behaviour appearing early.
- First **design-system PRs** (CMDS) — contributing to shared infrastructure, not just your squad's code.

**Why not yet Senior:** still primarily executing within one product surface; design was mostly handed to you; no documented design-doc or cross-functional negotiation yet.

### Year 2 (2022–23) — **crossing into Senior (IC3)**
**What the record shows:** SMS product **end-to-end through the entire stack** — React UI → CmAPI → gRPC services → protobuf contracts (`cm.protobuf`, `kafka-acls`, `jvm-libs`, `TrackingServices`). In parallel, **led the createsend.com JS toolchain modernisation** (yarn workspaces, Vite, esbuild, Node 16 LTS, TypeScript 4, Prettier 2.7).

**Promotion-relevant signals:**
- **Impact beyond your own tickets:** the toolchain work changed how *every* frontend engineer builds. That's the canonical IC2→IC3 trigger.
- **First Confluence authored docs** (Node-bump reference, Signup Forms audit) — you started leaving the codebase more legible than you found it.
- **Vertical-slice ownership** across 5 repos for a single feature (SMS-155 link tracking) — you stopped needing a backend engineer to "do the backend half."
- Reviews widened to 29 authors across multiple squads — "JS-crew polyglot."

**Why this is the crossing point:** the toolchain stewardship + full-stack vertical ownership + first design docs is the package that defines Senior.

### Year 3 (2023–24) — **solidly Senior (IC3)**
**What the record shows:** Shopify Migration Assistant + Commerce Management across a **service mesh** (monolith + `cm.protobuf` + `ThirdPartyListImporter` + `campmon.hex`). The **MER-665 cross-service permission contract** landed across 4 repos in coordination. Authored the **CopyWorkflowService architecture deep-dive** still used to onboard AJ engineers.

**Promotion-relevant signals:**
- **Contract design** (not just contract consumption) — you defined protobuf/schema shapes that other services depend on.
- **Coordinated multi-service change as a default move**, not a one-off.
- Authoring **architecture-reference docs that onboard others** — multiplier effect.
- Reviewing across **8+ projects beyond your own** — becoming a reviewer-of-record.

### Year 4 (2024–25) — **Senior, with the first Staff-shaped signals**
**What the record shows:** deep AJ-tribe feature ownership (UCF Advanced Expressions, Wait-Until step, condition-path swap — each end-to-end across monolith + microservice). **Bloom Bootstrap greenfield** — bootstrapped a new product prototype from zero (docker, Cognito auth, DevX) and acted as **tech-lead reviewer** for others on it. Three-repo gRPC change (`AJ-575`). Terraform + DynamoDB PITR infra work. GDPR-aware CAL-audit feature work.

**Staff-shaped signals starting:**
- **Tech-lead on a greenfield** — you set the patterns others followed.
- **Security/privacy-by-design** baked into feature work (GDPR audit on CAL logs).
- **"The AJ person who reviews everything"** — 84 reviews concentrated on becoming the tribe's review backbone.
- First **bug-bash organising** — owning cross-functional pre-release QA, a coordination role beyond coding.

### Year 5 (2025–26) — **top-of-band Senior / feature tech lead; Staff case forming**
**What the record shows:** explicitly operating as **feature tech lead** (teammates' words). Owned **CRM-Lite Subscriber Profile** end-to-end: authored the **LDR in the official Architecture space**, drove DBA / GDPR / platform / product conversations *before* code, then delivered ~15 PRs through to the **production-enablement flip**. **181 reviews** — the dominant reviewer on the tribe. **WorkflowLookupService monolith→netcore migration** (three reverts to land). **Technical screener for mid-level hires** with hire/no-hire authority.

**The Staff case (what's genuinely there):**
- **Design-doc-first leadership** — an LDR that goes through the formal architecture process, then drives a quarter of delivery.
- **Cross-functional pre-design negotiation** — chat → doc → PR pattern, brokering DBA/GDPR/platform decisions.
- **"You have the most context here"** — repeatedly the person product/PM/leads defer to.
- **Multiplier effects:** mentoring 2–3 junior engineers (Christopher Luong, Fan Li, Sharareh), hiring authority, reviewer-of-record, onboarding docs.
- **Tenacity on hard platform work** that others would bounce off (the 3-try netcore migration).

### Year 6 (2026, partial) — **sustaining the Year-5 level**
Complex Campaign Series, GrpcClient v2 migration, Webpack 5; continued tribe leadership and AI-augmented delivery with measured time-deltas. No level change visible in two months — consolidating, not stepping up again yet.

---

## Evidence matrix against Staff (IC4)

The honest scorecard — what's met, partial, and not-yet for the next rung.

| Staff criterion | Status | Evidence |
|---|---|---|
| End-to-end ownership of large, ambiguous features | ✅ **Met** | CRM-Lite, Campaign Series, SMS product, Commerce |
| Design-doc leadership / architecture review | ✅ **Met** | LDR in `arc` space; onboarding investigation matrix; architect sign-off obtained |
| Multiplier effect on other engineers | ✅ **Met** | 558 reviews, mentoring juniors, onboarding docs, JS-crew steward |
| Cross-functional technical leadership | ✅ **Met** | DBA / GDPR / platform / product negotiations drive the design |
| Hiring / bar-raising | ✅ **Met** | Technical screener with hire/no-hire calls |
| Tenacity on hard, deep changes | ✅ **Met** | 3-try WorkflowLookupService migration; multi-repo gRPC |
| **Cross-*org* (not just cross-tribe) impact** | ⚠️ **Partial** | Influence is deep within Boole/AJ; toolchain work reaches all FE eng, but most initiatives are tribe-scoped |
| **Owning the architecture call, not ratifying it** | ⚠️ **Partial** | You author strong LDRs, but the deepest calls are signed off by the architecture function (Lance) — you're an excellent *consumer* of it |
| **Multi-quarter initiative that reshapes how the org builds** | ❌ **Not yet** | Your big efforts are large features/migrations, not platform-defining programs others build on top of for years |
| **Setting technical direction across teams** | ❌ **Not yet** | Direction-setting is within-tribe; no documented org-wide technical strategy ownership |

**Reading the matrix:** 6 of 10 Staff criteria are clearly met, 2 partial, 2 not-yet. That's exactly the profile of a **strong Senior with a forming Staff case** — not a Staff engineer who's under-titled, and not a mid-level reaching. The two "not-yet" rows are the specific, actionable gap.

---

## What would close the gap to Staff

Concrete, based on what the record shows is missing — not generic advice:

1. **Own an initiative whose blast radius is the org, not the tribe.** Your JS-crew toolchain work is the closest existing example (it touches all FE engineers) — lean into that lane. A "modernise the monolith frontend build for every team" charter would read as Staff; "ship CRM-Lite for Boole" reads as Senior.
2. **Be the architecture decision-maker of record, not the LDR author who gets it signed off.** You already do the analysis; the step up is when *your* LDR is the thing other teams' LDRs get measured against — i.e. you become (part of) the architecture function for a domain.
3. **A multi-quarter platform program others build on.** The contact-model rework you've alluded to in Slack ("what the previous-previous exec had been asking for the past 5 years") is exactly this kind of Staff-defining program if you were to own it end-to-end.
4. **Make the multiplier legible.** You mentor and review heavily, but it's implicit. Staff packets need the "I uplifted N engineers / I set the pattern M teams adopted" framing — your Confluence docs and bug-bash process are already evidence; name them as deliberate force-multiplication.

---

## One-line summary for a manager / recruiter

> Clement is a **Senior Software Engineer operating as a feature tech lead** — full-stack end-to-end ownership, architecture-doc leadership, the tribe's reviewer-of-record, and a hiring bar-raiser. The written record supports a Senior rating without reservation and contains a credible, forming case for Staff; the remaining distance is *org-scoped* (vs. tribe-scoped) impact and owning architecture direction rather than authoring-and-ratifying it.
