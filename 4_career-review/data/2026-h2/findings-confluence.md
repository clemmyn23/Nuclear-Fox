# Confluence findings (2026-05-28 → 2026-11-10) — saved from subagent report

Authored 3 pages, edited 3, 0 comments. No LDR/RFC/PRD/postmortem in window. Pre-window pages not updated.

## Authored
1. **SMS: Twilio compliance embeddable** — COMPOSE/2451767325 (last mod 15 Sep 2026; Jira COM-1619, epic COM-1620)
   - Problem: replace in-house SMS registration wizard (SmsRegistrationNew.tsx) + manual Google-form provisioning with Twilio's white-label Compliance Embeddable.
   - Scope: Toll-Free Verification IN; AU/UK Alphanumeric Sender ID BLOCKED (no Twilio docs yet); US/CA A2P 10DLC OUT; Infobip→Twilio backfill (~250 accounts) OUT.
   - Decision recorded: "Rollout is Sales-Led first, not Self-Serve (agreed per team discussion, 7 Sep)". Self-serve needs SMS Credits which CleverBridge (prob ChargeBee) can't sell.
   - Risk flagged: "no clean rollback once a brand/campaign is created via the embed" → staged rollout, not big-bang.
   - Architecture: CmAPI thin proxy over ISmsSharedServicesApiV3 gRPC client; Shared Services owns Twilio Initialize.
   - Plan: 11 Jira tasks COM-1646..COM-1656 (FF routing US/CA→embed, AU/UK legacy; pre-provisioning spike; CmAPI spike; embed container; token fetch; lifecycle — track onInquirySubmitted not onComplete "which isn't guaranteed to fire"; status display; resume keyed off phone number; theming; surgical legacy cleanup; testing).
   - Estimate: re-estimated ~7–11 days vs Shared Services' 5–8 day placeholder.
   - Reviewer (Tim Cranfield, 7 Sep) comments folded in: "We don't currently support 10DLCs…", "CmAPI would not be calling Twilio directly".
   - PM References page credits "New Tech Audit + Estimates for Frontend and CM API (Clement Ng)". PM Proposal adopts his Checkpoint 1 (Sales-led, TFN, US/CA).
2. **Playbook - Drip campaigns (complex campaign series)** — AJ/2350841928 (last mod 29 Jul 2026)
   - Runbook for Advanced Drip rollout (AJ-1111): isolated ComplexSequenceMailingSendServiceAgent; single thread because evaluation can block ~9 min; `cs-` prefix so it doesn't claim regular campaigns; isolated "so that a cohort waiting on convergence never blocks normal campaign sends".
   - Architecture: Redis lock 15-min TTL renewed every 5 min, Kafka ContactCohortMembershipChanged, gRPC w/ Polly, reset to Draft on failure; 10 reschedule attempts; 900,000 ms alert threshold.
   - 7 metrics, 7 anomaly runbooks ("Retry Delivery in HEX"), instrumentation gaps found (no complex-sequence send metric → propose `is_complex_sequence` tag; no MailingType; shared queue gauges; DD logs unconfirmed); Datadog gotchas.
   - Outgoing TL: "the best playbook in either space; use it as the template".
   - Timeline: prod bug bash 17 Jul; convergence fix AJ-1278 verified in prod 31 Jul; Showcase 10 Sep (Fan Li presented Advanced Drip for Mitnick) ⚠️ uncorroborated — no 10 Sep showcase event or doc exists (12-month sweep, [../findings-meeting-notes-12mo.md](../findings-meeting-notes-12mo.md) §1); likely conflates the 21 Jul drip demo (Chris Luong) and the 13 Oct journey-reporting demo (Fan Li).
3. **Creating a spoofed sales-led billed-out-of-app account for development use** — COMPOSE/2471461091 (17 Sep)
   - Eng has no Salesforce access → documented write path (SFDC→Plan Provisioning Service→DynamoDB→SQS) and read path (Redis 5-hr TTL, gRPC fallback); steps. A teammate (Alexis Tzanos) later published a scripted version (COMPOSE/2536669243, 22 Oct).

## Contributed / mentioned
- Playbook: CRM Lite data population error queues (AJ/1809842179, contributor, 14 Jul) — DLQs, alert thresholds >1 warn / >100 alert, protobuf decoder script.
- Minor edits: Using CAL (YODA), Setup and run monolith locally (DEV).
- **Journeys Context — Handover (WIP)** (AJ/2409758790, by outgoing TL Samantha Crome, Aug–Oct): "Book time with Russell, David, Clem and Tom." WorkflowBuilder/Journey Designer knowledge holder: "Clement Ng (blacksmith) — also wrote the Drip campaigns and Campaign series playbooks, and made the last functional change to both Tavern repos". Commerce journeys: Rashmita Pinto + Clement. Priority order: Drip → Graylog→Datadog (AJ-961) → Journey Reporting. TL has no named successor. Monitor duty: CRM Lite, Agency Status, Onboarding, Complex Sequences.
- PM pages (ProdMgmgt): Proposal for Compliance Embeddable — ideal state "Sales can sell SMS as a feature"; ~250 customers on Infobip; self-serve off (CleverBridge no SMS credits); manual Google-form provisioning w/ data issues + support overhead; 6 legacy flags. Checkpoints CP1 TFN US/CA sales-led; CP2 Sender IDs UK/AU; CP3 Infobip migration; CP4 NZ/RC bundles; CP5 self-serve "Early 2027".
- Engineering Teams page (22 Oct): Team Mitnick — EM Shenny Mackie, TL Russell Abedin, PMs Karthik + Jarrod Taylor; members incl Clement, Fan Li, Christopher Luong, Alexis Tzanos. Contexts: Campaigns UI, SMS, List & Subscribers, Journeys, Integrations. No Boole team → Boole merged into Mitnick ~Aug–Sep 2026 (inference). Lovelace standup 13 Aug mentions "organizational restructuring" and TL turnover.
- JS Crew member; crew meeting host roster (8 Dec 2026, 22 Jun 2027).
- JS Crew Presentations page: Biome "CI lint time from over 2 minutes to under 2 seconds" (PR #24324, Aug 2026) — unattributed.
- Bug Bash - Advanced Drip Campaigns - Branching (AJ/2341797889, 17 Jul) — context only.
