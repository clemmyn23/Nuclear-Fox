<!--
RAW: a teammate (Sha) ran their own AI sweep of Atlassian, GitHub and Slack for Clem's work and sent the results by Slack DM
on 2026-11-10 (DM D07VCQ3F83V, ts 1794308772.377639 and 1794308979). Copied verbatim below for reference.
This is a second-hand AI summary: verify a claim against its linked thread before using it in a résumé or interview
(see verification notes in findings-slack-clem-sweep.md). Raw file: names teammates.
-->

# Peer sweep from Sha (2026-11-10)

## Message 1 (22:06 AEDT)

*Features you shipped*
- Drip campaigns: the advanced series tree on React Flow, the timeline and scheduled dates, the basic drip refresh, and the rollout to every prod DB with a [playbook](https://campaignmonitor.atlassian.net/wiki/spaces/AJ/pages/2350841928) and Datadog dashboard ([thread](https://campaignmonitor.slack.com/archives/C0EBFDA75/p1785126771064119)). It went GA to every account type on 1 Oct, and Support says a customer is "SO PUMPED about drip campaigns" ([thread](https://campaignmonitor.slack.com/archives/C0E0BHJ87/p1793654145544579)). Shenny and Russell both called you out ([thread](https://campaignmonitor.slack.com/archives/C9U16V76E/p1791516056538239))
- The SMS Twilio compliance embed: you wrote the [discovery doc](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/2451767325) Karthik and Thompson worked from, joined Thompson's stand-ups as the CM engineer, and built the CM side: toll-free provisioning, setting up the client afterwards, gating and AU alphanumeric support. It replaces Support's manual provisioning and lays the groundwork for moving ~250 CM and Emma customers from Infobip to Twilio ([thread](https://campaignmonitor.slack.com/archives/C028M9THAAY/p1788764024380569)). Steven: "Looks like Clem did this work" ([thread](https://campaignmonitor.slack.com/archives/C08LTFG8RQB/p1793751222777379))
- On the same project, your registrationInfo question unblocked Thompson ([thread](https://campaignmonitor.slack.com/archives/C08LTFG8RQB/p1791332490890339)), and you caught that white-labelled agencies would see Marigold's terms in the embed ([thread](https://campaignmonitor.slack.com/archives/C08LTFG8RQB/p1792451743502459))
- Brand Hub V2: the data layer and colour editing are already merged
- Journey reporting groundwork: the feature flag client in RunnerService and the subscriber activity view

*Things everyone depends on*
- The local proxy overhaul, which CmAPI.NetCore local dev now requires. James: "Which Clem overhauled" ([thread](https://campaignmonitor.slack.com/archives/C0E42R8GH/p1789031694398309))
- Docker frontend builds (JC-411), your idea from 2022 with the first stages now merged, plus the build speed roadmap behind it and webpack 5 part 2 ([thread](https://campaignmonitor.slack.com/archives/G740DCZA5/p1791501576579439))
- The TeamCity audit that found 8+ dormant projects, some untouched since 2016 ([thread](https://campaignmonitor.slack.com/archives/C4AP41JA0/p1791949063994869))
- Bringing the CM GitHub bot back when it wasn't even your service. You traced the startup loop through the ECS events to the Graylog shutdown, moved it to Datadog, and had it back the same afternoon. Every crew's review pings depend on it ([thread](https://campaignmonitor.slack.com/archives/C57AD89RT/p1791509990752049))

*Production support*
- The UK publisher's broken RSS campaign: you found the nested dynamic content tags and the invalid feed, paused it, wrote the customer explanation and checked the next send ([thread](https://campaignmonitor.slack.com/archives/C12KJEXL4/p1784173972535859))
- Clearing the UCF error queue safely and shipping the multiple-values fix ([thread](https://campaignmonitor.slack.com/archives/C06BDJXDTB2/p1788309464177139))
- Flagging the Pkcs vulnerability with the patched versions, so James could ship the fix in about 30 minutes ([thread](https://campaignmonitor.slack.com/archives/C4YLF4KSN/p1792040235260969))
- Writing and deploying the trigger service healthcheck fix

*Crew, reviews and docs*
- Keeping the JS crew going after Liam left: the meeting, the recordings open to the whole org, and starting the crew direction conversation ([thread](https://campaignmonitor.slack.com/archives/G740DCZA5/p1785201853304269))
- Your React Flow talk at JS crew ([recording](https://campaignmonitor.slack.com/archives/C4YMJ2DD2/p1778558050997699))
- 75 reviews of other people's PRs since May, including Liam's Biome migration, the local proxy changes, Atlas and Liskov's Chargebee custom codes
- Your [spoofed sales-led account guide](https://campaignmonitor.atlassian.net/wiki/spaces/COMPOSE/pages/2471461091) for anyone working on billed-out-of-app accounts

## Message 2 (22:09 AEDT): "the extras that didn't make the first message"

*More on the features*
- Drip campaigns made the October agency newsletter ([post](https://campaignmonitor.slack.com/archives/C07P900TAMQ/p1793291401447719)), and another customer was "super excited" back in August ([thread](https://campaignmonitor.slack.com/archives/C0E0BHJ87/p1786109647612209))
- The JS crew notes say "React Flow performing well for advanced flows; no issues reported" ([notes](https://campaignmonitor.slack.com/archives/C4YMJ2DD2/p1787012491073359))
- Stamping complex sequence campaigns at creation so they go to their own sending agent ([thread](https://campaignmonitor.slack.com/archives/C4YLF4KSN/p1781585820727649))
- The drip campaigns help doc update with Jess and Tom ([thread](https://campaignmonitor.slack.com/archives/CSQF087UM/p1784249236726749))
- Moving the new SMS endpoints into CmAPI.NetCore after checking with the C# crew ([thread](https://campaignmonitor.slack.com/archives/C4YLF4KSN/p1791436776472939)), and confirming the provisioning alerts keep working with the embed ([thread](https://campaignmonitor.slack.com/archives/C08LTFG8RQB/p1792391936300919))
- Boole's Innovation Sprint prototype for seeing inside automated journeys ([post](https://campaignmonitor.slack.com/archives/C07P900TAMQ/p1781220772958829))

*Ops and tooling*
- Escaping user content in the GitHub bot's Slack notifications while you were in there, a small security fix ([PR](https://git.campmon.com/Engineering/GitHubTeamManagement/pull/7))
- The Hex tool for getting resource ownership from an ID, so owners can be looked up in Hex instead of SQL ([thread](https://campaignmonitor.slack.com/archives/C4YLF4KSN/p1788401055708249))
- UCF service hygiene: Datadog logging, the jvm-libs bump and JRE 25 to prod ([thread](https://campaignmonitor.slack.com/archives/C06BDJXDTB2/p1789430303926799)), plus taking Graylog out of metricservice
- Local proxy profiles ([PR](https://git.campmon.com/Engineering/localdev-tools/pull/76)) and removing node-notifier from the frontend builds ([PR](https://git.campmon.com/Freshview/createsend.com/pull/25500))
- Picking up Greg's journey clone error queue report and getting Support to ask the customer for access ([thread](https://campaignmonitor.slack.com/archives/C029N7PEQUQ/p1787876312890559))
- Answering Francois's CRM Lite engagement data question for SRE's archive work ([thread](https://campaignmonitor.slack.com/archives/C1X4NJ1PC/p1789611597041779))
- Two days at the AWS AI-DLC event in September

*Crew and reviews*
- Pushing for Claude to read the JS standards file before writing code, which fed into Sha's Lovelace work on getting LLMs to follow standards ([thread](https://campaignmonitor.slack.com/archives/G740DCZA5/p1781503776471259))
- Reviewing and testing Christopher's webpack 5 upgrade ([thread](https://campaignmonitor.slack.com/archives/G740DCZA5/p1781740698006789))
- The crew review of Dmitry's Chargebee custom codes repo ([thread](https://campaignmonitor.slack.com/archives/C4YMJ2DD2/p1777950103464079))
- Pointing Russell to the C# crew notify rule. Russell: "Thanks heaps Clement Ng - I missed this!!!" ([thread](https://campaignmonitor.slack.com/archives/C0CAS3M3J78/p1792540031444769))
- Nudging the crew on reviews in September ([thread](https://campaignmonitor.slack.com/archives/G740DCZA5/p1789029824110299))

*More kudos*
- The RSS customer, via Priya: "Thanks for spotting the issues and letting me know" ([thread](https://campaignmonitor.slack.com/archives/C0EDU0126/p1784175404457749))
- Naveed thanked you for the TeamCity audit ([thread](https://campaignmonitor.slack.com/archives/C4AP41JA0/p1791949063994869))
