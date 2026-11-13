# HR role & development form: draft responses (Nov 2026)

> Fill the ⟨⟩ placeholders before you submit; I couldn't find these in your notes, Slack, Confluence or Jira.
> I kept everything internal-facing. Nothing from `job-search/`, `comp/` or `interview/` is mentioned.

---

### Are you an IC (Individual Contributor) or a People Manager (you have FTE direct reports)?

**Individual Contributor**

---

### Walk through a typical day or week in your role. What tasks and responsibilities do you handle on an ongoing basis, and which decisions can you make independently versus with guidance or approval?

I'm a senior full-stack engineer in Team Mitnick (Campaigns UI, SMS, List & Subscribers, Journeys, Integrations, Brand Hub). In a typical week I:

- **Lead or build the team's priority feature.** This year that was the Drip Campaigns builder and its go-live, then SMS onboarding through the Twilio compliance embed. Now it's Brand Hub V2 colour and logo editing, where I'm the sole frontend owner. This covers discovery, technical breakdowns and estimates, ticket creation, implementation across React/TypeScript and C#/.NET, and demos at standup.
- **Review code and set standards.** I review about 2–3 PRs a day across the team and the JS Crew (163 PRs in the last 12 months), and I mentor through review, DMs and calls — four engineers this year, including our newest team member through his whole onboarding and a junior engineer whose manager pointed her to me. The coaching is measurable: my review comments on their PRs drop from 7–10 per PR to 0–1 within about three months as they ramp.
- **Support production.** I'm on the Mitnick Slack-monitor roster (~20 alert channels). This year I resolved four production incidents end-to-end, including a customer RSS send failure and a UCF dead-letter-queue regression.
- **Work across teams.** I work with PMs, design, the shared-services team (Thompson), the C# crew, DevOps and SRE. I also drive the Docker frontend-builds initiative (JC-411), which moved the frontend PR checks to Docker and cut per-PR build compute by ~69%.

**Decisions I make independently:** implementation and design within a feature, API and data-contract design (for example the idempotent SMS provisioning API), code-review approvals and standards, how to split and sequence tickets, incident triage and diagnosis, and tooling/CI changes for frontend builds.

**Decisions I make with guidance or approval:** schema changes on hot paths (agreed with the C# crew and DB reviewers), production data operations such as DLQ redrives (I get a 👍 before touching prod), rollout and release order (with the PM and feature flags), staffing and scope trade-offs (I recommend and the TL/EM decides; my SMS staffing split was adopted), and anything that affects other teams' pipelines or APIs.

---

### Primary product you support (I.e. CM, Emma, Vuture)

**CM (Campaign Monitor)**

---

### Has your role changed or evolved post-acquisition?

Yes, significantly. It has moved from senior feature engineer and reviewer to the engineer who leads the team's highest-priority, most ambiguous work.

- **Team structure:** Team Boole merged into Team Mitnick on 1 Sep, as part of "4 teams into 2". Our tech lead left without a named successor, and several other experienced engineers left around the same time. I was named one of the key knowledge holders for Journeys/WorkflowBuilder in the handover, and I'm now one of the main people holding that context in the merged team.
- **Scope:** the merged team covers far more product surface (SMS, Journeys, Campaigns UI, Lists, Integrations and the inherited Brand Hub). My work now spans all of these instead of one area.
- **Responsibility:** in September the EM asked me to take discovery on SMS onboarding ("one of Product's highest priorities"). I ended up as the technical lead in practice: I wrote the plan the PM adopted, staged the rollout, designed the provisioning API, negotiated an API change with the shared-services team, and got it to dev-complete and real-customer testing in about two months.
- **Ways of working:** more operational ownership (on-call, the Graylog→Datadog migration, incident follow-ups) and more cross-team work. I also ran the build phase of the AI-DLC experiment, whose evidence fed leadership's decision not to proceed.

My title hasn't changed with this. The tech-lead part of my work is done in practice, not as a named role.

---

### What results are expected from your role, and how are they measured or recognized?

**Expected:** deliver roadmap features to production reliably and on time, to a high quality bar; keep our services healthy; and raise the team's engineering quality through reviews, standards and mentoring.

**How it shows up today:**
- **Delivery milestones, with adoption.** Drip Campaigns went live for Direct customers in July and to every plan on 1 Oct — since launch, 688 client accounts have created 1,212 drip campaigns (446 of them the new branching type), and weekly adoption roughly 2.6×'d at the all-plans GA. The SMS compliance embed was dev-complete in early November, cleared for real customers on 5 Nov, and provisioned its first three customers in its first week live. Brand Hub V2 is behind a flag in prod.
- **Quality and reliability.** Launch readiness (dashboards, alerts, runbook), incidents resolved, and no rollbacks on my launches.
- **Recognition.** This is mostly informal: Slack shout-outs from the PM, TL and EM (for example "SMS Compliance Embeddable in full glory! Great work Clem, Alexis!!"). The outgoing TL called my drip runbook "the best playbook in either space; use it as the template."

**The gap:** we don't have explicit success measures for my role beyond "the feature shipped", and recognition doesn't connect to level or progression. I'd like us to agree on a few outcome measures per project (adoption, time-to-onboard, support tickets avoided) and on how this work counts towards the next level.

---

### What outcomes does your work influence (for example, customer experience, revenue, quality, efficiency, or risk), and who do you work with to achieve them? Include any people, projects, or improvements you lead.

- **Revenue & customer experience: SMS onboarding (technical lead in practice).** It replaces a manual, support-run registration process that only one person knew how to do, so Sales can sell SMS as a feature. It's also the foundation for moving ~250 customers from Infobip to Twilio and for self-serve SMS. *With:* SMS PM, a frontend partner engineer, the Thompson shared-services team, the C# crew.
- **Customer experience: Drip Campaigns.** I owned the builder canvas and launch readiness for branching email sequences, now available on every plan — 688 accounts have created 1,212 drips since launch (282 accounts on the branching type I built the builder for). *With:* the Boole TL and PM, design, a backend peer, SRE.
- **Customer experience: Brand Hub V2 "Correct the kit"** (sole frontend owner). Colour corrections are Brand Hub's most common customer request. *With:* the Brand Hub PM and a teammate.
- **Quality & risk.** I resolved four production incidents end-to-end this year. I flagged a high-severity CVE to the C# crew with the exact dependency path, and moved services off Graylog before its decommission. I also built a Hex lookup so engineers stop querying the prod DB to diagnose Journeys errors, and the EM had it linked from the playbook.
- **Efficiency: Docker frontend builds (JC-411, I created and lead it).** PR-check compute is down ~69% per push, which projects to ~4,850 agent-hours a year. Each check runs 1.8–8.5× faster, and the deploy package build is ~41% faster in shadow. Toolchain upgrades become a code change instead of an infra ticket. *With:* DevOps and JS Crew.
- **Decision quality: AI-DLC experiment.** I ran the build phase (307/307 unit + 72/72 parity tests), and the evidence fed leadership's go/no-go call, which avoided ~2× code and ~3× maintenance.
- **People.** I review across the team, mentored four engineers this year with measurable independence gains, serve as a technical interviewer for engineering hiring, and was interim JS Crew meeting owner (Sep–Oct).

---

### What career direction interests you, and do you currently have a growth or development plan?

I want to grow into a **Tech Lead / Staff-level engineering role**, owning technical direction for a product area across teams, not just delivering within one. Longer term I'm open to engineering management. I already lead a 25-person volunteer team outside work as Director of IT for a large convention, and I enjoy the people side.

**I don't currently have a formal growth or development plan.** I keep my own record of my work and decisions, but we haven't agreed on a plan, a target level, or a timeline together. I'd like to put one in place.

---

### What skills or experiences would you like to build over the next 6 to 12 months? What would meaningful progress look like?

1. **A named technical lead role.** Ideally this is SMS Checkpoints 2–3 (UK/AU sender IDs and the Infobip→Twilio migration for ~250 customers), or the Journeys area, where the handover noted there is no named successor tech lead. *Progress:* the role is named, I own the plan and the delivery, and the migration completes with the legacy provider retired.
2. **Owning outcomes after launch, not just delivery.** *Progress:* a "90 days later" impact readout for Drip Campaigns with the PM (adoption, sends, incidents), and agreed success metrics for Brand Hub V2 before it launches.
3. **Org-wide technical direction.** *Progress:* finish the Docker builds initiative with a before/after dashboard other teams can rely on, and author a design or standard other teams build on. Having a voice in architecture review would also count.
4. **Leadership and people skills.** Leading planning and estimation, giving feedback, and more structured mentoring (I was invited to the People Team's mentorship program). *Progress:* formally mentoring at least one engineer, and leading sprint planning for my workstream.

Meaningful progress overall would be a written plan with my manager, clear criteria for the next level, and a review date where we check them.

---

### How supported do you feel by your manager? What is working well, and where would you like the support or working relationship to strengthen?

**Generally well supported day to day.** ⟨Adjust if this isn't how you feel.⟩

**Working well:**
- I'm trusted with high-priority, ambiguous work and given room to shape it. When I recommended a different staffing split for SMS, my manager took it ("we'll go with what you've recommended!").
- Feedback and recognition are timely and generous in the moment, and my manager is easy to reach on Slack.
- I appreciated the check-ins during the team merge and the departures.
- My manager raises schedule concerns early and practically (for example, adding a second engineer to SMS in October), and we re-planned together.

**Where I'd like it to strengthen:**
- **Career development, not just delivery.** I'd like more of our time spent on where I'm heading, with a written plan and a target level.
- **Formalising the role I'm already doing.** I've been working as a tech lead in practice. I'd like help making that a recognised role, or understanding what's needed to get there.
- **Advocacy and visibility.** Help making my contributions visible beyond the team, especially since the reorg changed who knows my work. I'll own my half of this: I demo often in standups and presented our builder work to the JS Crew in May, but when my features reached the formal demo slot (Drip in July, SMS in October) a teammate or the PM presented them — I'll take the presenter seat for my own features and bring finished work to org-wide venues like the Weekly Technology Meeting.
- **Workload balance.** At times I've carried SMS, AI-DLC and incident work in parallel (including some very late nights in September). I'd like us to agree on priorities and limits earlier.

---

### How are your current 1:1's with your manager used and how often are you meeting?

I have a **fortnightly 30-minute 1:1 with my EM** (a standing series since July), plus a weekly 15-minute team round-robin check-in with a rotating teammate. I don't have a standing 1:1 with my TL — that contact is ad-hoc via Slack. When a 1:1 falls during leave it lapses rather than being rescheduled.

They're mostly used for **current work**: project status, blockers, priorities for the sprint and upcoming work, team changes, and general wellbeing check-ins. Career development comes up occasionally but isn't a regular topic. ⟨Adjust to match reality.⟩

---

### What is useful, and what would make them more valuable?

**Useful:** a quick way to align on priorities and unblock things. It's also a safe space to raise concerns, and was especially useful for context during the reorg.

**More valuable:**
- **A standing career-development 1:1 roughly monthly,** separate from delivery topics, working through a written growth plan.
- **A shared running doc** of goals, feedback and agreed actions, so progress carries over between conversations and into review time.
- **Regular, specific feedback** against the next-level expectations: what I'm doing well and what's missing.
- **Visibility into upcoming work** early enough that I can put my hand up for lead opportunities (like SMS Checkpoints 2–3).

---

### What about your role expectations, priorities, success measures, or career paths needs clarification?

- **Levelling and titles after the acquisition.** What the engineering levels are now, which one I'm at, and the criteria for the next one. My title is still "Software Engineer" despite five-plus years and lead-level scope.
- **Tech Lead as a role.** Whether Tech Lead is a recognised position in the merged team structure, how someone is appointed, and whether the work I've done on SMS and Drip counts towards it.
- **The IC vs management path.** Whether there's a senior IC track (Staff or equivalent) that doesn't require moving into management, and what the management path looks like.
- **Promotion and compensation process.** How and when promotions and pay reviews happen now, and who makes the decision.
- **Success measures.** How my performance is evaluated beyond shipping: what "great" looks like for my role this year.
- **Priorities across the merged team's areas.** How much of my time should go to SMS vs Brand Hub vs Journeys vs platform work like the Docker builds, so I'm investing where the business needs it most.
