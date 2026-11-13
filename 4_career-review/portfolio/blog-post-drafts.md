<!--
ENGINEERING BLOG-POST DRAFTS — portfolio content that doubles as interview talking points.
Built from real work (CRM-Lite LDR + the WorkflowLookupService migration). Sanitised: feature names only, no confidential internals.
⟨add detail⟩ = a real specific you can drop in. Don't invent metrics. Run past your employer's policy before publishing anything tied to CM.
-->

# Engineering Blog-Post Drafts

Two posts drawn from real work. Publishing these (dev.to, Medium, your own site, LinkedIn articles) is strong senior-signal portfolio content — and writing them sharpens the exact stories you'll tell in interviews. **Check CM's external-writing policy first; keep it to public feature names + general engineering lessons, not internal specifics.**

---

## POST 1 — "How do you know a distributed job is *done*?"
*~900–1200 words when finished. This is your strongest topic — it's a genuinely under-discussed problem and it's your own insight.*

**Draft opening:**
> Marking a task as "done" sounds trivial. It is — right up until the task is "process an unknown, changing number of records spread across systems you don't fully control." Then "are we done yet?" becomes one of the more interesting problems you'll design around.
>
> I hit this building a feature that backfilled every one of a customer's contacts — potentially millions, spread across many lists — into a single de-duplicated view. The work fanned out across a queue and flowed through an asynchronous pipeline I didn't own. There was no single moment where a thing could declare "complete."

**Outline:**
1. **The setup** — a paged fan-out (1,000 records per message, self-re-enqueuing) feeding an async contact pipeline that dedupes by email. ⟨add: the rough scale you designed for⟩
2. **Why "done" is hard** — the last message *you* send isn't the last *work* done; the pipeline is downstream and async; list size can change mid-job (people keep importing).
3. **Options I weighed:**
   - Pipeline emits a completion event back → cleanest, but it didn't exist.
   - Poll the DB on a schedule → works, but I dislike scheduled polling of hot tables; needs an index; feels like a workaround.
   - Time-bounded reconciliation → a `Finalising` state set when the last batch is emitted, flipped to `Complete` once `updated_at + buffer < now`, with a completion estimate of `queue wait + (record_count × pipeline throughput) + buffer`.
4. **The call** — went with the time-bounded approach as the pragmatic option, documented the dislike of polling, and named the "real fix" (a pipeline completion event) as future work.
5. **The lesson** — "done" in distributed systems is often a *probabilistic, time-bounded judgment*, not an event. Make the tradeoff explicit rather than pretending you have a crisp signal.

**Why it's a great post:** most "system design" content is rate-limiters and URL shorteners; this is a real, subtle problem with a non-obvious answer and an honest tradeoff. Reviewers and interviewers remember it.

---

## POST 2 — "What three reverts taught me about pulling a service out of a monolith"
*~800–1000 words. The resilience/maturity story, told honestly.*

**Draft opening:**
> Some migrations land on the first try. This one took three. I'm going to tell you about the two that got reverted, because that's where the actual lessons were.
>
> The job: lift a workflow-lookup service out of a 15-year-old .NET-Framework monolith into a standalone .NET Core gRPC service — without changing behaviour that live customer journeys depended on.

**Outline:**
1. **Why move it at all** — ⟨the real driver: decoupling / .NET Core / scaling / ownership⟩.
2. **Attempt 1 → revert** — ⟨what broke under production load that didn't show in test⟩. The lesson: ⟨e.g. prod traffic shape ≠ test⟩.
3. **Attempt 2 → revert** — ⟨what the second attempt fixed and what it still missed⟩.
4. **Attempt 3 → landed** — ⟨what was different: the change you made between tries⟩.
5. **Lessons:** reverting fast is a feature, not a failure; the gap between test and prod for a legacy service; how to de-risk the next extraction (shadow traffic, incremental cutover, feature-flagged routing — ⟨which you used⟩).
6. **Close** — extracting from a long-lived monolith is as much about *observability and rollback discipline* as it is about the code.

**Why it's a great post:** engineers respect honesty about reverts far more than a flawless-hero narrative; it signals exactly the maturity a Staff/senior interview probes for.

---

## Bonus topic ideas (one-liners, if you want a series)
- "Front-end build modernisation in a giant monolith: yarn workspaces → Vite → Webpack 5, one bundle at a time."
- "Running zero-downtime IT for a 45,000-person event with a volunteer team of 25." (Crosses into your SMASH talk — pairs with the conference CFP.)
- "Why I write the design doc before the code — and what a good Lightweight Design Review looks like."

## Publishing notes
- Lead with the problem, not your résumé; let the competence show through the reasoning.
- Every ⟨add detail⟩ is a real specific to insert — but never fabricate a metric to make a post punchier. "It took three attempts" is more credible than a made-up "40% latency reduction."
- Cross-post to LinkedIn (ties to the rewrite in `cv/linkedin-rewrite.md`) — it's the cheapest senior-signal you can manufacture.

---

## 🆕 Draft idea #3 (2026-11): "When a retry costs money: idempotency for third-party onboarding"
*Source: your SMS compliance-embed work. See interview/system-design-sms-compliance-provisioning.md. Generalise names before publishing and check your employer's blogging policy.*

**Hook:** "Our first version of the provisioning endpoint would have bought a second phone number every time a customer double-clicked."

**Outline**
1. The shape of the problem: a slow third party, a step that costs money, and a registration that can't be rolled back.
2. Why a random idempotency key isn't enough: two tabs, two admins and a support-tool retry are *different requests* for the *same intent*. Derive the key from the invariant (one number per customer).
3. Validate before you spend: region and eligibility checks before the purchase call.
4. Treating a 409 as success: "already exists" means "continue".
5. Upstream gateways lie: handling non-JSON 502/504s as typed errors.
6. Consolidating side-effect paths: three provisioning flows into one, idempotent on re-run.
7. Rolling out something irreversible: sales-led first, flags per region, a human in the loop.
8. The code we correctly didn't write: parking a status poller until the event stream existed.

**Closing line:** "Exactly-once is a property of your *outcomes*, not your *calls*."

## 🆕 Draft idea #4: "The AI migration we didn't ship"
1. The experiment: an AI-driven Node→C# port, 6 units, a parity harness (307/307 + 72/72).
2. Where AI-driven development shone: scaffolding and parity tests.
3. Where it looped: 2.5 days of back-and-forth, and the moment to call time.
4. The real cost model: 16k lines to replace 8k, observability lost, an irreversible data migration.
5. Why "no" was the valuable output, and what we reused.
