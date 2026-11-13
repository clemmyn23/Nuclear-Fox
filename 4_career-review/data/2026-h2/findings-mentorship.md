<!--
RAW: mentorship deep-dive, run 2026-11-12. Sources: Slack DM crawls (Chris Luong D09UX9Q0AUQ,
Melisa Irmako D0C63EKQKPY, Gen Bruno D089H07T2UB), channel sweeps (#cm-team-boole-dev,
#cm-team-boole-eng-prod), and git.campmon.com API (authored-PR counts by month; review states and
inline-comment counts on every PR of theirs that cng commented on).
Window: Nov 2025 → Nov 2026 (since the last CADD), with pre-window Gen Bruno data for context.
Names teammates — keep internal. The analysis docs should refer to roles.
-->

# Mentorship findings — the four engineers, their growth, and your fingerprints on it

**Headline:** across the CADD window you ran a consistent, measurable coaching loop with four
less-experienced engineers: heavy review + DM + call support early, deliberately stepping back as
they stood up. The pattern is visible in the data: **inline comments per PR fall to near zero over
roughly 3 months per engineer while their PR throughput holds or rises.**

| Engineer | Title | Started | PRs in window (merged) | Their PRs you reviewed | Your review arc |
|---|---|---|---|---:|---|
| Chris Luong ("oolong") | Software Engineer | ~Dec 2025 | 49 (44) since Dec 2025 | 12 (43 inline comments) | Dec–Feb: changes-requested ×3, 4–10 comments/PR → Mar–Apr: clean approvals, 0–1 comments |
| Melisa Irmako | Full Stack Engineer | ~Aug 2026 | 22 (16) | 4 (11 inline comments) | 30 Sep: changes-requested + 10 comments → 5 & 9 Nov: clean approvals, 0 comments |
| Sherry Lotfi | Full Stack Engineer | ~Nov 2025 | 70 (63) | 19 (20 inline comments) | Light-touch throughout; peak 7 comments (Jun), mostly targeted singles |
| Gen Bruno | Full Stack Engineer | (pre-window) | ~119 since Jan 2025 | 28 (16 inline comments) | Peer-mentee: 2 changes-requested ever; deep DM/call support on infra |

---

## 1. Chris Luong — onboarding mentor in practice, Dec 2025 → mid-2026

**The relationship:** Chris joined Team Boole ~Dec 2025. You were his de-facto onboarding buddy:
the DM history is a continuous help channel from his first weeks, and he opens with "Good morning
Clem" dozens of times. It includes at least two live calls ("chris.luong has started a meeting",
2 Feb 2026; "zoom?" → "ye") on top of asynchronous coaching.

**His output trajectory (git.campmon.com):** Dec 9 PRs → Jan 6 → Feb 4 → Mar 6 → Apr 5 → May 4 →
Jun–Jul 8 → Oct 5. 49 PRs, 44 merged (90%). He was publicly co-credited on the Drip Campaigns GA
with you and Fan ("Thank you Clem, Fan and Chris" — TL, 9 Oct).

**Your review arc on his PRs (states + inline comments):**

| Date | PR | Your reviews | Inline comments |
|---|---|---|---:|
| 2025-12-15 | #21609 | 4× commented → approved | 4 |
| 2026-01-16 | #21938 | changes-requested ×2 → approved | 7 |
| 2026-02-25 | #22386 | changes-requested → approved | 10 |
| 2026-03-11/17 | #22487, #22555 | straight approvals | 0 |
| 2026-04-02/15 | #22766, #22903 | approvals | 1, 5 |
| 2026-06-25 | #23685 | changes-requested → approved | 11 |
| 2026-07-23 | #24009 | approved | 2 |

The June spike (#23685) is the exception that proves the coaching: it was the AI-overengineered
locking PR. You told him directly — *"I think your claude way overengineered things"*, *"frontend I
don't like the setTimeout locking implementation… I'm not convinced we need that part at all"* —
then walked him to the simpler computed-check design ("timer is the wrong tool for this job") and
let him implement it. He refactored, asked one clarifying question about React Query invalidation,
and you taught the `mutationKey`/`invalidateQueries` distinction he then verified himself.

**What you actually taught him (all verbatim in the DM):**
- **Schema design:** "you managed to create 3 indexes for a table with 2 columns… that's redundant";
  pointed him at `CS_SequenceCampaigns.sql` as the pattern to copy; explained *why* his
  `CS_CampaignLists` analogy was wrong (29–30 Apr).
- **The deploy pipeline, end-to-end:** when his PR stalled the deploy scheduler (10 Mar), you
  narrated the whole TeamCity chain ("so I'll break down what I'm seeing for you… deploy scheduler
  triggers every 10 minutes… runs every integration test suite… that's why you can see version
  numbers skipping"), validated his rerun instinct, and then coached the *communication*: "message
  heini for closure. Say something like…".
- **Production operations, safely:** CRM Lite stuck-queue triage under supervision (14 Jul) —
  "errrr go to the account and check first… if it's confirmed stuck stuck then yea purge"; SQS purge
  mechanics (18 Feb); putting the SQL into the playbook because "only DBAs can modify prod data"
  (19 Feb). He used his own protobuf-decoding + Claude trick back at you — the skill transferring.
- **Escalation norms:** who the architect is; GDPR question routed to the architect and answered
  with the reasoning (19–20 Feb); "Should really ask Yuri for design stuff"; design feedback with no
  designer → "#html-css or #cm-product-design… dump that article and see what they say".
- **CM engineering standards:** cross-app imports and bundle bloat (explained via the
  `PrimaryAddOnUpsell`/`AudienceBanner` example — *why*, not just *what*), one-component-per-file,
  lint, lock-file hygiene, "shouldn't touch code that isn't relevant to the PR", JS standard docs.
- **AI hygiene (before the org's bot existed):** "can you like go through this and make it less AI
  slop looking… remove unnecessary comments, don't export stuff that's not used" (10 Apr); "do you
  think you can remove the derpy robot comments?" (6 Jul). By July Chris is self-policing token
  spend and prompting styles with you comparing notes as peers.
- **Decision ownership — the signature move:** "tbh you know more about the implementation than me
  at this point… just make a decision and then support your decision" (22 Apr); "exercise your free
  will" (20 Mar); "I don't want to make decisions uwu" (23 Apr — refusing to decide *for* him);
  "in that case you can decide and post the learnings in our team channels" (3 Mar).
- **FF/deploy judgment** (30 Sep): taught the deploy-vs-prod flag heuristic and the risk caveat
  about stale integration tests, ending with "put a note in #deploy-env if it's like a risky FF".

**Growth summary:** by March his PRs pass review clean; by July he's debugging prod queues with his
own tooling and catching your bugs ("did you already handle this bug in your PR? #23903"); by
September he's running FF rollouts with you as a sanity-check only; in October he's one of three
engineers publicly credited on the team's flagship GA.

## 2. Melisa Irmako — structured junior mentoring, Oct–Nov 2026 (ongoing)

Her manager pointed her to you ("Henry would like me to add unit tests… he asked maybe to ask you").
The DM record is a compressed, textbook coaching sequence over ~6 weeks:

- **2 Oct:** BEM naming — linked cssguide.campmon.com, and she reflects "I should of asked and not
  just guess". Same day: you noticed her AI-revised PR replies were "missing bits here and there",
  coached her on reasoning settings, and normalised asking reviewers to elaborate ("we are here to
  help :)"). Then test-writing from zero: pointed her at `SnapshotHeader.spec.tsx`, scoped "two new
  tests: FF enabled renders, FF disabled doesn't", reviewed her first attempt live (casing
  convention, unnecessary `<Router>` wrapper), set the next increment (false case for coverage).
- **6 Oct:** `screen.debug()` technique for diagnosing her A/B test assertion; introduced her to the
  AI review agent as a first-pass reviewer on her PR.
- **9 Nov:** 15-minute Google Meet when she asked for synchronous help.

**Measured change:** her first reviewed PR (#24871, 30 Sep) took a changes-requested and **10**
inline comments from you; #25442 (2 Nov) took 1; #25552 (5 Nov) and #25582 (9 Nov) were clean
approvals with **0**. Her merge record: Aug–Oct had 6 closed-unmerged PRs; in November she is 4-for-4
merged. Five weeks from "where do unit tests go?" to clean, test-bearing PRs.

## 3. Sherry Lotfi — ramping peer, Nov 2025 →

Joined ~Nov 2025 into the CRM Lite work you were feature-leading. You reviewed **19** of her PRs
across createsend.com, RightToBeForgotten, runnerservice and triggereventcatalogservice. Your
style with her was deliberately lighter (she's experienced in other stacks): mostly clean approvals
with occasional targeted comments (4 on #22267 in Feb, 7 on #23544 in Jun, 3 on #23750). In-channel
she repeatedly cc'd you on CRM Lite schema/code questions (Feb–Mar 2026: `CL_ClientCRM` column
renames, custom-fields API, stopping the dev scheduled agent — you were one of the named approvers).
Her throughput roughly doubled over the year: ~4–5 PRs/month in her first quarter to 7–9/month by
mid-2026 (70 PRs, 63 merged in the window), with no changes-requested from you after June.

## 4. Gen Bruno — mid-level peer-mentee on Journeys infrastructure (context: starts pre-window)

28 of her PRs carry your review across 2025–Feb 2026. Only 2 ever took a changes-requested
(#21249, #21295 — Nov 2025, the window's start). The DM record shows the deeper work:
- **The localstack/SQS debugging masterclass (7 May 2025):** you explained the whole
  workflow-instance testing technique — trigger a journey with a long delay step in deploy, "yoink
  that workflow instance from the deploy sqs… feed it into the fake aws that is our local-stack
  sqs" — the technique she then used independently.
- **Pairing calls:** "wanna do end to end testing together? I'll start the zoom in the dev channel"
  (21 May 2025); round-robin call 26 Aug 2025 ("cng has started a meeting").
- **Terraform structure** (Jan 2026): interpreted a reviewer's comment for her, sketched the
  module layout, corrected himself in the open ("or maybe not… I think what you have is right"),
  and sent her a reference PR for SQS-via-terraform.
- **Incident context-filling:** AJ-731 — she asked for card details; you reconstructed the
  context from the incident thread and filled in the task description (31 Jul 2025).
- **Small-but-telling:** BEM class-name fix with the exact corrected string; catching the missed
  call-site in `AgencyPerformanceReportGenerator.cs` within minutes of her push.
Her 2026 record (8–14 merged PRs/month peaks) is the strongest of the four; your role was
unblocking infrastructure knowledge, not basics.

---

## Cross-cutting: what the mentoring style looks like in data

1. **Front-load, then withdraw.** Chris: 43 inline comments over 12 PRs, of which 32 land in his
   first 4 months + the one AI intervention; Melisa: 10 → 1 → 0 → 0 in five weeks. The decline is
   the point: comments stop because the standards transferred.
2. **Teach the why.** Cross-app imports explained via bundle bloat; NOLOCK/distinct-count semantics
   explained via the one-CRM-list invariant; locking explained via "timer is the wrong tool".
3. **Push decisions back.** "Make a decision and then support your decision" recurs with every
   mentee; you consistently refuse to be the decider on their tickets.
4. **Safety rails on prod.** Every prod-touching coaching moment includes a verification step
   first and an escalation path ("only DBAs modify prod", "ask for 👍", "check the account first").
5. **AI hygiene as a standard you set early** (Apr 2026 with Chris, Oct 2026 with Melisa) — later
   institutionalised when the org's AI review bot started quoting your comments ("Reinforcing
   @cng's earlier comment").

## Honest caveats (keep these in the self-review)
- Growth is multi-causal: their own effort, other reviewers (Fan, James, Sam), and team structure
  all contributed. Claim the coaching, not sole credit for their trajectories.
- Inline-comment decline can partly reflect growing familiarity and smaller tickets, not only
  skill transfer. The merge-rate and throughput trends corroborate, so the direction is safe.
- Chris's Sep dip (1 PR) coincides with the team merge and his pull onto other streams — not a
  performance signal either way.
- None of this is a formal mentorship assignment; it's emergent. That's an argument *for* the
  named-TL conversation, not against the evidence.
