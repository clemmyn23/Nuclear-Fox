<!--
CONFERENCE / MEETUP CFP — built from your existing internal talk "Preparing IT Infrastructure for an Anime Convention" (CM eng retreat, Jun 2025, on YouTube).
You've already given it once — that de-risks the proposal massively. This packages it for an external submission.
-->

# Conference / Meetup CFP — "Running Production IT for a 45,000-Person Event"

You already delivered a version of this internally (engineering-wide retreat, Jun 2025 — [recording](https://www.youtube.com/watch?v=bBZFJ9uXrbU)). That means: proven material, existing slides, and a video you can attach to a submission. Submitting externally is high-leverage senior signal and great LinkedIn/portfolio fodder.

## Title options
1. **Running Production IT for a 45,000-Person Event (with a Volunteer Team)**
2. **Zero Critical Failures, Five Years Running: Reliability Lessons from the Convention Floor**
3. **The Network Always Dies at Doors-Open: Building IT That Survives a Live Event**

## Abstract — short (≈60 words, for the submission form)
> Every year, a 25-person volunteer team stands up the IT behind one of Australia's largest conventions — ticketing, networking, access control, and live incident response for 45,000+ attendees — and it has to work the first time, on the day, with no second chances. This talk covers the architecture, the DevOps, and the people decisions that have delivered five consecutive events with zero critical failures.

## Abstract — long (≈150 words, for the program)
> Most production systems get retries, rollbacks, and a quiet Tuesday to fix things. Live events get none of that: the date doesn't move, 45,000 people show up in a two-hour window, and the venue network will betray you at the worst moment.
>
> As Director of IT for SMASH! — one of Australia's largest pop-culture conventions — I'll walk through how a 25-person volunteer engineering team designs for that constraint: offline-tolerant door-scanning, ticketing at burst scale, access control, and on-site incident response. I'll cover the hardware and DevOps realities you don't hit in a data centre, the architectural choices that trade features for "works under stress," and — just as importantly — how you lead, delegate, and keep morale in a volunteer org where you can't pay anyone. Five years, zero critical failures, and a lot of lessons that transfer straight back to everyday software engineering.

## Talk outline (≈30–40 min)
1. The constraint nobody else has: an immovable date + a burst crowd + a hostile network (5m)
2. Architecture: ticketing + offline-first scanning + access tiers (8m)
3. The DevOps/hardware reality of a venue, not a cloud (6m)
4. Incident response when "roll back" isn't an option (6m)
5. The people problem: leading 25 volunteers, delegation, morale, succession (6m)
6. What it taught me that transfers to "normal" engineering (4m)
7. Q&A

## Key takeaways (organisers love these explicit)
- How to design for availability when you have *one shot* and a bad network.
- Why "works under stress" beats "does everything" under a hard deadline.
- Reliability and incident practices that transfer from events to any production system.
- Leading and retaining a technical team with zero financial leverage.

## Audience & level
Intermediate; relevant to backend, SRE/DevOps, and engineering leaders. No event-industry knowledge needed.

## Speaker bio (≈60 words)
> Clement Ng is a senior software engineer (Campaign Monitor / Marigold) with 8+ years across SaaS, real-time systems, and event-scale infrastructure. He's also Director of IT for SMASH!, one of Australia's largest conventions, where he's helped grow the technology and team from five founding engineers to a 25-person operation serving 45,000+ attendees — with a five-year zero-critical-failure record.

## Where to submit (Sydney / AU, general — check current CFP status yourself)
- **DDD Sydney** (community, very accessible for a first external talk)
- **Local meetups** — SydJS, Sydney .NET User Group, DevOps Sydney, SRE-flavoured meetups (low barrier; great warm-up)
- **YOW! / NDC Sydney** (bigger; the existing recording strengthens these)
- Internal-first option: offer it at a future company event at your *next* employer as an onboarding-era visibility move.

## Submission tips
- Attach the existing recording — a proven talk is a huge de-risk for organisers.
- Lead the pitch with the *constraint* ("immovable date, burst crowd, bad network"); it's instantly intriguing and not the usual conference fare.
- Meetups first (fast yes, low stakes), then pitch the bigger confs with "previously delivered at …".
