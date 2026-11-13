# CADD self-review — draft responses (Nov 2026)

> Window: since the last CADD (~Nov/Dec 2025) → Nov 2026.
> Every number is measured — sources in [data/2026-h2/findings-impact-numbers.md](data/2026-h2/findings-impact-numbers.md)
> and [data/2026-h2/findings-mentorship.md](data/2026-h2/findings-mentorship.md).
> Tone: confident, specific, honest about misses. Trim to the form's length limits; the bold
> opening sentence of each answer survives any cut.

---

## 1. Do I consistently deliver work that meets the expectations of my role? (Performance & Results)

**Yes — this year I delivered the team's two highest-priority features to production and they are
measurably adopted.** Since the last CADD I authored 106 PRs (86 merged) and reviewed 163 for
others, but the results I'd point to are outcomes, not volume:

- **CRM Lite (Nov–Mar):** acted as feature lead — took the design through architecture review (LDR
  in the `arc` space), settled schema and GDPR-deletion decisions with the DBAs and platform team,
  and delivered the backfill pipeline sized for 20-million-contact lists. Product and PMs
  repeatedly routed design questions back to me ("you probably have most context in this area —
  what do you think?").
- **Advanced Drip Campaigns (Apr–Oct):** owned the builder frontend and launch readiness —
  dashboards, alerts, the runbook (reused as the template for later launches), and the go-live
  call to SRE. Shipped to every plan on 1 Oct. **Since the July launch: 688 client accounts have
  created 1,212 drip campaigns — 446 of them the new branching type, by 282 accounts — and weekly
  adoption ~2.6×'d after the all-plans GA**, with ~1 in 6 creators coming back to build more within
  weeks. (These are feature-level numbers: the team built Drip; my part was the builder frontend
  and launch readiness.)
- **SMS compliance embed (Sep–Nov):** asked to own discovery for one of Product's highest
  priorities; wrote the technical plan the PM adopted, designed the idempotent provisioning API
  (a retry can never buy a second number), merged three duplicate provisioning paths into one, and
  reached dev-complete in ~2 months. Cleared for real-customer registrations on 5 Nov, with the
  first customers now in flight. It replaces a manual process only one person knew how to run, and
  is the foundation for migrating ~250 customers off the legacy SMS provider.
- **Quality:** my launches shipped behind flags with staged rollouts and had no rollbacks; I
  resolved four production incidents end-to-end, including a customer's failing RSS sends
  (root-caused in ~80 minutes) and a cross-team dead-letter-queue regression.

Where I fell short of my own bar: the SMS build ran ~3 days past the 30 Oct target (we re-planned
with a second engineer mid-month), and in July a production incident shipped through a colleague's
webpack PR that I approved — I was the sole approver, and I've tightened how I review build-config
changes since.

## 2. Do I take ownership of responsibilities and follow through on commitments? (Accountability & Ownership)

**Yes — the pattern this year was being handed ambiguous problems and carrying them to done,
including the parts nobody was assigned.**

- SMS: discovery → plan → staffing proposal (adopted: "we'll go with what you've recommended!") →
  API design → cross-team negotiation (got the shared-services team to make `registrationInfo`
  optional to break a chicken-and-egg dependency; in staging the next day) → dev-complete → demo.
  I flagged the risks early (irreversible carrier registrations → staged rollout; black-box
  callbacks → early-access application) and the gaps (a hard-failed number leaves a customer stuck
  → proposed the support-escalation path).
- Launch readiness on Drip was self-assigned: I created the design-alignment card, built the
  dashboard and alert channel, wrote the 7-runbook playbook, and told SRE when we were live.
- Incidents: I take them to root cause, not mitigation — e.g. decoding the DLQ protobuf, proving
  the redrive was safe, tracing the regression to another team's PR, and shipping the patch (lead:
  "I can't express how great what you've done here is!").
- When I break something, I say so and fix it: my Docker-builds config change broke other teams'
  CI on 6 Nov — I owned it in the channel ("my bad"), scoped the fix the same day, and added the
  per-pipeline flag + rollback plan the remaining stages now use.
- Commitments survive me being away: before leave in October I handed over running PRs with
  explicit asks ("pls help move it along tomo when I'm away"), and my Stream A PRs were clean
  enough to be the handover artefact ("inspect the PRs that Clem put together, merge them in…").

## 3. Do I communicate clearly and collaborate effectively with others to move work forward? (Collaboration & Communication)

**Yes — a lot of my value this year was communication: plans PMs could adopt, decisions written
down before code, and coaching that made four engineers more independent.**

- **Written design work:** the SMS tech audit (adopted into the PM's rollout plan, including my
  re-estimate of 7–11 days over the 5–8 placeholder), the Drip launch playbook (named "the best
  playbook in either space; use it as the template"), and the dev-account recipe a teammate later
  automated.
- **Cross-team:** negotiated the API change with Team Thompson, coordinated per-brand theming with
  design, worked the C# crew and DB reviewers through the send-pipeline schema decision with an
  impact audit (7 additive files vs ~20–30 incl. hot send procs), and I'm the named owner other
  teams check with (sign-off requested before routing the SMS endpoint 100% to netcore; "Clem is
  looking into it" during the CI break).
- **Mentoring, with measured results:** I coached four engineers this year through DMs, calls and
  reviews — our newest team member from his first week (SQL schema design, the deploy pipeline,
  prod-ops safety, our JS standards), and a junior engineer from "where do unit tests go?" to
  clean, test-bearing PRs in five weeks. The data shows the transfer: my inline comments on their
  PRs drop from 7–10 per PR to 0–1 within about three months while their merge rates rise, and the
  AI review bot now quotes my review standards back to the team.
- **Keeping the team informed:** posted the team-merge redirect, demoed at standups and innovation
  sprints, summarised the all-hands strategy video for the team, and drafted the customer-facing
  explanation for the RSS incident that Support sent.

Where I can improve: some of my coaching and decisions live in DMs; I want more of them in team
channels and Confluence so they scale beyond the people I talk to. Demos tell a similar story: I
demo often in standups and presented our React Flow builder work to the JS Crew in May (recorded
and shared), but when my features reached the formal demo slot — Drip in July, my SMS embed in
October — a teammate or the PM presented them. The slot itself rarely ran this year, so the fix
isn't attendance: it's taking the presenter seat for my own features, and bringing finished work
to venues that reliably run, like the Weekly Technology Meeting.

## 4. Do I adapt to change, learn new skills, and incorporate feedback into my work? (Adaptability & Growth)

**Yes — this was the year of the reorg, and I adapted by absorbing scope rather than shrinking.**

- **Org change:** our tech lead left in August with no named successor and the team merged into
  Team Mitnick days before I was handed SMS. I picked up the Journeys knowledge-holder role named
  in the handover, onboarded into a wider surface (SMS, Brand Hub, Campaigns UI), and kept
  delivery going through the transition.
- **New skills:** C#/.NET service porting at depth (AI-DLC Stream A: 6 units, SSRF-hardened
  adapters, 307/307 unit + 72/72 parity tests), Docker-based CI pipelines and TeamCity DSL,
  Twilio's compliance/provisioning domain, and AI-assisted development used critically — I ran the
  experiment *and* wrote the honest assessment ("gone a bit past the whole 'use AI to save time'
  threshold") that leadership cited in its no-go decision ("That's what made this decision
  possible").
- **Incorporating feedback:** when a senior reviewer challenged my schema choice I audited instead
  of argued, and we landed a better version of the plan (non-null column, constraint dropped,
  cleanup logged as debt). When a reviewer caught my endpoints duplicated in legacy + netcore, I
  fixed it the same morning. After the webpack incident I changed how I review build-config PRs.
  When my manager flagged SMS schedule risk, I split my in-flight work so a second engineer could
  start the same week.
- **Growth I'm asking for:** I've been doing tech-lead work without the title — I'd like a named
  tech-lead role on SMS Checkpoints 2–3 (UK/AU sender IDs, the ~250-customer Infobip→Twilio
  migration) or the Journeys area, and a written development plan with criteria for the next level.

## 5. Do I effectively contribute positively to team goals and a collaborative working environment? (Contribution & Impact)

**Yes — beyond my own tickets, I multiplied the team: reviews, mentoring, tooling, and the unglamorous
work that keeps everyone else fast.**

- **Reviews:** 163 PRs reviewed across the team and JS Crew this window; I set and taught standards
  (React Query invalidation over reloads, one component per file, no cross-app imports, AI-slop
  hygiene) that are now quoted back by both teammates and the AI review bot.
- **Mentoring:** four engineers coached with measurable independence gains (detail above); invited
  by the People Team into the mentorship program; technical screener for engineering hiring.
- **Platform contributions with numbers:** initiated and lead the Docker frontend-builds epic —
  PR-check compute **−69% per push** (faster on 233/233 same-commit pairs), checks 1.8–8.5×
  faster, ~4,850 agent-hours/yr projected back, deploy package −41% in shadow — in the gaps around
  roadmap work (tooling was roughly a third of my H2 PRs), and being transparent about what hasn't
  improved yet (pool queueing).
  Also: the local proxy overhaul the monolith devs needed ("you will need the updated version of
  the local proxy. Which Clem overhauled"), the Hex lookup that stopped engineers remoting into
  prod SQL (EM: "Super useful!"), Graylog→Datadog migrations before decommission, a CVE flagged
  with the exact dependency path (fix shipped 29 minutes later), and the TeamCity dead-project
  audit DevOps verified and approved.
- **Team glue:** interim JS Crew meeting owner through the transition (then handed over cleanly),
  Mitnick alert-roster participant (~20 channels), bug-bash organiser, demo presenter, and the
  person who posts the summary so nobody else has to.

**The sentence I'd put on the year:** the team's two biggest bets shipped and got adopted, four
engineers got measurably more independent, and the build system got 69% cheaper — and I can show
the receipts for all three.

---

## 6. What are you most proud of from the last six months? *(optional question — answer it anyway)*

**SMS onboarding: being handed one of Product's highest priorities two days after our team merged
and our tech lead left — and landing it.** My manager asked me to take discovery on 1 September;
nine weeks later it was dev-complete and cleared for real customers, with the first three
registrations through the embed in its first week live. Along the way I wrote the plan the PM
adopted, designed a provisioning API where a retry can never buy a second number, merged three
duplicate provisioning paths into one, and got a partner team to change their API in a day to break
a circular dependency — all against a vendor product that turned out to be a pilot program.

Two more I'd put beside it:
- **Drip Campaigns going to every plan in October** — I owned the builder and the launch readiness,
  and the adoption is real: 688 accounts have created 1,212 drip campaigns since the July go-live,
  and the runbook I wrote was named the template for future launches.
- **Four engineers measurably more independent** — I coached our newest team member through his
  whole onboarding and a junior from "where do unit tests go?" to clean, test-bearing PRs in five
  weeks. My review comments on their PRs drop from 7–10 to 0–1 within about three months; that
  decline is the point.

## 7. What would help you do your best work over the next six months? *(optional question — answer it anyway)*

I'll be direct, because vague answers to this question haven't moved anything:

1. **Compensation that matches the role I'm actually doing.** I've been at mid-level pay and title
   for over five years while this year operating as the technical lead on the team's two biggest
   projects, with measured outcomes. I'd like a formal compensation and title review this cycle,
   benchmarked against the scope described in this review and the Sydney market — and I'd like the
   outcome, or the concrete criteria and date for it, **in writing**. Recognition in Slack is
   genuinely appreciated; it doesn't compound. Pay does.
2. **The named tech-lead role, not just the work.** I led SMS in practice; I want to lead SMS
   Checkpoints 2–3 (UK/AU sender IDs and the ~250-customer Infobip→Twilio migration) — or the
   Journeys area, where the handover named no successor — with the title attached, so the
   responsibility and the recognition stop living in different places.
3. **A written development plan** with the criteria for the next level and a review date, owned
   jointly with my manager in our 1:1s rather than left to review season.
4. **Clear priorities and limits across the merged team's surface.** In September I carried SMS,
   the AI-DLC experiment and incident response simultaneously, including some very late nights.
   I'd rather we agree explicitly what drops when the plate fills than find out by burning out.
5. **A platform to show finished work** — a regular slot in the team showcase and the agreed
   adoption metrics (the instrumentation now exists) so outcomes are visible without me having to
   be the one narrating them.

---

### Appendix: numbers at a glance (sources: findings-impact-numbers.md)
| Metric | Value |
|---|---:|
| PRs authored / merged (window) | 106 / 86 |
| PRs reviewed for others | 163 |
| Drip: accounts / drips created since launch (all types) | 688 / 1,212 |
| Drip: accounts / drips on the new branching type | 282 / 446 |
| Drip: weekly-adoption step-change at all-plans GA | ~2.6× |
| SMS: discovery → dev-complete | ~2 months |
| Provisioning paths merged | 3 → 1 |
| PR-check compute per push | −69% |
| Projected CI agent-hours saved per year | ~4,850 |
| Production incidents closed end-to-end | 4 |
| Mentees with measured growth | 4 |
