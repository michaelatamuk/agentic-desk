# Nullius, explained simply

**One-page summary:** [`nullius-onepages.svg`](nullius-onepages.svg).

*As of 28 November 2026. Sources: the repository at `main@d0c6777`, version 0.2.0, its README, concepts, standard, architecture, builder, results and supported-agent documentation. Nullius is built by another team in the company. This note is context, not our roadmap.*

## The short version

- **Nullius is a local workbench for evaluating AI agents.** You run a benchmark against an agent, and it opens every score into the evidence behind it.
- The point is to answer a harder question than “what was the score?”: **did the agent fail, or did the benchmark fail?**
- It uses **controls**: an empty agent (`nop`) should score nothing, and a reference answer (`oracle`) should score everything. If those checks fail, the task is suspect.
- It brings benchmarks, agents and capabilities in through a **catalogue** and a **proof system**. A benchmark says which abilities it needs; an agent proves those abilities with a test kit; only proven pairs are offered.
- It runs on this machine, an SSH host, several machines, containers or Harbor, and reads Nullius/Harbor jobs plus ATIF and OpenTelemetry exports.
- It is **Beta, version 0.2.0**, Apache-2.0, Python 3.12+, with a local web UI at `127.0.0.1:5057`. It is not a model or an agent; it is the evaluation layer around them.

## What it is

The Latin tag is **Nullius in verba** — “take nobody’s word for it.” That is the product idea.

A benchmark score usually hides its own production. A low number could mean the agent was bad, the harness was broken, the model was rate-limited, a setup step failed, a file was missing, or the benchmark’s verifier is wrong. Nullius keeps the run, the trial, the verifier report, the conversation, the trace, the tool calls and the output files together, so a reader can see which of those happened.

It is an **evaluation framework and a viewer**, not an agent framework. It drives agents, scores them and shows the evidence; it does not try to be the agent.

## The four things a failure can be

Nullius separates the causes instead of collapsing them into “failed”:

| Branch | What it means | Where it goes |
|---|---|---|
| **The agent failed** | The task was reached; the tests failed, no patch was produced, or the agent raised an error. | Counted as a miss. |
| **Never reached it** | Rate limits, API errors, setup errors, missing infrastructure. | Counted in raw solve rate; excluded from adjusted solve rate. |
| **Unknown** | The trial left no verdict. | Kept in the denominator; shown as `—`, not 0%. |
| **The benchmark failed** | A control found the task broken. | Feasibility view; the task should not be trusted. |

That is why the headline is not one number. Nullius reports **raw solve rate** (all trials), **adjusted solve rate** (leaving out infrastructure failures) and **mean score** (for graded benchmarks). The gap between raw and adjusted is the cost of infrastructure; it does not tell you what the excluded tasks would have scored.

## Controls: checking the benchmark

Every run starts with two checks beside the agent:

- **`nop`** does nothing. It should score **0**.
- **`oracle`** applies the reference answer. It should score **all**.

If `nop` passes or `oracle` fails, the verifier cannot be trusted on that dataset. The README gives the concrete example: GSM8K at `openai/grade-school-math@3101c7d` gives `nop` 0/1319 and `oracle` 1319/1319. A benchmark that fails this is not a hard benchmark; it is a broken one.

The standard also checks that the units come out the same twice and that no answer sits in the prompt. That is the difference between “the agent is bad” and “the task is bad.”

## The standard: ports and proofs

The most interesting design is the **Nullius standard**. It replaces ad hoc “we wrote a script for this benchmark” integrations with three rules:

| Idea | Rule |
|---|---|
| **Ports, not tags** | A port is a named, versioned contract, such as `agent.workspace/v1`. A benchmark lists the ports it needs; an agent or capability lists the ports it offers. A pair fits only when every needed port is offered. |
| **A claim is proven, not written** | A port enters the agent’s offer list only through its conformance kit. A claim whose basic checks later fail is taken back. |
| **Nullius stands in the middle** | It starts the agent, hands it the workspace, and acts as its model endpoint. A relay holds the key and records every call. |

The version-1 ports include:

- `agent.task/v1` — one prompt in, one answer out.
- `agent.workspace/v1` — the agent reads and writes files in the unit’s workspace.
- `agent.tools/v1` — the agent calls MCP tools, including decoys, chains and retries.
- `agent.conversation/v1` — several prompts in one session, with memory of earlier turns.
- `agent.search/v1` — search a collection, find a source and answer with evidence.
- `agent.browser/v1` — a browser through an MCP server.
- `agent.computer/v1` — a desktop seen in screenshots and driven by mouse and keyboard.
- `cap.memory/v1` — add a session and recall facts from it.

A proof records which checks and skills passed, and which kit version it used. That is why the catalogue can show, honestly, that an agent fits some benchmarks and not others. A refusal names the missing port instead of silently skipping the benchmark.

This is the part worth copying: **an integration is a proof, not a claim**, and a benchmark’s needs are explicit.

## Bringing things in

The catalogue has three kinds of entry: **benchmarks**, **agents** and **capabilities**. Bundled entries are read-only; a user entry overrides a bundled one by whole folder. Additions go in the user catalogue and survive application upgrades.

The import path is a prompt for a coding assistant:

- `/import-benchmark`
- `/import-standard`
- `/import-agent`
- `/import-capability`

The import skill pins the upstream, wraps its own code, proves it and reports what fits. It asks before adding any code of its own. There is also a manual path.

The bundled catalogue includes benchmarks such as GAIA, GSM8K, HumanEval, OSWorld 1/2, SWE-bench Verified, τ³-bench, Terminal-Bench 2.0, LoCoMo, LongMemEval and Open Telco. Agents include Codex, Goose, OpenCode, mini-SWE-agent, SWE-agent, Terminus-2, **DigitalMate** and **JiuwenSwarm**. Capabilities include Mem0.

## How a run works

The **Run builder** is a sequence of choices:

```text
Runner → Benchmark → Dataset → Agent → Model → Limits → Where → Review
```

- **Runner:** Nullius standard, or Harbor, or a benchmark’s own “Original” scripts.
- **Benchmark and dataset:** the tasks and the scorer.
- **Agent and model:** only agents that proved the benchmark’s ports are offered. A model is chosen separately; “Like the paper” keeps the paper’s fixed models, “Like the leaderboard” keeps the leaderboard’s rules, and “Any of your choice” lets you change them.
- **Limits:** task count, name filter, concurrency, attempts, retries, timeouts, spending caps, call caps, turns per conversation.
- **Where:** this machine, an SSH host, several machines (one shard each), a container, or a Boat VM.
- **Review:** checks every prerequisite, then runs only when you press **Run**.

A **launch** starts one or more **runs**; a run is one agent on the launch’s tasks; a **trial** is one task attempted by one run. The controls are runs too. Several agents and datasets can run in one launch, each as its own job.

On the standard path, Nullius:

1. Starts the benchmark’s driver, which fills the unit’s workspace and returns the prompt, or what to add and recall for a capability.
2. Starts the agent in that workspace over **ACP** (Agent Client Protocol), or calls the capability over JSON lines.
3. Routes model calls through a **relay** that holds the key and records every call.
4. Scores the result with the benchmark’s verifier.
5. Writes a Harbor-shaped job: one trial per unit, `result.json`, `events.jsonl`, the agent trajectory, the trace, verifier output and the relay record.

The **local backend is not a sandbox**: an agent runs as you, in the unit’s workspace, and the run is refused without `--unsandboxed`. The **container backend** gives each unit its own container, with the relay as a sidecar and the key only in the relay. The **Boat backend** puts each unit in its own VM. The safety section is explicit about all three.

## Reading the evidence

A trial opens into:

- **Outcome and error** — did it reach the task, or fail in setup or a provider call?
- **Verifier report** — which check accepted or rejected it?
- **Conversation and tool calls** — what the agent did.
- **Trace** — call timing and failures, where recorded.
- **Artifacts** — files the attempt produced.
- **Judgement** — a judge model’s answers, if you asked for one.

The **judge** is optional and paid. It never gates the run; it is a second opinion kept beside the evidence. `Reconcile` shows where the judge disagrees with the recorded outcome.

**Compare** puts the same benchmark before and after a change beside each other: the tasks both runs share, the ones that disagree first, then a task-by-task view. It warns that a different task set alone can move the score, so check dataset, model, agent and setup before attributing a change.

## What you can open

Nullius is not only a runner. It opens results it did not produce:

| Input | What it does |
|---|---|
| **Nullius and Harbor jobs** | Opens the same Harbor-shaped job directories. |
| **ATIF trajectories** | Converts them into one job. |
| **OpenTelemetry spans** | Converts OTLP/JSON span exports into one job. |

That makes it useful as a viewer for evaluation results from other teams, not only as a runner.

## Local by design

- The web UI is loopback by default. The network is used to serve a run (model calls, installs, a host), registry lookups and judge calls, nothing else.
- Sources are not overwritten. Bundled resources are read-only; user entries go in the user catalogue.
- Settings, licences, user catalogue entries and runs live outside the installed package. `nullius paths` shows where; `NULLIUS_HOME` selects a separate profile.
- Provider keys are saved in Settings and stay on the Nullius host. The agent never sees the key; the relay does.
- Logs are redacted; the relay names credentials but never their values.
- A real run can call paid APIs. The controls call no agent, but a judge or embedding model can still be called. Review names what the run will do.

## Status and limits

- **Version 0.2.0**, classifier **Beta**. The repository is active daily; `main` was at 27 November 2026 when this note was written.
- **Apache-2.0**, with bundled fonts under the SIL Open Font License.
- **Python 3.12+**, `uv`, Docker or Podman for the container backend, and Docker for Harbor. Flask is the only runtime dependency; the backend is designed to run without Flask.
- **Not a hosted service.** It is a local workbench with a web UI and a CLI; there is no multi-tenant leaderboard service in the repository.
- **Evaluation quality depends on the controls and the verifier.** A benchmark with no controls has no evidence of validity. A judge is a second opinion, not a gate.
- **The local backend is not a sandbox.** Use the container or Boat backend when that matters.
- **The catalogue is a proof system, not a universal compatibility layer.** An agent that lacks a port is not offered for a benchmark that needs it.

## How it relates to our products

This is the most useful part for us: Nullius already lists **DigitalMate** and **JiuwenSwarm** as supported agents.

| Agent | What the catalogue says |
|---|---|
| **DigitalMate** | Its Personal Agent service, run as Hive Home with its owned WorkSwarm runtimes. The default `0.1.13` proves one-task and search; `0.1.13-fixes` also proves workspace files, MCP tools and conversation. It fits GSM8K, HumanEval, Open Telco, GAIA, SWE-bench Verified, τ³-bench and Terminal-Bench 2.0. It does **not** prove computer use, so OSWorld is not offered. |
| **JiuwenSwarm** | The openJiuwen WorkSwarm agent, driven over ACP from PyPI. The default `0.2.8` proves one-task, workspace files, MCP tools, conversation and search; it fits GAIA, GSM8K, HumanEval, Open Telco, SWE-bench Verified, τ³-bench and Terminal-Bench 2.0. It does **not** prove computer use, so OSWorld is not offered. The `0.2.9` entry currently lacks `agent.search/v1`, so GAIA is not offered for that version. |
| **AgentDescent** | Same public repository owner (ThinkFlowLab), adjacent layer. AgentDescent improves an artifact; Nullius evaluates the agent and shows evidence. There is no wired integration, but a Nullius benchmark result is exactly the kind of evidence AgentDescent’s held-out gate needs. |
| **OpenDirector** | Same public repository owner. OpenDirector is a video creation app; Nullius is an evaluation platform. No direct integration today. |
| **PPMA / Orbit** | No catalogue entries. They could be added if they expose an ACP agent or a command; the standard is the integration path. |
| **ScienceDiscovery** | No catalogue entry. |

The practical lesson: Nullius makes a missing capability explicit. DigitalMate and JiuwenSwarm are strong on coding, terminal, search and tool benchmarks, but neither has a proven computer-use port, so the desktop benchmarks are not offered. If we want those results, the work is to prove `agent.computer/v1`, not to argue about the benchmark.

## Why it matters

- **It treats evaluation as evidence, not a number.** The trial-level verifier report, trace and conversation are the product.
- **It separates the agent from the benchmark.** Controls and feasibility views are the right response to “the score is low.”
- **It makes integrations composable.** Ports and proofs are a better contract than a bespoke script per benchmark.
- **It can evaluate our agents today.** DigitalMate and JiuwenSwarm already have catalogue entries with explicit port coverage.
- **It is local and inspectable.** The web UI is a viewer over files on disk, not a black-box service.

## Open questions

- **How many catalogue entries are truly proven rather than merely listed?** The port table is the answer; read it before trusting a “supported” label.
- **Will the Nullius standard spread beyond this project?** Ports and proofs are a good idea, but adoption is the test.
- **Can the controls catch subtle benchmark bugs?** A passing `nop` or failing `oracle` is a strong signal; a benchmark can still be ambiguous in ways the controls miss.
- **How large a run can it manage?** Local, SSH, shards and containers are supported; the practical ceiling is not stated.
- **Will it connect to AgentDescent?** The two are complementary, but there is no pipeline that feeds Nullius evidence into AgentDescent’s reward.
- **What is the production path?** It is Beta, local-first and single-user; a hosted team evaluation service would be a different product.

## Sources

- README: <https://github.com/thinkflowlab/nullius>
- Introduction: `docs/README.md`
- Core concepts: `docs/concepts.md`
- The standard: `docs/standard.md`
- Architecture: `docs/how-it-works.md`
- Run builder: `docs/builder.md`
- Read results: `docs/results.md`
- Supported agents: `docs/agents/supported/README.md`, `digitalmate.md`, `jiuwenswarm.md`
- Package metadata: `pyproject.toml`
