# Issues

One file per upstream issue or pull request, written so that someone can understand the problem
without opening the tracker.

## Naming

`NNNN-type-slug.md`

- `NNNN` is the upstream issue or PR number, zero-padded to the width used by that tracker.
- `type` is `bug` or `feat`.
- `slug` is a short description in lowercase hyphens.

Examples: `0026-bug-anti-repetition-prompt.md`, `0370-feat-autonomous-execution-mode.md`.

Do not rename these files. The number is the link to the tracker, and renames break every reference
to them.

## Folders

| Folder | Component |
|---|---|
| `agent-core/` | The agent loop, harness, rails and tools |
| `jiuwenswarm/` | The product layer: sessions, teams, modes, verification |
| `channels/` | Channel code: IDE plugins, web UI, browser extension |
| `summaries/` | Roll-ups that cover many issues at once |

`channels/` here means channel *code*. The shipped Channels product is documented in
`channels/overview.md` at the repository root.

## What one file contains

1. The problem as a user sees it.
2. The mechanism, with file and function names.
3. The proposed fix.
4. What was actually implemented, and what was left out.
5. How it was verified.

Keep the heading order the same across files so they can be skimmed and compared.

## Summaries

A summary in `summaries/` is not an issue file. It exists when a set of issues shares one cause, or
when a release needs a single page that says what changed across many tickets.
