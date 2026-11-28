# What's New in JiuwenSwarm — November 2026

November changed the unit of work from a task to a team. A team can hold a goal, its leader can run on
Claude Code or Codex, each member can start its own workflow and carry its own shell and settings, and
Word, Excel and PowerPoint became one workspace. The month also added the surfaces around that work: a
Memory page, a reverse-engineering workbench, system-level plugins, floating app companions and a
stricter enterprise configuration chain. About 2,200 commits landed across the two repositories in
four weeks.

*Last updated: 2026-11-28.*

## What JiuwenSwarm is

JiuwenSwarm is a platform for running AI agents. It runs the agent loop — ask the model what to do,
call the tool it names, feed the result back — and adds sessions (the record of one conversation),
memory, tools (the actions an agent can call), skills (packaged instructions), teams and connections
to chat apps. Several products in the company run their agent work on it; DigitalMate is one.

The Python package is published as **`workswarm`**, which is why some products call the same platform
**WorkSwarm**.

## What runs underneath

Two repositories make the platform:

1. **`agent-core`** — the base runtime and the code that runs one agent: the loop, tools, prompts,
   memory, teams and the harness that hosts another agent product.
2. **`jiuwenswarm`** — the server around it: channels (web, desktop, IDE, TUI), the gateway that
   connects chat apps to agents, skills, the enterprise layer and the Office add-in.

Products sit on top of both and call them through the gateway or the Python API.

A **harness** is the code that runs one agent: its prompt, its model calls and its tool loop. The
built-in harness is the one JiuwenSwarm ships; Claude Code and Codex are external harnesses.

**Coverage** — read from the newest `origin/develop` in both repositories on 28 November:

| Repository | Commit | Merged | What it is |
|---|---|---|---|
| `agent-core` | `e60add22a` | 2026-11-28 15:38 +08:00 | MCP `call_tool` timeout forwarding |
| `jiuwenswarm` | `1586ff3e7` | 2026-11-28 15:38 +08:00 | thinking language follows the match rule |

Not read this edition: the enterprise deployment environments and the cloud images.

Everything here is tagged:

- **[NEW]** — a capability that did not exist before.
- **[UPGRADE]** — an existing capability re-worked until it feels new.

---

# The big things

## 1. A team can hold a goal, not just a task list — [NEW]

A team is one leader agent plus member agents working from a shared task board. The board says what
is done; a goal says what the task must achieve. A member opens a goal when it claims a task, and
before it can mark the task done, its completion claim is checked. A refusal comes back with the
remaining work attached, and the member keeps working. If the goal reaches its attempt limit it turns
**BLOCKED** and reports to the leader, who can take over.

The leader has a goal of its own: it opens after the user's message is delivered, stays open until
the other members are idle, and gates whether the team can finish. `NativeHarness` has its own stop
rule, and `spawn_teammate(goal=...)` opts a member in. On 20 November the leader goal became a
setting: scheduling mode has a leader sub-switch, the leader and member policies are validated
together, and the leader's completion assessment runs in its own trace.

Why it matters: a team can no longer call a task finished just because a member says so. Nine
end-to-end cases cover a lazy member whose first submission is refused, a reviewer round that re-opens
the goal, a mid-run reassignment, and a member whose goal blocks at its limit. Members on someone
else's harness, human members and bridge members are outside this scope.

## 2. The team leader can run on Claude Code or Codex — [NEW]

`LeaderSpec.cli_agent` names an entry in `external_cli_agents`. The team leader then runs on the
Claude or Codex SDK harness instead of the built-in one. It keeps the leader tools — `build_team`,
`create_task`, `view_task`, `spawn_teammate`, `shutdown_member` — and the leader prompts, and it
continues across runs inside the same session. When the team enables swarmflow, the external leader
holds `swarmflow` and the asynchronous task tools, so it can start and collect workflows.

Forking the team is refused with an external leader. The path was exercised with real Claude Code
2.1.305 and `codex-cli`, including a Claude leader with a Claude teammate and a Codex leader with a
Codex teammate. Pause on a provider that can abort but cannot pause now degrades to a graceful abort.
One operational catch: the Codex SDK can prefer its bundled CLI over the one on `PATH`, so point
`cli_path` at the current binary. An external leader still does not get a fork, team memory or the
failure-reliability channel.

## 3. Every teammate can start its own workflow — [NEW]

`swarmflow` starts a workflow: an asynchronous run whose steps are executed by worker agents, with the
result injected back into the conversation. Until now only the leader could call it; a member that
needed a workflow had to ask the leader, which put every run's narration, result and pause inside the
leader's context.

The tool now opens to in-process teammates. A teammate starts its own run, pauses and resumes it, and
consumes its own result. The shared machinery — worker model resolution, the concurrency governor and
the budget ledger — is built once by the leader and shared by reference, so every run draws on one
pool with one set of limits.

Two details define it: every progress event names its **executor**, and narration and result injection
follow that field; and resume follows the work, so a paused run goes back to the member that last
executed it if it is online. Shutting down a member stops and seals the runs it owns and leaves its
neighbours alone. A Claude Code or Codex member can be given the same tool through its host; the
end-to-end tests covered in-process members.

## 4. Every teammate gets its own shell and settings — [NEW]

Two members in one process used to share the process environment, so a `git` author, a proxy or a
token could leak from one to the other. `ExecutionEnvironment` now holds immutable `values` and
`overrides` (a null value deletes), resolved at each tool call and bound in a context manager that
restores the previous scope on error or cancel. The order is: the host's base environment, then
`values`, then explicit call arguments, then `overrides`. Local shell execution merges into a copy;
the sandbox receives only the differences, so a host environment is never copied in.

Settings live per session in `team_session_settings`, a JSON blob with a version, written with an
atomic check-and-set. They survive member rebuilds, cold recovery and cross-process calls. The platform
resolver reads the shared database on every tool call; if the database is unreachable it fails rather
than silently falling back to an old value. Environment values are redacted in execution logs.

## 5. Word, Excel and PowerPoint become one workspace — [UPGRADE]

The add-in now serves PowerPoint, Word and Excel from one build, with a manifest per application. The
pane attaches the open document to a conversation and runs that conversation's tools inside the
document; the add-in and the server read the same `tools.json` and `profile.json`.

Word and Excel attach, chat, answer the backend's approvals and questions, and show each turn's tool
calls; their tools arrive with their own contracts. PowerPoint runs the read-only tools and builds
and edits slides as native objects with `presentation_apply_patch`. Each turn that wrote has an undo
icon: new slides are deleted, changed and deleted slides are re-inserted from exports, and the deck's
order is restored. Code the model writes against a slide's XML runs in a sandbox worker, and a patch
that fails part way rolls itself back.

The three Office applications need PowerPointApi 1.8, WordApi 1.6 and ExcelApi 1.13. WPS Writer and
Spreadsheets arrived on 19 November; WPS Presentation is not covered.

## 6. An AI colleague for every employee — [NEW]

The beta2 AI-colleague feature (`jiuwenmate`) merged into `develop`. Each employee gets a colleague
with a persona template, a chosen set of capabilities and published configuration versions. Editing
and publishing are separate: a request keeps the version it was accepted with until a new one is
published.

Colleagues are available in web private chat, WeLink and DingTalk, and since 20 November in SwarmChat
group chats, where they can be added to a group and reply when mentioned. They answer approvals, run
scheduled tasks and use the CLI. The default colleague, 小九 (Xiao Jiu), is created once and is not
recreated after a user deletes it.

## 7. Memory becomes a page you can manage — [NEW]

Memory gets an entry in the left navigation and a switch under Settings → Memory → Memory management,
off by default. The page shows the personal memories the Memory service permits, with its own model
settings; the Swarm chat model stays separate. It is a view and a control, not a new memory engine:
closing it does not stop recall, extraction or tools.

The month also added team document memory and a bundled memory plugin, so Work, Code and Team modes
can share one document runtime while keeping their access boundaries. The page needs a Memory build
that supports the Portal; the locked JiuwenMemory 0.2.1 supports reads and writes, but not the Portal
or its model settings.

## 8. A reverse-engineering workbench — [NEW]

A new **Reverse** area has a guided setup page for Node.js, the REA runtime and the REA MCP server.
MCP is the standard way the platform connects external tools to an agent. The page installs and detects
capability cards for Ghidra, IDA, Kuna, Hopper, Frida, GDB, JADX, apktool, browser and Electron
analysis, and reports each card as available, installing, needs configuration, partial or failed, with
one remaining-time estimate for the whole task.

The inventory in this checkout lists **229 tools in 77 groups**: decompiling, function analysis,
Frida and GDB sessions, APK and firmware inspection, SQLite, PCAP and WASM inspection, browser and
Electron capture, evidence bundles and reconstruction-coverage checks. It is a workbench around the
existing agent, not a new model or a new agent platform. Commercial tools such as IDA still need their
own licence and upstream MCP setup.

## 9. System plugins become packages — [NEW]

A system plugin can now ship as a bundle package, with a system-plugin market page, install, update,
uninstall and recovery states, and a token-weather example. A development skill and a DeepSeek Harness
plugin converter turn an existing plugin into a JiuwenSwarm system plugin.

This changes what a system plugin can carry — multiple components, their assets and their lifecycle —
without replacing the existing plugin API. It also gives the platform a place to publish and recover
system-level capabilities that are not tied to one agent.

## 10. Floating app surfaces and team companions — [NEW]

An app can publish a surface in **desktop** mode (a separate native window) or **overlay** mode (a
floating surface inside the app, with the workspace still visible). In overlay mode the plugin
receives input inside the surface rectangle, the host keeps it inside the app viewport, and closing it
destroys the container and reports `ui.closed` back to the plugin.

Team sessions gain member child windows and the leader's public replies. Only the desktop client can
open child windows; overlay mode has no child-window path. Overlay mode also does not support native
screenshot transitions or hit testing.

## 11. Enterprise data and policy move behind one gateway — [UPGRADE]

Enterprise checkpoints now land in MySQL or PostgreSQL; the personal edition keeps SQLite. The same
gateway serves both editions, with a team control store (stable `team_id`, owner, lifecycle, human
memberships), team quota and route binding, and E2A (Everything-to-Agent) in `openjiuwen-protocol`.
Web session list, rename and pin go through E2A in both editions.

Policy became explicit. The execution guard is its own template slot instead of being driven by a
model row's retry count. Per-agent Keycloak credentials can be selected for MCP calls, the agent
identity is carried in the user context, workspace quotas and a usage bar arrived, and the Swarmflow
policy can come from the expert package template.

## 12. A workflow you can install as a skill — [NEW]

`skillpack_distill` takes a completed multi-skill workflow and distils it into a SkillPack: a root
`SKILL.md` that describes an ordered workflow over ordinary skills. Nested packs and swarm-style skills
are refused as members, so a pack stays a plain composition of single-agent skills.

Installation is confirmed and transactional. You inspect the plan — members and instructions — and
confirm. The ZIP is thin: a plugin wrapper, the root instructions and `skillpack.lock.json`, with no
member sources inside. The lock records Hub asset IDs, exact versions and SHA-256 digests; missing
members are fetched from the same Hub. Reuse requires matching provenance, version, digest and
unchanged local content. A failure restores directories and registration, and startup recovers an
interrupted commit. Uninstalling a pack keeps its members; uninstalling a skill that a pack uses is
blocked.

A complete query match can offer the pack directly, bypassing the workflow composer. Routing has three
modes — `off`, `shadow` (evaluate and log only) and `confirm` — and the product entry points are off by
default.

## 13. The agent learns from its own runs, now as a plugin — [UPGRADE]

TTSE (Two-Track Self-Evolution) reads past runs and writes two kinds of notes: facts about the
environment (FACT) and hints about which capability to use (TIP). Later prompts include the notes. It
never rewrites `SKILL.md` and never asks for approval. It is the sibling of skill-body evolution.

On 3 November it became a native plugin for the main coding agent, built on the generic plugin runtime
(contract v1). Code mode gets TTSE only that way; agent and work modes keep the built-in rail behind
`react.ttse.enabled`, still off by default. Banks are kept per mode, under `.ttse/work/` and
`.ttse/code/`, never inside your project. Auto-dream removes expired notes, merges near-duplicates and
deletes low-quality ones on fixed intervals. Installing the plugin does not switch tracing on.

---

# The rest, by theme

These are the remaining changes that matter to a product reader. The list is not exhaustive.

## Teams and orchestration

- **SwarmChat rounds**: collaboration-space sessions run as explicit rounds, each with saved state and
  its own lifetime for background model tasks, so a round resumes after a restart.
- **Group routing**: plain conversation and substantive work are separated; task cards fold inside the
  group; workers clean up after an abnormal exit; a process identity fingerprint still matches after a
  clock change.
- **Group auto-reply**: an unmentioned request can be routed to an expert, and a group can coordinate a
  team instead of waiting for a mention.
- **Stopped approvals**: a native member that stops with an unread approval card can be restarted from
  its original checkpoint instead of blocking the team's completion.
- **Interrupts**: clients echo the `interrupt_id`; interrupts are told apart by kind; a permission
  answer is bound to the interrupt that asked for it.
- **Notifications**: targeted group notifications reach the member they name.
- **External members**: an external harness member now gets the team's execution environment, so its
  Git identity no longer falls back to the host's.
- **Team memory**: document memory and a team memory rail share one runtime while keeping per-member
  access boundaries.
- **Host-managed members**: a host can register an existing AI colleague as a group member without
  starting another runtime; each session can use its own Git identity.
- **Smaller fixes**: SwarmChat compression events; a display-only `label` on `VerifyVote`; task
  attribution in `view_task`; grouped swarmflow traces; the routed model named in model-group calls;
  expert category tabs from loaded data; members can be removed dynamically; human-member deliveries;
  batch expert-team invitations.

## Clients and channels

- **Client attachments**: a client attaches to one conversation, binds a stable resource key, runs that
  conversation's tools and renews a lease. One resource belongs to one conversation.
- **HarmonyOS**: Huawei login sessions and a local connection between processes on the phone.
- **WeLink**: several assistants share a reader with a confirmed handoff; the channel gains mail and
  calendar capabilities.
- **DingTalk**: employee authorization, group collaboration and employee CLI capabilities.
- **Appearance**: a settings module for interface font, interface size and code font.
- **Voice**: full-duplex ships its speech-recognition bundle; the lost voice-transcription
  configuration and empty recording results are fixed.
- **Workspace panel**: a file viewer, a usage bar and a quota banner in the web workspace.
- **Session restart recovery**: large histories restore without the memory amplification, and
  in-flight streams resume after reconnecting to the local process.

## Platform

- **ACP and Multica**: a native ACP provider, thinking options, remote MCP transports and a Multica
  runtime entry point let an external agent connect through ACP without a bespoke adapter.
- **Sandbox**: the `yuanrong` sandbox provider became `adx`; the AIO provider gets a written contract;
  JiuwenBox kills a Windows process group; shell commands gain process ownership, output directories
  and a registry.
- **MCP**: `call_tool` timeouts now reach the stdio and Playwright clients; entry-level `ssl_verify` for
  dynamic token requests; an end-to-end check of the enterprise two-token flow.
- **Models**: an OpenAI Responses request-parameter fallback; Anthropic disabled-thinking and output
  limit handling; reasoning profiles; GLM-5.3-Flash reasoning levels.
- **Capability index**: one search for skills, experts and MCP servers; a directly configured
  `ReActAgent` can load skills on demand with `SkillUseRail`, without a `DeepAgent`.
- **Coding memory**: native file memory or Jiuwen document memory, selected in `config.yaml`, local
  hashing vectors by default, reloads without a restart.
- **Connector sources**: a standard source interface, with the App Hub as the first source.
- **Symphony**: expert task planning and task-tier routing; dynamic sub-agents.
- **React agent**: a structured termination reason on every finish; cancel context and empty-response
  handling.
- **Observability**: an export gate separates "collect a trace" from "export it"; a sequence store
  shares repeated trajectory prefixes; cost, TPOT and served-model attributes reach LLM spans.
- **Personal context**: the coding agent can cap its personal context, merge and retire entries, and
  count tokens per run; local Markdown and Office workbook fetch feed the same store.
- **Gateway**: request tracing across routing and message handling; team and agent tracing read one
  configuration; compatibility specs for runtime data and stream boundaries; explicit message-queue
  wire settings.
- **Packaging and deployment**: the Dockerfiles consolidate under `jiuwenswarm-ee`; an i18n catalog
  covers common messages; an edition gate separates personal and enterprise behavior; the updater
  recognises `uv` editable installs.
- **Compatibility**: A2A terminal streaming marks the last chunk; jiuwenbox handles team members; the
  runtime-data compatibility spec records the regression evidence next to the contract.

## Self-evolution

- **PromptSearchOptimizer**: a multi-candidate prompt search loop scores candidates on correctness,
  completeness, latency, tokens and cost, penalises drift from the objective, and detects overfitting
  on held-out cases.
- **RSI promotion**: Harness tasks score from 0 to 1; a target must beat its frozen baseline by more
  than 0.05, every target must stay improved and no non-target may regress by more than 0.05 before a
  promotion.
- **Harness package preview**: a package can be inspected before promotion; a worker-shutdown bug is
  fixed.

## Content and plugins

- **Google provider**: on top of Sheets and Slides, the cloud-document module gains Docs, comments and
  discovery.
- **Background music**: Design generates music through vLLM-Omni or OpenRouter Lyria.
- **Designer continuity**: crowd presence is decided by the agent and exits by the storyboard, so a
  crowd no longer disappears between shots.
- **SkillPack hardening**: parallel validation no longer times out; an explicit selection does not
  double-confirm; packs are reusable across sessions; Windows long paths work; a duplicate plugin
  install prompts instead of replacing silently.
- **Medical knowledge base**: a DeepSearch plugin for clinical guidelines with hybrid retrieval,
  citations and a 2024-versus-2020 comparison.
- **Topic recommendations**: suggestions appear before the session, not only mid-conversation.
- **Office files**: personal context collects `.docx`; file reading handles GBK text plus `.docx` and
  `.xlsx`; the Office pane gained a version check and no longer schedules work.
- **Built-in tools**: `generate_chart` and `diff_files` join the tool set.
- **App Hub**: apps published to the Hub can be installed locally with a run-consent prompt, a bound
  project and an update that keeps `data/` and `.git`; the market panel handles install, update,
  uninstall and local publish.
- **Email**: the web conversation reads `.eml` and Outlook `.msg` through `read_email`.
- **App market**: apps can declare AI roles, and the detail page shows the role cards, avatars and
  team conversation notes.

---

# Still open

Some of these are in progress, some are built but off by default, and some are deliberate limits. This
is not a release schedule.

- **An external leader cannot fork a team**, and it does not get team memory or the failure-reliability
  channel yet.
- **Goal checks do not cover every kind of member.** Members on someone else's harness, human members
  and bridge members are outside the scope.
- **External-CLI members are not covered by the swarmflow end-to-end tests.** Their contract cannot
  support a background run and later follow-ups.
- **WPS Presentation is not covered.** Writer and Spreadsheets panes exist; Presentation is not.
- **App Hub has not met the real Hub.** Its tests use a mocked Hub; the real network, download and
  process start were not covered.
- **AI colleagues in group chats have not run end to end.** No real model, Feishu, DingTalk or WeLink
  test yet.
- **SkillPack routing is off by default.** So is the shortcut that offers a complete query match
  directly to the user.
- **TTSE is still off by default**; installing the plugin does not turn tracing on.
- **The Memory page needs a newer Memory build.** It is off by default; the locked JiuwenMemory 0.2.1
  supports reads and writes, but not the Portal or its model settings.
- **The REA setup has no recorded cross-platform install run.** The page, its states and the runtime
  handoff are in the repository; a full install on Windows, macOS and Linux is not recorded here.
- **Team approval recovery is narrow.** It covers same-process native members with a known
  checkpoint. External-CLI, human and bridge members are outside it.
- **The enterprise chain is only partly proven.** Execution-guard binding has one cluster log;
  Swarmflow policy and per-agent Keycloak credentials are covered by unit tests and a simulated
  Gateway, not a full enterprise run. An execution-guard template can stay cached for up to an hour.
- **Floating surfaces have a desktop limit.** Member child windows need the desktop client; overlay
  mode does not support screenshot transitions or hit testing, and the real desktop E2E was not run.
- **Microsoft email is read-only.** `.eml` and `.msg` are read up to 20 MiB; encrypted or RTF-only
  messages, and Outlook contacts, calendar items and tasks, are not read.

---

# See also

- [October 2026](whats-new-2026-10.md)
- [JiuwenSwarm, explained simply](../overview.md)
