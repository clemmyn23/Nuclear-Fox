# Neutral performance analysis — November 2026

Written by an independent reviewer. Advocacy framing in the AI-drafted documents (CADD draft, SMS feedback pack, parts of the findings files) was discounted; only verbatim quotes, timestamps, PR/review counts and measured numbers were weighed.

**Q1 verdict:** You are not underperforming — the primary record (PRs, Slack verbatims, third-party verification sweeps) supports performance at the senior (IC3) bar, clearly above mid, and clearly below staff; but the record also contains real quality lapses and a layer of overclaiming in your own drafts that you should strip before anyone else reads them.

**Q2 verdict:** Your manager's critique is borne out — the evidence is consistent with, not contrary to, "doesn't make enough noise": your highest-value work lives in DMs, PR descriptions and Jira, your credit at the one public moment that mattered came in the replies, and status on your flagship project was re-derived from scratch while you were away because you left no single readable artifact.

---

## Q1 — Level

**Against the mid (IC2) bar:** comfortably exceeded. A mid engineer is given a problem; you were handed goals. The EM started SMS with "Would you be up for taking the discovery piece" (1 Sep DM), and your discovery became the plan the PM adopted, your re-estimate replacing the placeholder. Nobody treating you as mid appears anywhere in the record.

**For the senior (IC3) bar — the primary evidence, not the adjectives:**

- End-to-end ownership of ambiguous work: SMS discovery (7 Sep) → 11 tickets → idempotent provisioning API (#25046) → cross-team API change (Thompson made `registrationInfo` optional, in staging next day, 7–8 Oct, verified) → three provisioning paths merged to one (#25080, 2,264 tests green) → dev-complete 2 Nov → first 3 real customers w/c 2 Nov (Amplitude). The partner team independently found your fingerprints: "Looks like Clem did this work" (4 Nov).
- Judgment under pressure, verbatim: the UCF DLQ triage ("too tired to be touching prod" — asked for a 👍 first; patch fixed 6 of 8 failure modes; TL: "I can't express how great what you've done here is"); the RSS root cause ~1h20m after assignment, customer explanation drafted, verified send 6 days later; the AI-DLC call-out ("gone a bit past the whole 'use ai to save time' threshold") that fed leadership's no-go.
- Multiplier: 163 reviews in the CADD window; two mentees with genuinely measured arcs (Chris: 7–10 comments/PR → 0–1 in ~3 months; Melisa: 10 → 0 in five weeks, 4-for-4 merged in November). Others ask your sign-off before touching prod SMS routing (James, 16 Oct and 4 Nov) and raise your name unprompted ("Clem is looking into it").
- Platform work with a real measurement: PR-check compute −69%/push, faster on 233/233 same-commit pairs (TeamCity, 10 Nov).

**The counter-evidence, engaged honestly:**

- **3 Jul webpack incident.** You were the sole approver on a colleague's webpack 4→5 monolith PR (#23212), approved at 00:06 UTC and merged at 00:07; a missing import broke RSS one-click campaigns with "quite a few support cases." A one-minute approve-to-merge on a build-system change touching everything is a review-rigor failure — and review rigor is exactly the senior duty you're credited with elsewhere. A genuine mark against, not a footnote.
- **6 Nov CI break.** PR #25501 broke TeamCity builds across other teams' projects ("I didn't think it would affect everything, my bad"). Owned and fixed same day — but underestimating blast radius on shared infrastructure is a second instance of the same class of error.
- **SMS schedule.** The slip itself is small (30 Oct target → 2 Nov dev-complete) and the Twilio-side blockers are documented in Twilio's own words. But the EM initiated the 12 Oct check-in and proposed the second engineer; you re-planned well, you did not pre-empt. The vendor-blame framing in the feedback pack also glosses that your own re-estimate of 7–11 dev-days became ~9 weeks elapsed.
- **Credit and role.** On Drip you owned the builder frontend and launch readiness; the backend engine was mostly a peer's, Sam was publicly credited with "tech leading this through to delivery," and the GA announcement's special-thanks named the PM, not you. "Technical lead in practice" is your own label — no one at CM has used it, and the window's one open leadership seat (JS crew captain) went unfilled at a meeting you were absent from. Being handed discovery and having a staffing suggestion adopted is strong senior evidence; it is not a lead role.
- **Overclaiming in your drafts, specifically:** the "1,212 branching campaigns" one-liner is wrong — 446 of 1,212 were branching; 688 accounts / 1,212 drips are feature-level numbers (frontend was yours, send engine wasn't); "four engineers coached with measured growth" is really two (Sherry was light-touch routine reviewing; Gen is a pre-window peer); ~4,850 agent-hours/yr is a projection, and push-to-all-green is currently *worse* than before the Docker switch (488s vs 327s, pool queueing); "no rollbacks" has no independent verification; the "AI bot quotes my standards" rests on one observed instance. None of this is fabrication — every number traces to a source — but the attribution and framing inflate.
- **Tooling share:** ~17 of 59 Jun–Nov PRs are tooling/ops/Docker (~29%), above your own stated ~20% cap, though roadmap work (Drip, SMS, Brand Hub) clearly dominated.

**Against the staff (IC4) bar:** not met, and file 15 says so correctly — impact is tribe-scoped, the deepest architecture calls are ratified by the architecture function, and there is no multi-quarter org-shaping program (Docker builds is the candidate, unfinished). File 16's use of SMASH volunteer work to back-fill the staff case is irrelevant to CM performance.

**Net:** performing at senior, titled and paid at mid. The gap is between title and work, not between work and expectations — with the caveat that two preventable incidents this year sit on the quality line a senior is supposed to hold.

## Q2 — The visibility critique

The record supports your manager, not you.

**Where the work was invisible:**
- Mentoring — your strongest multiplier evidence — exists almost entirely in DMs. It took a private crawl of three DM channels to reconstruct it. Your own CADD draft concedes this: "some of my coaching and decisions live in DMs."
- Drip GA (9 Oct): the announcement credited the PM for "driving the bulk"; your name appears only in replies, shared with Fan and Chris. Nothing in the record shows you surfacing your launch-readiness work to that audience beforehand.
- SMS, 22 Oct–4 Nov: with you on leave, the PM reconstructed the init flow from a staging walkthrough ("which is when I believe we send the region…") and a partner engineer asked "What is `Init`?" about a flow you had designed in the open on 7 Oct. Everything existed — in Jira, PR descriptions and threads — and none of it was readable by the people who needed it. You've owned the fix (a one-page state-of-the-build), which is an admission the critique is right.
- Confluence output fell from 9 pages (Y5) to 3 (Y6) while the work got bigger.
- No adoption dashboard exists for any feature you shipped; the Amplitude numbers were pulled privately on 12 Nov, not published.

**Where it was visible:** you demo at standups, posted "live on all prod DBs" to #cm-sre, posted the merge redirect, and summarize for the team. The gap is not shyness; your visibility runs engineer-to-engineer while announcements and status run through PMs — partly structural (the reorg changed who knows your work), but the DM habit, the missed crew meeting and the missing handover doc are yours.

**Five behaviours, all grounded in things you already do or have drafted:**
1. Before any leave, post the one-page state-of-the-build to the epic and team channel (you committed to this in the SMS pack — do it).
2. Publish the Drip "90 days later" readout with the PM in #cm-product-updates — the numbers are already pulled; today they live in a private file.
3. Move one coaching interaction per week from DM to the team channel or a short Confluence note, as you did with the deploy-pipeline walkthrough for Chris.
4. Ask the PM, pre-launch, how engineering credit will appear in the announcement — you already post to SRE; extend the same move one channel up.
5. Make the asks you've drafted (named TL on SMS Checkpoints 2–3; the Journeys gap) out loud in a 1:1, and show up to the meetings where roles are assigned.

## Confidence and what would change my mind

**Q1: moderately high (senior, not underperforming).** The record is self-assembled, but the peer-verification sweep checked 33 of 34 claims against source threads and corrected the inflations, which raises trust. What would move me: your manager's or EM's own written assessment; evidence the backend peers carried more of SMS/Drip than the PR record shows; more solo-approval incidents; team-relative review/incident data showing peers at the same bar.

**Q2: high (the critique is borne out).** Nearly every exhibit is consistent with it, and your own documents concede the mechanism twice. What would move me: evidence your status updates reached decision-makers and were disregarded, or the manager's verbatim remark showing he meant something narrower.

---

## Addendum — 13 Nov 2026: re-weighed against the meeting-note corpus and Clem's corrections

This analysis was finalised just before [findings-standup-notes.md](data/2026-h2/findings-standup-notes.md)
landed (61 Gemini meeting notes, Sep–Nov) and before Clem's corrections of 13 Nov. Re-weighing:

**What the new evidence moves:**
- "Your updates didn't reach decision-makers" no longer holds at team level. The corpus has him
  speaking in 47 of 61 notes, giving 5 working-software demos, and the EM, TL and PM deferring to
  him by name; the PM relays his estimates to leadership. This meets the exact "what would change
  my mind" condition stated above for Q2.
- "Zero demos at the formal showcases" is literally true but was over-read as a behavioural choice.
  The 27 Oct showcase transcript (re-read 13 Nov) shows the session fell inside his 22 Oct–1 Nov
  leave — and his SMS compliance embed was its headline demo, presented end-to-end by the PM, with
  Alexis and the TL named in the credits and Clem not mentioned once. That is a sharper and
  narrower exhibit than the original: the work reaches stakeholders fine; the person doesn't travel
  with it.
- SMS leave-period confusion: the evidence pack ([sms-embed-feedback-2026-11.md](sms-embed-feedback-2026-11.md))
  documents a staged pre-leave handover and vendor delays acknowledged in writing by Twilio.
  Clem's correction — knowledge transfer was fully carried out to another dev; the delays were
  Twilio's — is supported for the engineering handover. What remains his is the narrower,
  already-owned gap: no single PM-readable build-state page, so status was re-derived in channels
  while he was out.

**Clem's corrections recorded, with verification status:**
1. *"Team demos are agreed skipped events… calendared dates landed at inconvenient times."* —
   Conflicts with the two in-window notes (10-13 and 10-27 both ran, with named demoers). Possibly
   true of other occurrences; unresolved. Use neither framing in a submitted document until the
   dates are reconciled.
2. *"Drip adoption numbers are constantly monitored by PMs."* — Plausible (Amplitude project
   226438 charts exist); the sweep verified only that no shared org dashboard exists. The bullet
   above ("numbers pulled privately, not published") overstated; "nobody watches adoption" was
   never supported.
3. *SMS KT complete / delays were Twilio's* — supported (see above).

**Revised Q2 verdict:** the critique narrows from "doesn't make enough noise" to "the noise lands
engineer-to-engineer; in stakeholder venues the work is narrated by PMs." Confidence drops from
high to moderate. The five recommended behaviours stand — the 27 Oct transcript is now the best
argument for #2 and #4 (publish the adoption readout; agree pre-launch how engineering credit
appears), because the mechanism it shows is credit flowing by default to whoever presents.

### Second pass, 13 Nov — the 12-month sweep ([data/findings-meeting-notes-12mo.md](data/findings-meeting-notes-12mo.md))

Four agent sweeps extended the corpus to Nov 2025 → Nov 2026 (Drive + Calendar, with Slack/Zoom
verification). Three further moves:

1. **The showcase venue barely existed — Clem's correction is supported.** Of ~20 calendared team
   demo slots in 12 months, 4 verifiably ran and one was explicitly skipped on transcript ("Thank
   you for letting everyone know that there's no demo", 29 Sep); the Boole series was deleted and
   recreated under 4 recurring-event IDs with ≥6 fortnights missing entirely. "Zero demos at
   showcases" is therefore not a behavioural finding: there was close to no venue.
2. **He did present cross-team — on Zoom, where Gemini can't see.** 12 May 2026, JS Crew: "Clem is
   going to be talking about the React Flow package and how team Boole have been trialing it
   recently with their work on Campaign Series" — recorded, link shared in #javascript. He also
   runs and records the JS Crew series itself from Sep 2026, and the team's bug-bash forms (May
   2025, Dec 2025, Mar 2026/CRM Lite with Jira triage) are owned by his account.
3. **The critique sharpens into its final, narrow form: in rooms above the team, his work is
   narrated by others.** At the 4 showcases that ran, Drip was demoed by his mentee (21 Jul) and
   his SMS embed by the PM (27 Oct, during his leave, unnamed). At the Weekly Technology Meeting,
   Drip credit went to Fan Li and Melisa, SMS to the Thompson team, and JC-411/Docker builds was
   never attached to his name; his only org-wide mentions are thanks for service to others' work
   (Biome PR testing, AI-DLC driving) plus one "rockstar" welcome — and the 27 Aug Gemini summary
   literally dropped his garbled "CLM" from the credit list. The 1 Oct promotions list (three
   peers to senior) does not include him.

**Final Q2 verdict:** the broad reading ("doesn't demo, hides work") is unsupported across the
full window. What is supported, with high confidence, is narrower: his work travels upward
without his name attached, because others hold the microphone in the venues that matter and no
published artefact (readout, dashboard, byline) anchors the credit to him. The five behaviours
stand, re-aimed: take the presenter seat for his own features, publish the Drip/JC-411 readouts
under his own byline, and make the asks to the people who hold the microphone.
