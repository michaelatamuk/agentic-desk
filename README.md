# agentic-desk

Working notes on agentic AI: the monthly industry briefing, the platform we build on, the apps we
build, LAIX, Cortex, Channels, and the research behind them.

This repository is writing, not code. Product code and the documents that describe it stay in
`jiuwenswarm`.

## Where things are

| Folder | What it holds |
|---|---|
| `news/` | The monthly agentic AI briefing, one canonical file per month |
| `openjiuwen/` | Issue write-ups, release notes, ideas and assessments for the platform we build on |
| `apps/` | Apps built on top of an agentic platform, treated as a black box |
| `laix/` | LAIX, the middleware between apps and agentic platforms |
| `cortex/` | Cortex, middleware ideas that may or may not join LAIX |
| `channels/` | Channels, the shipped surfaces, kept as portfolio material |
| `research/` | Other companies, other harnesses, other projects |
| `assets/` | Shared images and decks |
| `archive/` | Superseded material, kept for history |

Every file at the root of this repository is this README or a migration record. Documents live in a
folder.

## Rules

1. **A folder is a project you work on.** If a document does not belong to one of the projects
   above, it belongs in `research/` (about someone else) or `news/` (about the industry).
2. **A file is named for what it is.** `laix/overview.md`, `cortex/scope.md`,
   `openjiuwen/operating-environment.md`. Lowercase, hyphens, no spaces.
3. **Dates go on snapshots only.** `research/2026-10-06-competitor-mechanisms.md` will not be
   updated, so it carries its date. `apps/pitch.md` is edited in place, so it does not.
4. **One canonical file per month.** `news/2026-10.md` is the briefing for October. Variants live in
   `news/drafts/` and never ship. Superseded months move to `news/archive/`.
5. **Issue files keep the upstream number.** `openjiuwen/issues/agent-core/0026-...` is traceable to
   the ticket; do not rename it to a nicer title.
6. **No `v2`, `final`, `new` or `old` in a shipped filename.** Git keeps the versions.

## What does not live here

Anything that describes or plans code: `Implementation.Overview.md`, `full_prompt/`, `plugins/`,
`20_improvements/`, `browser/`, `mobile/`, `sdk/`, `teams/`, `tracehound/`, `vibestudio/`, and the
`usability/` dataset. Those stay in `jiuwenswarm/docs-michael/` because they would go stale if
separated from the code they describe.

The test when a document is ambiguous: **will I revise this in the next two months, and is it
written for a person rather than for the build?** Yes to both means it belongs here.

## Cadence

- `news/` — one briefing per month. Process in `news/PROCESS.md`, format in `news/FORMAT.md`.
- `openjiuwen/whats-new/` — one release note per month that ships something.
- Everything else is written when there is something to say, not on a schedule.

## History

This repository was split out of `jiuwenswarm` with full file history. See `MIGRATION.md` for what
moved, what stayed, and how the split was done.
