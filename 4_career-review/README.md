# Clement Ng — Career Review at Campaign Monitor (2021–2026)

> **🆕 2026-11-10 refresh ("6 months later"):** GitHub, Jira, Confluence, Slack and TeamCity re-mined for Jun–Nov 2026. Start here:
> 1. [06-year6-current.md](06-year6-current.md): Year 6 rewritten (Drip launch → team merge → **SMS onboarding tech lead** → Brand Hub)
> 2. [interview/ownership-and-decisions.md](interview/ownership-and-decisions.md): **the answer to the interview feedback** (ownership, decisions, pet-project trap); 16-entry decision log
> 3. [interview/impact-metrics-playbook.md](interview/impact-metrics-playbook.md): user and business impact per project, with how to measure what's missing
> 4. [cv/clement-ng-resume-2026-11.md](cv/clement-ng-resume-2026-11.md) + [render](cv/render/resume-2026-11-editorial.html): **new résumé**
> 5. [interview/final-round-cheat-sheet.md](interview/final-round-cheat-sheet.md): the one-pager before a final round

> **🆕 2026-11-12 additions (CADD prep):**
> - [cadd-self-review-2026-11.md](cadd-self-review-2026-11.md) — CADD draft, all five questions, measured numbers
> - [hr-form-responses-2026-11.md](hr-form-responses-2026-11.md) — HR role/development form draft (1:1 cadence calendar-verified)
> - [neutral-performance-analysis-2026-11.md](neutral-performance-analysis-2026-11.md) — independent-agent verdicts: senior-level; visibility critique narrowed by the meeting-note corpus (13 Nov addendum)
> - [data/findings-meeting-notes-12mo.md](data/findings-meeting-notes-12mo.md) — **12-month meeting-note sweep (13 Nov)**: the team demo slot verifiably ran only 4× in 12 months (29 Sep explicitly skipped); JS-crew React Flow/Campaign Series talk verified (12 May, recorded); org-wide venues credit his work to others; no Gemini notes exist before Jun 2026
> - [sms-embed-feedback-2026-11.md](sms-embed-feedback-2026-11.md) — SMS retro evidence pack (Twilio's written admissions)
> - [comp/pay-gap-brief-2026-11.md](comp/pay-gap-brief-2026-11.md) — why pay sits below peers; the move
> - Measured impact: [data/2026-h2/findings-impact-numbers.md](data/2026-h2/findings-impact-numbers.md) (drip 688 accts / 1,212 drips / 446 advanced; SMS first 3 embed customers) · [findings-mentorship.md](data/2026-h2/findings-mentorship.md) (4 mentees, review arcs) · [findings-instrumentation-hooks.md](data/2026-h2/findings-instrumentation-hooks.md) · [findings-meeting-notes.md](data/2026-h2/findings-meeting-notes.md) · [findings-standup-notes.md](data/2026-h2/findings-standup-notes.md) (61 meeting notes mined: speaks in 47, 5 demos, ~55 action items, zero formal-showcase demos — but the slot itself rarely ran; see findings-meeting-notes-12mo.md)
> - Shipped: Jira [COM-1825](https://campaignmonitor.atlassian.net/browse/COM-1825) (SMS funnel instrumentation) created under COM-1620; implementation PRs open: [#25691](https://git.campmon.com/Freshview/createsend.com/pull/25691) (COM-1825, ⚠️ includes an SMS_Client schema column) · [#25690](https://git.campmon.com/Freshview/createsend.com/pull/25690) (COM-1796 Brand Hub edit events) · [value-created-2026.md](value-created-2026.md) ($-value model)

**Tenure:** 2021-04-08 → present (5 years, 7 months as of 2026-11-10)
**GitHub:** [cng](https://git.campmon.com/cng) on git.campmon.com
**JIRA:** campaignmonitor.atlassian.net

## Headline numbers

### Code
- **~588 PRs authored** (~507 merged); was 532 / 464 at the May review, plus 56 new since and 43 more merged (incl. 3 that were still open in May)
- **~620 PRs reviewed** for other authors (558 + 62 new since May)
- **466 review comments** captured across 187 PRs (33% of reviewed PRs got ≥1 comment from you)
- **128 distinct teammates'** work reviewed
- **43+ distinct repositories** touched
- **26 JIRA projects** spanned across authored + reviewed

### Design / planning / writing
- **24 Confluence pages authored** including 1 LDR in the official `arc` Architecture space (+3 in 2026-H2: Twilio compliance tech audit, Drip Campaigns playbook, sales-led dev-account recipe)
- **44 Confluence pages contributed to** as editor / major contributor (incl. the LDR template itself)
- **4 Bug Bash sessions organised** for major feature releases (2024–2026)
- **~25 substantive Slack threads** captured across squad-eng, JS-crew, dev-recruitment, and DBA / GDPR / product DMs
- **Hiring authority** — technical screener for mid-level engineering candidates

## Files in this review

### Analysis (read these)
- [00-executive-summary.md](00-executive-summary.md) — top-down narrative and at-a-glance table
- [01-year1-onboarding.md](01-year1-onboarding.md) — Year 1: UX1, CA, design-system contributions
- [02-year2-sms.md](02-year2-sms.md) — Year 2: SMS product + JS toolchain modernisation
- [03-year3-commerce.md](03-year3-commerce.md) — Year 3: Shopify, Automation Recipes, CL streaming export
- [04-year4-journeys.md](04-year4-journeys.md) — Year 4: AJ tribe deep work, Bloom greenfield
- [05-year5-platform.md](05-year5-platform.md) — Year 5: gRPC migration, Campaign Series, CRM Lite
- [06-year6-current.md](06-year6-current.md) — **Year 6 (Apr–Nov 2026, rewritten 2026-11):** Drip Campaigns launch, Boole→Mitnick merge, SMS onboarding tech lead, AI-DLC experiment, Docker builds, Brand Hub V2, 4 incidents
- [07-growth-signals.md](07-growth-signals.md) — cross-cutting analysis of professional growth
- [08-jira-projects.md](08-jira-projects.md) — every JIRA project you've touched (authored + reviewed)
- [09-notable-prs.md](09-notable-prs.md) — highlight reel across all 5 years
- [10-jscrew-review-activity.md](10-jscrew-review-activity.md) — review patterns: who, where, when
- [11-repo-breakdown.md](11-repo-breakdown.md) — every repo you've worked in, with counts
- [12-review-comment-patterns.md](12-review-comment-patterns.md) — themes and samples from your actual review-comment text
- [13-slack-architecture-discussions.md](13-slack-architecture-discussions.md) — substantive Slack discussions: design decisions, DBA negotiations, post-incident debugging, JS-crew interventions
- [14-confluence-design-docs.md](14-confluence-design-docs.md) — all 21 Confluence pages you authored + 44 contributed-to, including the CRM-Lite LDR in the Architecture space
- [15-ic-level-assessment.md](15-ic-level-assessment.md) — evidence-based IC-level estimate (Senior, Staff-trending) and the year-by-year progression that led there
- [16-ic-level-assessment-with-resume-data.md](16-ic-level-assessment-with-resume-data.md) — IC estimate augmented with the full 8-yr résumé + 6 yrs of SMASH! engineering leadership; how the leadership axis completes the Staff/Lead case

### CV / résumé deliverables
- 🆕 [cv/clement-ng-resume-2026-11.md](cv/clement-ng-resume-2026-11.md) — **current résumé** (Nov 2026), rebuilt around feature leadership + impact; renders: [editorial](cv/render/resume-2026-11-editorial.html) · [ATS-plain](cv/render/resume-2026-11-ats-plain.html)
- [cv/clement-ng-resume-2page-draft.md](cv/clement-ng-resume-2page-draft.md) — newest 2-page résumé draft: full 8-yr career + CM real-feature detail + SMASH leadership, fact-checked against source data
- [cv/resume-variants.md](cv/resume-variants.md) — three role-targeted cuts of the résumé: Staff/Senior+ IC, Engineering Manager/Tech Lead, Backend/Platform
- [cv/linkedin-rewrite.md](cv/linkedin-rewrite.md) — LinkedIn headline options, About, experience bullets, skills order, open-to-work strategy
- [cv/render/](cv/render/) — **styled print-ready HTML renders** of the verified résumé → PDF: `resume-editorial.html` (single-column typographic), `resume-sidebar.html` (two-column), `resume-ats-plain.html` (portal-safe). See [cv/render/README.md](cv/render/README.md)
- [cv/cover-letter-and-outreach-templates.md](cv/cover-letter-and-outreach-templates.md) — 6 parameterised templates: cover letter, recruiter reply, referral ask, LinkedIn note, follow-up, thank-you
- [cv/clement-ng-cv.md](cv/clement-ng-cv.md) — earlier 2-page CV draft (CM-focused, written before résumé/SMASH data)
- [cv/experience-section.md](cv/experience-section.md) — condensed 10-line experience entry for dropping into an existing CV

### Interview prep
- 🆕 [interview/ownership-and-decisions.md](interview/ownership-and-decisions.md) — feedback diagnosis, project re-ranking (lead with features, not tooling), 16-decision log, scripted answers, next-6-months plan
- 🆕 [interview/impact-metrics-playbook.md](interview/impact-metrics-playbook.md) — per-project user/business impact: what you can claim now (✅), projections (📐), what to go measure (🔍) + query sketches
- 🆕 [interview/final-round-cheat-sheet.md](interview/final-round-cheat-sheet.md) — one-page crib for hiring-manager / values rounds
- 🆕 [interview/system-design-sms-compliance-provisioning.md](interview/system-design-sms-compliance-provisioning.md) — system-design prep #3: idempotent, money-spending, irreversible third-party onboarding (from your SMS work)
- [interview/star-story-bank.md](interview/star-story-bank.md) — **22** STAR stories (10 new from Jun–Nov 2026: SMS lead, staffing call, cross-team API, Drip launch, schema disagreement, AI-DLC no-go, UCF incident, own mistake, Docker builds, reorg), mapped to question types
- [interview/system-design-crm-lite.md](interview/system-design-crm-lite.md) — system-design prep #1 (batch/throughput) built from your CRM-Lite LDR
- [interview/system-design-smash-ticketing.md](interview/system-design-smash-ticketing.md) — system-design prep #2 (low-latency/availability) from the SMASH ticketing build; scaffold to fill with your real choices
- [interview/tell-me-about-yourself.md](interview/tell-me-about-yourself.md) — 30-sec & 2-min opening scripts (IC and Lead/EM angles)
- [interview/reverse-interview-questions.md](interview/reverse-interview-questions.md) — questions to screen *employers* for the dysfunction you're leaving (churn, frozen promos, under-levelling)

### Comp & negotiation
- [comp/sydney-market-rate-and-negotiation.md](comp/sydney-market-rate-and-negotiation.md) — Sydney market-rate brief (estimates) + negotiation script
- [comp/negotiation-roleplay-script.md](comp/negotiation-roleplay-script.md) — the negotiation dramatised as a 5-beat script with tactic annotations
- [comp/cost-of-staying-model.md](comp/cost-of-staying-model.md) — illustrative model of the comp gap compounded over 5 years (~$300k)

### Job search
- [job-search/target-company-shortlist.md](job-search/target-company-shortlist.md) — Sydney target companies by category, with fit notes (general guidance)
- [job-search/tracker.csv](job-search/tracker.csv) — pipeline tracker template (companies, stages, comp, next actions)

### Growth & portfolio
- [growth/skills-gap-plan.md](growth/skills-gap-plan.md) — 6–12 month plan to close the Staff-IC gap or formalise the EM/Lead track
- [growth/brag-doc-promo-packet.md](growth/brag-doc-promo-packet.md) — living impact record mapped to a Senior→Staff ladder
- 🆕 [portfolio/docker-frontend-builds-results-2026-11.md](portfolio/docker-frontend-builds-results-2026-11.md) — **Docker frontend builds, measured** (TeamCity, same-commit pairs): PR-check compute −69% per push, checks 1.8–8.5× faster, deploy package −41% (shadow), the agent-pool queue caveat, the 6 Nov CI break quantified, résumé bullets and an upgraded STAR #21
- [portfolio/blog-post-drafts.md](portfolio/blog-post-drafts.md) — two engineering blog-post drafts (distributed-job completion; migrating out of a monolith)
- [portfolio/conference-cfp.md](portfolio/conference-cfp.md) — CFP package for your SMASH infra talk (abstract, outline, bio, where to submit)
- [portfolio/personal-site-content.md](portfolio/personal-site-content.md) — fun content grab-bag for your single-page site: taglines, RPG "character sheet", easter-egg code snippets, microcopy 🔨🐱
- [portfolio/site/](portfolio/site/) — **four complete drop-in `index.html` single-pagers** (RPG/forge, interactive terminal, modern/playful, convention badge) — zero-dependency, work offline; see [portfolio/site/README.md](portfolio/site/README.md)

### Raw data (CSVs — open with Excel/Numbers/grep)
- 🆕 [data/2026-h2/](data/2026-h2/) — Jun–Nov 2026 findings: [GitHub](data/2026-h2/findings-github.md) · [Jira](data/2026-h2/findings-jira.md) · [Confluence](data/2026-h2/findings-confluence.md) · [Slack](data/2026-h2/findings-slack.md) · [TeamCity build stats](data/2026-h2/findings-teamcity.md) (superseded by [Docker vs Windows builds](data/2026-h2/teamcity-docker-builds/README.md)) · ["Clem" name-mention sweep](data/2026-h2/findings-slack-clem-sweep.md) · [Peer sweep from a teammate](data/2026-h2/peer-sweep-sha-2026-11-10.md) + [its verification](data/2026-h2/findings-slack-peer-verification.md) · PR lists (`authored_new.tsv`, `reviewed_new.tsv`). Note: raw files name teammates; the analysis docs use roles.
- [data/authored-prs.csv](data/authored-prs.csv) — all 532 PRs you authored
- [data/reviewed-prs.csv](data/reviewed-prs.csv) — all 558 PRs you reviewed
- [data/review-comments.csv](data/review-comments.csv) — all 466 review comments you authored
- [data/own-pr-comments.csv](data/own-pr-comments.csv) — issue comments on your own PRs (5 captured — partial)
- [data/jira-tickets.csv](data/jira-tickets.csv) — JIRA ticket details (partial: 67 of 535 tickets fetched)
- [data/jira-projects-summary.md](data/jira-projects-summary.md) — all 26 JIRA projects, with team mapping
- `data/comments-per-pr/` — per-PR JSON files with raw comment data (~187 files)

### Helper scripts and intermediate files (kept for reproducibility)
- `scripts/merge_comments.py` — merges per-PR JSONs into review-comments.csv
- `scripts/_extract_jira_keys.py` — extracts unique JIRA keys
- `scripts/extract_prs.py` / `scripts/extract_prs.js` — PR metadata extractors
- `process_prs.py` — original authored-PRs CSV processor
- `data/reviewed-chunk-1.txt` … `reviewed-chunk-6.txt` — split chunks used for parallel comment fetching
- `data/page1-urls.txt`, `data/_jira_keys.txt` — intermediate data files from agent runs

## Gaps and follow-ups

- **Full JIRA enrichment** — only 67 of 535 tickets were fetched (mostly AJ project, current team). Remaining 468 keys are in the CSVs but un-enriched. Re-run with broader JIRA permission scope to complete.
- **Issue comments on your own PRs** — only 5 captured from recent PRs. Older years not fully traversed.
- **Review-comment volume** — 466 comments / 187 PRs is comprehensive but the agents skipped review threads where you only added approvals or non-substantive reactions. The substantive engagement is well captured.
- **Slack — curated, not exhaustive** — file 13 contains ~25 high-signal threads. There are thousands more messages by Clement; future passes could broaden the keyword set.

## How to use this review

1. Skim [README.md](README.md) and [00-executive-summary.md](00-executive-summary.md) for the top-down view.
2. Read the per-year files (01–06) in sequence to feel the arc.
3. Read [07-growth-signals.md](07-growth-signals.md) for cross-cutting growth observations.
4. Skim [09-notable-prs.md](09-notable-prs.md) for the highlight reel.
5. Read [12-review-comment-patterns.md](12-review-comment-patterns.md) for your engineering judgment in your own words.
6. Read [13-slack-architecture-discussions.md](13-slack-architecture-discussions.md) and [14-confluence-design-docs.md](14-confluence-design-docs.md) for the design + planning work that doesn't appear in PRs.
7. For CV writing: start at [cv/clement-ng-cv.md](cv/clement-ng-cv.md) for the 2-page draft, or [cv/experience-section.md](cv/experience-section.md) if you want a 10-line drop-in.
8. Drill into specific PRs via the CSVs when you want to remember the detail.
