# LAIX interfaces

**Draft, nothing here is agreed.** LAIX has two boundaries. Both need a written contract before
either side writes code.

## North: what an app sees

An app should be able to use LAIX without knowing which platform runs underneath.

| The app provides | LAIX provides |
|---|---|
| The experience: screens, audio, sensors, user goals | A decision: wait, ask, guide, act, verify, escalate |
| The outcome it wants to improve | A measurement of whether the action helped |
| Its user's constraints: latency, cost, interruption tolerance | A policy that respects them |
| Approval for destructive actions | A request for that approval at the right moment |

## South: what LAIX needs from the agentic platform

| Need | Why |
|---|---|
| Run a named skill with typed arguments | LAIX decides; the platform executes |
| Cancel a running action | The situation changed |
| Ask for approval and receive a decision | The action is destructive |
| Read and write session state | Experience state outlives one turn |
| Stream events with trace ids | Cost, latency and debugging |
| A model capability level, not a model name | Portability across platforms |

The last row is the important one. If LAIX names models, it is tied to one platform's catalogue.

## Boundary with Cortex

Cortex and LAIX overlap on model routing, context selection and execution. See
`cortex/scope.md` for the three decisions that have to be made before this contract can be final.

## Open questions

1. Does LAIX own the experience state, or does the platform? If both, which one is authoritative
   after a reconnect?
2. Is the decision engine a service, a library linked into the app, or both? The deck proposes an
   edge library for decisions under one second and a cloud service for state and learning — that is
   two implementations of one policy.
3. Where does the outcome measurement run? It needs data the app has and the platform does not.
4. What happens when LAIX decides to act and the platform refuses? The failure path is not described
   in the brief.
