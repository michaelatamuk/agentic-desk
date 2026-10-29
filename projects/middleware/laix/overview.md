# LAIX — brief overview

LAIX is the decision layer for the right moment. It sits between an AI app and the agentic platform
underneath it, deciding whether, when and how the app acts, and reusing the platform, the serving
engine and the models below it instead of replacing them.

> Converted from `assets/LAIX_Brief_Overview_v1.0.pptx` (11 slides). Slides that contain only
> diagrams are noted but not reproduced. **Every number in this document is a 2027 target, not a
> result.**

## The problem

Models, agents and multimodal input and output work. What is missing is the application intelligence
that runs an experience over time. Most AI apps are still request and response: the user carries the
context and the timing. They interrupt at the wrong moment, stay silent when help is needed, and
never check whether the help worked.

The enemy is **mistiming**.

The deck lists five challenges that every live AI app hits:

| # | Challenge | Why today's tools do not solve it |
|---|---|---|
| 1 | **Continuous state** — what is happening now, toward which goal, how certain, over seconds to sessions | Chat history and agent memory store what was said or planned, not the live situation |
| 2 | **Right action, right moment** — wait, ask, guide or act without interrupting | Still open for frontier video models, which either spam or go silent |
| 3 | **Compute cost and latency** — always-on multimodal reasoning on every frame is slow and expensive | Serving engines make each call cheaper; nobody decides which calls are worth making |
| 4 | **No outcome measurement** — did the cue improve the next rep, did the user find the object | Apps optimise clicks or satisfaction, not measured improvement |
| 5 | **Rebuilt in every app** — timers, thresholds, session state and feedback logic are hand-coded per app | No reusable layer, so delivery is slow and nothing is learned across apps |

Challenges 1–3 are verified from vendor documentation and papers. Challenges 4–5 are a hypothesis:
the deck estimates they cost 30–50% of engineering effort, to be validated in Q1 2027.

## The proposed layer

Three layers. LAIX builds only the middle one.

| Layer | Contents |
|---|---|
| **L1 · Apps** | Sports coach, accessibility, cooking, creative, news, future apps |
| **L2 · LAIX** | Live Context, Experience State, Decision Engine, Execution bridge, Outcome Learning, Resource policy |
| **L3 · Existing infrastructure** | openJiuwen / WorkSwarm (agents, skills, memory, tracing), vLLM-Omni (omni-modal serving), speech, vision and language models, edge detectors, Huawei Cloud and Ascend |

LAIX itself is six components:

- **Live Context** — cheap detectors run always; a deep model is called only when the situation is
  relevant or uncertain.
- **Experience State** — goal, phase, beliefs with confidence, expiry and past actions.
- **Decision Engine** — chooses wait, ask, guide, act, verify or escalate under cost, latency,
  interruption and risk constraints. This is the centre of the proposal.
- **Execution bridge** — dispatches to platform skills, with approval, cancel and recovery.
- **Outcome Learning** — measures whether each action helped and adapts per user and per app.
- **Resource policy** — model tier, edge or cloud, and skipping inference when it is not needed.

The loop is: observe, understand, maintain state, decide, act, verify, adapt.

[`laix-architecture-overview.png`](laix-architecture-overview.png) is the one-page picture: inputs from
users, devices and apps on the left; the five stages — perceive, decide, orchestrate, share and
collaborate, adapt and learn — in the middle; Digital Mate, PPMA and JiuwenSwarm/Orbit on the right;
and the key capabilities, technologies, component boundaries and value underneath.

Delivered as a runtime plus a Python and TypeScript SDK, evaluation and observability tools, and
three reference apps. An edge library handles decisions under one second; a cloud service handles
state, learning and evaluation.

## The product

LAIX is a runtime and SDK for product teams building live AI apps. The end user never opens LAIX;
they feel the result in the app.

The first product is the decision layer behind a real reference app — the coach — not a new app
studio, and not another agent framework.

| Question | Answer |
|---|---|
| Who buys? | The product team building a live AI app |
| What do they get? | A decision layer: state, timing, action, verification and outcome learning |
| What do they stop building? | Their own timers, thresholds, confidence scoring and outcome loop |
| First reference app | The coach: one real app, one clear outcome |
| Proof | Intervention precision, +15% outcome, −30% model calls, ≥60% reuse |
| Price | A paid pilot, then an SDK/runtime licence or usage-based fee |
| Why not build in-house? | Time, evaluation data, reuse across apps, safety |
| What it is not | A model, an agent framework, or an app studio |

## Six-month proof

One engine, one reference app and three proofs — timing, outcome and reuse — in six months. The ten
decision classes are the test suite; the coach is the first story.

## How it differs

| Existing | What it does well | The gap LAIX fills |
|---|---|---|
| Realtime APIs (OpenAI, Gemini Live) | Live voice and video, tools | No goal state, no outcome learning |
| Agent frameworks (LangGraph, openJiuwen) | Plans, tools, memory | Not timing-aware or perception-aware |
| Serving (vLLM-Omni) | Fast, cheap model calls | Does not decide which calls to make |
| Vertical apps (Be My AI, form coaches) | Good single-domain experience | Hand-coded, not reusable |
| **LAIX** | Reuses all of the above | The decision layer for the right moment: timing, outcome and reuse |

The deck is explicit about what LAIX is not: not another model, agent framework, assistant or app
studio.

## Technical approach

| Component | Approach | 2027 target |
|---|---|---|
| Continuous context | Event-driven perception: lightweight detectors find change, uncertainty or anomalies; deep multimodal models are triggered selectively | Deep-model calls per session |
| Experience state | Temporal state graph, Bayesian belief updates, confidence decay and expiry, tracking goals, observations and past actions | Decision quality with and without state |
| Decision intelligence | Contextual bandits and constrained Markov decision processes, choosing an action by expected benefit, interruption cost, latency and risk | Intervention precision ≥ 85% |
| Outcome learning | Causal attribution where possible, bandit feedback otherwise, learning which interventions improve measured outcomes | User outcome +15% against baseline |
| Adaptive inference | Cascaded inference, uncertainty-based escalation, adaptive sampling, edge and cloud routing under latency and cost budgets | −30% deep-model calls, ≤ 1 s response |
| Reliable execution | Event-driven state machines over platform skills, with approval gates, verification, timeouts, cancellation and recovery | Verified-action rate, safe recovery |

Design principle: safety rules first, learned policies only when the data justifies them. LAIX builds
the decision layer and reuses openJiuwen, vLLM-Omni and the models.

## Targets

All targets are for 2027. The baseline is the same models plus a stateful agent that decides timing
with a language model.

| Metric | Target |
|---|---|
| User outcome | +15% task success or measured improvement |
| Intervention precision | ≥ 85%, meaning AI acts only when experts agree it should |
| Deep-model calls | −30% at the same or better quality |
| Response timing | ≤ 1 s after the right moment |
| Core reuse | ≥ 60% of runtime components unchanged across three apps |
| Developer effort | ≤ 50% of today's time to build a live feature |

Method: controlled user studies (for the coach, about 24 users across 6 sessions), expert-annotated
decisions, A/B tests in the reference apps, and quarterly go/no-go gates.

## Demos

These already exist. They are test beds for one technology across four timescales, not five
products.

| Demo | Today | What it proves | 2027 role |
|---|---|---|---|
| Personal sports coach | Pose-based coaching | Continuous perception, cue timing, measurable gain | Flagship 1 |
| Fridge to recipe | One-shot recipe from a photo | Task state, changing constraints, approved actions | Flagship 2 |
| Object finder for visually impaired users | Object recognition from images | Uncertainty: get a better view, verify, escalate | Flagship 3 |
| InkWell | Children's book from an idea | Creative state across sessions | Reuse probe |
| News in One Minute | Daily one-minute summary | Personal priorities, story continuity over days | Reuse probe |

Timescales: seconds (object finding), minutes (coaching, cooking), sessions (creative), days (news).
No new demos are planned for 2027.

## 2027 plan

| Quarter | Work | Gate |
|---|---|---|
| Q1 | 15+ developer and product-team interviews, strong baselines set up, reference architecture, experience-state runtime v0, sports-coach baseline instrumented | Problem confirmed by ≥ 60% of teams; no overlap with internal Huawei projects |
| Q2 | Live Context integration, hybrid decision engine (rules, language model, calibrated scorer), first closed loop end to end on the coach, first user-outcome study | Intervention precision ≥ 80% and beats the strong baseline |
| Q3 | Outcome learning from logged data, cooking app on the same runtime, reuse and cost measurement, SDK v0.5, accessibility lab protocol with a partner | ≥ 60% reuse; −20% cost per useful action |
| Q4 | Three reference apps on one runtime, LAIX-Bench, documentation, open-source release candidate, one external pilot and one paper | +15% user outcome; pilot letter of intent leading to a 2028 decision |

Team: 11 people — architecture and integration 1, context and state 2, decision intelligence 3,
outcome and efficiency 2, SDK and reference apps 3.

End-2027 deliverables: runtime plus SDK, three reference apps, LAIX-Bench, KPI study results, an
open-source release candidate.

Out of scope: models, serving engine, agent framework, new demos. Dependencies: openJiuwen,
vLLM-Omni, Huawei Cloud, an accessibility partner.

## Decks

Two decks sit in this folder.

| File | What it is |
|---|---|
| [`laix-brief-overview-v1.0.pptx`](laix-brief-overview-v1.0.pptx) | The original LAIX proposal: the problem, the layer, the product, the six-month proof, technical approach, targets, demos and the 2027 plan. Slides 1, 2, 5, 7, 8 and 9 are diagrams and images only, so those points are not in the text above. |
| [`laix-system-1-decision-v1.1.pptx`](laix-system-1-decision-v1.1.pptx) | A later deck, made after v1.0, with suggestions for our development work, LAIX included. All eight slides are images; there is no text layer to search or quote. |

If an image-only slide carries a decision, write it down in this file.

Every slide is also exported as a PNG under [`slides/`](slides/), named by slide number and the title
at the top of the slide.

## See also

- [The LAIX case](laix-case.md) — the decision layer for the right moment, and its symbiosis with
  PPMA.
