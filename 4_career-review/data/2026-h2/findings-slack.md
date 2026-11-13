# Slack findings — U01SKCA6MHC ("blacksmith"), 2026-05-28 → 2026-11-10
Read-only. Short verbatim quotes. [Inference] = interpretation. Customer names/PII deliberately omitted.

## Cast (as seen in Slack; official titles per Confluence "Engineering Teams" page where they differ)
- Russell Abedin ("rusty") — Team Mitnick TL (Confluence) / acts as manager in Slack: sprint must-dos, decisions, 1:1s.
- Shenny Mackie ("shen") — EM (Confluence) / assigns work, delivery lead.
- Karthik Ramaswamy Iyengar — SMS PM. Jarrod Taylor — PM drip agency rollout + Brand Hub V2. Tom Evans — Boole PM.
- Sam Crome — Boole TL, credited "tech leading" drip; left 2026-08-27. Yuri Fontes — designer.
- Tim Cranfield, Steven Li — Team Thompson (SMS shared services). Alexis Tzanos — SMS frontend partner.
- Melisa Irmako — junior/intern mentored. Chris Luong, Fan Li, Sherry Lotfi — engineers. James Dunlop — senior C#/DB reviewer. Liam Callaway — Biome lead (left 09-04).

## Reorg / role
- 07-22 #all-marigold: Advanced drip launch credits Team Boole collectively; Sam "tech leading this through to delivery". Clement not named.
- 08-20 "Boolnick team merge and Journeys domain handover"; 09-01 #jellyfish-marigold "4 teams will merge down into 2 teams… AJ, COM = Team Mitnick".
- 09-02 Clement posts merge notice in #cm-team-boole.
- Departures: Sam (08-27), Jay Chen (09-03), Liam (09-04), Subrat leaves JS crew (07-30). [Inference] Clement one of the most senior ex-Boole engineers holding Journeys/workflow context.
- **09-01 DM, EM→Clement:** "new project… Twilio form… Would you be up for taking the discovery piece of this work on for our team".
- **09-28 DM, TL:** "On your plate: SMS Provisioning, AI-DLC stream A… SMS Provisioning is one of Product's highest priorities at the moment." Clement recommended someone else take SMS frontend while he integrated shared-services endpoints with CmAPI. TL: "thank you for a really thoughtful response… we'll go with what you've recommended!" Sprint must-dos: "Clem to focus on the CMAPI / Integration work. Bring Alexis on to focus on the front end work".
- JS crew: 07-28 raised "crew direction going forward, and who to lead the crew"; meeting-notes owner by 09-29; handed meeting ownership to Sha 10-13. [Inference] interim organiser.

## Drip campaigns (Jun–Oct)
- 06-12 DM designer: "Can you add everything to AJ-1190. That'll be the card for final design alignment".
- 06-22 posted scheduling date-time edge cases; 06-23 "We can now create campaign and condition nodes."; 07-15 UX proposal for sibling-branch scheduling; 07-16 "No tracking = no open clicks" (plain-text constraint); 07-17 coordinated help-doc publish.
- 06-17→19 DB decision: pushed back on a key constraint; after call with senior C# reviewer: "Let's make the column non-null… Let's drop the constraint… this pattern is not used anywhere else in the code base." #c-sharp: "We don't think reusing the column is a good idea."
- **Launch readiness (AJ-1155):** 07-22 posted dashboard + playbook for feedback; gave PM the FF + DB release-order steps; 07-24 "Created dashboard… Created alerts. See #campaign-sequence-alerts"; **07-27 #cm-sre: "Drip campaigns (Complex campaign series) is now live on all prod DBs. Playbook… DD Dashboard"**; 08-07 env:prod filter.
- Launches: Advanced for Direct live 07-22 (1 DB) → all DBs 07-27; **all account types live 10-01** ("every account, across all plans"), SRE post links Clement's playbook; 10-09 announcement "Much of the groundwork was delivered by Team Boole". No adoption numbers.

## SMS Twilio Compliance Embed (Sep–Nov)
- Why: 08-15 PM: "None of us other than Greg have done provisioning" (single-person manual process). 08-06 Twilio announced toll-free verification compliance changes effective Sept 15, 2026 [Inference: raised compliance bar]. 09-08 sales-led first; self-serve blocked on SMS credits via billing (Team Liskov). 09-28 "one of Product's highest priorities". Scope: US/CA TFN + AU alphanumeric; UK stays manual (no Twilio embed).
- Discovery: 09-07 "initial vibe" page — flagged no theming info / no callback ("anything that happens after that is gonna be a black box"), asked "Have we applied for early access?" → PM submitted the Twilio form. 09-10 "CM does not support A2P 10DLC numbers", raised region gating. 09-11 mapped old→new flow. 09-15 discovery DONE, created tasks; new CmAPI endpoint "should streamline the overall sms provisioning process". 09-17 spoofed sales-led account how-to. 09-18 reused TL's old SMS form scaffolding: "I might have underestimated the work…". 10-01 "SMS is probably 2 weeks left… Alexis is blocked until I merge my PRs" → PM rolled up "2–3 weeks (~20/10)".
- **Cross-team:** 10-07 #cm-thompson-support "chicken-egg problem" — number needed before embed token, but provisioning a number needed the details the form collects → Thompson agreed, made `registrationInfo` optional, staging by 10-08.
- 10-12 "SMS embed token grab is working"; 10-19 designed post-submission notification with Thompson; 10-20 "The endpoints are in staging. PRs have been merged."; 10-21 theme set IDs Direct/agency (white-label), live demo at standup.
- [Inference] on leave ~10-22→11-01.
- Outcome: 11-02 "US / CA TFN - Dev Complete, QA in Progress; AU Alphanumeric - Dev Complete". **11-04 PM: "SMS Compliance Embeddable in full glory! Great work Clem, Alexis!!"** + e2e demo video. 11-04 Thompson engineer: "Looks like Clem did this work". 11-05 cleared to test with real customers. 11-09 "a few customer requests" pending Twilio approval.

## AI-DLC Stream A + Brand Hub V2
- 09-23 ~1am working; TL: "You have gone above and beyond and this certainly wasn't an expectation".
- 09-28 "We did it!!" — Brand Kit collection path ported Node→C#/.NET: SSRF-hardened adapters, gRPC surface, parity harness, **307/307 unit + 72/72 parity tests**. TL: "Thank you for seeing this through!"
- 09-28 process feedback: "Claude has been going back and forth… for the past 2.5 business days… gone a bit pass the whole 'use ai to save time' threshold." TL: "Such a great call out". Recommended human review + staging deploy before merge.
- 11-03 TL decision: not proceeding — "The costs and risks currently outweigh the benefits… a worthwhile experiment… That's what made this decision possible." Clement: "Goodbye my PRs".
- Brand Hub handed from Team Zuse ~08-31. 11-03 Clement + Fan freed to work on edit features. BrandHubV2 flag in prod 11-06. 11-10 PM: "This is looking great".

## Tooling
- Webpack 5: AI work log "~1 day with AI vs ~1 week manually"; migration analysis for JS crew; landed by 07-06.
- localdev-tools #74 modernisation (Node 24, Vite, simple/advanced UI).
- Docker FE builds (JC-411) 10-09 "migrating the /app and /shared frontend builds to run on docker instead of the bare windows build agents… side-by-side".
- 10-14 TeamCity cleanup: audited ~8 dead projects + 5 configs (last builds 2016–2023); DevOps "good to go… Thanks".
- **Biome = Liam Callaway's initiative** ("CI lint times down from over 2 mins to under 2s"); Clement's role minor (reviewer/follow-on).

## Observability / internal tools
- Graylog decommission deadline 30 Sept. 09-15 "UCF service graylog migration and java upgrade - DONE. Deployed to prod".
- 10-09 GitHub bot: #6 Graylog→Datadog fix, #7 escape user content (07-15 "the < in the PR title broke the bot"), #8 fargate.
- Hex resource-ownership (live 09-16): look up account details from Journeys error IDs "rather than remoting into prod sql database". EM: "Super useful!… link to this from the playbook". TL: "Always love these productivity boosters".

## Journey reporting (Innovation Sprint)
- RunnerService gRPC V2 ("~1–2 hrs vs half a day"); AJ-1195 Subscriber History UI with Claude + Figma ("CSS implementation time roughly halved"); AJ-1213 mocks; proposed multi-dimensional filtering. Productionisation (AJ-1307) led by others.

## Incidents
1. **06-15 trigger-service healthcheck** — unblocked on-call engineer; checked prod Consul via jumpbox; "Leader election was dropped in the .core port, so all 6 instances run the heartbeat" → 429s; advised against restart; stopgap + root-cause fix; routed to platform/C# owners; deployed 06-25.
2. **07-15→22 RSS customer failure** — assigned by TL; root cause nested dynamic-content tags (explained intermittency) + invalid feed; drafted customer-ready explanation, paused automation, worked through support, confirmed next send succeeded.
3. **09-02→04 UCF DLQ** — decoded protobuf, confirmed idempotent SETs, reconstructed Redis keys, offered 3 options, asked for 👍 before touching prod ("It's a bit late and I'm too tired to be touching prod."); found "an actual bug in the contact attribute service"; patch fixes "6 of the 8". TL: "I can't express how great what you've done here is!"
4. **10-09 GitHub bot outage** — self-detected; Datadog/ECS timeline (~200 unhealthy events); ruled out code change; Graylog shutdown hypothesis; "We are back!" same day; hardening PRs same afternoon.
5. **11-06 self-caused CI break** — PR #25501 broke TeamCity builds across projects: "I didn't think it would affect everything, my bad" → fixed quickly with `chain=pr`.
6. 10-15 flagged CVE (System.Security.Cryptography.Pkcs) build break to C# crew. 08-28 spotted journey-copy failures himself; asked support for customer permission to investigate.

## Praise
- PM 11-04 "SMS Compliance Embeddable in full glory! Great work Clem, Alexis!!"; Thompson 11-04 "Looks like Clem did this work".
- TL: 09-04 "I can't express how great what you've done here is!"; 09-23 "gone above and beyond"; 09-28 "Thank you for seeing this through!", "Such a great call out", "a really thoughtful response… I love it!"; 09-03 "productivity boosters"; 11-02 "Thank you heaps for all the reviews… so great to have you back!!!"
- EM 09-16 "Super useful!… great stuff, thank you Clem!". PM 11-10 "This is looking great." PM 11-02 wants Clem/Alexis free "so they can move on to more exciting projects".

## Mentoring
- Junior (Oct DMs): unit-test structure (FF on/off, `screen.debug()`), BEM naming, JS conventions, how to ask reviewers for clarification, caution on AI-rewritten PR replies; her manager pointed her to him.
- On-call engineer AWS access escalation; DB design + SQL tracing of UCF steps with another engineer; async-conversion guidance ("completely ok to convert old methods to async, within reason… better to log everything").
