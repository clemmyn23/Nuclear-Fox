<!--
RAW: line-by-line verification of the peer sweep (peer-sweep-sha-2026-11-10.md) against the actual Slack threads,
done 2026-11-10 by a read-only research pass. 33 of 34 links read (C028M9THAAY not accessible). Names teammates.
Use the VERDICT column, not the peer list, when quoting anything. Times are Sydney (AEST until 4 Oct, AEDT after).
-->

# Peer-sweep verification (2026-11-10)

| Link | Date | Verdict | What Clem did (vs others) | Quotes / numbers |
|---|---|---|---|---|
| C0EBFDA75 p1785126771064119 | 27 Jul 14:32 | CONFIRMED | Told SRE drip ("Complex campaign series") was live on all prod DBs; linked his playbook and a Datadog dashboard | "now live on all prod DBs" (Clem) |
| C0E0BHJ87 p1793654145544579 | 3 Nov 08:15 | CONFIRMED quote; Clem not named | Christy (CS) relayed customer call; praise to "product team" | "the customer is SO PUMPED about drip campaigns" |
| C9U16V76E p1791516056538239 (#cm-product-updates) | 9 Oct 14:20 | CONFIRMED | GA announcement (Jarrod) credits Tom "for driving the bulk of this project"; Clem credited in replies, shared with Fan and Chris Luong | Shenny: "huge props to the awesome engineers who worked on this"; Russell: "These guys are the real heroes behind this… Thank you Clem, Fan and Chris". GA 1 Oct |
| C028M9THAAY p1788764024380569 | 7 Sep 16:53 | NOT VERIFIABLE | Parallel post by Karthik in #cm-team-mitnick-eng-prod (C029VG5MEGM p1788764126920529) links first draft of the discovery doc | "all our 250 odd (CM and Emma) customers on Infobip" (Karthik's figure) |
| Confluence 2451767325 | mod. 15 Sep | CONFIRMED author | Clem authored; 11 tasks under COM-1620, ~7–11 days; Infobip→Twilio migration of "~250 accounts" explicitly out of scope | 11 tasks; 7–11 days |
| C08LTFG8RQB p1793751222777379 | 4 Nov 11:13 | CONFIRMED | Steven (Thompson/Shared Services) found Clem's code in SmsComplianceEmbedService.cs; Clem confirmed one-call flow (create SS customer → buy number → start session) | Steven: "Looks like Clem did this work" |
| C08LTFG8RQB p1791332490890339 | 7 Oct 11:21 | CONFIRMED (direction corrected) | Clem found the chicken-and-egg (embed token needs a number; provisioning needed the form's details), asked to provision without registrationInformation. Tim agreed; Steven made it optional, in staging next day. Unblocked **Clem's own** CM work | Tim: "we should support not passing the registration info"; ~1 day turnaround |
| C08LTFG8RQB p1792451743502459 | 20 Oct 10:15 | PARTLY | Clem flagged T&C/privacy URLs prefilled with meetmarigold.com; Karthik drew the white-label conclusion, opened Twilio ticket | Clem: "prefilled with meetmarigold.com urls"; Karthik: "For white-labeled, this will reveal the brand" |
| C0E42R8GH p1789031694398309 (#engineering-syd) | 10 Sep 19:14 | PARTLY | James: updated local proxy needed to run monolith locally after routes moved to CmAPI.NetCore. ≥3 devs needed it. What the overhaul involved isn't stated | James: "you will need the updated version of the local proxy. Which Clem overhauled." |
| G740DCZA5 p1791501576579439 | 9 Oct 10:19 | PARTLY | Clem kicked off JC-411 (his 2022 idea), first PR #25020. No "merged / roadmap / webpack 5 part 2" in thread | Clem: "revive my 2022 pet project idea" |
| C4AP41JA0 p1791949063994869 (#devops) | 14 Oct 14:37 | CONFIRMED | Audited CreatesendCom TeamCity projects with no builds since Apr 2025: 8 projects (oldest last built 2016-08-30) + 5 stale skunkworks configs, to make room for new JS pipelines. Naveed verified, wrote Confluence page 2519859209, approved. Archiving not shown | Naveed: "these are all good to go… Thanks blacksmith 🙌" |
| C57AD89RT p1791509990752049 (#deploy-env) | 9 Oct 12:39 | CONFIRMED | Reported bot down; Datadog ECS events (~200 unhealthy cycles since 8 Oct 18:33 UTC); no code change since Nov 2025; hypothesised Graylog shutdown → startup loop; PR #6 Graylog→Datadog; back 15:21. Francois and t4 helped | ~2h40m from report to restore |
| C12KJEXL4 p1784173972535859 | 16 Jul 13:52 | CONFIRMED | Sam assigned it ("blacksmith is looking into this first"). Clem found nested `<data>` tags in 2 layouts + invalid feed (duplicate xmlns:media), drafted customer explanation, paused automation, verified 22 Jul send | Root cause ~1h20m after assignment |
| C0EDU0126 p1784175404457749 | 16 Jul 14:16 | CONFIRMED | Priya (Support) contacted client; Clem checked previews 17 Jul, confirmed 22 Jul send | Client: "Thanks for spotting the issues and letting me know, both issues should be fixed now"; 6 days to verified send |
| C06BDJXDTB2 p1788309464177139 | 2 Sep 10:37 | PARTLY | Decoded error-queue payloads, found idempotent SET ops, laid out 3 safe options, redrove one workflow. "Multiple-values fix" not shown in thread. Contains PII; don't quote | 5 queue entries |
| C4YLF4KSN p1792040235260969 (#c-sharp) | 15 Oct 15:57 | CONFIRMED | Flagged high-severity Pkcs advisory, traced to MimeKit 4.15.1 → Pkcs 8.0.1/10.0.0, gave patched versions 8.0.2/10.0.13, showed local build failing. James shipped PR #25133 | 29 min flag → PR; 3 of 20 projects affected |
| G740DCZA5 p1785201853304269 | 28 Jul 11:24 | PARTLY | Clem proposed a crew-direction/leadership chat (before Liam left on 4 Sep). 29 Sep: became meeting-notes owner; gave org-wide access to recordings. Not shown running the meeting | "start a chat about the crew direction going forward, and who to lead the crew" |
| C4YMJ2DD2 p1778558050997699 | 12 May | CONFIRMED (topic unverified) | Liam posted recording of Clem's presentation | "Here's the recording for those that missed Clem's presentation" |
| C07P900TAMQ p1793291401447719 | 30 Oct | CONFIRMED feature only | Oct customer newsletter: "AGENCY: Drip Campaigns" | — |
| C0E0BHJ87 p1786109647612209 | 7 Aug | CONFIRMED feature only | Customer "super excited" about drip | — |
| C4YMJ2DD2 p1787012491073359 | 18 Aug | CONFIRMED feature only | Crew notes | "React Flow performing well for advanced flows; no issues reported" |
| C4YLF4KSN p1781585820727649 | 16 Jun | CONFIRMED | PR #23545 set agent type for complex sequences; re-review after dropping column reuse | — |
| CSQF087UM p1784249236726749 | 17 Jul | PARTLY | Tom wrote / Jess published help doc; Clem updated in-code help links | — |
| C4YLF4KSN p1791436776472939 | 8 Oct | CONFIRMED | Asked James where new endpoints go → netcore default; PR #25031 follow-up to #24999 | — |
| C08LTFG8RQB p1792391936300919 | 19 Oct | PARTLY | Clem asked whether provisioning alerts keep working; Steven/Karthik confirmed | — |
| C07P900TAMQ p1781220772958829 | 12 Jun | CONFIRMED team credit | Boole Innovation Sprint prototype (journey visibility); Clem 1 of 7 | two-week prototype |
| C4YLF4KSN p1788401055708249 | 3 Sep | CONFIRMED minimal | PR #24483 Hex resource ownership from ID | — |
| C06BDJXDTB2 p1789430303926799 | 15 Sep | PARTLY | Deployed UCF to prod incl. JRE 25 (other hygiene items not in this message) | — |
| C029N7PEQUQ p1787876312890559 | 28 Aug | CONFIRMED | Replied for team on journey-clone error queue; asked Support for customer permission | — |
| C1X4NJ1PC p1789611597041779 | 17 Sep | CONFIRMED | Answered SRE's CRM Lite data-archive question (60-day limit is a product decision) | 60 days |
| G740DCZA5 p1781503776471259 | 15 Jun | PARTLY | Asked for Claude to read js-standard.md first; Lovelace link not in thread | — |
| G740DCZA5 p1781740698006789 | 18 Jun | CONFIRMED light | Chris Wright drove webpack 5 (PR #23212) | "Both Clem and I have had a look" |
| C4YMJ2DD2 p1777950103464079 | 5 May | CONFIRMED | Reviewed/approved Dmitry's Chargebee custom-codes PR | — |
| C0CAS3M3J78 p1792540031444769 | 21 Oct | CONFIRMED | Forwarded PR-notify thread to Russell | "Thanks heaps blacksmith - I missed this!!!" |
| G740DCZA5 p1789029824110299 | 10 Sep | CONFIRMED | Nudged crew on reviews | — |

**Confluence 2471461091**, "Creating a spoofed sales-led billed-out-of-app account for development use" (COMPOSE, author Clement Ng, last modified 17 Sep 2026): explains the write path (Salesforce → Plan Provisioning Service → DynamoDB + SQS) and read path (Redis, 5h TTL, gRPC fallback), then how to fake a sales-led account for dev; warns it skips the SQL-side handler.

## Corrections to the peer list
1. registrationInfo: unblocked Clem's own CM work; Steven shipped the API change in ~1 day.
2. White-label: Clem flagged the prefilled Marigold URLs; Karthik drew the white-label conclusion and escalated.
3. Local proxy: overhaul confirmed; needed to run the monolith locally after the CmAPI.NetCore route move. Details of the overhaul not in thread.
4. JS crew: direction proposal predates Liam leaving; Clem became notes owner and opened recordings org-wide; not shown running the meeting.
5. Docker: only the kickoff + PR #25020 in thread.
6. TeamCity: 8 dormant projects (oldest 2016) + 5 skunkworks configs; Naveed wrote the audit page; archiving not shown.
7. GitHub bot: "wasn't even your service" / "every crew depends on it" not stated; Francois and t4 helped.
8. UCF: "multiple-values fix" not shown shipped.
9. Drip GA: Tom credited for driving the bulk; Clem credited in replies alongside Fan and Chris. Customer quotes praise the feature/product team.
10. Help doc: Tom/Jess; Clem did in-code links.
11. ~250 customers: Karthik's figure; Clem's doc puts the migration out of scope.
12. Pkcs: 29 min is accurate; James shipped the fix.
13. Lovelace link and React Flow talk topic not verified.

## Strongest new evidence (top 5)
1. RSS incident, assigned → root cause in ~1h20m → customer explanation → paused → verified send 6 days later; customer thanked him.
2. Pkcs vulnerability: exact dependency trace + patched versions → fix PR in 29 min.
3. SMS: authored discovery doc; "Looks like Clem did this work" from the partner team reading the code.
4. GitHub bot: diagnosed from ECS events, shipped Graylog→Datadog; restored ~2h40m after report.
5. Drip: announced prod-wide rollout with his playbook + dashboard; named at GA: "the real heroes… Thank you Clem, Fan and Chris".
EOF