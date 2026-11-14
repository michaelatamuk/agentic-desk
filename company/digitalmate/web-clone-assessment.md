# DigitalMate Web clone — how close is it?

*Compared on 14 November 2026. Clone: `digitalmate-web@3733223` (29–31 October, v0.4.0,
58 commits). Upstream: `DigitalMate@9eea155a` (31 October) and `@62278b8f` (14 November).*

*Read-only assessment. Nothing in the web project was changed.*

## Verdict

"Does it match" has three different answers:

- **As a UI reimplementation** — largely yes. It covers most of the October screens.
- **As a client of the real service** — no. It speaks the previous protocol generation, has
  no account login, and most behaviours are local mocks.
- **As a copy of current DigitalMate** — no. It is frozen on 31 October: one day after the
  protocol rename, and two weeks before the connection foundation.

## Scorecard

Estimates, not measurements.

| Dimension | Match | Why |
|---|---|---|
| Screens and flows (October) | ~75% | Home, chat, discovery, skills, settings, artifacts, approvals, attachments and memory all exist |
| Local behaviour | ~80% | Mock engine, RSS, A2UI, artifacts, calendar and backup are genuinely implemented |
| Live streaming | ~10% | The bridge sends `orbit.request` but listens for `orbit.task.text`; upstream emits `digitalmate.task.text` |
| Authentication | 0% | Pre-issued Bearer token; no Huawei/AGC exchange, no account switch |
| Attachments | 0% live | Local preview only; no `attachment.upload` |
| Server integration | 0% | No Personal Agent, no WorkSwarm, no v3.1 |
| Current (14 Nov) parity | ~35% | Misses all November work |

## The protocol gap is the important one

From git, in order:

| Date | Event |
|---|---|
| 29 Oct | Clone's first commit |
| **30 Oct** | Upstream `9f419939` *"run DigitalMate on WorkSwarm"* introduces `digitalmate.request`, `digitalmate.task.text` and `/digitalmate/ws` |
| 31 Oct | Upstream tip `9eea155a`; clone's last commit |

At upstream `9eea155a`: 29 files mention `digitalmate.request`, 21 mention
`digitalmate.task.text`, 25 mention `/digitalmate/ws`. `orbit.request` survives in four
places, one of which is a backward-compatibility check in `server.py:3933`.

The clone's bridge (`server/orbit.ts`) sends `method: "orbit.request"` with
`agent_id: "orbit"`, and listens for `event === "orbit.task.text"`.

The counts confirm it. In the clone, 2 files mention `orbit.request`, 3 mention
`orbit.task.text`, 1 mentions `/orbit/ws`; **zero** mention any `digitalmate.*` name or
`/digitalmate/ws`.

**Consequence:** the request may still be accepted through the legacy alias, but the text
event never matches. The bridge would connect, submit, and receive nothing it recognises.
Its fake gateway (`npm run bridge:fake`) implements the old names, so the smoke test passes
while a real gateway would not.

## What genuinely matches

- **A2UI**: 36 components, JSONL parser, surface store, update coalescing and JSON Pointer
  semantics.
- **Bilingual UI**: full English and Simplified Chinese, switchable and persisted.
- **Discovery**: local candidate pool, search, RSS/Atom/RDF import with SSRF, redirect,
  timeout and size guards.
- **Chat shell**: task rows, stop/retry/clear, copy/share, execution trace.
- **Artifacts**: save, browse, preview, slides and A2UI surfaces.
- **Approvals and quota**: approval cards, connection quota and failure states.
- **Android**: Capacitor shell, widget, notifications and share.

## Screens

Current DigitalMate has two tabs — **Chat** (`DigitalMateHome`) and **Discovery** (`A2uiHome`) —
plus Settings, with sub-pages for skills, artifacts and connections. The clone mirrors that
shell (Home / Discovery / Settings) and adds demo surfaces.

Route list comparison:

| Screen or flow | Current DigitalMate | Clone | Gap |
|---|---|---|---|
| Chat tab | `DigitalMateHome` + `CloudHome` (session drawer, queue dialog, quota, voice dock) | `ChatView`, `Composer`, `AttachmentSheet` | No session drawer or queue dialog |
| Discovery tab | `A2uiHome` + `SharedWaterfallCard` + Daily Brief | `DiscoveryView` | Local pool only; no Daily Brief module |
| A2UI home | `A2uiHome` | `A2uiSurfaceView` | Both render A2UI; clone is mock-fed |
| Settings | `Settings` | `Settings` | Match, plus demo-only settings |
| **Connections** | `DigitalMateConnectionsPage` **(new)** | — | **Missing** |
| Skills | `SkillCenter` Index / Detail / Publish / CapabilityDetail | Skill detail, install, local publish | No CapabilityDetail; publish is a local export |
| Artifacts | `ArtifactListPage` + `ArtifactPreviewPage` | Local browse and preview | Server artifacts missing |
| **SVG preview** | `SvgPreviewPage` **(new)** | — | **Missing** |
| **Report card** | `ReportCardPreview` **(new)** | — | **Missing** |
| Atomic service | `AtomicServiceProbe` | — | HarmonyOS-only; not applicable to web |

Three screens were added **after** the clone was written, and they are the visible current gap:

1. **Connections** — the account page for Feishu, Gmail and Outlook.
2. **SVG preview** — a dedicated page for rendered diagrams.
3. **Report card preview** — the structured-result card added in November.

The clone also has screens the current app does not route to: Companions, Labs, a calendar
sheet, Diagnostics, local backup, the guided demo and the PWA install/offline views. Those are
extras, not parity.

At route level: current DigitalMate has **ten functional areas**; the clone covers about
**five** (chat, discovery, A2UI, settings, part of skills and artifacts). Four of the five
missing are actionable on web — connections, SVG preview, report card and capability detail.
Atomic service is HarmonyOS-specific.

## Gaps at clone time (31 October)

- **Sign-in**: the native app exchanges Huawei Account Kit or AGC for a Gateway Bearer token,
  and handles revocation and account switching. The clone accepts a token issued elsewhere.
- **Cloud skills**: the native app installs from the skill service; the clone uses local JSON.
- **Custom MCP**: real per-conversation remote tools; the clone has mock references only.
- **Attachment upload**: native uploads and passes source IDs; the clone previews locally.
- **Task progress outside the app**: upstream's activity panel, home-screen card and waking
  notification (#304). The clone has a browser notification and an Android widget.
- **Reconnect**: native reconciles against an authoritative snapshot; the clone retries the
  bridge but keeps local task state.
- **Topics**: upstream had parallel topics by late October. The clone has no topic model.
- **Server memory**: cross-session memory lives on the server; the clone edits a local profile.

## Gaps versus current (14 November)

- **Default backend** is now `digitalmate`; `workswarm` is the legacy option.
- **v3.1 server**: Agent Service, Router, Session Store, Model Gateway, Plugin Gateway.
- **Connections**: foundation, Feishu, Gmail/Outlook, mail Signal pipeline.
- **Project Hive**: Beebou and Bee.
- **Hosted sessions/context**, production template, startup prewarm.
- **Client additions**: SVG/media streaming, attachment captions, report cards, home image
  preview.
- **Reliability**: capacity recovery, idle WebSocket handling, model timeouts, quota codes.
- **Protocol**: `digitalmate.*` and `/digitalmate/ws` — already true on 31 October.

## Why their `docs/parity.md` looks better than it is

Their legend has one symbol for "the screen exists" and no separate symbol for "it works
against the real backend". Several rows are ✅ and then say the real thing is absent:

- "Attachments and upload ✅ … **no upload**"
- "Skill publish / OAuth 🟡 … **no OAuth or marketplace account**"
- "Real Orbit/WorkSwarm transport 🟡 … **needs gateway URL + Bearer token**"

The notes are honest; the symbols overstate live capability. Read the "Notes" column, not the
tick.

## How to verify in an hour

1. Point the bridge at a current gateway: `ORBIT_GATEWAY_URL=wss://…/digitalmate/ws` plus a
   real token. Send one message. Expect no recognised text event.
2. Rename the two strings in `server/orbit.ts`: `orbit.request` → `digitalmate.request` and
   `orbit.task.text` → `digitalmate.task.text`. Retest. This isolates protocol mismatch from
   every other gap.
3. Try to sign in. There is no login route; the bridge only accepts a pre-issued token.
4. Run their suite. Note that it exercises the mock and the old event names, so a green run
   says nothing about protocol compatibility.

## Bottom line

The clone is a good **prototype of the web and Android experience** and a poor **client of the
current service**. Use it as a UI and interaction reference. To make it a compatible front
end, the cheapest path is: keep the UI, replace the transport with `digitalmate.*`, add the
account exchange, then wire attachments and skills.

## Evidence

- Clone: `README.md`, `docs/parity.md`, `docs/architecture.md`, `docs/roadmap.md`,
  `docs/protocol/orbit.md`, `server/orbit.ts`, `package.json`.
- Upstream: `docs/architecture/digitalmate-conversation-integration.md`;
  `git log -S` and `git grep` at `9eea155a` and `62278b8f`; commit `9f419939` (the rename).
