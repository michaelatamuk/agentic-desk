# Idea filters — what makes a new app worth building

Use this before writing a concept note or a roadmap. It is the upstream test; the
[Stage Playbook](stage-playbook.md) is the downstream test for how the demo is performed.

The short version: **a new app must be a place a role returns to for different tasks, with one
physical verb, a trust beat and a real wedge — not a productive workbench, a control room or a
dashboard with animations.**

---

## The experience

- **Not a productive app at demo stage.** It can be productive later; the demo must be 100% sexy.
- **No slides, no next-next, no dashboard tour.** If the audience watches screens change, it fails.
- **One hero verb.** The presenter does one physical thing: drag a lens, scrub time, move the sun,
  paint a world, capture a meeting.
- **Immediate consequence.** Something visible changes because of the interaction.
- **A memorable metaphor.** Lens, flood, shadow, evidence web, capture — not "a workspace with
  panels."
- **A 90-second arc:** cold open → first touch → agent works → trust beat → audience choice → reveal.
- **The AI must be wrong once.** The human rejects it; the system re-ranks. That is the 2026 trust
  story.
- **Audience agency.** The room makes one real decision with a visible consequence.
- **A repeatable line.** One sentence the audience can say afterwards.

## The weekly demo — what SD's cadence teaches

SD is not built as one launch. It is built as a cadence. In roughly three months it landed **272
feature commits, 329 test commits, 582 fixes, 198 docs commits and 91 CI commits**, with release tags
every few weeks and visible capability changes weekly or biweekly.

What the commits actually add:

- **UI-visible slices:** desktop workbench, project/session management, settings, artifact preview,
  CSV/table viewer, onboarding, sample session, interface language, error diagnostics.
- **Trust features:** consent, permissions, sandboxing, reviewer, execution machines, remote runners,
  audit and provenance.
- **Platform breadth:** model providers, skills, Claude Code/Codex, MCP, connectors, memory, remote
  execution.
- **Quality:** tests, docs, CI gates and release notes ship alongside features.
- **Onboarding:** first-run, sample session, guided tour and model setup are product features, not
  demo debt.

The pattern to copy:

1. **One visible capability per cycle.** A manager can see it in 30 seconds.
2. **One proof point.** A test, benchmark, audit, benchmark case or before/after number.
3. **One trust feature.** Consent, permissions, sandboxing, provenance or audit.
4. **One adoption feature.** Sample data, first-run, onboarding, language or a repeatable demo path.
5. **One "next".** End every demo with what ships next.
6. **Compound.** Each release should make the next demo easier and the platform story stronger.
7. **Release notes as a narrative.** One human-written highlight, generated counts underneath.
8. **Quality is part of the show.** A feature that ships with tests and docs is more demoable than a
   feature that only works once.

**What managers want to see:**

- What changed for the user?
- How do we know it works?
- Is it safe and governed?
- Will people actually use it?
- What does it save: time, cost, risk?
- What is next?
- Can I try it or forward it?

**The weekly demo filter:**

- Can a manager understand it in 30 seconds?
- Can it ship as a visible slice in 1–2 weeks?
- What proof moves?
- What trust or safety story does it strengthen?
- What does it compound with?
- Does it show a platform capability — tool use, memory, trace, evaluation — not just a prompt?
- What is the next release?
- Can it be demoed twice without drift?

**Sustained excitement = cadence × compounding × proof × narrative.**
Excitement without cadence dies. Cadence without compounding becomes feature sprawl.

**Conference cut vs manager cut:** the conference is 90 seconds of emotion, one verb and an audience
choice. The manager demo is 10 minutes of proof, adoption, safety and roadmap. They are two cuts of the
same core — do not build two products.

## The usage pattern

- **People should come back for different tasks, not just different cases.**
- **"Different task" beats "different incident."** A new flood is a new case; a new investigation,
  report, brief or alert is a different task.
- **Task breadth matters more than screen count.** Many screens around one job is a dashboard museum.
- **The role's day should pass through it** — a queue, a project, a shift, a session.
- **Daily is ideal, but not mandatory.** If it is project-based, sell to the production company/team,
  not the freelancer.
- **Vertical is fine if it is broad.** Vertical market + many tasks (SD, RootCause) can be daily.
  Vertical + one task (GeoResponse) is event-driven.
- **Horizontal = many industries/roles.** Do not confuse horizontal market with horizontal task
  breadth.

## The domain

- **The domain must be inherently sexy.** Construction was rejected. Space, music, fashion, forensic
  trust, live shows and private memory are emotionally legible.
- **Not "control something."** No command centres, dispatch, live control, monitoring consoles or
  operations rooms.
- **Creation, exploration, verification or communication** is the right shape.
- **A deep artifact/canvas** — a site, a stage, an orbit, a session, a memory — not a form.
- **A real buyer and a real pain**, not just a cool demo.

## The market

- **Check for a red ocean.** If it already exists, do not enter with "better." Enter with a different
  job, segment or value curve.
- **A sharp wedge beats a broad platform.**
- **Avoid AI chat wrappers** and "Copilot for X."
- **Why now?** A 2026 reason: agents, multimodal, on-device, regulation, privacy, cost.
- **Why this team?** A distribution, data or workflow advantage.

## The technology

- **NPU only if it is structural**, not acceleration.
- The test: **would the product still work if inference moved to the cloud?** If yes, the NPU is not
  the reason.
- Real NPU reasons: privacy, latency, offline, always-on, chain of custody, low power.
- **No fake NPU story.** Optional hardware is better than hardware-dependent.
- **The demo must be offline, deterministic, resettable and have a fallback.**

## Platform leverage — agent or wrapper?

A direct LLM call is not a sin. A thin wrapper presented as an agentic platform is.

The test: **what does the platform uniquely enable that the product needs?**

- If nothing, the product can still be good — but it is not evidence for the platform.
- If orchestration, tools, memory, skills, sandboxing, evaluation, provenance, model routing,
  on-prem/NPU or governance matter, the platform must be the backbone and visible in the demo.

| Level | What it looks like | What a manager sees |
|---|---|---|
| Prompt wrapper | One call → text | A generated answer |
| Tool-using agent | Plan → tools → evidence → human | Work being done |
| Platform-native | Orchestration, memory, skills, connectors, sandbox, eval, provenance, model routing, NPU | A system that compounds |

**Platform filter:**

- Is this platform-native, hybrid or deliberately standalone?
- What does openjiuwen / PPMA uniquely enable here?
- Where is the agentic loop visible: tools, memory, citations, recovery, audit?
- Remove the platform — does the product still work? If yes, the platform is a plugin, not the moat.
- Does the demo show the platform, not just the output?
- If direct LLM is the right choice, does the product say “LLM-assisted” instead of “agentic
  platform”?

**Red flags:**

- It is a prompt wrapper wearing an “agentic” badge.
- The platform is a logo, not the architecture.
- The demo hides the agent trace.
- A direct cloud LLM sits inside a privacy/offline/NPU promise.
- There is no evaluation, provenance or failure story.

## The ecosystem

- **Complement, don't compete.** Strong fit with PPMA: RECALL captures; PPMA remembers and acts.
- **Clear boundaries and a contract.** What each product owns, what it refuses to do, how data moves.
- **One product's output is another's input.**
- **Integration is distribution**, not just plumbing.

## The business

- **Named user, named buyer, budget, pilot, recurring revenue.**
- **Measure the right thing:** task families per user per month, return trigger and time-to-value —
  not just DAU.
- **Data rights, consent and licensing are first-class**, not footnotes.
- **Demo cost should be low:** no special hardware, no live network, no customer data.

## The red flags

- It is a workbench.
- It is a control room.
- It is a dashboard with animations.
- It is a single-task vertical tool.
- It is an event-only console.
- It is a crowded market with no wedge.
- It needs hardware to be impressive.
- The NPU is only for speed.
- It is a prompt wrapper wearing an “agentic” badge.
- The platform is a logo, not the architecture.
- The demo hides the agent trace.
- A direct cloud LLM sits inside a privacy/offline/NPU promise.
- The demo needs the presenter to explain why it matters.
- It competes with PPMA instead of feeding it.
- It has only an architecture story, with no visible 1–2 week slice.
- It needs a big-bang launch to be impressive.
- The demo is a one-off, not a repeatable path.
- Every release is a random feature, not a compounding platform.
- There is no proof, trust or adoption story for managers.

## The 10-question filter

1. What is the one verb?
2. Who returns tomorrow, and why?
3. How many task families does the role really own?
4. Is it creation/verification, or control?
5. What is the 90-second stage moment?
6. What is the trust beat?
7. Where is the NPU structural?
8. Who is the buyer and what is the wedge?
9. What does it integrate with — and what does it refuse to do?
10. What is the line the audience repeats?

---

## How to use this

1. Write the one-sentence idea.
2. Answer the 10 questions in order.
3. If any of the first four answers are weak, stop and reshape the idea.
4. Decide **platform-native, hybrid or standalone**; if platform-native, define the visible agentic loop.
5. Define the **1–2 week visible slice**, the **manager proof** and the **next release**.
6. Only then write the concept note.
7. Only after the concept survives, write the stage-first roadmap.
8. Before the first demo, record the 90-second conference cut and the 10-minute manager cut.

The non-negotiables are **not** that every idea must be daily, horizontal or NPU-native. They are:

- it is not a control room,
- it has one hero verb and one trust beat,
- the role has more than one task,
- a claimed NPU is structural,
- it complements the ecosystem instead of duplicating it.
