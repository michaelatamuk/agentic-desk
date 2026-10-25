# Migration from jiuwenswarm

This repository was created on 25 October 2026 from `jiuwenswarm` at commit `cbde92cfa`, taking the
contents of `docs-michael/` that are still being worked on.

## Method

`git fast-export` was run on the source repository, limited to the paths that move. The result was
imported into a new repository with `git fast-import`, and the files were then placed in their final
locations with `git mv`. History is preserved for every moved file:

```
git log --follow -- news/2026-10.md
```

The rest of `docs-michael` — including `usability/`, `plugins/`, `20_improvements/`, `full_prompt/`
and the per-feature plan folders — was not exported and remains in `jiuwenswarm`.

## What moved

| From `jiuwenswarm/docs-michael/` | To `agentic-desk/` |
|---|---|
| `agentic-news/` | `news/` (with `drafts/` and `archive/`) |
| `issues/` | `openjiuwen/issues/` |
| `whats-new/` | `openjiuwen/whats-new/` |
| `agentic-platform/` | `apps/` |
| `publishing_apps/` | `apps/publishing/` |
| `agent-operating-environment.md` | `openjiuwen/operating-environment.md` |
| `robotic-reasoning-brain.md` | `openjiuwen/robot-brain.md` |
| `new_audiences_discovery.md` | `openjiuwen/audiences.md` |
| `modes.md`, `teampulse-*.md` | `openjiuwen/ideas/` |
| `research-flow-improvement-plan.md` | `openjiuwen/assessments/research-flow.md` |
| `agentic-stack-vertical.md` | `apps/stack.md` |
| `mini-product-ideas.md`, `killer-ideas.md`, `viral-app-thinking.md` | `apps/ideas/` |
| `build-*.md`, `taketwo-architecture.md` | `apps/builds/` |
| `50_Multimodal_Agent_Apps_v2.pptx` | `apps/multimodal-agent-apps.pptx` |
| `openjiuwen-cortex.md` | `cortex/overview.md` |
| `openjiuwen-channels.md` | `channels/overview.md` |
| `competitor-mechanisms-and-demos.md`, `harness-comparison.md`, `laya-study.md`, `icode-architecture.md` | `research/`, with dates added to the snapshots |
| `Channels.jpeg`, `Cortex.jpeg` | `assets/images/` |
| `_archive/` | `archive/` |

91 files moved. `news/2026-10-v3.md` became `news/2026-10.md`; the long news version became
`news/drafts/2026-10-news.md`, the five-story cut became `news/drafts/2026-10-cut.md`, and
`2026-10-alt.md` became `news/archive/2026-10-alt.md`.

## What did not move

Everything that describes or plans code: `usability/` (165 files), `plugins/` (14),
`20_improvements/` (6), `full_prompt/` (2), `browser/`, `mobile/`, `sdk/`, `teams/`, `tracehound/`,
`vibestudio/`, and `Implementation.Overview.md`. They belong next to the code they document.

## Reproducing the split

From `jiuwenswarm`:

```powershell
$paths = @('docs-michael/agentic-news', 'docs-michael/issues', ...)
$arg = ($paths | ForEach-Object { '"' + $_ + '"' }) -join ' '
cmd /c "git fast-export New-Features-Integration -- $arg > export.fi"
```

In the new repository:

```powershell
git init -b main
cmd /c "git fast-import < export.fi"
git checkout -f New-Features-Integration
git branch -m main
```

Then move the files with `git mv` and commit. Do not copy files by hand; a copy loses the history
that shows why the current version exists.

## Pending

`docs-michael/` still holds the original files. Delete it from `jiuwenswarm` only after this
repository has been reviewed, and leave a short `docs-michael/MOVED.md` pointing here so existing
links do not dead-end.
