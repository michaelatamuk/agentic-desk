# Cortex scope

**Draft.** This file records what is decided and what is not. Nothing here is a commitment.

## What Cortex is today

`overview.md` describes a collection of independent projects that improve the agent itself. They
fall into seven areas:

| Area | Projects |
|---|---|
| Skills | SkillTend (online maintenance), SkillForge (offline optimisation) |
| Multi-agent safety | `jiuwen_atm`: tool repair, memory guard, topology mutation |
| Runtime and isolation | MicroSwarm (thin agent runtime) |
| Agent quality | Stability, execution control, output quality, evaluation, team verification |
| Routing and context | Thalamus (context selection), optmod (local routing proxy), PerfRouter (benchmark-driven) |
| Memory | jiuwenswarm-memtier (tiered memory) |
| Observability | agent-core OpenTelemetry, TraceHound |

Each project can be used on its own. That is a strength for adoption and a problem for positioning:
"a collection of projects" is not something a customer buys.

## Why it might become middleware

Three of the areas are already the kind of thing a product would call middleware rather than a
feature:

- **Routing** decides which model answers a request.
- **Context selection** decides what the model sees.
- **Runtime** decides where the agent runs and what it may touch.

If those are sold separately from the platform, Cortex is middleware. If they stay inside the
platform, Cortex is a feature list and this folder is documentation rather than a product.

## Relationship to LAIX

LAIX sits above the agent and decides whether and when an app acts. Cortex sits inside and below the
agent and changes how the agent behaves. The overlap is real in three places:

| Question | Cortex answer today | LAIX answer |
|---|---|---|
| Which model runs? | PerfRouter, optmod | Resource policy: model tier, edge or cloud |
| What does it see? | Thalamus | Live Context: cheap detectors, deep model only when needed |
| How does it act? | MicroSwarm, `jiuwen_atm` | Execution bridge: dispatch, approve, cancel, recover |

Two layers deciding the same thing is how a platform ends up with two routing systems that disagree.

## Not decided

1. Does Cortex ship as a separate middleware product, or as features of openjiuwen?
2. Does it merge with LAIX, share a runtime with it, or stay independent?
3. For each of the three overlaps above, which layer owns the decision?
4. If they stay separate, what is the interface between them?

Answer these before either team writes code that assumes an answer. The cheapest time to decide is
now; the most expensive is after both have a scheduler.
