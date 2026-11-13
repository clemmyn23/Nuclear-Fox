<!--
RAW: name-mention sweep, run 2026-11-10. Searched Slack for "clem" and "Clement" in OTHER people's messages
(-from:U01SKCA6MHC), 2026-05-28 → 2026-11-10. Read-only.
About 463 hits examined, ~230 unique, ~30 relevant and new. Names teammates.
Search method: a full "clem" pass sorted by timestamp (9 pages) and again by score (4 pages), plus "Clement" and topic
combinations. Timestamp paging alone missed some messages. False positive: a customer surnamed Clement.
-->

# "Clem" name-mention sweep (2026-11-10)

## 1. Praise and recognition
- **Drip GA, #cm-product-updates, 2026-10-09.**
  - Shenny (EM): "huge props to the awesome engineers who worked on this @blacksmith @Fan Li and @oolong" — https://campaignmonitor.slack.com/archives/C9U16V76E/p1791516056538239
  - Russell (TL/manager): "These guys are the real heroes behind this :hero: Thank you Clem, Fan and Chris for all the hard work involved" — https://campaignmonitor.slack.com/archives/C9U16V76E/p1791516150615879
  - Caveat: the PM's announcement "Special thanks" list doesn't name Clem.
- **People Team mentorship invite, DM, 2026-08-07.** John Cheng (People Team): "I thought of you as someone who could really benefit from (and contribute to) these kinds of conversations, whether as a mentee, a mentor, or both." — https://campaignmonitor.slack.com/archives/D0BC8DST8E7/p1786060789741099
  - 08-26: also invited to the Speed Mentoring Program.
- **Russell (DM).**
  - 08-20: "I wanted to say that I am really looking forward to getting to work with you again." — https://campaignmonitor.slack.com/archives/D01V797FL6L/p1787191214267979
  - 09-30: "Awesome Clem!!! Well done." Clem had fixed a local CmAPI.NetCore setup problem. — https://campaignmonitor.slack.com/archives/D01V797FL6L/p1790748980757149
  - 09-04: "Thank you Clem - that'll be a good win for us" (UCF patch). — https://campaignmonitor.slack.com/archives/C02AMHMB3G9/p1788496390064479

## 2. Asked to own, decide, or be the go-to person
- **Sam (Boole TL), #cm-team-boole-eng-prod, 2026-08-10.** On a customer's CRM Lite suppressed/GDPR view: "I think clem implemented that work, we can have a chat with him tomorrow". Clem answered while on leave. — https://campaignmonitor.slack.com/archives/C028YGQLACS/p1786339022809729
- **Jay Chen, DM, 2026-08-25.** Asked Clem to confirm it was safe to raise drip MAX_SEQUENCE_NODES from 30 to 60. — https://campaignmonitor.slack.com/archives/D08S8017GKD/p1787625888400129
- **Chris Luong, #cm-team-mitnick-dev, 2026-09-04.** On a microservices/Datadog architecture diagram: "(may need Clem to review this)". — https://campaignmonitor.slack.com/archives/C02AMHMB3G9/p1788506108573109
- **James Dunlop asked Clem's sign-off on prod SMS routing.**
  - 10-16 DM: routing the compliance-embed endpoint 100% to netcore. — https://campaignmonitor.slack.com/archives/D01T6URQ5M5/p1792108076107739
  - 11-04 group DM: removing the legacy route. — https://campaignmonitor.slack.com/archives/C0CEP0S1QG2/p1793755843898759
- **Matthew Nicholls (DevOps).**
  - 11-05 #devops: "DevOps is probably closest to the right place for teamcity builds as code". — https://campaignmonitor.slack.com/archives/C4AP41JA0/p1793856500066689
  - PR #25501 (JC-413): "Interested in how this plays out Clem".
  - 11-10: LGTM. — https://campaignmonitor.slack.com/archives/C4AP41JA0/p1794289151398859
- **James, #deploy-env, 2026-11-06.** "If the only failing builds are the (new) 'front-end merge' checks - you can ignore them and merge. Clem is looking into it." — https://campaignmonitor.slack.com/archives/C57AD89RT/p1793932690433869
- **Russell, 09-09.** Thanked Clem for legacy Journeys guide knowledge: "Thank you heaps Clem! That's great info". — https://campaignmonitor.slack.com/archives/C029VG5MEGM/p1788916682710699
- **Local dev help.**
  - Rowena 10-08: local proxy → stopped IIS site; "Thanks clem". — https://campaignmonitor.slack.com/archives/C02AMHMB3G9/p1791432833054599
  - Also asked: Alexis 10-02, Chris Luong 09-30 and 07-14, Sam 07-29.
- **Mitnick Slack Monitor Roster** (09-21, 11-02). About 20 alert channels, incl. #campaign-sequence-alerts and #sms-compliance-alerts. — https://campaignmonitor.slack.com/archives/C029VG5MEGM/p1793573400537299
- **Innovation Sprint demo presenter.**
  - EM plan 06-04: "Demo - Fan + Clem + Sherry (maybe)". — https://campaignmonitor.slack.com/archives/C0B396Y34SD/p1780548025875499
  - EM 06-23: "are you ok to do today's demo?"
- **Russell, 10-01.** "inspect the PRs that Clem put together, merge them in, test in the deploy environment…" (AI-DLC Stream A handover). — https://campaignmonitor.slack.com/archives/C029VG5MEGM/p1790832394815639

## 3. Customer and business impact
- Nothing materially new beyond the peer sweep. On the drip GA thread, a CS/sales person asked for a customer walkthrough video.

## 4. Negative or critical
- **07-03 PagerDuty "RSS One click campaign incident".**
  - Cause: PR #23212 "Update monolith build from Webpack 4 to Webpack 5" (author Christopher Wright). Clem was the **sole approver** (approved 00:06 UTC, merged 00:07 UTC).
  - Fix: PR #23795 by Oliver Toon (missing Spinner import). "Quite a few support cases."
  - SRE: "I am going to add Chris and Clem as reviewers to the fix PR".
  - Fixed that night by SRE and others; no blame.
  - Link: https://campaignmonitor.slack.com/archives/G5GDKDV6F/p1783080085203169
- **EM SMS schedule check, DM 10-12.** "there's quite a few cards remaining so am wondering if we need to push it out… Would it help if we got Alexis onto it too?"
  - She asked for points on COM-1699/1701/1702. Clem split the work so Alexis could build on COM-1700.
  - Target 10-30; dev-complete 11-02.
  - 10-20: she asked him to consolidate COM-1651/1652.
  - Link: https://campaignmonitor.slack.com/archives/D02UZBV5L83/p1791781277322609
- **10-02.** The discovery doc said Twilio doesn't support alphanumeric; Karthik corrected it and Twilio enabled it the same day. — https://campaignmonitor.slack.com/archives/C029VG5MEGM/p1790897998185879
- **10-13 James review.** Endpoints were built in both legacy and netcore in #25046; Clem fixed it that morning. — https://campaignmonitor.slack.com/archives/D01T6URQ5M5/p1791845329157629
- **09-30 Russell group DM.** "a bit of feedback… how we want to work together as a team" (to Clem, Chris and Fan; content not in Slack). — https://campaignmonitor.slack.com/archives/C0C5EMPN6K0/p1790730592559449
- 08-18/08-25: IT chased an overdue YouCanBook.me migration reply. Trivial.

## 5. Other notable
- **JS crew notes, 08-03.** "Crew captain • No direct volunteers… Clem absent". Don't claim crew lead. — https://campaignmonitor.slack.com/archives/G740DCZA5/p1785733606663209
- **Biome confirmed as Liam's.** Liam to Clem, 08-21: "Sounds like you've found your next project Clem" (re dropping babel). — https://campaignmonitor.slack.com/archives/G740DCZA5/p1787276878619649
- **10-12.** Russell asked for Clem, Chris and Fan to be added to the Team-Mitnick GitHub team.
- **Private context (self-review only, never a résumé).** EM wellbeing check-ins after the July company announcement and the August leaver news; self-reported weekly mood was low mid-Jun to mid-Sep.
