# ScienceDiscovery, explained simply

*As of 29 October 2026. Sources: the repository README, the jiuwenswarm repository and issue #582.*

## What it is

[ScienceDiscovery](https://github.com/openJiuwen-ai/sciencediscovery) is openJiuwen's all-in-one
research workspace. It covers literature review, hypothesis, code, experiments and tuning in one
place, and keeps a record of where each result came from.

- It runs **locally**: a Linux binary (Windows through WSL 2) or macOS from source. The browser UI is
  on `127.0.0.1:4310`.
- The agent reads papers, writes and runs Python, R and shell inside a fail-closed sandbox, and
  records code, environment, logs and cited evidence per deliverable.
- Planning and multi-agent orchestration distribute a task across sub-agents and a skill library.
- A CLI, `ScienceDiscovery run`, sends a task to a running service and streams the result as text or
  JSONL.
- TypeScript, Apache-2.0, version 0.2.0. The repository was created in August 2026 and is active.

## Relationship to JiuwenSwarm

- Its README says it is **built on JiuwenSwarm**, and that every deployment path uses JiuwenSwarm by
  default.
- jiuwenswarm contains an [artifact-provider stub](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/jiuwenswarm/agents/harness/common/rsi/mock_artifact_provider.py)
  that names ScienceDiscovery as an implementation owned by another repository. The two share an
  artifact contract.
- [Issue #582](https://github.com/openJiuwen-ai/sciencediscovery/issues/582) compares its own
  time-to-first-token with DigitalMate's and notes that DigitalMate has no matching issue.
- It does **not** use Orbit. A code search finds only a CSS class named `empty-orbit`.

## Why it matters here

ScienceDiscovery is a sibling product whose default backend is JiuwenSwarm, while DigitalMate runs on
Orbit. That makes it the counter-example in the DigitalMate study: JiuwenSwarm is an active backend
for another team's product, not only a path kept for rollback.

It also contrasts the deployment models. ScienceDiscovery is a single-user local workspace; DigitalMate
is a multi-tenant phone service with one container per user.
