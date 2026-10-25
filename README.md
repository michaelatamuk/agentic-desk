# agentic-desk

Notes and analysis on agentic AI: a monthly industry briefing, the platform we build on, and the
apps and middleware we are building on top of it.

## Contents

| Folder | Contents |
|---|---|
| `industry/` | Monthly briefing on the industry, and studies of what others built |
| `projects/` | The things we work on — see below |
| `strategy/` | Direction across the projects: what we build and why |

## Projects

| Folder | Contents |
|---|---|
| `projects/openjiuwen/` | Issue write-ups, release notes, code studies and design proposals |
| `projects/middleware/laix/` | LAIX, a decision layer between apps and the platform |
| `projects/middleware/cortex/` | Cortex, plugins that extend the platform |
| `projects/apps/` | Apps built on top of the platform, and the interface they may use |
| `projects/apps/max/` | Max, the smart home app: product, algorithms and demo |
| `projects/channels/` | Channels, the shipped surfaces, as portfolio material |

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

## History

Split out of `jiuwenswarm/docs-michael` on 25 October 2026 (source commit `cbde92cfa`). File history
was exported with `git fast-export`, so `git log --follow` works on every file here.
