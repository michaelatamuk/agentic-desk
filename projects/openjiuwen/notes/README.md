# Notes

Studies of how openjiuwen works inside, written while reading the code. They are not official
documentation and not release notes. Some are the only explanation that exists for a subsystem;
others cover behaviour that no document mentions.

## Structure

One folder per subsystem, named after the code it covers. A folder is created when the first note
for that area is written; add a row here when you create one.

| Folder | Covers |
|---|---|
| `prompts/` | How the model context is assembled |
| `sessions/` | Session lifecycle, persistence and resume |
| `teams/` | Team dispatch, tasks and member workspaces |
| `tools/` | Tool registration, execution and results |
| `memory/` | Memory tiers, retention and retrieval |
| `gateway/` | Protocol, channels and transport |
| `runtime/` | Loops, rails, budgets and stop conditions |
| `observability/` | Traces, replay and diagnostics |

Depth stops at the subsystem: `notes/prompts/context-assembly.md`. A note that needs its own
subfolder is a signal that the subsystem deserves one, not that the note needs nesting.

## Provenance

A note is true for a specific commit, not for the project in general. Put the code it describes on
the second line, and list the source paths it relies on:

```
Code: openjiuwen agent-core @ <sha> (<version>) · jiuwenswarm <branch> @ <sha> · <date>
Files: openjiuwen/harness/prompts/sections/, openjiuwen/harness/prompts/assembler.py
```

Before reusing a note, check whether anything it quotes has moved:

```powershell
git log --oneline <sha>..origin/<branch> -- <the paths on the Files line>
```

The two prompt notes predate this rule and still need a stamp.

## Naming

Name the note for the question it answers, not for the file it documents: `context-assembly.md`,
`layer-order.md`, `session-resume.md`. Lowercase, hyphens, no dates — the stamp carries the date.
