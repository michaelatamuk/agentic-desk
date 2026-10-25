# Plugins

A proposal for making agent-core and jiuwenswarm configurable instead of hard-coded: behaviour comes
from a composition file, not from editing the core.

**State:** design proposal, not scheduled, not implemented.

## The idea in three lines

- `agent-core` is the framework: contracts, the loop, the loader. It runs standalone.
- `agent-tools` holds generic implementations any integrator may use, ignore, or replace.
- `jiuwenswarm` is one product: its composition plus product-specific plugins.

Dependency runs one way: `agent-core` ← `agent-tools` ← `jiuwenswarm`.

## Reading order

1. `rewrite.md` — the full proposal: what is hard-coded today, the target shape, the migration.
2. `architecture.md` — the system at a glance, for someone new to the codebase.
3. `types.md` — what kinds of plugin exist, and which layer owns each.
4. `placement.md` — which layer a given piece of code belongs in.
5. `responsibilities.md` — who maintains contracts, security and compatibility.
6. `config-example.md` and `config-example.json` — what the end state looks like to a user.

## Background

The model being copied is DeepSeek's harness kernel, studied in
`industry/studies/deepseek-harness.md`.

## Not in this folder

The three per-repo implementation plans, the phased programme overview and the Jiuwen2DSH variant
remain in `jiuwenswarm/docs-michael/plugins/`. They are build sequences for one branch, not the idea.
