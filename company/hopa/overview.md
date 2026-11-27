# HOPA, explained simply

**One-page summary:** [`hopa-onepages.svg`](hopa-onepages.svg).

*As of 28 November 2026. Sources: the local checkout at `agents-demo/hopa@b0b3f217`, its README, status page, architecture, turn-flow, coverage and changelog. HOPA is built by another team in the company. This note is context, not our roadmap.*

## The short version

- **HOPA is a personal assistant that uses your phone’s apps for you.** You say what you want; it opens apps, taps, types, reads the screen and answers.
- It is **not a chat that describes actions**. It has hands: a runtime that acts, checks that the screen changed, and records the run.
- **Money always asks.** A payment shows the item, total and seller, and waits for **Deny** or **Allow**. A “yes” is never remembered.
- It runs on **HarmonyOS** and was built to share one conversation between a phone and a HarmonyOS 2-in-1 laptop.
- **The current work has moved to Android.** The status page (13 November) says Android is the active client, Windows is next, and Harmony is frozen. The Harmony app is the shipped prototype; the Android app is the active one.
- It is a **working prototype**, Apache-2.0; this note does not rely on a release number. The bridge suite has 121 tests.

## What it is

HOPA stands for **HarmonyOS Personal Assistant**. The idea is simple: you have better things to do than tap through menus. You ask in your own words, and HOPA uses the app or website: it opens the app, reads the screen, taps, types, scrolls, goes back, and tells you what happened.

The product is built around two claims:

1. **It has hands.** A runtime actually operates the phone, then observes the screen again to check the action landed. A failed step is named; it is not hidden inside a chatbot reply.
2. **Money is different.** A payment is a decision, not a chat message. HOPA shows the item, the total and the seller, and asks every time. The approval is written in your language, not in raw action names.

The supported asks span phone apps (WeChat, Feishu, Xianyu) and websites (Zhihu, Xiaohongshu, Bilibili). It runs websites in its own browser; app control needs the app installed, and HOPA names a missing app instead of guessing a package.

## The current status, which the README does not fully show

The README is a HarmonyOS product showcase. The status page is newer and changes the roadmap:

- **HarmonyOS:** the shipped prototype. Chat, browsing, app control through the PC bridge, the run pane and the payment gate are real. On-device app control needs Huawei’s accessibility ACL, which is still a pending account/legal step on retail phones.
- **Android:** the **active client**. A debug app launches on an API 35 emulator with the loop, chat, settings, conversations, profiles, runs, capabilities and launchpad. The bridge, accessibility, Room persistence and approval sheet are the next pieces.
- **Windows:** next in line.
- **Harmony:** **frozen** (ADR-0020). The Harmony notes describe the shipped app, not the active roadmap.

So the honest summary is: **HOPA shipped a HarmonyOS prototype, and is now rebuilding the product on Android, with Windows after that.** The product idea is the same; the platform bet moved.

## One turn, from a prompt to an answer

HOPA reads the screen, asks what to do next, acts, and reads the screen again. It tries four paths in order, and each can return an action, a question or a final answer:

| Order | Path | What it is | If it is not sure |
|---|---|---|---|
| 1 | **Graph** | A hand-written graph for an app HOPA knows: the current screen is a node, the next actions are edges. A decision model picks the edge. | Next path |
| 2 | **Tree ranker** (Android, optional) | Scores the visible controls against the goal. | Next path |
| 3 | **Small local model** | A model file on the phone. | Next path |
| 4 | **API model** | A cloud model such as DeepSeek. | The turn stops |

The graph does not ask a language model; its confidence is how well an edge fits the screen and the goal. A model’s confidence is part of its reply. A path that is not sure hands the step to the next path instead of guessing.

Two shortcuts sit outside the picture: a simple command (“open”, “back”, “home”, “scroll”, “wait”) is answered in one step with no model, and a saved recipe that worked before for the same words is replayed before the model is asked.

The user sees **Graph · Camera**, **Cloud · deepseek-v4-flash** or the local model’s name while it works; the note under the answer says the path, the steps, the confirmations and the tokens.

## The action gate

Every action — from the agent, a benchmark, a user macro, a scheduled task or a test — goes through one executor:

```text
guards → payment approval → execute → verify → record
```

The rules are strict by design:

- **Guards** check the schema, the allow-list, the risk and the preconditions before anything touches the device.
- **Payment is fail-closed.** Anything classified as payment, or as something that could lead to payment (opening checkout, entering card details, confirming an order), requires explicit approval. If classification is uncertain, it is treated as payment.
- The **model cannot set or clear the payment class**; the executor owns it.
- A denied payment produces a record with `approved=false` and **no execution**. The agent must not retry another way.
- **Verify** observes the screen after the action and compares it with the expectation. A failed verification is recorded; it does not “fix” a payment.
- **Record** is append-only. Editing or deleting a run record is a bug.
- **Human takeover** pauses the loop for login, 2FA or payment, and resumes only after an explicit hand-back.

This is the part worth studying: the assistant is built so that the dangerous class of action cannot be reached by a clever prompt.

## Phone, laptop and the bridge

HOPA started on the phone, but it also runs on a HarmonyOS 2-in-1. The two are one conversation: ask in your hand, open the laptop, and the same thread is there, with the same steps and the same picture of what HOPA did.

The **PC bridge** is the only part that touches a device and the only part that keeps state. It is a Python process, not a feature of one app:

- `GET/POST /chats` merges by content (`role:at:text`) with tombstones for deletes, so either app can start or finish a thread.
- `/images` is a content-addressed image store on the PC, so a screenshot taken on the phone is visible on the desk.
- One pooled listener serves every device, routes by `X-Hopa-Role` or `/d/<serial>/…`, and authorises each caller once.
- There is no cloud account. For a phone away from the cable, `hopa-bridge relay` on a public host plus `hopa-bridge cloud-link` on the PC keeps the same store and tokens.
- The bridge works over an `hdc` reverse tunnel, or the cloud relay. It launches, taps, types, reads, scrolls and goes back.

The bridge is for a trusted network, and pairing one device means it may act on the others in the pool. That is a deliberate convenience with a real trust cost.

## The modes

There are five modes, and the rules do not change with the presentation:

| Mode | Reading | Behaviour |
|---|---|---|
| **Everyday** | 13.5 pt | rail and metrics where there is room |
| **Easy** | 15 pt | fewer controls, no rail |
| **Power** | 13 pt | metrics and schedules |
| **Social** | 13 pt | no rail, no metrics |
| **Kid** | 16 pt | no history, parent PIN to leave; blocks payments and public posts |

The Kid mode is the clearest example: the same action gate, but the allowed set is narrower and the history is hidden behind a parent PIN.

## The architecture

HOPA has three layers, and dependencies point one way:

```text
entry (UI shell) → capabilities → core
```

- **`core`** is pure ArkTS: the action model, the executor, the approval policy, the model client, the run record and capability interfaces. It has no UI or OS-kit imports, so it can be tested on the host.
- **`capabilities`** are independent leaves: browser, sandbox, accessibility, system, model clients. A capability may import `core`; it may not import a sibling capability.
- **`entry`** is the composition root: the running app, pages, navigation and one service per concern (conversations, schedules, runs, export, settings, approvals, bridge, model factory, logging).

The current repository also has **Android, Windows and backend** builds, plus `services/` for the bridge, relay, wire format, brain, evaluations and tools. The Harmony app is one client; the engine and services are shared.

Perception is a tree first, then OCR, then vision for custom-drawn screens. Observations are redacted and hashed before storage or a model call.

## What works, what does not

**Works on the shipped Harmony prototype**

- Chat, memory, skills, plans, batch, runs and export.
- Browsing: read a page, click, type, back/forward/reload, recent pages.
- App control through the PC bridge: launch, read, tap, type, scroll, back.
- Payment gate, approval sheet, run pane with steps, frames and cost.
- Five modes; phone/laptop shared conversation.
- Models: OpenAI-compatible, Anthropic, Gemini, DeepSeek.

**Partial or next**

- On-device app control needs Huawei’s accessibility ACL; the bridge is the development path.
- Speech is partial on the phone; the bridge handles transcription and speech.
- MCP tool calling is not built yet; the engine has no tool-calling path.
- Chinese copy is partial; the newer pages are English-only.
- Desk mode depth is partial; Easy/Kid are type-and-chrome on the desk.
- Window repaint after long idle is a known defect.
- The Android client is early: bridge, accessibility, Room persistence and approval sheet are next.
- HOPA sees the visible screen only; login, CAPTCHA and verification codes stay with the user; some apps block automation and HOPA hands over.

## How it relates to our products

| Product | Relationship |
|---|---|
| **DigitalMate** | The closest product. Both are personal assistants for a phone, and both run tasks for one person. DigitalMate is a HarmonyOS app with a cloud server and a discovery feed; HOPA is a phone assistant that operates other apps directly, with a PC bridge and a payment gate. DigitalMate delegates execution to WorkSwarm; HOPA has its own action loop and model clients. HOPA is also moving to Android, so the platform overlap is narrowing. |
| **openJiuwen / JiuwenSwarm** | No direct integration. HOPA has its own engine, action model and model clients; it is not built on JiuwenSwarm. |
| **FlyBot / Belle** | Different surface. FlyBot is a self-hosted team workspace; Belle is a team-chat coworker. HOPA is a personal phone assistant. |
| **MobileGym** | Complementary. MobileGym is a simulated phone and benchmark for GUI agents; HOPA is a real assistant with app control. HOPA also has its own small benchmark (HOPA-Bench: 5 tasks now, 20 at M2, 50 at v2). |
| **Nullius** | Complementary evaluation layers. Nullius runs benchmarks and shows evidence; HOPA has its own run receipts and bench. No integration. |
| **AgentDescent** | Could improve HOPA’s prompts or skills from examples, but there is no integration. |
| **OpenDirector / PPMA / Orbit** | No direct relation. Different products, different layers. |

The closest description: **HOPA is a phone-operating personal assistant with a strong action gate.** It is closer to DigitalMate than to the platform products, but it is built around GUI control and payment safety rather than cloud tasks and a feed.

## Why it matters

- **The action gate is a good pattern.** One executor, guards, payment approval, verification and an append-only record; the model cannot talk its way past it.
- **The payment boundary is concrete.** Item, total and seller in plain words; Deny or Allow; never remembered. That is a better answer than “the agent is careful”.
- **It is honest about platform limits.** The bridge exists because accessibility is restricted; the status page says what is shipped and what is not.
- **It shows the cost of a platform pivot.** The Harmony app shipped, then the team moved to Android and Windows. The product idea survived; the client work restarted.
- **It is a real GUI-agent product**, not a benchmark. MobileGym can test a GUI agent; HOPA shows what one looks like when a person uses it.

## Open questions

- **Will the Android client reach the Harmony prototype’s coverage?** The loop, chat and runs are there; bridge, accessibility, persistence and approvals are next.
- **Can on-device app control replace the PC bridge?** That depends on Huawei’s ACL on Harmony and on Android accessibility permissions.
- **Will Windows become a first-class client?** The repo has a Windows app; the status says next.
- **Can the action gate stay strict as capabilities grow?** A new action type is a new chance to misclassify payment; the rule is to treat uncertainty as payment.
- **How does HOPA compare with DigitalMate in daily use?** HOPA has hands and a payment gate; DigitalMate has cloud tasks and a feed. They may be complementary rather than direct substitutes.

## Sources

- README: `README.md` in `agents-demo/hopa`
- Status: `docs/project/status.md`
- Architecture: `docs/design/architecture/overview.md`, `layers.md`, `turn-flow.md`
- Coverage: `docs/design/product/coverage.md`
- Changelog: `CHANGELOG.md`
- Conventions: `CLAUDE.md`
- Repository: `https://github.com/agents-demo/hopa`
