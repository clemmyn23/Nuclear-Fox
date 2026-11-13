# Standup / meeting-notes findings — Clement Ng, 2026-09-01 → 2026-11-12
<!-- Method: Google Drive search for Google Meet "Notes by Gemini" docs, read via Drive connector (summary + transcript where present), Clem-only extraction via 5 parallel subagents. Corpus: 61 docs read — 39 Mitnick standups, 7 Stand up + Sprint Review + Planning, 2 Team Mitnick demo sessions, 4 Javascript crew meetings, 6 Thompson - SU (SMS shared-services standup; pre-filtered with fullText 'Clem' from 44 docs in window), 1 SMS - Catch up, 2 Brand Hub Edit Kit sessions. CAVEAT: Gemini notes are AI-generated — summaries can misattribute, and transcripts garble his name (Clen, Clam, Clim, Clint, CLM, CL, C); quotes are machine transcription, not certified verbatim. [summary]/[transcript] marks the source layer; [Inference] marks my reading. -->

## What the standups show, in one paragraph
Across 61 Gemini meeting notes Clement speaks in 47 and is the named owner of whichever stream he is on: UCF incident (early Sep), AIDLC Stream A (late Sep), the SMS Twilio Compliance Embed end-to-end (Sep–Oct, including guest membership of another team's daily standup as Mitnick's integration owner), and Brand Hub 1A (Nov). He gives working-software demos inside standups (Oct 19 end-to-end Twilio embed; Oct 13 in Thompson's standup) but gave zero demos in the two formal "Team Mitnick - demo" showcase sessions in the window. Third-party references are overwhelmingly deferral and credit — Shenny routes staffing around him, Karthik defers SMS scope/ordering to him, Russell thanks him publicly at least five times — and the only negatives are mild waiting-on nudges (Sep 24, Oct 8, Nov 2) plus his own self-deprecation ("sorry it's getting delayed again"). He also carried recurring team chores: board-master/monitor duty for whole weeks, backlog triage, and cross-reviewing as the team's JS-crew reviewer.

## Demos / walkthroughs given (5; none in formal demo sessions)
- **2026-09-04, Mitnick standup** — live teach-in on the UCF/SQS error queue: pulled stuck messages, decoded JSON with his `msg.sh` tooling, reconstructed cache keys, explained kill-vs-redrive rules. Russell: "Thank you very much Clement for looking at those raising it… and teaching us how to deal with them." [transcript]
- **2026-09-14, Thompson - SU (other team)** — walked Team Thompson through the SMS provisioning flowchart at Karthik's request: "this is the existing SMS provisioning process we have…" [transcript]
- **2026-09-15, Sprint Review** — drove the full SMS embeddable discovery walkthrough: presented and story-pointed every card he'd created, solo. Shenny: "Clem, maybe you can drive… you'll be the only engineer working on these cards." [transcript]
- **2026-10-13, Thompson - SU** — live screenshot demo of COM-1700: "I made the call to share services to buy the number… the call to get the token… you can see the form rendering in the page." [transcript]
- **2026-10-19, Mitnick standup** — end-to-end demo: CM API locally, SMS setup screen, Twilio compliance iframe, token/inquiry wiring, status polling, number purchase, profit/non-profit form variants. Russell: "lot of progress so far, CL[em]." [transcript/summary]
- **Formal "Team Mitnick - demo" sessions (10-13, 10-27): no demo *by* Clement in either — but the 10-27 transcript (re-read 13 Nov) reframes it.** The session fell inside his 22 Oct–1 Nov leave, and his SMS compliance embed was its headline demo — presented end-to-end by the PM (Karthik), who named others in the credits ("PM, uh, Alexi[s] have been actively working on this, rusty obviously supporting us") and did not mention Clement once. On 10-13 he demoed COM-1700 in Thompson's standup the same day; the Mitnick session's demoers were Fan Li, Melisa, Russell, Karthik. [Clem's correction, 13 Nov: team demo sessions are "agreed skipped events by the entire team" when the calendared dates land at inconvenient points in the dev cycle. RESOLVED, same day, by the 12-month sweep (../findings-meeting-notes-12mo.md §1): supported — the 29 Sep demo was explicitly skipped on transcript, the Boole series was deleted/recreated under 4 recurring-event IDs with ≥6 fortnights missing, and only 4 of ~20 calendared slots verifiably ran. The two sessions above are the exceptions, not the rule.]

## Decisions made / owned out loud
- **09-04** — SMS delivery estimate on the spot for Karthik: "I think it's delivered in one sprint with test" (logged as "80% confidence"). [transcript]
- **09-11** — pushed back on a proposed spike's feasibility: "We don't have a token… the token is from the other team"; offered the fallback "Maybe just render the blank box and page." [transcript]
- **09-15** — created the SMS embed epic + cards and self-pointed them; raised the theming gap Karthik had no answer for. [transcript]
- **09-29** — sprint scope cuts voiced by him: "get rid of testing, get rid of the cleanup, get rid of the theming… We keep the spikes"; re-pointed spike 1648 3→5 ("Put it to five"). [transcript]
- **10-07** — scoped the ask to Thompson: "should be small. We're just asking them to make some of the fields optional in the existing endpoint." [transcript]
- **10-19** — triage he drove: session-ID storage unnecessary ("team Thompson is managing… storing the session"), resume/submit "Might come for free" → closed redundant cards, merged status-display + lifecycle cards. [transcript]
- **10-21** — challenged Karthik's feature-flag proposal: "New feature flag for allowing what?"; answered region SME questions (tied to signup IP, customers "Can't even change" it). [transcript]
- **11-04 (Brand Hub inception)** — with Russell, added the feature-flag requirement to backend data-layer slices (tickets 93/94): "That's a good idea… maybe on the UI… squeeze it in." Became an Aligned decision. [transcript/summary]
- **11-11** — set the Brand Hub V2 feedback process when Jarrod asked "Clement question for you too": "This is a thread in Slack… post all the screenshots there and then we can respond"; Karthik endorsed; became the team decision. [transcript/summary]

## Incident & bug pickups
- **09-02 → 09-09, UCF (update-custom-field) errors** — raised the open OA himself ("There is an OA in the public channel. Anyone look at it?"), triaged the 81M-subscriber agency live, diagnosed the root cause ("the contact attribute service was returning two rows… instead of one… our custom field thingy doesn't handle two and then so it dies"), shipped the fix: "the UCF bug is fixed and no more errors" (09-09). [transcript]
- **09-23** — distinguished Chris's new UCF-adjacent alerts from his earlier fix ("This is different. This looks different."); Chris: "This might be good for CL to take a look at." [transcript]
- **09-30** — relayed an alert he caught in Thompson's standup (SMS account raising alerts in shared-services channels) to Mitnick's parking lot. [transcript]
- **10-09** — reported/diagnosed the dead GitHub alert bot ("It was still working this morning, but it was like delayed. Now it's dead."); Russell escalated to tech-leads off the back of it. [transcript]
- **10-16** — chased a Microsoft vendor issue: "still under investigation after I chase them up." [transcript]
- **11-03** — raised two dashboard items live while board master (oil-brand SMS access setting; campaign-send confirmation email not sending) and got them triaged. [transcript]

## Mentoring / unblocking others
- **09-17** — fallback reviewer for Melisa while Chris away: "Chris suggested just to reach out to Clement for the comments he's made." [transcript]
- **10-01** — gave Rowena his test client for SMS testing ("you can use mine"); joined the parking-lot session creating a hex test client. Russell thanked "Fan, Chris, and Clement… getting involved in that area". [transcript/summary]
- **10-02** — sent Melisa a unit-test example: "Clem has been helping me by sending me… an example" (Melisa). [transcript]
- **10-02 → 10-21, Alexis onboarding** — unblocked Alexis onto the embed front end ("you can replace my hello world placeholder page"), reviewed the embed (Alexis: "reviewed by Rusty and Clem. Thank you very very much"), flagged endpoint changes ("I moved them from get to post"), and ran a structured pre-leave handover. Alexis, 10-20: "Clem has a very awesome bedrock for me to build on. So, not much confusion." [transcript]
- **11-09** — volunteered to help Melisa's local-rendering blocker when Russell asked "Is anyone in a good spot to help out?"; Shenny: "Oh, thanks CL." [transcript]
- **11-10 (JS crew)** — drove the meeting's only action item with review feedback on David's Playwright skill: "Compared to manual, it's like a huge improvement… compare to other automated tests, it's really long. Make it shorter." [transcript/summary]
- Recurring: team's crew reviewer ("my stuff… ready for team review. But I'm crew", 11-09); board-master/monitor for full weeks (Sep 23–25, Nov 2–6). [transcript]

## SMS Twilio Compliance Embed — week by week (compressed)
- **w/c 09-01** — assigned discovery; Shenny: "We were thinking he would be great to jump on this one"; Karthik: "you and Clement for you primarily." [transcript]
- **w/c 09-08** — updated spec doc 1619; grilled Karthik on theming/tokens; invited into Thompson standups as Mitnick's front-end owner. [transcript]
- **w/c 09-14** — joined Thompson ("we have a guest Clement"); Billy's consensus that CM API sits with Mitnick and "Clement Ng and Karthik… will investigate and handle the implementation"; discovery finished, epic + cards created and pointed; feature flag created ("none reusable… which is why Clement has created a brand new" — Karthik). [summary/transcript]
- **w/c 09-21** — stalled by AIDLC workshop; "no progress. I am still writing the routing code"; Karthik's nudge: Thompson "waiting for Twilio on the alpha numeric or waiting for you on this one" (09-24); resumed 09-25 ("I'll have a PR up later today"). [transcript]
- **w/c 09-28** — monolith VM build pain ("not really building because it's running out of memory"); split PR into backend/frontend; redid AI-generated gating checks manually ("AI was confusing… I have a much clearer idea if I do it manually"). [transcript]
- **w/c 10-01** — 1646 PRs merged to staging; Okta-on-VM outage diagnosed; picked up spike 1648. [transcript]
- **w/c 10-05** — spike done; asked Thompson for an optional-fields endpoint; broke CM API into "tiny cards"; skeleton PR; crew review moved new endpoints to .NET Core. [transcript]
- **w/c 10-12** — 1700 merged ("all set up in 1700… I shouldn't be touching the endpoint shape anymore"); 1701 tested locally ("It posts a slack channel. It insert stuff into the database"); demoed end-to-end in Thompson standup; committed to the Oct-30 target despite leaving on the 22nd. Shenny: "we've been working with team Thompson and Clem. Amazing work so far." [transcript]
- **w/c 10-19** — full demo in Mitnick standup; 1701+1699 merged "up to production this morning"; 1733 alphanumeric iterated "with [Claude] code"; proactive handover ("feel free to take over. I will try to leave a lot of notes in the PR"); self-reported stress before wedding leave — Russell took a review card "so that we don't put too much on Clem". [transcript]
- **10-22 → 11-01, on leave** — 1733 moved to done in his absence; Karthik testing from "clim's wiki"; 10-28: "we don't have Clem around to confirm that" (Infobip/sender-ID question); 11-02 Alex Lai (Thompson): "I was blocked by C[lem], but I just merged it this morning anyways." [transcript]
- **w/c 11-02** — back jet-lagged; UK alphanumeric removal "design is done. I got approved by Greg" — merged/deployed (11-05); tasked at SMS Catch-up with SMS-experience cleanup + Agora automation (with Karthik, Alexis); Karthik shields his time on the Twilio theme bug: "no additional time needs to be spent on it by Clement." [transcript/summary]

## Drip / Brand Hub / Docker / other streams
- **Greylog migration (Sep)** — metric service off Greylog 09-09; SMS greylog card done 09-17, completing the journeys greylog epic — Shenny: "thank you Clement for taking up the SMS one that's done done too." [transcript]
- **AIDLC Stream A (Sep 23–28)** — drove Bedrock code generation through the units, overnight runs ("I spent like a whole hour fixing it"), PR out of draft 09-28. Russell to Jarrod (PM): "Clem has bravely been going through all that. Thank you Clem taking for the team." Also Russell's welfare check: "You were up way too late last night doing this. Are you okay?" [transcript]
- **Docker builds (Oct)** — "started my new pet project… move everything to docker script… I'm just gonna let AI do everything" (10-09). [transcript]
- **Brand Hub 1A (Nov)** — designated to unblock the stream on day one back (Shenny, 11-02 tech disc: "with Clement available for tomorrow… he can potentially look at the front end… color picker"); picked up FE with mock data 11-03; data-layer + UI tickets credited to him in the 11-04 inception summary ("Clement handles the data layer and UI tickets for color editing and image deletion"); merged to prod overnight by 11-06 ("Thank you, Clam. Awesome. Good progress." — Shenny); three stacked PRs for team review 11-12; agreed to take the 1-pt Brand-Hub-as-core-feature tech discovery (1822) and COM-1795 ("I'll let you Clement do it" — Jarrod). [transcript/summary]
- **AI adoption** — initiated the "Can we send Claude epics?" discussion (11-04) that became his action item (test an epic through Claude, review card by card); consistent verify-first stance: "I still don't trust Claude completely." [transcript]

## Third-party references (positive AND negative)
Positive / deferral / credit:
- **09-03** Karthik: "It's already assigned to Clement both of those and he's working on it." [transcript]
- **09-04** Russell: "Thank you very much Clement for looking at those raising it… and teaching us how to deal with them." [transcript]
- **09-07** Russell (support-channel migration ping Clem did unprompted): "Thank you, Clement, for doing that. Really appreciate it." [transcript]
- **09-14** Karthik: "Clem you you're in a good position to pick that up too, right?" (CM API); Billy/Tim consensus assigning CM API implementation to "Clement Ng and Karthik". [transcript/summary]
- **09-15** Russell on his cards: "small enough… well described enough. People can pick them up… thanks for doing that." [transcript]
- **09-28** Russell to the PM: "Clem has bravely been going through all that" (AIDLC leftovers). [transcript]
- **10-02** Russell: "Clem called this out during one of the PRs… it was really good of you, Clint, to raise it" (feature-flag removal caught in review). [transcript]
- **10-13** Shenny: "we've been working with team Thompson and Clem. Amazing work so far." [transcript]
- **10-16** Karthik: "Clem, thank you so much for all the updates." [transcript]
- **10-20** Alexis: "Clem has a very awesome bedrock for me to build on." [transcript]
- **11-02** Shenny deferring staffing: "I think you're the one that would be jumping on to either one of those two." [transcript]
- **11-05** Russell: "you've just come off the plane… and you jumped straight into BrandHub after working on SMS… just been really impressed with how you picked that up and run with it." [transcript]
- **11-10** Shenny sequencing others' work so it "doesn't block… stuff that Clem is doing there" — treated as critical path. [transcript]

Negative / waiting-on / chasing (all mild; no criticism of quality found anywhere in the corpus):
- **09-07** Russell probed whether to take the unstarted greylog card off his plate (Clem self-flagged: "I have not started"). [transcript]
- **09-24** Karthik: Thompson "are waiting for Twilio on the alpha numeric or waiting for you on this one." [transcript]
- **09-29** his own apology: "sorry it's getting delayed again" (SMS gating build issues). [transcript]
- **10-08** Shenny: "we've got no status changed in a few days here on 1648… anything can help with the unblocking?" [transcript]
- **10-28** Karthik: "I'm a little concerned because obviously we don't have… Clem around to confirm that" — [Inference: a bus-factor dependency on him, not a criticism]. [transcript]
- **11-02** Alex Lai (Thompson): "I was blocked by C[lem], but I just merged it this morning anyways" (PR pending while Clem was on leave). [transcript]
- **10-21** self-reported: "I'm stressed out packing and then I'm trying to get SMS over [the line]" — Russell responded by offloading a review card. [transcript]

## Stats
| Metric | Count |
|---|---|
| Notes read | 61 (39 Mitnick SU, 7 sprint reviews, 2 demo sessions, 4 JS crew, 6 Thompson SU†, 1 SMS catch-up, 2 Brand Hub) |
| Notes where he speaks | 47 |
| Notes where he is only mentioned (incl. present-but-silent) | 9 |
| Notes with no mention | 5 (incl. BOTH formal demo sessions) |
| Demos / walkthroughs given | 5 (all in standups/reviews; 0 in formal demo sessions) |
| Action items assigned to him (incl. joint) | ~55 (Sep 12, Oct 18, Nov 10, sprint reviews 4, Thompson/Brand Hub 11) |

† Thompson corpus pre-filtered: 6 of 44 Thompson - SU docs in the window mention him; he attended 4 as the guest SMS integration owner.

## Visibility read
This corpus mostly weakens the "doesn't make enough noise" critique at team level: Clement speaks in 47 of 61 notes, demos working software repeatedly, voices scope and triage decisions out loud, and his updates demonstrably reach decision-makers — the EM (Shenny), TL (Russell) and PM (Karthik) all defer to him by name, and Karthik relays his estimates and findings to product/leadership ("give me some kind of a high level estimate" for the leadership team, 09-28). Where the critique retains force is venue and register: he gave zero demos in the two formal "Team Mitnick - demo" showcases in the window — his demos land in daily standups and another team's standup, where the audience is people who already know his work — and his self-presentation runs understated-to-apologetic ("sorry it's getting delayed again"; "I'm so sorry" for jet lag) while his wins are usually narrated by others (Russell, Karthik, Shenny) rather than claimed by him. [Inference] The evidence pattern is high substance, high within-team visibility, low self-promotion in stakeholder-facing ceremonies.
