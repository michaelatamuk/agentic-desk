# agentic-desk

Notes and analysis on agentic AI: a monthly industry briefing, the platform we build on, the apps and
middleware we are building on top of it, and products our company builds elsewhere.

## Contents

| Folder | Contents |
|---|---|
| `industry/` | Monthly briefing on the industry, and studies of what others built |
| `projects/` | The things we work on - see below |
| `company/` | Company products and platforms; context, not our roadmap |

## Projects

| Folder | Contents |
|---|---|
| `projects/strategy/` | Our proposal for what to build on top of Jiuwen: the three parts, what not to build, where to start |
| `projects/openjiuwen/` | Our work in openJiuwen: issue write-ups and design proposals |
| `projects/middleware/laix/` | LAIX, a decision layer between apps and the platform |
| `projects/middleware/cortex/` | Cortex, plugins that extend the platform |
| `projects/apps/` | Apps built on top of the platform, and the interface they may use |
| `projects/apps/max/` | Max, the smart home app: product, algorithms and demo |
| `projects/openjiuwen/channels/` | Channels, the shipped surfaces, as portfolio material |

## Company products and platforms

Products and platforms built by the company. Most belong to other teams; openJiuwen is one we
contribute to. They are context and comparison; we do not own their roadmap. See `company/README.md`
for the boundary.

| Folder | Contents |
|---|---|
| `company/openjiuwen/` | openJiuwen, the company platform we contribute to: product context, code studies and release notes; our work is under `projects/openjiuwen/` |
| `company/ppma/` | PPMA, a memory-first agent that manages ongoing projects: the four directions, the loop and everyday scenarios |
| `company/digitalmate/` | DigitalMate, the HarmonyOS task app |
| `company/opendirector/` | OpenDirector, a local AI video creation workspace |
| `company/agentdescent/` | AgentDescent, a research framework for evolving prompts, skills, agent directories and code |
| `company/nullius/` | Nullius, a local AI evaluation workbench for benchmarks, agents and evidence |
| `company/flybot/` | FlyBot, a self-hosted workspace for AI agents, conversations and teamwork |
| `company/belle/` | Belle, an AI coworker for team chat, built primarily on JiuwenSwarm |
| `company/mobilegym/` | MobileGym, a browser-hosted mobile GUI agent simulator and benchmark |
| `company/hopa/` | HOPA, a phone-operating personal assistant with a hard payment gate |
| `company/orbit/` | Orbit, the per-user cloud engine behind DigitalMate |
| `company/sciencediscovery/` | ScienceDiscovery, a local research workspace built on JiuwenSwarm |

## Conventions

File names are lowercase with hyphens. A document revised in place has no date; a snapshot opens
with `YYYY-MM-DD`.

`industry/briefings/` holds one canonical briefing per month, with drafts in
`industry/briefings/drafts/` and superseded months in `industry/briefings/archive/`.

Issue files keep the upstream number and type, for example
`projects/openjiuwen/issues/agent-core/0026-bug-anti-repetition-prompt.md`.

## Briefings

The research process is in `industry/briefings/PROCESS.md`; the structure is in
`industry/briefings/FORMAT.md`. Studies of other companies and projects that feed the briefing are
in `industry/studies/`.

Product what's-new editions live in `company/<product>/whats-new/` and are written to stand alone:
each opens with what the product is and what runs underneath it. The format and process are in
`company/digitalmate/whats-new/FORMAT.md` and `PROCESS.md`.

## History

Split out of `jiuwenswarm/docs-michael` on 25 October 2026 (source commit `cbde92cfa`). File history
was exported with `git fast-export`, so `git log --follow` works on every file here.
