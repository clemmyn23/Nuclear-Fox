# SMS Twilio Compliance Embed — feedback & evidence pack (Nov 2026)

> **Purpose:** the receipts for the retro / a 1:1 with the EM-TL. The delays and churn on this
> project were caused by the external vendor and by status being re-derived from scratch instead of
> read from the artefacts I left — not by missing engineering work or missing handover.
> **This is the evidence version. Don't send it as-is** — the "What I'd actually say" section at the
> bottom is the sendable form. Every claim below has a link or timestamp.

---

## 1. What I delivered, when (all before or on time)

| Date | Delivered | Evidence |
|---|---|---|
| 7–15 Sep | Discovery + tech audit, scope, 11 tickets, re-estimate 7–11d vs the 5–8d placeholder | Confluence COMPOSE/2451767325; PM's proposal adopts it |
| 7–8 Oct | The "chicken-egg" init-flow problem **identified, raised with Thompson, and resolved** — `registrationInfo` made optional, in staging next day | #cm-thompson-support thread, 10-07 |
| 9–14 Oct | Idempotent provisioning API (region check before purchase, 409=continue, typed errors) | [#25046](https://git.campmon.com/Freshview/createsend.com/pull/25046) |
| 12 Oct | "SMS embed token grab is working" — init flow **tested in staging with the PM watching** | team channel, 10-12 |
| 12–20 Oct | 3 duplicate provisioning paths merged into 1 (2,264 tests green); enabled-status gating | [#25080](https://git.campmon.com/Freshview/createsend.com/pull/25080), [#25079](https://git.campmon.com/Freshview/createsend.com/pull/25079) |
| 16 Oct | TFN delete/re-provision edge case found and worked **directly with Thompson (Steven)** | DM, 10-16 |
| 19–21 Oct | AU alphanumeric sender IDs; per-brand theme IDs (Direct/Agency) wired; post-submission notification designed with Thompson; **live demo at standup** | [#25163](https://git.campmon.com/Freshview/createsend.com/pull/25163); team channel 10-19→21 |
| 20 Oct | **"The endpoints are in staging. PRs have been merged."** | team channel, 10-20 |
| 21 Oct | Pre-leave handover: *"This one is pending csharp review. Pls help move it along tomo when I'm away. Thanks team"* — remaining work split so Alexis could build on COM-1700 | team channel, 10-21 |
| 2–5 Nov | Dev complete (US/CA TFN + AU alpha); PM: *"in full glory! Great work Clem, Alexis!!"*; cleared for real customers | 11-02 → 11-05 |

I was on leave ~22 Oct–1 Nov. Everything above the line was done, in staging, demoed, and handed
over before I left. First 3 real customers were provisioned through the embed in its first week
live (Amplitude `Set Up SMS`, w/c 2 Nov).

## 2. The delays were external — Twilio's own thread says so

All in #ext-campaignmonitor-twilio, mostly the PM escalating (credit where due — he pushed hard):

- **Alphanumeric was a pilot product, not a late integration by us.** Twilio, 4 Nov: *"Compliance
  Embeddable purely isn't supported anywhere right now. Australia is a pilot program"* (UK: console
  only, roadmap 2027). Our side had asked for alphanumeric docs since **16 Sep** ("The deck says
  it's a pilot project").
- **Twilio hadn't actually enabled our accounts.** 27 Oct, staging returned
  `404 /v1/SenderIdRegistrations not found`. Twilio (Mya): *"Initially only the CM Group was
  enabled. On Thursday, I enabled the remaining dev accounts. **I apologize for the delay and
  frustration.**"* — three weeks after the 13 Oct request, despite a July email saying the accounts
  were enabled. This happened while I was on leave; it was never ours to fix.
- **The Agency ThemeSetId bug is Twilio's, acknowledged by Twilio.** 3 Nov (PM): *"ThemeSetId error
  for Alphanumeric — Mya, we discussed on an email thread and **you acknowledged that there is an
  issue with our Theme**."* 4 Nov (Twilio): *"I followed up with the team this morning and they
  will resolve this as soon as possible."* ThemeSetIds were requested 24 Sep–2 Oct via Twilio's
  Google-Form process (their stated ETA: ~10 days; 1 Oct PM: "It's been over 2 weeks and I have had
  to keep our engineers on standby"). My code had per-brand theme support wired by 21 Oct —
  blocked on their asset, and the PM himself logged it as "not blocking us" (1 Oct).
- **No e2e test support from the vendor.** 31 Oct, Twilio: no coordinated ISV testing
  ("349 ISVs successfully test over time with the regular process") — so "how does rejection look"
  could not be verified before launch no matter what we built.
- **Whitelabel T&C/Privacy gap:** raised by us, deferred by Twilio to **Q2/Q3 2027**.

## 3. The 4 Nov thread — settled work re-asked as if it were open

[The thread](https://campaignmonitor.slack.com/archives/C08LTFG8RQB/p1793749282892569), annotated:

- The PM asks Thompson to confirm whether init creates the customer record before buying the
  number. Thompson's engineer: *"What is `Init`?… I'm not exactly sure what the CM code does."*
- This exact flow was **designed in the open on 7 Oct** (the chicken-egg thread, with Thompson),
  implemented in #25046, **tested in staging together on 12 Oct**, and documented in the Jira cards.
- It resolves only when Steven reads the code: *"it looks like it does. Looks like Clem did this
  work"* — and I confirm from the thread: *"yea we do that. create the customer in SS, buy the
  number. start the embed session, all in the first call."*

No harm done to the system — but this is the mechanism by which "confusion" becomes "attributed
delay": a settled decision, re-opened in a channel where the people who settled it weren't asked
first, leaves the written impression that the state of the build was unknown. Multiply by the
Twilio threads and the project *reads* chaotic even though the engineering landed on time.

**Related pattern, same week (22 Oct, the day I left):** the status update posted to two channels
reconstructs the flow from a staging walkthrough ("which is when **I believe** we send the
region…") — the flow was in the tech audit and the PR descriptions. Re-deriving state from the UI
instead of the artefacts invites exactly the questions that followed.

## 4. My misses — owned, for credibility

- The discovery doc originally said Twilio didn't support alphanumeric; the PM corrected it and
  Twilio enabled it the same day (2 Oct). Mine.
- A reviewer caught endpoints duplicated in legacy + netcore in #25046; fixed that morning. Mine.
- 18 Sep: "I might have underestimated the work" — the original placeholder was mine to re-set, and
  I did re-set it (7–11 days), but the 30 Oct target still slipped to 2 Nov dev-complete. Shared.
- I could have left one **single-page "state of the build"** doc on 21 Oct (what's merged, what's
  in staging, what's blocked on Twilio, who owns what while I'm out). Everything in it existed —
  but spread across Jira, PRs and threads. That's the gap that let status be re-derived.
- The standup record shows two concrete costs of that gap while I was on leave: a Thompson PR sat
  blocked on my review (*"I was blocked by C[lem], but I just merged it this morning anyways"*,
  2 Nov) and the PM had a question only I could answer (*"we don't have Clem around to confirm
  that"*, 28 Oct). Same root cause, same fix: the build-state doc plus a named review delegate.

## 5. What I'd actually say (sendable version — retro or 1:1)

> A few process observations from the SMS embed, now that it's live:
>
> 1. **Our delays were vendor delays, and we should name them that way.** Account enablement
>    (3 weeks, apologised for by Twilio), the Agency theme bug (acknowledged as theirs), UK embed
>    (doesn't exist — pilot program), and no vendor e2e test support. Engineering was dev-complete
>    on the code we control before my leave, and the first real customers went through in week one.
>    When we report timeline slip, the cause should travel with the number.
> 2. **One source of truth for build status.** Questions about what the init call does, or what's
>    in staging, kept being re-asked in channels after they were settled in Jira/PRs/threads —
>    including while I was on leave. I'll own this: before my next leave I'll post a one-page
>    state-of-the-build. In return, I'd ask that status questions go to the epic (or to me/Alexis)
>    before being posted to partner-team channels as unknowns — re-deriving the flow from staging
>    walkthroughs is how settled decisions started looking like open risks.
> 3. **Keep the escalation energy** — the pressure on Twilio in #ext-campaignmonitor-twilio was
>    excellent and is the main reason the external blockers cleared at all.
>
> I'm raising this because the project was a success — discovery to real customers in ~9 weeks
> against a vendor pilot — and I want the record to read that way, and the next one to be smoother.

## 6. If it comes up in a review conversation (one-liner)

> "Every deliverable on our side was merged, in staging and demoed before my leave, with a named
> handover. The three things that slipped — account enablement, the Agency theme, UK — were all
> Twilio-side, two of them acknowledged by Twilio in writing. I'll take one improvement: next time
> I'll leave a one-page build-state doc so status never has to be reconstructed."
