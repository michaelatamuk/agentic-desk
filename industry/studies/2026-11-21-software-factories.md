# Software Factories — Study Notes

*Compiled 21 November 2026. Covers the wave of writing and product launches from late September to 21 November 2026, plus the parallel Chinese wave from May 2026, with earlier material where it explains the current claims. Vendor and self-reported numbers are marked, for example *(company claims)* or *(reported)*. A claim that is reported rather than confirmed is marked the same way.*

## Contents

1. [The short answer](#1-the-short-answer)
2. [Three different things called a software factory](#2-three-different-things-called-a-software-factory)
3. [Why the old idea came back](#3-why-the-old-idea-came-back)
4. [The vocabulary that settled](#4-the-vocabulary-that-settled)
5. [What a line looks like](#5-what-a-line-looks-like)
6. [Timeline: the last six weeks](#6-timeline-the-last-six-weeks)
7. [The evidence](#7-the-evidence)
8. [Software factories in China](#8-software-factories-in-china)
9. [Light versus dark](#9-light-versus-dark)
10. [The product and money map](#10-the-product-and-money-map)
11. [What a factory needs](#11-what-a-factory-needs)
12. [What to measure](#12-what-to-measure)
13. [Failure modes](#13-failure-modes)
14. [How to start in 90 days](#14-how-to-start-in-90-days)
15. [Open questions](#15-open-questions)
16. [What to take from it](#16-what-to-take-from-it)
17. [Sources](#17-sources)

---

## 1. The short answer

- **The word is old; the worker is new.** A "software factory" was proposed in 1968 and built by Japanese electronics firms in the 1970s and 1980s. What changed in 2025–2026 is that coding agents can now take a ticket through several stages of delivery on their own.
- **It is an operating model, not a product category.** A factory is the queue of work, the context each agent receives, the checks a change must pass, the approval rules, and the production feedback that creates the next task. You can build one from existing tools. Vendors sell pieces of it.
- **The bottleneck moved from writing code to verifying and approving it.** Generation, tests and scanning are now cheap at scale. Human judgment at the review gate is the expensive, non-scaling step.
- **The credible version is a "light factory".** People own intent, architecture and the changes where a wrong answer is expensive. Agents do the rest. A "dark factory" ships code nobody reads; it looks fast and accumulates a debt that appears later.
- **The evidence is promising but thin.** The best public case studies are single-company and self-reported. The best independent study says more code is written, not proportionally more software shipped. Treat productivity multiples from vendors and consultancies as claims to test, not facts.
- **China is building them too, with a different shape.** Banks, energy groups and government agencies buy private-deployed lines from Huawei, Gientech, China Electronics Cloud, BoCloud and others; the MIIT plan targets 20,000 software firms using intelligent programming tools by 2028. The claims are mostly vendor-reported. See section 8.
- **The main risk is comprehension debt:** the gap between how much code exists and how much any person still understands. Green tests do not close it.

---

## 2. Three different things called a software factory

The phrase is used for three unrelated things. Check which one a document means before arguing about it.

| Meaning | Period | What it describes | What it optimises |
|---|---|---|---|
| **Traditional software factory** | 1968–2000s | Standardised tools, process and measurement for software production. Hitachi opened a "software works" in 1969; NEC, Toshiba and Fujitsu followed. Later, outsourcers used the term for large delivery centres with rate cards and service levels. | Predictability, cost per unit, quality control |
| **AI factory** | 2024– | Data-centre capacity that produces AI models and inference. Nvidia and cloud providers use the term this way. | Compute throughput, model production |
| **Agentic software factory** | 2025–2026 | A delivery system where AI agents do coordinated development work while people set intent, constraints, acceptance criteria and approval policy. Work enters as a ticket, specification or incident; verified changes come out. | Throughput of shipped changes at controlled risk |

This note is about the third meaning. The first meaning still appears in procurement and in Spain and Latin America, where "fábrica de software" usually means an offshore or nearshore delivery centre. The second meaning appears in infrastructure discussions. Neither is the subject here.

---

## 3. Why the old idea came back

The original argument was that software should be produced like a manufactured product: standard tools, reusable parts, measured work, predictable quality. Robert Bemer proposed a "software factory" at General Electric in 1968. Hitachi created a software facility in 1969. Michael Cusumano documented the Japanese factories in *Japan's Software Factories* (1991). The model produced real gains in standardised, long-lived systems, but it struggled with novel work, because ideas are harder to stamp out than parts.

Three changes made the idea worth revisiting:

1. **Agents can do multi-step work with tools.** A coding agent can read a repository, plan, edit several files, run tests, read the failures and revise. That is not one autocomplete suggestion; it is a small worker.
2. **The cost of a code change fell sharply.** The marginal cost of producing a change is moving toward the cost of compute. The constraint moves to the stations after writing: environments, tests, review, release.
3. **The surrounding machinery matured.** Isolated cloud machines, tool protocols, repository-level instructions, preview environments, scored test runs and orchestration services made it possible to run many agents against the same process.

The result is a real shift in the shape of engineering work, not a new model capability by itself. The factory is mostly the control system around the agents.

| New in 2025–2026 | Recycled from earlier waves |
|---|---|
| Agents can take a ticket through several stages, not just suggest a line | The word "factory" and the assembly-line image |
| The cost of one code change falls toward the cost of compute | Standardised tools and process (1968–1990s) |
| Sandboxes, orchestration, scored test runs and review tools are products | Rate-card delivery centres and service levels (2000s) |
| Verification and approval become the visible constraint | Vendor category names and maturity models |
| Public case studies publish before-and-after numbers | Productivity multiples without independent measurement |

The honest summary: the problem is old, the worker is new, and most of the current noise is about the label.

---

## 4. The vocabulary that settled

The most useful framing comes from Addy Osmani, who works on Claude Code at Anthropic, and from Dex Horthy of HumanLayer. It has three layers:

| Term | Plain meaning |
|---|---|
| **Loop** | One agent doing one job on repeat: gather context, act, check the result, go again until a condition is met. |
| **Harness** | The environment around the loop: the isolated machine, the tools it can reach, the memory it keeps, and the gates that define "done". |
| **Factory** | Many harnessed loops running at once, fed by a queue of work and drained through a review gate into production. People own the system from above. |

Two more terms matter:

- **Light factory.** People stay in the loop where judgment matters. Agents do most of the building, but a person reads what ships, and human judgment moves earlier, to product, design and architecture.
- **Dark factory.** Agents scope, build and ship code without anyone reading the details. Machines write the change and other machines verify it. The image comes from lights-out manufacturing, where the floor runs without people and therefore without lights.

The rule underneath is **back pressure**: give a loop only as much autonomy as you can cheaply and reliably verify, and no more. A check that is cheap, frequent, hard to fake and immediate can earn a loop the dark. A change to authentication, billing, a data migration, secrets or a public interface keeps the lights on.

The cost is **comprehension debt**: the widening gap between how much code exists and how much any person still understands. Tests can stay green while the gap grows. The failure is usually quiet and late, not a single dramatic outage.

---

## 5. What a line looks like

Teams describe the stages slightly differently, but the shape is common. This version follows Sonar's explainer and Paul Iusztin's O'Reilly account.

| Stage | What happens | Who owns the decision | Evidence produced |
|---|---|---|---|
| **1. Intake** | A bug report, feature idea, incident or specification enters a queue. Duplicates are merged and routed. | People set priorities; tooling routes | A scoped task with a source |
| **2. Product thinking** | Agents gather user data, competitor examples and research. People decide what problem is worth solving and what success looks like. | People | A short problem statement and success measure |
| **3. Planning** | The agent reads the repository, standards and architecture rules, then proposes a plan. A person grills the plan and approves it. | People, with agent research | Tickets, acceptance criteria, an architecture decision record |
| **4. Implementation** | A coding agent writes the change in an isolated environment with only the permissions it needs. | Agent, within limits | A branch, a diff, a pull request |
| **5. Independent checks** | Tests, type checks, static analysis, security scanning and dependency checks run. The checks were not written by the agent that wrote the change. | Tooling; people own coverage | Pass or fail, with findings |
| **6. Review** | A reviewer agent or a person compares the change with the plan, the architecture and the standards. Failures return to the implementing agent. | Agent or person, by risk | Review comments and resolutions |
| **7. Approval and release** | A risk rating decides who can approve. Low-risk changes may merge on evidence; high-risk changes go to a person. Release follows the normal pipeline. | People set the rules; agents or people apply them | An approval record tied to a commit |
| **8. Monitor and feed back** | Logs, metrics, alerts, incidents and user reports become new work. A failed health check rolls the release back. | People own the response; agents can act | Production evidence and a new queue item |

A **context layer** runs across all eight stages: the repository, the architecture notes, the glossary, the standards, past decisions and examples. Weak context at the front produces weak plans and expensive rework later. OpenAI's harness report makes the same point: a short map file with pointers to deeper documents works better than one large instruction file.

Two design points matter more than the rest:

- **Bounded permissions.** An agent reaches only the repositories, data and actions its task needs. Credentials are injected outside the agent's environment where possible.
- **Explicit approval boundaries.** The system knows which changes can pass on automated evidence and which need a person. The boundary is written down, not discovered at merge time.

---

## 6. Timeline: the last six weeks

### Earlier, because it explains the wave

| Date | Item | Type |
|---|---|---|
| July 2025 | HumanLayer runs a fully "lights-off" development process. The reversal is published later. | Experience |
| 11 February 2026 | OpenAI publishes "Harness engineering: leveraging Codex in an agent-first world": about one million lines and 1,500 pull requests in five months with no manually written code. | Case study |
| April 2026 | Factory announces Factory 2.0 and a $150M Series C at a $1.5B valuation. | Product and money |
| 30 June 2026 | AI Engineer World's Fair in San Francisco runs a dedicated Software Factories track. Dex Horthy gives "Harness Engineering is not Enough: Why Software Factories Fail". | Conference |
| 15 July 2026 | Addy Osmani publishes "Own the Outer Loop". | Framework essay |
| 20 July 2026 | Addy Osmani publishes "Software Factories, Light and Dark". | Framework essay |
| 15 September 2026 | Factory raises $200M at a $5B valuation. | Money |
| 25 September 2026 | Osmani publishes "Human Judgment Doesn't Leave the Software Factory, It Relocates" at O'Reilly. | Framework essay |

### The six weeks to 21 November

| Date | Item | Type |
|---|---|---|
| 15 October 2026 | Warp publishes tactics for rolling out software factories. | Vendor post |
| 29 October 2026 | Warp publishes "7 core components for building a software factory". | Vendor post |
| 2 November 2026 | Sonar publishes "What Is an Agentic Software Factory?", a long explainer with definitions, components and a pilot checklist. | Vendor explainer |
| 4 November 2026 | Warp publishes "Don't vibe code your software factory": factories need configuration, orchestration, measurement, audit logs and security. | Vendor post |
| 5 November 2026 | Warp publishes on the code-review bottleneck. | Vendor post |
| 11 November 2026 | Opsera publishes "Software Factory vs Dark Factory: Human-in-the-Loop Wins". Andrew Finch gives "Building a Safe Software Factory" at AI Engineer CODE 2026. | Vendor post; conference talk |
| 12 November 2026 | ContextQA publishes a verification-led guide to building an AI software factory. | Vendor guide |
| 13 November 2026 | Stack Overflow publishes "Your coding agent shouldn't grade its own homework". | Practitioner article |
| 16 November 2026 | Warp publishes on adoption challenges. Addy Osmani publishes "How the Claude Code team thinks about verification": about 90% of the team's code is written and reviewed by Claude. | Vendor post; practitioner article |
| 17 November 2026 | Islo launches enterprise software factories with $15M from Insight Partners. | Product and money |
| 19 November 2026 | Warp publishes "Becoming a factory engineer". OpenAI publishes "How OpenAI's Performance Factory keeps ChatGPT fast" — a different use of "factory", about latency work, not software delivery. | Vendor posts |
| 20 November 2026 | Runway publishes "Building a Software Factory" with numbers from its own delivery line. Stack Overflow republishes Paul Iusztin's O'Reilly article on software factories as "Inside a software factory". | Case study; practitioner article |
| 21 November 2026 | This note. | — |

The density is the story. In six weeks the term moved from a few essays and vendor posts to product launches, a funding round, two detailed case studies and a mainstream practitioner article. China ran a parallel wave of policy targets, vendor launches and enterprise deployments. That is what a category looks like while it is being formed.

### China, in parallel

| Date | Item | Type |
|---|---|---|
| 29 May 2026 | China Electronics Cloud launches an "AI software factory". | Product |
| 1 June 2026 | Gientech launches the GienCoder intelligent software factory. | Product |
| 2 June 2026 | Wuhan announces more than 10 "super software factories" for 2026. | Policy target |
| 26 June 2026 | BoCloud launches BoCoder Factory. | Product |
| 2 July 2026 | Xunsu Intelligence presents its AI-Ready software factory. | Demo and talk |
| 23 July 2026 | Tencent launches CodeBuddy NPC, a cloud agent that works from issue to pull request and CI. | Product |
| 4–5 September 2026 | QECon Shanghai runs tracks on Harness Engineering and AI-native software factories. | Conference |
| 2 and 11 September 2026 | MIIT issues and publishes the "AI + Software" special action plan. | Policy |
| 17 September 2026 | Tencent WorkBuddy 5.5.6 adds full-stack app generation. | Product |
| 4 November 2026 | Gientech and Huawei announce an Ascend-based AI-native software factory. | Product |
| 5 November 2026 | Alibaba Cloud Yunxiao launches its AI workbench. | Product |
| November 2026 | IDC publishes a Neusoft AI-native software engineering case. | Analyst report |

---

## 7. The evidence

### 7.1 Runway: a working line, with numbers

Runway published the most detailed public account on 20 November 2026. It is a single company, reporting its own results, and it is not a controlled study. It is still the best picture of what a line looks like when it runs.

The company handed one station at a time to agents, and decided how each handover would be judged before looking at the results.

| Station | Before | After |
|---|---|---|
| **Write and pass CI** | An engineer prompted an agent and carried the change to green by hand | Agents wrote 38% of merged pull requests in October, up from 0.1% in June; in a sample of 100 agent pull requests, 78 had no commits from a person; about 3,000 agent pull requests a month |
| **Review** | People reviewed every pull request, about 200 a week in the core API repository | An AI reviewer with the same context as the author; 93% of its comment threads were resolved or led to a change; cost per review fell to about a third; about 1,000 reviews a week in the core repository and 3,000 across six repositories |
| **Approve** | Median wait for a first approval was 2.3 hours | A separate agent rated each change low, medium or high risk. Low risk could merge on AI approval; high risk went to a person. Median wait fell to about five minutes; about seven in ten reviewed merges went through on AI approval alone. A person objected to 15 of 977 AI-approved changes (1.5%). One in a thousand AI-only approvals was reverted, against about one in two hundred for human approvals |
| **QA** | People clicked through the product by hand | Agents drove browsers through the live product in parallel. In the first four days the loop found 86 confirmed bugs; agents fixed all of them, 67 were verified by rerun, and 68 of 71 fix pull requests were written entirely by agents. Median time from first seen to merged was 4.6 hours |
| **Fix breaks** | Someone noticed an alert and fixed it | Agents retried checks, diagnosed failures and applied known fixes. In the first two weeks they saw about 140 alerts; all but one were fixed without calling a person; median time from red to green was 23 minutes. Automatic rollback fired in production |
| **Run the line** | Engineers started agents, ordered merges and babysat stalled runs | A coordinator read the issue tracker and dispatched work. In its first two weeks it dispatched over 14,000 agent tasks, which led to about 1,900 pull requests and 442 ordered merges |

Runway's summary of the change: the median time from "ready for review" to merge fell from about 11 hours to under two, and weekly merged pull requests more than doubled. The company says it decided how each station would be judged before looking at its results, ran the coordinator read-only first, and re-checked merge gates at the exact commit being merged.

**What to take from it.** The account attributes the gains to the line, not to a single better model. The company built the sandboxes, tests, risk ratings, preview environments, rollback and measurement first, then gave away one station at a time. The numbers are a floor in one sense: Runway counts only pull requests it can attribute to an agent.

**What not to take from it.** This is one company, with a strong engineering team, a modern codebase and a product where browser-based QA is possible. It does not show that the same results transfer to a ten-year-old enterprise system. The comparison of AI and human approvals is also affected by which changes each approves; Runway says it compared across risk levels and found them comparable, but the full data is not public.

### 7.2 OpenAI: five months, zero hand-written lines

OpenAI published its harness report on 11 February 2026. A team started from an empty repository in late August 2025 and built an internal product with no manually written code. After five months:

- about one million lines of code across application logic, tests, CI configuration, documentation and internal tooling;
- about 1,500 pull requests opened and merged;
- three engineers at the start, seven by the end; average throughput of 3.5 pull requests per engineer per day;
- an estimate of about one tenth of the time it would have taken to write by hand;
- agent-to-agent review, with humans reviewing when they choose;
- minimal blocking merge gates, short-lived pull requests, and corrections treated as cheap;
- custom linters and structural tests that enforce architecture and "taste" rules;
- a repository knowledge base treated as the system of record, with a short map file and deeper documents;
- recurring cleanup agents that find drift and open small refactoring pull requests, like garbage collection.

The team's framing is "Humans steer. Agents execute." People set priorities, translate feedback into acceptance criteria and validate outcomes. When an agent struggled, the team treated it as a missing capability, tool or guardrail and had the agent write the fix.

**Caveats.** This was a new product in a controlled environment, not a legacy system. OpenAI says the end-to-end autonomy depends on the specific structure and tooling of that repository and should not be assumed to generalise. There was no independent audit. "Zero hand-written code" is a constraint the team chose, not proof that the result is cheaper or better than a human-built product.

### 7.3 Anthropic's Claude Code team: verification is the product

On 16 November 2026, Addy Osmani described how the Claude Code team verifies work. The team says about 90% of its code is written and reviewed by Claude. The interesting part is not the percentage; it is the machinery that makes the percentage tolerable.

- **Run the change, not just the tests.** The team prefers end-to-end checks that boot the app and drive it like a user. A unit test can pass while the feature is broken.
- **Use tests that are hard to fool.** End-to-end tests, property tests that generate thousands of inputs, and differential tests that compare an old system with a new one on the same inputs.
- **Separate the grader.** In internal testing, a separate grader checking Claude's work against a rubric improved task success by up to 10 points over a standard loop, with the largest gains on the hardest problems.
- **Failures bring a person in.** Claude runs the checks and tries to fix failures. If a check is still failing after three rounds, it stops and asks a person.
- **Code owners write the checks.** The people who own the code write and tune the checks until they flag what the owner would flag.
- **Changes cannot modify their own checks.** The review rules are read from the base branch, never from the pull request under review. A gate a change can edit is not a gate.
- **Observe before enforce.** A new commit gate can run in off, observe or enforce mode. Observe mode logs what would have been blocked so false positives can be reviewed first.
- **Review the reviewers.** The team tracks how many merged changes were reverted, how many were rejected before merge, and a size-matched set of changes that stayed clean. It tunes the reviewer against real incidents and reverts.

**Caveats.** This is the vendor's own team, reporting its own practice. The 90% figure covers writing and review, not design or product decisions. There is no baseline showing what the same team would achieve without the system.

### 7.4 NBER: more code, not more software

The strongest independent evidence is a working paper by Mert Demirer, Leon Musolff and Liyuan Yang, first published in May 2026 and revised in September 2026. It combines public GitHub data with internal Microsoft telemetry on more than 500,000 developers.

| Measure | Effect of adopting coding agents |
|---|---|
| Commits (task-level output) | About +240% cumulative across autocomplete, agents that work alongside a developer, and autonomous agents |
| Releases (shipped software) | About +30% |
| Lines of code, agents that work alongside a developer | About +958% |
| Pull requests, agents that work alongside a developer | About +86% |
| Releases, agents that work alongside a developer | About +20% |
| Pull requests, autonomous agents | About +68.5% |

The authors' interpretation is a "weak link" model: code review, quality control and release capacity are human bottlenecks, so gains at the writing stage attenuate as work moves toward production. They estimate an elasticity of substitution of 0.23 between AI and human effort, which indicates strong complementarity rather than replacement. They also find more experimentation: developers add 7 times as many lines but delete 12.2 times as many, create 79% more branches, and abandon more project ideas.

**Caveats.** This is a working paper, not a peer-reviewed final result. It covers open-source developers and four software marketplaces, with little coverage of enterprise software; the authors cite other work finding the same attenuation in enterprise settings, with smaller effects. The data run through mid-2026. The estimates describe what happened so far, not a forecast.

**A note on a widely repeated number.** Sonar's explainer summarised the paper as "lines of code up 2,450% while shipped releases rose 30%". The paper's published table gives 957.5% for lines of code and 19.8% for releases for agents that work alongside a developer, and 1,254.9% for autonomous agents, with releases not separately reported. The direction is the same, but use the paper's table when quoting a figure.

### 7.5 Faros AI: quality signals

Dex Horthy cites a Faros AI report on what happened after teams adopted coding tools in early 2026:

- review comments up 25%, and 22.7% longer;
- 31.3% of pull requests merged with no review at all;
- incidents per pull request up 242.7%;
- monthly incidents up 57.9%;
- bugs per developer up 54%.

Horthy calls this a correlation signal, not a smoking gun. It is consistent with the review bottleneck: more changes arrive than people can read, so review is skipped and defects escape. It is not proof that agents caused the incidents.

### 7.6 HumanLayer: the dark-factory bill

Dex Horthy's team at HumanLayer tried full lights-off development in July 2025. They read the specs and tickets, gave small and medium work to background agents, and stopped reading the code. The result, in his account:

- an issue eventually appeared that the agent could not solve with better prompting or ten different reproduction attempts;
- a person had to dig into a codebase they had stopped reading three months earlier, while the site was down and users were unhappy;
- by about the third such incident in November, the team decided it would be easier to rewrite; a cofounder spent two weeks rewriting by hand.

His conclusion is not that agents are bad at coding. It is that models do not reliably improve or even preserve codebase quality over time without human steering. He points out that there is no good benchmark for maintainability: the tests that show an agent fixing an isolated bug do not measure whether the repository is still easy to change after months of autonomous work. He estimates that a fast-changing repository can become hard for agents after three to six months, and calls that an observation, not a universal threshold.

### 7.7 Vendor and consultancy claims

| Claim | Source | Status |
|---|---|---|
| 3–5x productivity for organisations running an agentic software factory | BCG Platinion, cited by Sonar | Consultancy claim; no independent measurement published |
| 4.5x size-adjusted output per developer; median time to merge from 11.2 hours to 3.1 hours between November 2025 and July 2026 | Augment Code, about its own team | Self-reported; the company describes it as not a controlled experiment |
| About $60M annualised revenue in 2026 | Sacra estimate for Factory | Third-party estimate, not audited |
| Up to 36% fewer tokens and 92% fewer issues in committed code | Sonar, about its own product | Vendor test; not independent |
| Customers moving from pilots to 24/7 lines | Islo launch post | Vendor customer stories; no independent audit |

These are signals worth testing in your own environment. They are not evidence that the same result will appear in a different codebase, team or product.

---

## 8. Software factories in China

China is not just watching this wave. It is building the same thing under the same name, with a different centre of gravity: banks, energy groups, government agencies and state-owned enterprises as buyers; private deployment; measurable acceptance rates; and a national policy target. Most of the public material is in Chinese, and most of the numbers are vendor-reported.

### 8.1 The policy push

The strongest signal is not a product launch. It is the MIIT "AI + Software" special action plan (工信部信发〔2026〕209号), issued on 2 September 2026 and published on 11 September. It sets targets:

- by 2028: intelligent programming tools and platforms used by 20,000 above-scale software enterprises; 100 software-enterprise intelligent transformation projects; 100 benchmark agent-software applications in key industries; 5 high-quality open-source projects;
- by 2030: key software fully intelligent, with intelligent programming and agent software as new growth areas.

The plan explicitly calls for agent-driven intelligent programming tools with project-level, full-process autonomous development; intelligent transformation of software enterprises' development processes; security review of AI-generated code; agent software app stores and Skills libraries; and standards for intelligent programming capability maturity. It supports procurement with "compute vouchers" and local pilot programmes. This is a demand driver, not only a vendor story.

Local governments have their own targets. Wuhan said in June 2026 that it would build more than 10 "super software factories" in 2026 and cover 1,000 above-scale software enterprises with AI-assisted development. Jinan talks about "agent factories" and one-person companies. The 15th Five-Year Plan names intelligent R&D tools as a priority.

### 8.2 The vendors

| Vendor or product | What it is | Date and status | Claim to note |
|---|---|---|---|
| **Huawei Cloud CodeArts / "intelligent R&D production line"** | A full lifecycle platform — requirements, code, build, test, release, operations — with Pangu and other models; CodeArts Agent ("码道") and an "intelligent software factory" scenario | On the market; Huawei Cloud Stack product page and a March 2026 engineering article | 30% end-to-end efficiency; CNOOC saved 30% of R&D hours; Postal Savings Bank has 4,000 developers, 30% code-generation acceptance, 60% unit-test acceptance and 290,000+ lines generated *(vendor claims)* |
| **Gientech (中电金信) "源启·GienCoder 智能软件工厂"** | Spec-driven development plus harness engineering; requirements, design, development and quality; 20+ industry agents, 80+ skills, 90%+ RepoWiki coverage | Launched 1 June 2026; 300+ enterprises and institutions *(vendor claim)* | A state-owned big bank reached 49.1% code acceptance, 50.2% file acceptance and 100% unit-test generation coverage; testing cycle cut by more than a week *(vendor claims)* |
| **Gientech + Huawei "AI-native software factory"** | Integrated hardware-software AI Coding solution on Ascend, with Gientech's factory process | Announced 4 November 2026 at a Huawei AI Coding summit | A state-owned big bank with 4,000 developers: code acceptance up 20%, core product R&D cycle down 40%; an energy group reached 93.6% AI-generated code acceptance *(vendor claims)* |
| **China Electronics Cloud (中国电子云) "AI软件工厂"** | Requirements, design, development and operations; 30+ skills, 300+ business components; open model access; private deployment | Launched 29 May 2026 | 70+ key-industry customers, 10,000+ developers, 5B+ lines of software produced *(vendor claims)* |
| **BoCloud (博云) "BoCoder Factory"** | Enterprise AI software-factory infrastructure: web cockpit, project hub, IDE and operations; cloud planning plus local execution; seven-step loop | Launched 26 June 2026 | SWE-bench 83.13% solve rate; token cost down 60–70% *(vendor claims)* |
| **Xunsu Intelligence (迅速智能) "AI-Ready software factory"** | A requirements modeler that turns natural-language requirements into a domain model, plus a multi-agent factory that turns the model into tasks and code | Presented 2 July 2026 at the China AI Agent Conference | A campus visitor system ran end to end; six sub-agents, DeepSeek-V4-Pro and OpenAI's command-line agent; people only at the initial requirement and final acceptance *(demo, not a production case)* |
| **Alibaba Cloud** | Yunxiao (云效) AI assistant and AI workbench across requirements, code review, testing, pipelines and release; Qoder CN (formerly Tongyi Lingma), Qoder Cloud Agents and QoderWake digital employees | AI workbench November 2026; Qoder CN rebranded May 2026 | A full DevOps plus agent stack, but not sold under the "software factory" name *(product documentation)* |
| **Tencent** | CodeBuddy, the CNB research platform and CodeBuddy NPC (a cloud agent that takes an issue to a pull request, tests and CI fixes); WorkBuddy app generation on CloudBase | CodeBuddy NPC July 2026; WorkBuddy 5.5.6 September 2026 | CodeBuddy 4–5x code production and a two-week requirement cut to two days; a zero-human NPC Team built a small game; 10,000+ apps a day created by agents on CloudBase *(vendor claims)* |
| **Neusoft** | AI-native software engineering: knowledge assetization, human-machine collaboration and continuous value operation | IDC Perspective, November 2026 | An IDC case study, not an independent productivity measurement |
| **ByteDance** | Trae and SOLO desktop coding agent | On the market | A coding agent and workspace, not a full factory *(product positioning)* |

The list is not exhaustive. It shows the shape: Huawei and the systems integrators sell a whole line to banks, energy companies and government; Alibaba and Tencent sell the platform, coding agent and cloud runtime; startups sell a narrower factory or a requirements-to-code pipeline.

### 8.3 What is distinct about the Chinese version

- **The buyer is often a bank, energy group, government or state-owned enterprise.** The sale is usually a private deployment, with data not leaving the customer's domain, domestic models and a domestic stack (信创). That is different from the US startup-led, cloud-first pattern.
- **The unit sold is the whole line, not a coding agent.** Many vendors start with requirements and design, then code, test, release and operations. The pitch is "software industrialisation" (软件工业化) and "AI-native software engineering" (AI 原生软件工程), not just autocomplete.
- **Measurable acceptance rates are the common metric.** Code acceptance rate, file acceptance rate, unit-test coverage and R&D cycle time are quoted in almost every case. They are useful, but they are vendor-reported and usually not independently audited.
- **The "dark factory" debate is less prominent.** The emphasis is "controllable, traceable, measurable" (可控、可追溯、可度量), with a person at key gates and data staying on-premises. The American conversation is more about light versus dark and comprehension debt; the Chinese pitch is more about industrialisation, compliance and scale.
- **Harness engineering is a shared vocabulary.** Tencent's leadership says AI has entered the "Harness era" (Harness 时代). Gientech uses "SDD + Harness Engineering"; the QECon Shanghai agenda runs a "Harness Engineering (驾驭工程)" track. Huawei describes the software factory as the automation of non-creative work, with people doing the creative work. This is the same idea as the US "harness", framed as engineering discipline.
- **Policy is a demand driver.** The MIIT plan sets adoption targets, supports procurement and asks for standards. Local governments set "super software factory" targets. This is not only vendor marketing.

### 8.4 What to be sceptical about

- **Most numbers are vendor-reported.** 49.1% acceptance, 93.6% acceptance, 30% efficiency, 5B lines: none has an independent audit comparable to the NBER study. Treat them as signals to test, not benchmarks.
- **"Software factory" is used loosely.** Some products are full lifecycle platforms; some are a coding agent with a dashboard; some are app generators. Ask what enters the line and what gates the merge.
- **Demos are not production.** Xunsu's campus visitor system and Tencent's zero-human game show that a chain can run, not that a codebase stays maintainable for years.
- **Private deployment can slow the improvement loop.** Data-not-out-of-domain and domestic-model requirements are real advantages for regulated buyers, but they can limit model choice, telemetry and the speed of feedback.
- **Adoption targets are not quality targets.** Counting enterprises that use a tool is not the same as shipping more software. The NBER caution applies in China too: more code is not automatically more released software.

### 8.5 Where to read the Chinese material

- MIIT plan, official text: <https://www.miit.gov.cn/jgsj/xxjsfzs/wjfb/art/2026/art_91a26793271e4c77aca49ecde4472999.html>
- MIIT explainer: <https://www.miit.gov.cn/zwgk/zcjd/art/2026/art_47ad799a4f9b4c00b34ae764438ffe2a.html>
- Huawei Cloud Stack intelligent R&D production line: <https://www.huaweicloud.com/product/huaweicloudstack/ai-devcloud.html>
- Huawei software engineering practice: <https://www.infoq.cn/article/IPk1UBNeqdj88ZlEWFsk>
- Gientech GienCoder launch: <https://www.gientech.com/news-detail/1835.html>
- Gientech + Huawei, November 2026: <https://www.sfia.org.cn/article/5791072571360816>
- China Electronics Cloud AI software factory: <https://caijing.chinadaily.com.cn/a/202606/09/WS6a27814ea310942cc49b0b63.html>
- BoCloud BoCoder Factory: <https://www.bocloud.com.cn/dynamic/show-2673.html>
- Xunsu Intelligence AI software factory: <https://zhidx.com/p/575448.html>
- Wuhan "super software factories": <https://www.wuhan.gov.cn/sy/whyw/202606/t20260602_2772342.shtml>
- Tencent CodeBuddy NPC: <https://news.qq.com/rain/a/20260723A08OOM00>
- Tencent "cloud software factory" interview: <https://news.dayoo.com/finance/202603/27/171077_54941279.htm>
- Alibaba Cloud Yunxiao AI workbench: <https://help.aliyun.com/zh/yunxiao/getting-started/>
- Qoder CN product family: <https://help.aliyun.com/zh/lingma/introduction-of-lingma>
- QECon Shanghai 2026 agenda: <https://www.qecon.com.cn/Agenda-SH2026>
- IDC and Neusoft report: <https://my.idc.com/getdoc.jsp?containerId=CHC55026426&pageType=PRINTFRIENDLY>

## 9. Light versus dark

The argument is not "agents versus people". It is where to put the lights.

| | Dark factory | Light factory |
|---|---|---|
| **Who reads the change** | Nobody; machines check machines | A person reads the changes that matter |
| **Where judgment sits** | Goals at the start, outcomes at the end | Product, design and architecture before work starts; approval at the gate |
| **Main cost** | Comprehension debt and late failures | Review capacity and slower throughput |
| **Best fit** | Small, cheap, hard-to-fake checks; short loops; low-consequence work | Long-lived systems; high-consequence changes; regulated work |
| **Failure mode** | Quiet drift, then a hard incident in code nobody knows | The review queue becomes the bottleneck and the line stalls |

Addy Osmani's test for whether a loop can run unattended:

1. The check is **cheap**.
2. It runs **often**.
3. It is **hard to fake**.
4. It answers **immediately** and does not drift over time.

Examples that pass: a pass-or-fail test, a type check, a property test, a small lint fix, a dependency bump with a green build. Examples that fail: a subtle production bug that tests cannot catch, a change with a large blast radius, a decision that shapes the system for a year, anything touching authentication, billing, secrets, data migrations or a public API contract.

Keep loops short. Horthy's rule of thumb is that an agent holds up for three to ten steps and starts losing the thread past twenty. Short loops are easier to verify, and a mistake is easier to localise.

The mistake to avoid is setting every loop to the same mode. All dark and the codebase becomes unknown; all lit and the review queue blocks everything. The skilled work is deciding which switch belongs where, and moving it as the evidence changes.

---

## 10. The product and money map

The category is forming quickly. The useful split is by what the product actually does, not by the label.

| Product | What it sells | Status on 21 November 2026 | Evidence |
|---|---|---|---|
| **Factory** | Droids (coding agents), Missions (long-running multi-agent work), and a Software Factory layer across the lifecycle; model routing; on-premises and air-gapped deployment | Raised $200M at a $5B valuation on 15 September; Factory 2.0 launched in April; customers include Nvidia, Blackstone, RBC, Palo Alto Networks, Adobe and T-Mobile *(company claims)* | Vendor customer list; Sacra revenue estimate; no independent productivity study |
| **Warp** | Factories: a cloud platform for running coding agents, with factories-as-code, orchestration, evals, benchmarks, model routing and integrations; Oz as an agent product | Publishing a steady series through October and November; position is "factory as infrastructure" | Vendor posts; customer examples; no independent study |
| **Islo** | Lines (a defined process with agent and deterministic stages) and Machines (persistent isolated environments); credential gateway; evals on historical tickets | Launched 17 November with $15M from Insight Partners; part of the Incredibuild family; customers include Obert, Rite, Incredibuild, ARIMLABS and Alien *(company claims)* | Vendor launch post; customer quotes; no independent study |
| **Sonar** | Independent verification and governance around agents: static analysis, code review, security, remediation | Explainers and product launches through 2026; positions itself as the verification layer, not the factory | Vendor tests; some cited research on AI judges; no independent factory study |
| **ContextQA** | Verification-led guides and tooling for AI software factories | Published a guide on 12 November | Vendor content |
| **Opsera** | DevOps orchestration; compares light and dark factories | Published on 11 November | Vendor content |
| **Coding-agent vendors** (Anthropic, OpenAI, Cognition, Cursor and others) | The worker and the harness | Shipping continuously; increasingly selling review, verification and orchestration around the agent | Vendor reports and case studies |

The money matters for two reasons. First, it shows buyers exist: Factory reached a $5B valuation before most enterprises had a factory. Second, it shows where the margin is moving: from the coding agent toward the orchestration, verification and governance around it. A coding agent is becoming a component; the line is the product.

Chinese vendors are covered separately in section 8. Most of them sell a whole line to banks, energy groups and government rather than a coding agent to startups.

---

## 11. What a factory needs

A practical checklist, assembled from the sources above.

**Intent and rules**

- A written problem statement and a measure of success for each item of work.
- Acceptance criteria before the agent starts, including security and architecture expectations.
- A definition of "done" that a machine can check.

**Context**

- Repository-level instructions that point to deeper documents, not one giant file.
- Architecture notes, standards, a glossary and past decisions in the repository.
- Examples of good changes, so the agent has something to imitate.

**Execution**

- An isolated machine per task, with the toolchains and services the product needs.
- Least-privilege access: only the repositories, data and actions the task needs.
- Credentials injected outside the agent's environment where possible.
- The ability to stop, redirect and resume a run without throwing it away.

**Checking**

- Tests written independently of the agent that wrote the change.
- Static analysis, type checks, security scanning and dependency checks.
- A preview environment where the change can actually run.
- Property tests, end-to-end tests and differential tests where they fit.
- A rule that a change cannot edit the check that judges it.

**Approval**

- A risk rating for each change, with a person on the high-risk cases.
- A written rule for which risk classes can merge on evidence.
- Code owners for critical areas: authentication, billing, migrations, secrets, public interfaces.
- An audit record that ties the approval to the exact commit.

**Operations**

- Logs, metrics and traces the agent can read while it works.
- A one-call rollback and a health check after release.
- A queue that turns incidents and user reports into new work.
- Cost tracking per task, per change and per accepted change.

**Improvement**

- Scored test runs on your own historical tickets, not only vendor benchmarks.
- A weekly review of where agents stall, where changes need rework and which checks produce false alarms.
- The ability to change one stage without re-platforming the whole line.

---

## 12. What to measure

Generated lines, pull requests opened and agent tasks dispatched are inputs. They are easy to increase and do not tell you whether the factory works.

| Measure | Why it matters | Direction |
|---|---|---|
| **Shipped changes per week** | The output that reaches users | Up |
| **Revert rate** | Whether the changes were good | Down |
| **Escaped defects** | Problems found after release | Down |
| **Lead time from ready-for-review to merge** | Whether the line is actually faster | Down |
| **Review effort per change** | The scarce human cost | Down, without losing defects |
| **Human intervention rate** | How often a person has to rescue a run | Down, until it hits the work that needs judgment |
| **Rework rate** | Changes that come back for another round | Down |
| **Cost per accepted change** | Tokens, compute and human time together | Down |
| **Share of changes a person still understands** | Comprehension debt | Up, or at least stable |
| **Agent utilisation or token spend** | Input, not output | Context only |

The most important measure is the pair **shipped changes and revert rate**. A line that ships twice as much and reverts twice as often has not improved. A line that ships the same amount with fewer people may have improved, or may have moved the work into review and incident response where it is harder to see.

---

## 13. Failure modes

| Failure | What it looks like | What to do |
|---|---|---|
| **Review bottleneck** | The queue grows faster than reviewers can read; review is skipped | Measure review latency; route low-risk changes to evidence-based approval; keep high-risk review |
| **AI slop** | Verbose comments, cryptic names, duplicated helpers, tests that agree with the author | Independent checks; code-quality rules; cleanup agents with small, reviewable changes |
| **The agent grades its own homework** | The same model writes the code and the test that proves it works | Separate the grader; use tests the author cannot edit; property and differential tests |
| **Architecture drift** | Each change looks reasonable; the system slowly loses its shape | Enforce boundaries with linters and structural tests; review architecture upstream |
| **Comprehension debt** | Code exists that nobody can explain; incidents take longer to diagnose | Keep people on design and high-risk changes; read a sample; track ownership |
| **Security and secrets** | An agent can reach credentials, the network or production | Least privilege; credential gateway; deny-by-default egress; audit every call |
| **Flaky tests** | The agent learns to retry rather than fix | Treat flakiness as a defect; do not let the agent skip or sleep its way past it |
| **Overbuilt factory** | A grand pipeline that nobody can debug or stop | Start with one repository and one job; keep granular commands; add autonomy gradually |
| **Vendor lock-in** | The process is encoded in one product's configuration | Keep the process description portable; test model and harness swaps |
| **Measurement gaming** | Dashboards show more pull requests and tokens, not more shipped software | Measure shipped changes, reverts and escaped defects |

---

## 14. How to start in 90 days

1. **Pick one repository and one repeated job.** Dependency upgrades, test coverage, pull-request review or a single class of bug. Do not start with the whole lifecycle.
2. **Write the acceptance criteria and the definition of done.** If a machine cannot check it, it is not ready for an agent.
3. **Build the checking layer before the autonomy.** Independent tests, static analysis, security scanning, a preview environment and a rollback.
4. **Give the agent a real environment and least privilege.** A stripped-down sandbox that cannot build the product cannot verify the product.
5. **Rate changes by risk.** Start with a person approving everything; let evidence-based approval in only for low-risk changes.
6. **Run new gates in observe mode.** Log what would have been blocked before blocking anything.
7. **Measure shipped changes, reverts, escaped defects, review time and cost per accepted change.** Publish the numbers to the team.
8. **Review the line weekly.** Find where agents stall, where changes need rework and which checks are noisy.
9. **Expand one station at a time.** Add parallelism, more stages and more autonomy only when the evidence holds.
10. **Keep a stop button and a rollback.** A line you cannot stop is not a factory; it is a runaway process.

---

## 15. Open questions

- **Can maintainability be measured?** There is no fast, reliable benchmark for whether a codebase stays easy to change. Without one, agents are trained and judged on task success, not long-term quality.
- **Does agent-to-agent review scale without collusion?** Two agents from the same model family may share the same blind spots. Independent checks and different methods matter more than another reviewer.
- **What happens to comprehension over years?** The current evidence covers months. There is no long-running public case study of a five-year-old system built this way.
- **Will model vendors own the harness and the factory?** The coding agent is becoming a component. The orchestration, verification and governance layers are where the product competition is moving.
- **How will auditors and regulators treat agent-approved changes?** A risk-based approval record is not the same as a person signing off. Regulated industries will test this.
- **Will the label survive?** "Software factory" may be absorbed into CI/CD, or replaced by next quarter's term. The practices — clear intent, isolated execution, independent checks, risk-based approval, feedback — will outlast the label.
- **How much of the evidence is early-adopter bias?** The public case studies come from strong teams with modern codebases and significant engineering investment. The average enterprise result is unknown.

---

## 16. What to take from it

- **The factory is the process, not the tool.** A prompt chain is not a factory. The durable assets are the written intent, the context, the checks, the approval rules and the production feedback.
- **Verification is the bottleneck.** Invest there first. A better coding agent does not fix a weak review gate; it fills the queue faster.
- **Keep people where a wrong answer is expensive.** Authentication, billing, migrations, secrets and public interfaces. Move judgment upstream, to product and architecture, where it is cheaper.
- **Measure shipped changes and reverts, not activity.** Pull requests, lines and tokens are inputs. They are easy to increase and easy to game.
- **Start small and earn autonomy.** One repository, one job, one station at a time. A line that can be stopped and rolled back is worth more than a grand pipeline that cannot.
- **For our own work, the harness is the machine tool, not the product.** The differentiator is the verification and governance around the agent: what it may touch, what evidence it must produce, who approves, and how the result is audited. That is the part worth building carefully.

---

## 17. Sources

### Primary case studies

- Runway, "Building a Software Factory", 20 November 2026: <https://runway.com/news/engineering/building-a-software-factory>
- OpenAI, "Harness engineering: leveraging Codex in an agent-first world", 11 February 2026: <https://openai.com/index/harness-engineering/>
- Addy Osmani, "How the Claude Code team thinks about verification", 16 November 2026: <https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/>

### Research and data

- Mert Demirer, Leon Musolff and Liyuan Yang, "Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools", NBER Working Paper 35275, May 2026, revised September 2026: <https://www.nber.org/papers/w35275>
- Faros AI report, cited by Dex Horthy; correlation signal, not a controlled study: <https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md>
- Sonar, "What Is an Agentic Software Factory?", 2 November 2026 (vendor explainer; cites BCG Platinion and Augment Code claims): <https://www.sonarsource.com/resources/library/what-is-an-agentic-software-factory/>

### Frameworks and essays

- Addy Osmani, "Software Factories, Light and Dark", 20 July 2026: <https://addyosmani.com/blog/software-factories/>
- Addy Osmani, "Human Judgment Doesn't Leave the Software Factory, It Relocates", O'Reilly, 25 September 2026: <https://www.oreilly.com/radar/human-judgment-doesnt-leave-the-software-factory-it-relocates/>
- Dex Horthy, "Harness Engineering is not Enough: Why Software Factories Fail", AI Engineer World's Fair, 30 June 2026: <https://ai.engineer/talks/Ib5GBkD555M-why-software-factories-fail>
- Paul Iusztin, "Inside a software factory", O'Reilly, republished by Stack Overflow, 20 November 2026: <https://stackoverflow.blog/2026/11/20/dispatches-from-o-reilly-inside-a-software-factory/>
- Stack Overflow, "Your coding agent shouldn't grade its own homework", 13 November 2026: <https://stackoverflow.blog/2026/11/13/your-coding-agent-shouldn-t-grade-its-own-homework/>

### Product and market

- Factory, "Factory raises $200M at $5B valuation", 15 September 2026: <https://factory.com/news/5-billion-valuation>
- Factory, "Factory raises $150M Series C", 16 April 2026: <https://factory.com/news/series-c>
- Islo, "Introducing Islo: the safe way to run enterprise software factories", 17 November 2026: <https://islo.dev/blog/launching-islo-enterprise-software-factories/>
- Warp, "Don't vibe code your software factory", 4 November 2026: <https://www.warp.dev/blog/build-production-software-factory>
- Warp, "7 core components for building a software factory", 29 October 2026: <https://www.warp.dev/blog/7-ways-to-build-a-software-factory>
- Warp, "Becoming a factory engineer", 19 November 2026: <https://www.warp.dev/blog/factory-engineering-software-factories>
- ContextQA, "How to Build an AI Software Factory with Claude Code", 12 November 2026: <https://contextqa.com/blog/how-to-build-a-verification-led-ai-software-factory/>
- Opsera, "Software Factory vs Dark Factory: Human-in-the-Loop Wins", 11 November 2026: <https://opsera.ai/blog/software-factory-vs-dark-factory>

### China

- MIIT, "AI + Software" special action plan, official text, 2 September 2026: <https://www.miit.gov.cn/jgsj/xxjsfzs/wjfb/art/2026/art_91a26793271e4c77aca49ecde4472999.html>
- MIIT explainer, 11 September 2026: <https://www.miit.gov.cn/zwgk/zcjd/art/2026/art_47ad799a4f9b4c00b34ae764438ffe2a.html>
- Huawei Cloud Stack intelligent R&D production line: <https://www.huaweicloud.com/product/huaweicloudstack/ai-devcloud.html>
- Huawei software engineering practice, 26 March 2026: <https://www.infoq.cn/article/IPk1UBNeqdj88ZlEWFsk>
- Gientech, GienCoder launch, 1 June 2026: <https://www.gientech.com/news-detail/1835.html>
- Gientech and Huawei, AI-native software factory, 4 November 2026: <https://www.sfia.org.cn/article/5791072571360816>
- China Electronics Cloud, AI software factory, 9 June 2026: <https://caijing.chinadaily.com.cn/a/202606/09/WS6a27814ea310942cc49b0b63.html>
- BoCloud, BoCoder Factory, 26 June 2026: <https://www.bocloud.com.cn/dynamic/show-2673.html>
- Xunsu Intelligence, AI software factory, 15 July 2026: <https://zhidx.com/p/575448.html>
- Wuhan, "super software factories", 2 June 2026: <https://www.wuhan.gov.cn/sy/whyw/202606/t20260602_2772342.shtml>
- Tencent, CodeBuddy NPC, 23 July 2026: <https://news.qq.com/rain/a/20260723A08OOM00>
- Tencent, "cloud software factory" interview, 27 March 2026: <https://news.dayoo.com/finance/202603/27/171077_54941279.htm>
- Alibaba Cloud Yunxiao AI workbench, 5 November 2026: <https://help.aliyun.com/zh/yunxiao/getting-started/>
- Qoder CN product family: <https://help.aliyun.com/zh/lingma/introduction-of-lingma>
- QECon Shanghai 2026 agenda: <https://www.qecon.com.cn/Agenda-SH2026>
- IDC and Neusoft, AI-native software engineering, November 2026: <https://my.idc.com/getdoc.jsp?containerId=CHC55026426&pageType=PRINTFRIENDLY>

### History

- Michael Cusumano, *Japan's Software Factories* (1991), and the MIT-hosted historical overview of factory concepts in software: <http://hdl.handle.net/1721.1/47992>
- Robert Bemer's 1968 paper is discussed in Osmani's essay and in the Cusumano history above.

### Method note

The timeline is built from publication dates on the linked pages. Funding dates are company announcements; valuations are not independently audited. Productivity numbers from Runway, OpenAI, Anthropic, Factory, Warp, Islo, Sonar, Huawei, Gientech, China Electronics Cloud, BoCloud and Tencent are self-reported unless a study is cited. The NBER paper is a working paper, not a final peer-reviewed result. Chinese policy targets are targets, not measured outcomes.
