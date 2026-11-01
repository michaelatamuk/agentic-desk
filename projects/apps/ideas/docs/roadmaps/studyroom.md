# StudyRoom — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"Host" means the StudyRoom app. "LAIX" means the pinned `laix` package. "On-site" means media and data
stay inside the school or pilot network. "Agent" means JiuwenSwarm orchestrates a host tool call.

**Status.** Concept + full scope. No code yet. Concept note: [studyroom.md](../concepts/studyroom.md).

**One line.** StudyRoom notices when a learner needs help, decides whether to wait, hint, ask a peer or
call the teacher, and shows why.

**Buyer.** Tutoring companies, small-group learning centres, universities and corporate training teams.

**User.** The student, the peer helper and the teacher or tutor running the session.

**The sentence the audience repeats.** *"It knew when not to interrupt."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc, trust beat, audience agency, demo architecture, acceptance tests and stagecraft.

Phases 4–7 adapt the proactive readiness, 2026 product-experience and production-wiring patterns
proven in RootCause, GeoResponse, CUE and RECALL.

---

## What StudyRoom is

A **live small-group learning room** built around one LAIX decision: **who needs what, when, from whom,
with what consent, and why**.

The host owns the room, the media, the exercises, the board, the consent, the teacher tools and the
services. LAIX owns the decision and its record.

## What StudyRoom is not

- **Not an LMS.** Courses, enrolment, grades and curriculum stay in the school's system.
- **Not a video conference.** WebRTC is a transport, not the product.
- **Not an autonomous teacher.** The teacher can always override.
- **Not a grading system.** It verifies answers; it does not certify learning.
- **Not surveillance.** No face recognition, emotion detection, attention scoring or always-on
  recording.
- **Not a copy of the LAIX LiveTogether zip.** New host app, new code, same product idea.
- **Not a second decision engine.** There is one LAIX decision path. No local `server/laix/` copy.

## What we borrow from the LiveTogether idea

The product pattern is good:

- a five-pane wall with students, story and LAIX;
- live evidence against an intervention line;
- visible options, scores and combined signals;
- consent as an animated, visible state;
- re-plan when the situation changes;
- a component strip that says what each service just did.

We borrow the **experience**, not the implementation.

## What we do not borrow

- The bespoke `server/laix/runtime.ts` decision engine.
- Its `ActionType` enum as the decision contract.
- Direct calls from a module named LAIX to PPMA, Digital Mate or JiuwenSwarm.
- Its single-process, unauthenticated demo assumptions for real students.
- Its custom decision schema instead of the LAIX `Decision` contract.

The new app uses the pinned `laix` package, a thin adapter and a learning policy plugin.

## The LAIX contract

The rule for the whole build:

> **The host owns the experience and the data. LAIX owns the decision. One adapter connects them.**

| Concern | Owner | Must not |
|---|---|---|
| Room, presence, exercises, answers, chat, board | Host | Enter LAIX as domain objects |
| Camera, microphone, STT, TTS, screen share | Host | Send raw media to LAIX |
| Consent, privacy, safeguarding, teacher override | Host | Be delegated to LAIX |
| PPMA profiles, progress, long-term memory | Host → PPMA | Be imported by LAIX |
| Digital Mate wording, TTS, delivery | Host → Digital Mate | Be called by LAIX |
| JiuwenSwarm tools, retries, idempotency | Host → JiuwenSwarm | Be called by LAIX |
| Situation, options, policy, verb, confidence, approval, re-plan | **LAIX** | Know the learning domain |
| Decision record, outcome, basis | **LAIX** | Store raw media |

LAIX receives only generic contracts:

- `Situation` with opaque subject ids, beliefs, constraints and attributes;
- `DecisionRequest` with options and a requested policy;
- `Action` options with benefit, risk, delay, cost, reversibility and approval needs.

LAIX returns one `Decision` with:

- a canonical verb: `wait`, `observe`, `guide`, `ask`, `act`, `verify`, `escalate`;
- an app action id such as `ask-ben` or `hint-alice`;
- score, confidence, confidence source and calibration flag;
- alternatives and constraints applied;
- `requires_approval` when a peer, guardian, teacher or external notice is involved.

## Repository shape

```text
studyroom/
  server/studyroom/
    laix_adapter.py          # only module that knows both vocabularies
    policy/learning.py       # app policy plugin; no LAIX internals
    room/                    # presence, exercises, answers, chat
    signals/                 # sensor and app event ingestion
    consent/                 # consent, privacy, safeguarding
    memory/                  # PPMA port and local stand-in
    mate/                    # Digital Mate port and local stand-in
    execute/                 # JiuwenSwarm port and local tools
    media/                   # WebRTC signalling, STT/TTS, board media
    api/                     # REST and WebSocket
    store/                   # SQLite dev, Postgres production
    projections/             # per-role filtered views
  web/src/
    student/                 # learner room
    teacher/                 # teacher wall
    stage/                   # 90-second story
    console/                 # engineering console
    components/              # shared design system
    lib/                     # websocket, media, i18n, telemetry
  tests/
    server/                  # adapter, policy, consent, API, WS
    e2e/                     # Playwright multi-browser
    load/                    # room and media load
    fixtures/                # deterministic packs and decisions
  docs/
    architecture.md
    laix-boundary.md
    consent-privacy.md
    deployment.md
    data-provenance.md
    limitations.md
    runbook.md
```

The adapter is the only place that imports both `studyroom` domain types and `laix` contracts. The
learning policy imports `laix` public types only; it never reaches into `laix.core` internals.

## What the four developed apps already prove

StudyRoom should reuse the **patterns**, not the code:

| App | Pattern to reuse | What not to copy |
|---|---|---|
| RootCause | `laix_adapter` + domain policy plugin; decision records; append-only audit; proactive watchlist; shift brief; tenant isolation; backup/restore; runbook | Factory data model and report workflow |
| GeoResponse | Evidence → situation → decision; proposals and approvals; resource budget; outcome loop; proactive scopes; notifications; API auth and rate limits; visual and load tests | Geospatial data model and map UI |
| CUE | Attention and cooldown; quiet hours; dedupe; delivery and signing; readiness lifecycle; exports; MCP/agent surface; design system; accessibility | Show-design data model and 3D canvas |
| RECALL | Pinned TypeScript package; adapter boundary; decision record; consent and redaction; PPMA north contract; offline/PWA; packaging tests; field/mobile capture | Meeting capture model and PPMA product scope |

### Inherited build checklist

- [ ] One pinned LAIX version; no local copy; isolation test **(S)**
- [ ] One adapter; one domain policy plugin **(M)**
- [ ] Decision record, outcome loop and audit **(M)**
- [ ] Approval and consent gates **(M)**
- [ ] Proactive readiness, not just the live room **(M)**
- [ ] Per-role projections, not one shared state object **(M)**
- [ ] Tenant and class isolation **(M)**
- [ ] Export, backup and restore **(M)**
- [ ] Structured docs, limitations and runbook **(S)**
- [ ] CI, e2e, load, accessibility and security checks **(M)**
- [ ] Offline/PWA mode where the classroom needs it **(M)**
- [ ] Honest real-vs-simulated panel **(S)**

## Cadence

- **Student:** every session, whenever stuck.
- **Teacher:** every session, plus a short brief before and after.
- **Admin:** weekly review of classes, consent, integrations and health.
- **Pilot:** one class, one subject, 90 days.

The daily loop is the teacher wall. The deep loop is the decision record and the next lesson.

---

## Phase 0A — The 90-second stage piece

Goal: a stage piece that makes the room feel the decision before the product exists.
Time: 2 weeks to build, 1 week to rehearse. No real classroom, no school network, no production auth.

**Set.** One laptop, one large screen, a microphone, a phone or camera as Alice's device, and a
printed decision card. The screen is the room.

**The verb.** Speak as Alice: *"I don't get it."*

**The cold open.** Three learners are working. Alice has two wrong attempts. The teacher cannot watch
all three. *"The quiet one is already behind."*

**The turn.** Alice's evidence crosses the line. LAIX asks Ben for help with consent. Ben accepts and
the board opens with only the current problem. Ben drops out. LAIX re-plans to a private hint. Alice
solves it.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | Alice stuck; two wrong attempts; teacher cannot watch all | Three panes, teacher wall |
| 0:10–0:25 | First touch | Presenter speaks Alice's line; hand raise toggles | Evidence bar rises, stays below line |
| 0:25–0:45 | Machine works | Ben offers; evidence crosses; LAIX compares options | Option list, consent request, verb |
| 0:45–1:05 | Trust beat | Hand raise was a false positive; teacher rejects ask-Ben; re-rank to wait | Teacher override, decision trace |
| 1:05–1:20 | Reveal | Evidence crosses again; ask Ben; Ben declines; re-plan to private hint; Alice solves | Consent, board, hint, verify |
| 1:20–1:30 | The line | Record shows wait, ask, decline, re-plan, hint | Decision record, reset |

### The trust beat, in detail

- Alice raises her hand while thinking. The camera motion signal is uncertain.
- LAIX proposes **ask Ben** because the combined evidence is just above the line.
- The teacher sees that Alice has returned to the problem and is not asking for help.
- The teacher rejects the decision with one reason: *"She is back on task."*
- LAIX re-ranks to **wait**, records the override and lowers the weight of the hand-raise signal for
  this session.
- The presenter says: *"It had enough evidence. It was wrong. The teacher stayed in charge."*

The correction is visible, stored and used next time. No accuracy number is claimed.

### Audience agency

Ben declines the consent request. The room chooses:

- **Ask Chris now** — free, but less context and a new explanation.
- **Give Alice a private hint** — fast and private, but less collaborative.

Both are defensible. The screen shows the trade-off and the decision. The presenter commits to the
room's choice and runs the consequence.

### Props and stagecraft

- One laptop and one physical phone as Alice's device.
- A printed decision card with the three options.
- A microphone for Alice's line; captions on screen.
- One sound cue for the evidence crossing; silence during the trust beat.
- A visible timer showing how long Alice was stuck.
- Reset: `R`, under five seconds.
- A fallback recording of the same run and a backup laptop.

### Phase 0A checklist

- [ ] Stage shell with three student panes, teacher wall, decision panel and story rail **(M)**
- [ ] One exercise (`2x + 3 = 11`) with answer, attempts and time **(S)**
- [ ] Alice's spoken line through the mic and STT, labelled with provenance **(M)**
- [ ] Hand-raise signal from camera motion, explicitly uncertain **(M)**
- [ ] Evidence bar against the intervention line **(S)**
- [ ] LAIX decision panel: verb, action id, alternatives, constraints **(M)**
- [ ] Wait moment: evidence below the line, no interruption **(S)**
- [ ] Ask moment: evidence above the line, consent required **(M)**
- [ ] Peer consent prompt for learner and helper **(S)**
- [ ] Shared board with only the current problem **(M)**
- [ ] Helper disconnect and re-plan to private hint **(M)**
- [ ] Teacher override with reason and visible re-rank **(M)**
- [ ] Decision record with wait, ask, decline, re-plan, hint **(M)**
- [ ] Audience choice: ask Chris or private hint **(S)**
- [ ] Reset under five seconds **(S)**
- [ ] Deterministic, offline, no model or network call on stage **(S)**
- [ ] 90-second fallback recording and backup laptop **(S)**
- [ ] Contrast and type test at 10 metres, 16:9 and 4:3 **(S)**
- [ ] Captions and a transcript for the spoken line **(S)**
- [ ] Data provenance sheet for every asset and signal **(S)**
- [ ] Three rehearsals: normal, hostile audience, no network **(S)**

**Do not build for 0A:** real WebRTC mesh, school login, multi-class, billing, admin, screen share,
recording, LMS integration, full whiteboard tools.

---

## Phase 0B — The functional demo

Goal: the booth and classroom-preview version that answers "is this real?" Same story, editable room,
real LAIX decisions, still deterministic and offline.

Time: 4 weeks after 0A. It can reuse the stage shell.

### 0B.1 The LAIX integration

- [ ] Pin `laix` to `v0.7.0` from the release tag **(S)**
- [ ] No local `server/laix/` copy; no second decision engine **(S)**
- [ ] `laix_adapter.py` maps host events to `Situation` and `DecisionRequest` **(M)**
- [ ] `policy/learning.py` implements the app policy plugin **(M)**
- [ ] Options: wait, observe, guide, ask, act, verify, escalate **(M)**
- [ ] Constraints: consent, privacy, no-interruption, cooldown, teacher-only **(M)**
- [ ] Decision fields: score, confidence, confidence source, calibrated, alternatives, constraints **(S)**
- [ ] Approval flag for peer help, teacher notice and external actions **(S)**
- [ ] Decision record and outcome loop **(M)**
- [ ] Adapter isolation test: only public `laix` imports **(S)**
- [ ] Version assertion: `SCHEMA_VERSION == "0.7.0"` and `POLICY_VERSION == "0.7.0"` **(S)**
- [ ] Replay fixture: event trace → expected decision shape **(S)**

### 0B.2 The room

- [ ] Three to five learners, one teacher, one session **(M)**
- [ ] Presence, join, leave and reconnect **(S)**
- [ ] Exercise state: problem, attempts, correctness, time **(S)**
- [ ] Chat and typed Tell Mate fallback **(S)**
- [ ] Private board and shared board with versioning **(M)**
- [ ] Answer submission and verification **(S)**
- [ ] Help request by button, chat and speech **(M)**
- [ ] Hand raise and voice activity signals **(M)**
- [ ] Teacher override, pause and block peer help **(S)**
- [ ] Session reset and scenario reset **(S)**

### 0B.3 The surfaces

- [ ] Student room: own problem, Mate, board, consent, captions **(M)**
- [ ] Teacher wall: states, evidence, decisions, consent, next action **(M)**
- [ ] Stage wall: five panes, story rail, reset **(S)**
- [ ] Engineering console: events, decisions, policy, latency, counters **(M)**
- [ ] Decision record view: what, why, evidence, approval, outcome **(M)**
- [ ] Booth mode: scenario picker, three-minute run, offline pack **(S)**
- [ ] Mobile-friendly student join and teacher review **(M)**

### 0B.4 The decision story

- [ ] Below-line wait **(S)**
- [ ] Above-line ask with consent **(M)**
- [ ] Helper decline and re-plan to hint **(M)**
- [ ] Helper disconnect and re-plan **(M)**
- [ ] Teacher override **(M)**
- [ ] Verification after the hint **(S)**
- [ ] Outcome recorded and shown **(S)**
- [ ] One duplicate intervention prevented **(S)**
- [ ] One cooldown suppression shown in the console **(S)**

### 0B.5 The fast example

The ZIP's 12-step story is the right format for a fast presentation. Build our own version as a
first-class example, not a throwaway demo.

- [ ] `examples/studyroom_fast_demo/` with `README.md`, `scenario.json` and `expected.json` **(S)**
- [ ] `python -m studyroom.demo --fast` starts the wall at `/?view=demo` **(S)**
- [ ] `--cli` prints the same 12 steps and LAIX decisions to the terminal **(S)**
- [ ] 12 steps mirror the ZIP's useful moments: wait, false hand raise, ask, consent, board, solve,
  disconnect, re-plan, record **(M)**
- [ ] Each step injects inputs only; LAIX produces every decision **(S)**
- [ ] Each decision shows verb, action, score, alternatives and constraints **(S)**
- [ ] Teacher override is available in the wall **(S)**
- [ ] `Next`, `Back`, `Restart` and `R` reset **(S)**
- [ ] Runs offline with no camera, microphone or WebRTC **(S)**
- [ ] Readable at 10 metres; story pane shows the modality used **(S)**
- [ ] The scenario is also a test fixture; expected decisions are asserted **(M)**
- [ ] A recorded 90-second fallback and a backup laptop **(S)**
- [ ] Clean-checkout run in under three minutes, measured **(S)**

### 0B.6 Data, determinism and rights

- [ ] Fixed scenario pack with fixed seed **(S)**
- [ ] Precomputed sensor inputs but live LAIX decisions **(S)**
- [ ] All fonts, images, audio and data local **(S)**
- [ ] No cloud dependency for the default demo **(S)**
- [ ] Provenance visible on every signal and decision **(S)**
- [ ] Clear real vs simulated table in the UI and docs **(S)**
- [ ] Synthetic or licensed learner data only **(S)**
- [ ] No real student media in the public demo **(S)**

### 0B.7 Tests and docs

- [ ] Unit tests for adapter mapping, policy, constraints and re-plan **(M)**
- [ ] Integration test over real WebSocket clients **(M)**
- [ ] Contract test for LAIX version and decision shape **(S)**
- [ ] Playwright e2e for three students and the teacher **(M)**
- [ ] Deterministic reset test **(S)**
- [ ] Load test with 10 rooms and 50 clients **(M)**
- [ ] Accessibility smoke test: keyboard, captions, contrast **(S)**
- [ ] `docs/architecture.md`, `docs/laix-boundary.md`, `docs/consent-privacy.md` **(M)**
- [ ] `docs/limitations.md` with honest stand-ins **(S)**
- [ ] Demo runbook and reset checklist **(S)**

### Demo architecture

- Fixed seed and fixed scenario; every run is identical.
- LAIX decisions are live; the scenario injects inputs, never decisions.
- No cloud model calls on stage; optional providers are disabled.
- Stage mode and booth mode are separate routes.
- The decision panel can switch between plain English and technical detail.
- A provenance panel answers "what is real?" in Q&A.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the product in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] The wait moment lands by 30 seconds.
- [ ] The trust beat lands by 60 seconds.
- [ ] The full arc runs in 90 seconds.
- [ ] Reset under five seconds.
- [ ] Two volunteers can run the consent choice without help.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers repeat the closing line.
- [ ] Three back-to-back runs show no drift.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to the wait moment: ≤ 30 s.
- Time to the trust beat: ≤ 60 s.
- Full run: ≤ 90 s.
- Volunteer completion: ≥ 80%.
- Qualified education conversations: ≥ 15.
- Pilot introductions booked: ≥ 5.

### Post-stage motion

- QR to the playable demo, not a signup form.
- One-page "one class, 90 days" pilot offer.
- A 10-minute booth version.
- Follow-up within 48 hours with the recording and the one-pager.
- Capture 15 named tutoring and teaching leaders.

---

## Phase 1 — First pilot

Goal: one class, one subject, one teacher, 90 days. Run alongside the existing lesson, not as a
replacement.

**Gate:** do not start the pilot until the stage piece passes all acceptance tests and the LAIX
adapter has contract tests.

### 1.1 Classroom, identity and roles

- [ ] Class creation and join code **(S)**
- [ ] Teacher, student, helper and observer roles **(S)**
- [ ] Session roster and attendance **(S)**
- [ ] Device check: browser, mic, camera, network **(M)**
- [ ] Local demo auth for the pilot **(S)**
- [ ] SSO/OIDC path designed, even if not enabled **(S)**
- [ ] Server-side role enforcement, not UI-only **(M)**
- [ ] Class and session isolation **(M)**
- [ ] Admin view for classes, users and data policy **(M)**
- [ ] Account deletion and export request path **(S)**

### 1.2 LAIX decision core

- [ ] Pin the release tag and record the exact version **(S)**
- [ ] Adapter maps events to `Situation`, `Belief`, `Constraint` and `Action` **(M)**
- [ ] Learning policy plugin with visible factors **(M)**
- [ ] Hard constraints run before scoring **(M)**
- [ ] Canonical verbs map to learning action ids **(S)**
- [ ] Decision alternatives include the rejected options and reasons **(S)**
- [ ] Confidence source and calibration shown honestly **(S)**
- [ ] Approval required for peer help, guardian notice and teacher escalation **(S)**
- [ ] Decision record includes evidence, basis, approval and outcome **(M)**
- [ ] Re-plan on consent revoke, helper decline, disconnect, timeout and tool failure **(M)**
- [ ] Attention and cooldown rules for interruption **(M)**
- [ ] Policy version pinned on every decision **(S)**
- [ ] No local LAIX copy; isolation test **(S)**
- [ ] Parity fixture: teaching team labels vs policy output **(M)**
- [ ] Bench pack for false positives, false negatives and interruption cost **(M)**

### 1.3 Signals and media

- [ ] Answer, attempt, correctness and time signals **(S)**
- [ ] Explicit help by button, chat and speech **(M)**
- [ ] STT with visible provenance and a typed fallback **(M)**
- [ ] Voice activity and speaking state **(M)**
- [ ] Hand-raise signal with low confidence **(M)**
- [ ] Presence and disconnect **(S)**
- [ ] Board edits and share state **(M)**
- [ ] Teacher override as authoritative evidence **(S)**
- [ ] Camera on/off and mic on/off controls **(S)**
- [ ] Echo guard while TTS is speaking **(M)**
- [ ] No face, emotion or attention inference **(S)**
- [ ] Optional vision off by default, with explicit opt-in **(M)**
- [ ] Sensor events only to LAIX; no raw media **(S)**

### 1.4 Student experience

- [ ] Join and device check without a manual **(S)**
- [ ] Own problem and own board **(M)**
- [ ] Help button and spoken help **(M)**
- [ ] Consent prompt with a plain explanation of what is shared **(S)**
- [ ] Consent revoke in one action **(S)**
- [ ] Peer explanation with captions **(M)**
- [ ] Private hint with a clear next step **(S)**
- [ ] Camera/mic off and privacy controls **(S)**
- [ ] No visibility of another learner's private work **(S)**
- [ ] Session end and record summary **(S)**
- [ ] Mobile and tablet layout **(M)**
- [ ] Reduced-motion and high-contrast modes **(S)**

### 1.5 Teacher experience

- [ ] Teacher wall with one card per learner **(M)**
- [ ] Evidence, decision and consent state at a glance **(S)**
- [ ] "Who needs what now?" queue **(M)**
- [ ] Approve, reject and override with a reason **(M)**
- [ ] Pause a learner or the room **(S)**
- [ ] Block peer help for a learner or session **(S)**
- [ ] Mark a safeguarding concern **(M)**
- [ ] Session brief before class **(M)**
- [ ] Post-session brief and next step **(M)**
- [ ] Decision record and replay **(M)**
- [ ] No raw media beyond the consented session **(S)**
- [ ] Keyboard shortcuts for the wall **(S)**
- [ ] Alert fatigue controls: dedupe, quiet hours, digest **(M)**

### 1.6 Consent, privacy and safeguarding

- [ ] Consent object with scope, purpose, actor, time and expiry **(M)**
- [ ] Peer consent for learner and helper **(M)**
- [ ] Guardian consent where required **(M)**
- [ ] Recording consent separately from session consent **(M)**
- [ ] STT cloud notice and opt-out **(S)**
- [ ] Vision opt-in and data path **(S)**
- [ ] Retention policy per class and per media type **(M)**
- [ ] Deletion and forget path **(M)**
- [ ] Redaction for transcripts and exports **(M)**
- [ ] Safeguarding escalation to a human, never a peer **(S)**
- [ ] No automatic discipline, grading or parent contact **(S)**
- [ ] DPIA and data-processing agreement for the pilot **(M)**
- [ ] Privacy review with the school **(M)**
- [ ] Consent audit and revocation audit **(S)**

### 1.7 Records, outcomes and memory

- [ ] Decision record schema and storage **(M)**
- [ ] Session timeline: events, decisions, approvals, overrides **(M)**
- [ ] Outcome labels: helped, not helped, unknown **(S)**
- [ ] Outcome loop feeds the policy priors, bounded and visible **(M)**
- [ ] PPMA port: profiles, progress and consent **(M)**
- [ ] Local PPMA stand-in for the pilot **(S)**
- [ ] No private history to peers **(S)**
- [ ] Student-visible record summary **(S)**
- [ ] Teacher-visible session review **(M)**
- [ ] Export: CSV, JSON and printable summary **(M)**
- [ ] Audit chain with verification **(M)**
- [ ] Backup and restore drill **(M)**

### 1.8 Deployment and operations

- [ ] Single-school deployment on a local server or private cloud **(M)**
- [ ] Docker Compose for app, database and optional services **(M)**
- [ ] TLS for camera and microphone **(S)**
- [ ] TURN server for restrictive networks **(M)**
- [ ] Secrets management, no keys in the repo **(S)**
- [ ] Rate limits and upload limits **(M)**
- [ ] Structured logs without raw transcripts **(S)**
- [ ] Metrics: events, decisions, interventions, consent, approvals, latency, errors **(M)**
- [ ] Health and readiness endpoints **(S)**
- [ ] Backup, restore and retention job **(M)**
- [ ] Kill switch for proactive features and peer help **(S)**
- [ ] Incident runbook and contact path **(S)**

### 1.9 Pilot measurement and gates

- [ ] Baseline: time to help, teacher interruptions, peer-help frequency **(M)**
- [ ] Baseline: student outcome on the pilot topic **(M)**
- [ ] Measure: time from struggle to help **(S)**
- [ ] Measure: interventions avoided below the line **(S)**
- [ ] Measure: peer-help uptake and success **(S)**
- [ ] Measure: teacher time saved **(S)**
- [ ] Measure: false positives and false negatives **(M)**
- [ ] Measure: consent coverage and revocation correctness **(S)**
- [ ] Measure: technical reliability and media quality **(M)**
- [ ] Weekly review with the teacher **(S)**
- [ ] **Gate 1** — four-week shadow mode: decisions visible to the teacher, no automatic peer help **(M)**
- [ ] **Gate 2** — 90-day pilot: teacher trust, consent coverage, no privacy incidents **(M)**
- [ ] **Gate 3** — production only after two green months and a signed data agreement **(S)**
- [ ] Kill criteria written before launch: false-positive rate, teacher overload, privacy incident **(S)**

---

## Phase 2 — Production

Goal: multiple classes and teachers, real integrations, paid seats and a reliable service.

### 2.1 Multi-class and multi-tenant

- [ ] School, programme and class hierarchy **(M)**
- [ ] Multi-teacher classes and co-teaching **(S)**
- [ ] Tenant isolation at the database and API layer **(L)**
- [ ] Role-based access with server-side enforcement **(M)**
- [ ] SSO/OIDC and SCIM provisioning **(L)**
- [ ] Per-tenant configuration and feature flags **(M)**
- [ ] Data residency options **(L)**
- [ ] Tenant-level retention and deletion **(M)**
- [ ] Per-tenant quotas and rate limits **(S)**
- [ ] Cross-class analytics without leaking learner identity **(M)**

### 2.2 LMS, SIS and calendar integrations

- [ ] Google Classroom roster and coursework **(M)**
- [ ] Canvas LTI 1.3 **(L)**
- [ ] Moodle LTI 1.3 **(M)**
- [ ] Microsoft Teams education tab **(M)**
- [ ] OneRoster / SIS roster import **(M)**
- [ ] Calendar sync for sessions **(S)**
- [ ] Grade passback only when the teacher opts in **(M)**
- [ ] Deep links to a session and a decision record **(S)**
- [ ] Webhook and API for external systems **(M)**
- [ ] Integration health and failure visibility **(S)**

### 2.3 Content and curriculum

- [ ] Problem bank for the first subject **(M)**
- [ ] Hint and worked-example generation with review **(M)**
- [ ] Curriculum tags and difficulty **(S)**
- [ ] Teacher-authored problems and rubrics **(M)**
- [ ] Content versioning and provenance **(S)**
- [ ] Localisation for the first two languages **(M)**
- [ ] Content safety and age appropriateness **(M)**
- [ ] Licensing and attribution for every asset **(S)**
- [ ] Offline content pack **(M)**

### 2.4 Real-time media at scale

- [ ] WebRTC mesh for small rooms **(M)**
- [ ] SFU path for larger rooms **(L)**
- [ ] TURN service and network diagnostics **(M)**
- [ ] Adaptive bitrate and device fallback **(M)**
- [ ] Captions and transcript sync **(M)**
- [ ] Optional recording with explicit consent **(L)**
- [ ] Media quality metrics: jitter, packet loss, RTT **(M)**
- [ ] Echo cancellation and speaking detection **(M)**
- [ ] Screen share and image board limits **(M)**
- [ ] Low-bandwidth mode: audio + board only **(M)**
- [ ] Browser support matrix: Chrome, Edge, Safari **(M)**

### 2.5 Teacher analytics and workflow

- [ ] Session brief: who needs attention, open consent, next step **(M)**
- [ ] Decision quality review: accepted, rejected, corrected **(M)**
- [ ] Intervention trends by class and topic **(M)**
- [ ] Teacher time saved estimate, labelled as an estimate **(S)**
- [ ] Student progress view, not a rank **(M)**
- [ ] Exportable session report **(M)**
- [ ] Parent/guardian summary only with consent **(M)**
- [ ] Teacher feedback loop on decisions **(M)**
- [ ] Alert fatigue dashboard **(S)**

### 2.6 Admin, billing and procurement

- [ ] School and programme accounts **(M)**
- [ ] Seat and classroom plans **(M)**
- [ ] Invoices, tax and purchase orders **(M)**
- [ ] Trial and pilot conversion **(S)**
- [ ] Usage dashboards and quotas **(S)**
- [ ] Security questionnaire pack **(M)**
- [ ] DPA, subprocessors and data map **(M)**
- [ ] Accessibility conformance report **(M)**
- [ ] Support tiers and SLAs **(M)**
- [ ] Status page and incident communication **(S)**

### 2.7 Reliability, security and compliance

- [ ] SLOs for join, decision, directive and board sync **(M)**
- [ ] Load test at 100 rooms and 500 clients **(L)**
- [ ] Chaos tests: disconnect, TURN failure, STT failure, database failover **(M)**
- [ ] Backup, restore and disaster-recovery drill **(M)**
- [ ] Penetration test and threat model **(L)**
- [ ] Dependency and container scanning **(M)**
- [ ] SBOM and release provenance **(S)**
- [ ] GDPR / FERPA / COPPA-style review for target markets **(L)**
- [ ] DPIA template and records of processing **(M)**
- [ ] Retention automation and legal hold **(M)**
- [ ] Audit export and signed records **(M)**
- [ ] Incident response and breach notification runbook **(M)**

### 2.8 Mobile, offline and low bandwidth

- [ ] Installable PWA for students and teachers **(M)**
- [ ] Offline shell and cached session pack **(M)**
- [ ] Reconnect and resume a session **(M)**
- [ ] Low-bandwidth audio-only mode **(S)**
- [ ] Push notifications for teacher alerts **(M)**
- [ ] Camera/mic permissions guidance per browser **(S)**
- [ ] Mobile capture for a photo of work **(S)**
- [ ] Touch targets and bottom sheets **(S)**

---

## Phase 3 — Scale

Goal: a school or district can run StudyRoom across many classes without adding support burden.

- [ ] District and institution hierarchy **(L)**
- [ ] Multi-region deployment and data residency **(L)**
- [ ] Device management and managed browser profiles **(M)**
- [ ] Roster automation and term rollover **(M)**
- [ ] Content partner programme **(M)**
- [ ] LTI / OneRoster / xAPI ecosystem **(L)**
- [ ] Scholarship or research accounts **(S)**
- [ ] Usage and cost observability per school **(M)**
- [ ] Support portal, training and office hours **(M)**
- [ ] Teacher community and decision-policy templates **(M)**
- [ ] Certification for accessibility and security **(M)**
- [ ] Multi-language support and regional compliance **(L)**
- [ ] Offline school-server mode **(M)**
- [ ] Managed TURN and media relay **(L)**
- [ ] Cost per active room and per decision **(S)**
- [ ] Capacity planning for term start **(M)**
- [ ] Partner and reseller enablement **(S)**

---

## Phase 4 — Proactive teacher readiness

Goal: make StudyRoom the teacher's daily readiness desk. Catch the learner who is slipping before the
next lesson, not after the test.

**Contract:** recommendations only. No automatic parent contact, discipline, grading or peer
involvement.

### 4.0 Scope and guardrails

- [ ] Watched object: class, learner, topic, session and consent state **(M)**
- [ ] Separate **Live room** from **Readiness** in navigation and permissions **(M)**
- [ ] Readiness plan per class: dates, topics, assessments, consent and ownership **(S)**
- [ ] Freshness contract for signals, progress and consent **(S)**
- [ ] Coverage contract: which learners and topics are watched, and the blind spots **(S)**
- [ ] Define "no action" as a valid, recorded outcome **(S)**
- [ ] Onboarding: class → roster → consent → topic → baseline → test **(M)**
- [ ] Pause, resume and kill switch per class, visible to the teacher **(S)**
- [ ] Start with one class, one topic and one risk type **(S)**

### 4.1 Class data and readiness

- [ ] Class calendar and topic sequence **(M)**
- [ ] Learner progress and attempt history, with consent **(M)**
- [ ] Topic prerequisites and misconception map **(M)**
- [ ] Assessment dates and deadlines **(S)**
- [ ] Consent and sharing status **(M)**
- [ ] Data quality: missing roster, stale progress, revoked consent **(S)**
- [ ] Change detection when a learner, topic or consent changes **(M)**
- [ ] Provenance on every readiness check **(S)**
- [ ] Teacher notes and context **(M)**
- [ ] Handoff between teachers **(S)**

### 4.2 Detection and alerting

- [ ] Early struggle pattern: repeated errors, time, disengagement **(M)**
- [ ] Peer-help dependency pattern **(M)**
- [ ] Consent or privacy risk **(M)**
- [ ] Missed session or repeated absence **(S)**
- [ ] Topic prerequisite gap **(M)**
- [ ] Assessment readiness risk **(M)**
- [ ] Adaptive thresholds by class, age and topic **(M)**
- [ ] Deduplicate and group risks by learner and topic **(S)**
- [ ] Human-readable readiness summary from evidence **(M)**
- [ ] Suggested check or action with effort and owner **(M)**
- [ ] Estimate impact, labelled as an estimate **(M)**
- [ ] Near-miss capture **(S)**
- [ ] "Why now?" evidence pack **(S)**

### 4.3 Anticipation

- [ ] 7 / 3 / 1-day readiness checks before a lesson or assessment **(M)**
- [ ] New learner or topic change triggers a re-check **(S)**
- [ ] Consent expiry and renewal countdown **(S)**
- [ ] Assessment deadline and revision plan **(M)**
- [ ] "What changed since your last look" digest **(S)**
- [ ] Backtest readiness checks over past classes **(M)**
- [ ] Recommendations only; no automatic intervention **(S)**

### 4.4 Readiness lifecycle

- [ ] Risk states: new → acknowledged → assigned → investigating → resolved / dismissed **(M)**
- [ ] Dismissal reason taxonomy **(S)**
- [ ] Assignment to teacher or teaching assistant **(M)**
- [ ] SLA timers for lesson and assessment deadlines **(M)**
- [ ] Learner timeline combining events, decisions and notes **(M)**
- [ ] "Why this risk" panel **(S)**
- [ ] Create a session plan or check from a risk **(M)**
- [ ] Post-action verification and reopen **(M)**
- [ ] "Fixed but not verified" items in the weekly brief **(S)**
- [ ] Risk-fatigue budget per teacher per week **(S)**
- [ ] Handoff to the live room without re-uploading context **(S)**
- [ ] Mobile readiness card **(S)**

### 4.5 Notifications and integrations

- [ ] Email with a signed deep link **(S)**
- [ ] Slack / Teams with acknowledge and assign **(M)**
- [ ] SMS / pager for critical safeguarding or assessment risks **(S)**
- [ ] Calendar sync for sessions and assessments **(M)**
- [ ] LMS task or announcement **(M)**
- [ ] Generic webhook with HMAC and retry **(S)**
- [ ] Per-tenant notification isolation **(S)**
- [ ] Quiet hours and digest fallback **(S)**

### 4.6 Trust, governance and safety

- [ ] Immutable audit of readiness checks, approvals and dismissals **(M)**
- [ ] Policy and model version pinned on every risk **(S)**
- [ ] Explainability per risk class **(M)**
- [ ] False-alarm cost and trend by class and reason **(M)**
- [ ] Teacher override analysis **(M)**
- [ ] Safeguarding sign-off, never automatic **(M)**
- [ ] Privacy review for learner data **(M)**
- [ ] Per-tenant isolation and encryption **(M)**
- [ ] No learner-facing risk before teacher validation **(S)**
- [ ] Kill switch and stop-all-readiness runbook **(S)**
- [ ] Explicit non-goals enforced: no discipline, no parent contact, no grading **(S)**

### 4.7 Readiness UI

- [ ] Class readiness board: learners, topics, status, owner and next action **(M)**
- [ ] Learner readiness card: evidence, consent, trend and next step **(M)**
- [ ] Topic and assessment drift views **(M)**
- [ ] Daily / weekly teacher digest **(S)**
- [ ] Notification preferences **(S)**
- [ ] One-click acknowledge / assign / dismiss with reason **(S)**
- [ ] "Why this risk" drawer **(S)**
- [ ] Dashboard: open risks, time-to-lesson, precision, teacher time saved **(M)**
- [ ] Mobile readiness card and deep link **(S)**
- [ ] Weekly brief: top risks, consents due and open items **(M)**

### 4.8 Commercial motion

- [ ] Per-class, per-programme and per-term pricing **(M)**
- [ ] SLA tiers: weekly readiness, lesson-week readiness, live room **(S)**
- [ ] 90-day readiness pilot: one class, shadow mode first **(M)**
- [ ] Pilot measurement: missed risks, time saved, teacher load **(M)**
- [ ] Renewal criteria and pilot credit **(S)**
- [ ] Partner motion with tutoring centres and schools **(S)**
- [ ] One-page "readiness in 90 days" offer **(S)**
- [ ] Security and procurement pack **(M)**
- [ ] Reference case with measured teacher time **(S)**

### 4.9 Platform and operations

- [ ] PostgreSQL store for classes, risks, consents and approvals **(M)**
- [ ] Object storage for exports and evidence packs **(M)**
- [ ] Job queue and scheduler for readiness checks **(M)**
- [ ] Multi-tenant configuration and quotas **(M)**
- [ ] Secrets vault for LMS and notification credentials **(S)**
- [ ] Observability: metrics, logs, traces and delivery dashboards **(M)**
- [ ] Backup/restore and DR drill **(M)**
- [ ] Offline readiness queue **(M)**
- [ ] Retention per class and per learner **(S)**
- [ ] Load test at 500 classes and 10,000 learners **(L)**
- [ ] Cost observability per class **(S)**

### 4.10 Pilot measurement and gates

- [ ] Baseline missed readiness items before the pilot **(S)**
- [ ] Time saved per teacher per week **(S)**
- [ ] Precision and recall against confirmed risks **(M)**
- [ ] Risks per teacher per day and time-to-acknowledge **(S)**
- [ ] Action conversion: risks that led to a session change **(S)**
- [ ] Cost per class and cost per actionable risk **(S)**
- [ ] **Gate 1** — four-week shadow mode; no learner-facing risks **(S)**
- [ ] **Gate 2** — 90-day pilot: precision ≥ 0.80, actionable rate ≥ 25% **(M)**
- [ ] **Gate 3** — production after two green months and a signed data agreement **(S)**
- [ ] Kill criteria: precision < 0.60, alert fatigue above budget, unsafe routing **(S)**

---

## Phase 5 — Product experience (2026, planned)

Goal: the room a teacher wants to open every day. The stage piece stays intact; this phase is the
product, not the demo.

### 5.0 Audit and principles

- [ ] Screen-by-screen audit at 1440, 1024, 768 and 390 px **(S)**
- [ ] Inventory every legacy tell: tiny type, permanent panels, fixed desktop, missing states **(S)**
- [ ] Interview five users per role: student, helper, teacher, teaching assistant **(M)**
- [ ] Write the 2026 principles and anti-patterns **(S)**
- [ ] Baseline task metrics: join, first help, consent, session review **(M)**

### 5.0A Visual direction

The direction is **a quiet rehearsal room, not a school dashboard**. The teacher is a conductor; the
room is a score of learners, cues, rests and interventions.

- [ ] Choose the visual direction and write it into the design brief **(S)**
- [ ] Separate the **stage theatre** palette from the **daily desk** palette **(S)**
- [ ] Define the metaphor: conductor's desk, learner strips, evidence line, decision dock **(S)**
- [ ] Define the type scale: 11 / 12 / 13 / 14 / 16 / 20 / 24 / 32 / 44 **(M)**
- [ ] Choose editorial display, room UI and evidence mono fonts; subset and self-host **(M)**
- [ ] Define the palette: warm paper, deep ink, one cobalt accent **(M)**
- [ ] Define semantic colours: waiting, consent, helped, safeguarding, shared **(S)**
- [ ] Prove contrast for every role in light, dark and high-contrast themes **(M)**
- [ ] Define spacing, radius, elevation and z-index tokens **(S)**
- [ ] Define motion tokens and the state-transition grammar **(S)**
- [ ] Design the signature components: learner strip, evidence line, decision dock, consent pair,
  room score, component strip, record timeline **(L)**
- [ ] Design the "why" drawer: evidence, alternatives, constraints and confidence source **(M)**
- [ ] Design the "what would change the answer?" view **(S)**
- [ ] Design the empty, waiting, observing, consent-pending, helping, re-plan, verified, escalated,
  offline and no-decision states **(L)**
- [ ] Design the teacher override as a first-class interaction, not a hidden menu **(M)**
- [ ] Design the student "ask" and consent preview in one screen **(M)**
- [ ] Design the stage wall as a separate theatrical surface **(M)**
- [ ] Write the anti-pattern list: neon dashboard, card grid, chatbot bubble, confetti, cartoon
  avatars, tiny type, permanent sidebar, surveillance video wall, 3D decoration **(S)**
- [ ] Run a five-second test on the chosen direction **(S)**
- [ ] Test the stage direction at 10 metres and 16:9 / 4:3 **(S)**

### 5.1 Brand and design system

- [ ] Logotype and app mark at 16, 32 and stage scale **(M)**
- [ ] One cobalt accent; semantic colour for waiting, consent, helped, safeguarding and shared **(S)**
- [ ] Light, dark and high-contrast themes designed together **(M)**
- [ ] Warm paper and deep ink base; no neon, glass or gradient decoration **(S)**
- [ ] Colour-blind-safe palette; status always has text and icon **(S)**
- [ ] Type: editorial display, Inter for the room, mono for evidence **(M)**
- [ ] Design tokens: colour, type, space, radius, shadow, motion **(M)**
- [ ] Accessible primitives for dialogs, menus, tabs, tooltips and comboboxes **(M)**
- [ ] Core components: learner strip, evidence line, decision dock, consent pair, room score, board, transcript **(L)**

### 5.2 Information architecture and command

- [ ] Class home: sessions, learners, consent and next action **(M)**
- [ ] Live room as the primary workspace; panels contextual **(M)**
- [ ] Global command palette (`Cmd/Ctrl+K`) **(M)**
- [ ] Role-based navigation that hides what the role cannot act on **(M)**
- [ ] Context rail: learners, decisions, consent, board, record **(M)**
- [ ] Session review and decision-record views **(M)**
- [ ] Mobile review for teachers and teaching assistants **(S)**
- [ ] Class and learner library **(M)**

### 5.3 Live room craft

- [ ] Student tile: video/avatar, speaking ring, captions, state **(M)**
- [ ] Teacher wall: evidence, decision, consent and next action without clutter **(L)**
- [ ] Learner strips along a room score, not a grid of equal cards **(L)**
- [ ] Evidence line with a visible threshold and a clear "below the line" state **(M)**
- [ ] Decision dock: verb, action, reason, alternatives and approval **(M)**
- [ ] Consent rail: who is asked, what is shared, accept / decline / revoke **(M)**
- [ ] Component strip: Mate, PPMA, LAIX and JiuwenSwarm last action **(S)**
- [ ] Stage wall: five panes, story rail and reset **(M)**
- [ ] Board: private/shared state, versions, images, screen frames **(L)**
- [ ] Decision panel: plain English first, technical detail on demand **(M)**
- [ ] Consent flow that explains exactly what is shared **(M)**
- [ ] Re-plan animation that shows what changed **(M)**
- [ ] Human override and signature visible on the record **(S)**
- [ ] 10-metre readability for the stage **(M)**
- [ ] Presenter mode: large type, keyboard-only, no accidental edits **(M)**

### 5.4 AI-native interaction

- [ ] Natural-language teacher commands: "who needs help?", "why did it wait?" **(L)**
- [ ] Intent parser with clarification and safe fallbacks **(M)**
- [ ] Agent sidecar that reads the current room context **(M)**
- [ ] Tool calls rendered as inspectable steps **(M)**
- [ ] "Why this decision?" with evidence and alternatives **(M)**
- [ ] "What would change the answer?" view **(M)**
- [ ] Never hide a refusal or a low-confidence answer **(S)**

### 5.5 Role flows and mobile

- [ ] Student flow: join → work → ask → consent → solve in ≤ 3 interactions per decision **(M)**
- [ ] Helper flow: offer → consent → explain → hand back **(M)**
- [ ] Teacher flow: brief → live wall → override → review **(M)**
- [ ] Teaching assistant flow: triage, notes, follow-up **(S)**
- [ ] Mobile-first layouts at 390 and 768 px **(M)**
- [ ] Installable PWA with offline shell **(S)**
- [ ] Bottom sheets, sticky actions and 44 px targets **(S)**

### 5.6 Accessibility and performance

- [ ] WCAG 2.2 AA audit and fixes **(M)**
- [ ] Full keyboard path and visible focus **(M)**
- [ ] Captions, transcripts and screen-reader labels **(M)**
- [ ] Reduced-motion mode **(S)**
- [ ] Performance budgets in CI: bundle, LCP, INP, CLS, media join time **(M)**
- [ ] Route-level code splitting and lazy media workers **(M)**
- [ ] Virtualized learner and decision lists **(M)**
- [ ] No external font or CDN calls **(S)**
- [ ] Low-bandwidth and audio-only mode **(M)**

### 5.7 Content, localisation and trust

- [ ] Voice and tone guide for students, helpers and teachers **(S)**
- [ ] Plain-language errors, empty states and disclaimers **(M)**
- [ ] Glossary: consent, evidence, intervention, re-plan, helper **(S)**
- [ ] Date, time, number and unit formatting per locale **(S)**
- [ ] English and Chinese UI copy from one source **(M)**
- [ ] Provenance visible on every signal and decision **(S)**
- [ ] AI-generated hints labelled and attributable **(S)**
- [ ] Human signature on approvals and session records **(S)**
- [ ] Audit trail accessible from the UI **(M)**

### 5.8 Engineering and assets

- [ ] React + Vite + strict TypeScript with no `any` in product code **(M)**
- [ ] Design tokens compiled from one source **(M)**
- [ ] Design-system package consumed by student, teacher and stage **(M)**
- [ ] Unit tests for evidence, policy, consent and board math **(M)**
- [ ] Final logo, icons, avatars, sounds and demo pack **(M)**
- [ ] Seeded demo pack with repeatable reset **(S)**
- [ ] Performance and accessibility checks in CI **(M)**

### 5.9 Research, rollout and gates

- [ ] Baseline SUS, task success and time-to-decision per role **(M)**
- [ ] Five-second test: "what does this product do?" **(S)**
- [ ] Five users per role complete the core task unaided **(M)**
- [ ] Design spike: shell, type, theme and command palette **(M)**
- [ ] Token and component foundation before screen rewrites **(M)**
- [ ] Rebuild the shell and navigation first **(M)**
- [ ] Migrate class home, live room, teacher wall and readiness **(M)**
- [ ] No text below 11 px in product chrome **(S)**
- [ ] Light, dark and high-contrast pass contrast **(M)**
- [ ] WCAG 2.2 AA signed off; keyboard reachability 100% **(M)**
- [ ] Time to first help drops ≥ 30% against baseline **(M)**
- [ ] SUS ≥ 80 with five pilot users **(M)**
- [ ] Keep the 90-second stage piece intact **(S)**

---

## Phase 6 — Production wiring

Goal: the code and integrations that make StudyRoom real for one class, not a demo shell.

### 6.1 LAIX adapter and policy

- [ ] `laix_adapter.py` is the only module that imports both worlds **(S)**
- [ ] Adapter maps host events to `Situation`, `Belief`, `Constraint` and `Action` **(M)**
- [ ] Learning policy plugin uses public LAIX types only **(M)**
- [ ] Policy version, schema version and package version pinned **(S)**
- [ ] No local LAIX copy; isolation test **(S)**
- [ ] Adapter contract tests for every verb and action id **(M)**
- [ ] Decision record round-trip and outcome loop **(M)**
- [ ] Re-plan fixtures for consent revoke, decline, disconnect and timeout **(M)**
- [ ] Decision bench with teacher labels **(M)**
- [ ] Upgrade runbook for a new LAIX tag **(S)**

### 6.2 Media and speech

- [ ] WebRTC mesh for small rooms **(M)**
- [ ] SFU path for larger rooms **(L)**
- [ ] TURN and network diagnostics **(M)**
- [ ] Microphone, camera and device switching **(M)**
- [ ] Voice activity, speaking state and echo guard **(M)**
- [ ] Browser STT with provenance and fallback **(M)**
- [ ] Optional on-device STT **(L)**
- [ ] TTS queue, per-student voice and captions **(M)**
- [ ] Optional recording with consent **(L)**
- [ ] Media quality metrics and alerts **(M)**
- [ ] Low-bandwidth and audio-only modes **(M)**

### 6.3 Board and shared work

- [ ] Private board state **(M)**
- [ ] Shared board only after consent **(M)**
- [ ] Typed steps, drawing, images and screen frames **(L)**
- [ ] Board versions and conflict handling **(M)**
- [ ] Board sync latency measurement **(S)**
- [ ] Image size and retention limits **(S)**
- [ ] Snapshot for the session record **(S)**
- [ ] Revocation closes the shared board immediately **(S)**
- [ ] Board replay **(M)**

### 6.4 PPMA, Digital Mate and JiuwenSwarm

- [ ] PPMA port for profiles, progress, consent and audit **(M)**
- [ ] Local PPMA stand-in for development **(S)**
- [ ] Digital Mate port for wording, personalization and TTS **(M)**
- [ ] Local Digital Mate stand-in **(S)**
- [ ] JiuwenSwarm port for tools and retries **(M)**
- [ ] Local tool adapter: hint, exercise, board, notes **(S)**
- [ ] Idempotency keys and duplicate prevention **(S)**
- [ ] Failure compensation and visible fallback **(M)**
- [ ] No host service imported by LAIX **(S)**

### 6.5 Auth, tenancy and data

- [ ] OIDC/SSO and SCIM **(L)**
- [ ] Server-side RBAC **(M)**
- [ ] Tenant isolation **(L)**
- [ ] PostgreSQL schema and migrations **(M)**
- [ ] Redis for sessions and queues **(M)**
- [ ] Object storage for exports and images **(M)**
- [ ] Encryption at rest and in transit **(M)**
- [ ] Secrets vault **(S)**
- [ ] Retention and deletion jobs **(M)**
- [ ] Audit chain and signed exports **(M)**
- [ ] Backup, restore and DR **(M)**

### 6.6 Observability and operations

- [ ] Structured logs with trace ids and no raw transcripts **(S)**
- [ ] Metrics: events, decisions, interventions, consents, approvals, re-plans **(M)**
- [ ] Latency: ingest, decision, event→directive, board sync, media join **(M)**
- [ ] Dashboards for room health, decisions and consent **(M)**
- [ ] Alerts for error rate, latency, media failure and queue depth **(M)**
- [ ] Cost observability: LLM, vision, STT, TURN, storage **(S)**
- [ ] Load test at 100 rooms and 500 clients **(L)**
- [ ] Chaos tests for media, STT, DB and queue **(M)**
- [ ] On-call runbook and incident process **(M)**
- [ ] Status page and maintenance mode **(S)**

### 6.7 Security and compliance

- [ ] Threat model: student, teacher, admin, media, board, integrations **(M)**
- [ ] Authentication and session security **(M)**
- [ ] Authorization tests for every role and tenant **(M)**
- [ ] CSRF, CORS, CSP and XSS controls **(M)**
- [ ] Upload validation and image limits **(S)**
- [ ] Rate limits and abuse controls **(M)**
- [ ] Dependency, container and secret scanning **(M)**
- [ ] Penetration test **(L)**
- [ ] SBOM and release provenance **(S)**
- [ ] DPIA, DPA and subprocessor list **(M)**
- [ ] GDPR / FERPA / COPPA-style review **(L)**
- [ ] Accessibility conformance report **(M)**
- [ ] Incident response and breach notification **(M)**

### 6.8 Deployment

- [ ] Single-laptop demo mode **(S)**
- [ ] Classroom LAN mode **(M)**
- [ ] School server mode **(M)**
- [ ] Cloud multi-tenant mode **(L)**
- [ ] Offline/air-gapped mode **(M)**
- [ ] Docker Compose for pilot **(M)**
- [ ] Kubernetes/Helm for production **(L)**
- [ ] TLS, reverse proxy and TURN **(M)**
- [ ] Backup/restore and DR drill **(M)**
- [ ] Upgrade and rollback procedure **(S)**
- [ ] Version pinning and changelog **(S)**

### 6.9 End-to-end production gate

- [ ] One real class, one subject, 90 days **(L)**
- [ ] Join → work → help → consent → board → verify → record, with no synthetic records **(L)**
- [ ] Teacher, student and guardian consent accepted **(M)**
- [ ] No privacy incident **(S)**
- [ ] Decision precision and recall meet the pilot gate **(M)**
- [ ] Media reliability meets the pilot SLO **(M)**
- [ ] LAIX adapter has no local copy and passes contract tests **(S)**
- [ ] Decision records are exportable and auditable **(M)**
- [ ] Runbook and rollback tested **(S)**

---

## Phase 7 — Evidence and research

Goal: prove that the decisions help learning, not only that the demo works.

- [ ] Pre/post assessment design for the pilot topic **(M)**
- [ ] Control or comparison group where ethical **(L)**
- [ ] Randomised or stepped-wedge design for a later study **(L)**
- [ ] Ethics review / IRB where required **(M)**
- [ ] Guardian and student consent for research data **(M)**
- [ ] De-identification and aggregation **(M)**
- [ ] Decision quality labels from teachers **(M)**
- [ ] False-positive and false-negative analysis **(M)**
- [ ] Calibration and confidence-source analysis **(M)**
- [ ] Bias review across age, language, gender and device **(L)**
- [ ] Interruption-cost analysis **(M)**
- [ ] Teacher workload analysis **(M)**
- [ ] Student experience and trust survey **(S)**
- [ ] Longitudinal retention and progress study **(L)**
- [ ] Publication or public report **(M)**
- [ ] Certification or evidence claim review with counsel **(M)**
- [ ] Stop criteria if evidence is negative **(S)**

---

## Not planned (with reasons)

- **Autonomous teaching** — the teacher remains accountable.
- **High-stakes grading or certification** — the product verifies work, not learning.
- **Face recognition, emotion detection or attention scoring** — surveillance, bias and trust risk.
- **Always-on recording** — data minimisation and consent.
- **Automatic parent contact or discipline** — safeguarding and legal risk.
- **Replacing the LMS or SIS** — integrate, do not clone.
- **A second decision engine** — one LAIX path, always.
- **Cloud-only media or inference** — schools need local and offline modes.
- **A dashboard-led product** — the live room and the decision are the product.
- **A marketplace for lesson content in the first version** — content quality and rights are a later
  problem.

---

## Dependencies and critical path

| Dependency | Blocks | Why |
|---|---|---|
| LAIX package pin + adapter | Policy, fast example, stage, pilot | One decision path |
| Learning policy | Every decision and re-plan | Domain logic |
| Consent model | Peer help, board sharing, real students | Legal and trust gate |
| Fast example | Stage rehearsal, presentation, regression fixture | Proof before media |
| Auth and roles | School deployment, teacher wall | Access control |
| Media stack | Real student pilot | Camera, mic and board |
| Records and outcomes | Pilot measurement, readiness | Evidence loop |
| Security review | Real students and procurement | Data protection |
| LMS/SIS integration | Daily teacher workflow | Roster and content |

The critical path is:

```text
LAIX pin → adapter → policy → fast example → stage → consent → pilot
                                      ↘ media → teacher wall ↗
```

Do not start real media before the decision loop and consent model are tested.

## Recommended order

1. **0A — the 90-second stage piece** (2 weeks). Build the wait moment, the trust beat and the line.
2. **Rehearse and red-team** (1 week). Acceptance tests, fallback, no-network run.
3. **0B — the functional demo** (4 weeks) with real LAIX decisions and deterministic inputs.
4. **The fast example** — `examples/studyroom_fast_demo/` and `/?view=demo`, one command, 12 steps.
5. **LAIX adapter and policy** before any real media. Prove the decision loop first.
6. **First pilot** — one class, one subject, 90 days, shadow mode first.
7. **Consent, privacy and safeguarding** before real students.
8. **Real media** after the decision loop is trusted.
9. **LMS/SIS integration** after the pilot shows teacher value.
10. **Phase 4 readiness** after the live room is stable.
11. **Phase 5 experience** once the product shape is settled.
12. **Phase 6 production wiring** before the first paid deployment.
13. **Phase 7 evidence** alongside the pilot, not after it.
14. **Phase 2 and 3 scale** only after two green pilots.

---

## Open decisions

- Which age group and subject first?
- Which buyer first: tutoring centre, university or corporate training?
- Which devices: school laptops, tablets or phones?
- Is browser-cloud STT allowed in the first pilot?
- Who owns consent: student, guardian, teacher or school?
- Which LMS/SIS integration comes first?
- Does the first version need real WebRTC, or are simulated signals enough?
- How much of the decision should the teacher see?
- What is the one learning metric the pilot will measure?
- Which content partner provides the first problem set?
- Is the first deployment local, school server or private cloud?
- Which LAIX policy pack should the learning policy build on?
- What is the hard line for peer help: consent from both learners, teacher, or both?
- Which signals are allowed in the first pilot: hand raise, voice, STT, board, all?
- What is the false-positive budget per lesson?
- Who signs the safeguarding and data-protection policy?

---

## Appendix A — Core contracts

### Event

| Field | Meaning |
|---|---|
| `event_id` | Unique event id |
| `session_id` | Room/session id |
| `user_id` | Opaque learner id |
| `type` | join, leave, answer, help, hand, speech, chat, board, consent, override, system |
| `modality` | video, audio, speech, board, chat, app, presence |
| `provenance` | real sensor, browser derived, app event, interpretation, simulated, system |
| `confidence` | 0..1, with source |
| `timestamp` | Host clock |
| `payload` | Typed event payload |
| `derived_from` | Parent event for interpretations |

### Situation

| Field | Meaning |
|---|---|
| `id` | Situation id |
| `at` | Timestamp |
| `subject` | Opaque learner or group id |
| `beliefs` | Propositions and confidence |
| `constraints` | Consent, privacy, no-interruption, cooldown, teacher-only |
| `attributes` | Evidence score, intervention line, urgency, flow state, time |

### Action option

| Field | Meaning |
|---|---|
| `id` | App action id (`ask-ben`, `hint-alice`) |
| `verb` | One of the seven LAIX verbs |
| `name` | Human-readable label |
| `expected_benefit` | 0..1 |
| `risk` | 0..1 |
| `delay_minutes` | Expected delay |
| `cost` | Money or resource cost |
| `disruption` | Interruption / social cost |
| `reversible` | Whether it can be undone |
| `requires_approval` | Consent or human approval |
| `metadata` | App-only fields, never interpreted by LAIX |

### Decision

| Field | Meaning |
|---|---|
| `verb` | Canonical verb |
| `action_id` | Chosen app action |
| `score` | Utility |
| `confidence` | 0..1 |
| `confidence_source` | Sensor, app event, interpretation, teacher |
| `calibrated` | Whether the confidence is calibrated |
| `alternatives` | Rejected options with reason |
| `constraints_applied` | Hard limits that changed the set |
| `requires_approval` | Whether the host must ask |
| `rationale` | Plain-language reason |
| `decision_id` | Stable id |
| `policy_version` | Pinned version |

### Consent

| Field | Meaning |
|---|---|
| `id` | Consent id |
| `subject` | Learner or guardian |
| `scope` | Peer, board, recording, STT, vision, research |
| `purpose` | Why the data is used |
| `granted` | Boolean |
| `granted_at` | Timestamp |
| `expires_at` | Optional |
| `revoked_at` | Optional |
| `actor` | Who granted it |
| `evidence` | UI event or signed record |

### Decision record

| Field | Meaning |
|---|---|
| `decision` | The LAIX decision |
| `request` | The generic request |
| `evidence` | Signals and references |
| `approval` | Who approved, when, why |
| `outcome` | Helped, not helped, unknown |
| `session_id` | Room |
| `created_at` | Timestamp |
| `audit_hash` | Chain link |

---

## Appendix B — API and WebSocket surface

### REST

- `GET /api/health`
- `GET /api/ready`
- `GET /api/status`
- `GET /api/rooms`
- `POST /api/rooms`
- `GET /api/rooms/{id}`
- `POST /api/rooms/{id}/join`
- `POST /api/rooms/{id}/reset`
- `GET /api/rooms/{id}/session`
- `GET /api/rooms/{id}/decisions`
- `GET /api/decisions/{id}`
- `GET /api/decisions/{id}/record`
- `POST /api/decisions/{id}/approve`
- `POST /api/decisions/{id}/reject`
- `POST /api/decisions/{id}/override`
- `GET /api/decisions/{id}/outcome`
- `POST /api/decisions/{id}/outcome`
- `GET /api/consent/{learner}`
- `POST /api/consent/{learner}`
- `POST /api/consent/{learner}/revoke`
- `GET /api/classes`
- `POST /api/classes`
- `GET /api/classes/{id}/roster`
- `GET /api/classes/{id}/readiness`
- `POST /api/readiness/{id}/{action}`
- `GET /api/admin/audit`
- `GET /api/admin/export`
- `POST /api/admin/backup`
- `GET /api/metrics`

### WebSocket

Client messages:

- `hello` — role, learner id, capabilities
- `event` — answer, help, hand, speech, chat, board, presence
- `answer` — directive option response
- `consent` — grant, decline, revoke
- `board` — operation, image, screen frame
- `control` — start, next, previous, reset, pause
- `webrtc` — offer, answer, ICE candidate
- `ping`

Server messages:

- `welcome` — session and role view
- `projection` — filtered room state
- `decision` — new decision
- `directive` — Mate, board, consent, tool
- `execution` — tool status
- `record` — decision record update
- `alert` — teacher or system alert
- `error` — typed error

Every message is schema-validated. A client cannot assert a correct answer; only the host can.

---

## Appendix C — Test matrix

| Layer | What it proves |
|---|---|
| Unit | Adapter mapping, policy scoring, constraints, consent, evidence math |
| Contract | LAIX version, decision shape, public imports, no local copy |
| Integration | WebSocket, room, consent, board, approvals, reconnect |
| E2E | Three browsers + teacher, fake media, board, stage run, reset |
| Load | 100 rooms, 500 clients, decision and sync latency |
| Chaos | Disconnect, TURN failure, STT failure, DB failover, queue backlog |
| Security | Auth bypass, role escalation, tenant isolation, XSS, upload, rate limit |
| Accessibility | WCAG 2.2 AA, keyboard, screen reader, captions, contrast |
| Visual | Stage at 10 m, desktop, tablet, phone, dark/light |
| Model eval | Decision agreement, false positives/negatives, calibration, interruption cost |
| Data | Provenance, retention, deletion, consent revocation, audit |
| Docs | Links, runbook, upgrade, limitations |

Required CI:

- [ ] Python lint, type check and tests **(M)**
- [ ] Frontend lint, type check and tests **(M)**
- [ ] Playwright e2e with one browser first **(M)**
- [ ] Contract test against the pinned LAIX tag **(S)**
- [ ] Link check and docs build **(S)**
- [ ] Docker build smoke test **(M)**
- [ ] Dependency and secret scan **(M)**
- [ ] Accessibility and performance budget checks **(M)**

---

## Appendix D — Security and privacy checklist

- [ ] Threat model reviewed before the pilot **(M)**
- [ ] Auth on every route and WebSocket **(M)**
- [ ] Role and tenant checks server-side **(M)**
- [ ] Session cookies or tokens with expiry and rotation **(S)**
- [ ] CRSF, CORS and CSP configured **(M)**
- [ ] Upload type, size and content validation **(S)**
- [ ] Rate limits per user, room and IP **(M)**
- [ ] Secrets in a vault, not in the repo **(S)**
- [ ] Encryption in transit and at rest **(M)**
- [ ] Raw media not logged or stored by default **(S)**
- [ ] Transcripts redacted before logs or exports **(M)**
- [ ] Consent and revocation audit **(M)**
- [ ] Retention and deletion jobs tested **(M)**
- [ ] Backup encrypted and restore tested **(M)**
- [ ] Dependency and container scanning **(M)**
- [ ] Penetration test before production **(L)**
- [ ] Incident response and breach notification **(M)**
- [ ] DPA, DPIA and subprocessor list **(M)**
- [ ] Guardian/minor consent flow reviewed **(M)**
- [ ] No emotion, face or attention inference **(S)**
- [ ] Safeguarding escalation to a human **(S)**
- [ ] Kill switch for peer help and proactive features **(S)**

---

## Appendix E — Deployment matrix

| Mode | Use | Requirements |
|---|---|---|
| Laptop demo | Stage and booth | Python, Node build, no network |
| Classroom LAN | One room | Local server, TLS, TURN optional |
| School server | One school | Postgres, Redis, TURN, backups |
| Private cloud | Pilot | OIDC, storage, monitoring, DPA |
| Multi-tenant cloud | Production | SSO, isolation, quotas, DR |
| Offline/air-gapped | Restricted school | Local media, local STT optional |

Every mode must state what is real, what is simulated and what is unavailable.

---

## Appendix F — Metrics

### Product

- Time from struggle to help.
- Interventions avoided below the line.
- Teacher interruptions avoided.
- Peer-help uptake and success.
- Teacher time on triage.
- Student trust and consent comprehension.
- False positives and false negatives.
- Learning outcome against baseline.

### System

- Join success and time.
- Decision latency p50/p95/p99.
- Event-to-directive latency.
- Board sync latency.
- Media join time and packet loss.
- STT error rate and fallback rate.
- WebSocket reconnect rate.
- Consent and approval latency.
- Error rate and queue depth.
- Cost per room and per decision.

### Safety

- Consent coverage.
- Revocation correctness.
- Privacy incidents.
- Safeguarding escalations.
- Unauthorized access attempts.
- Data deletion completion.

---

## Appendix G — Risk register

| Risk | Impact | Mitigation |
|---|---|---|
| Over-interruption | Students stop trusting the room | Hard evidence line, cooldown, teacher override |
| Surveillance perception | Parent or school rejection | No emotion/face, no recording by default, transparent provenance |
| Privacy incident | Trust and legal damage | Consent first, data minimisation, audit, pen test |
| False positive hand raise | Wrong peer request | Low confidence, teacher reject, learn from correction |
| Peer exposes private work | Harm and trust loss | Scope-limited share, consent, revocation |
| STT vendor cloud | Privacy concern | Disclosure, typed fallback, local STT option |
| Device/network failure | Lesson disruption | Audio-only mode, reconnect, offline pack |
| Teacher overload | Product abandoned | One queue, dedupe, digest, teacher time budget |
| LAIX API drift | Adapter breaks | Pin version, contract tests, upgrade runbook |
| Demo overfit | Pilot fails | Real pilot, recorded traces, teacher labels |
| Learning claim overreach | Credibility loss | Pre/post study, no demo claims |
| Cost creep | Unsustainable | Cost per room, quotas, caching, local inference |

---

## Appendix H — Failure and degradation matrix

| Failure | Product behaviour | Owner | Test |
|---|---|---|---|
| STT unavailable | Typed fallback; transcript marked unavailable | Host | Kill STT |
| Camera denied | Audio/board mode; no hand raise | Host | Deny permission |
| Mic denied | Board/text mode; no voice activity | Host | Deny permission |
| WebRTC/TURN failure | Reconnect; board-only fallback | Host | Block TURN |
| LAIX unavailable | Safe `wait`; teacher alert; no local engine | Host | Stop LAIX |
| Consent store unavailable | Fail closed: no peer help, no sharing | Host | Stop consent DB |
| PPMA unavailable | Queue memory writes; session continues | Host | Stop PPMA |
| Digital Mate unavailable | Text directive to teacher/student | Host | Stop Mate |
| JiuwenSwarm unavailable | Local safe fallback; visible failure | Host | Stop executor |
| Database unavailable | Preserve consent and records; stop unsafe actions | Host | Stop DB |
| Network lost | Offline pack and local session; sync on return | Host | Pull cable |
| Model or policy timeout | No decision; treat as wait; show reason | LAIX/Host | Delay engine |

Rules:

- Never silently switch to a second decision engine.
- Consent failures fail closed.
- Every degradation is visible in the console and the session record.
- The stage demo has a recorded fallback and a backup laptop.

## Appendix I — Retention defaults

Recommended defaults, reviewed per region and school policy:

| Data | Default | Export | Delete |
|---|---|---|---|
| Raw camera / microphone | Not retained | No | N/A |
| Transcript | Session-only unless saved | JSON / text | Yes |
| Board snapshot | Session-only | PNG / JSON | Yes |
| Decision record | 1 year | JSON / CSV / PDF | Yes |
| Audit record | 7 years or local policy | CSV / JSON | Tombstone |
| Progress / memory | PPMA policy | JSON | Yes |
| Research data | Off by default | Per study | Per study |

- No training on student data without separate consent.
- Deletion propagates to derived records with a tombstone.
- Legal hold overrides deletion and is audited.
- The school can export everything before leaving.

## Appendix J — Consent, outcome and override taxonomy

### Consent states

`not_asked` · `pending` · `granted` · `declined` · `revoked` · `expired` · `blocked`

### Outcome labels

`helped` · `not_helped` · `unknown` · `too_early` · `not_applicable`

### Teacher override reasons

`back_on_task` · `already_asked` · `consent_issue` · `not_appropriate` · `too_early` · `too_late` ·
`other`

Every override requires a reason. The reason is stored on the decision record and may adjust the next
decision's weights, but never silently changes the policy.

### Decision status

`proposed` · `awaiting_approval` · `approved` · `rejected` · `suppressed` · `executed` · `failed` ·
`expired`

## Appendix K — API compatibility and versioning

- [ ] API version in the path (`/api/v1`) **(S)**
- [ ] WebSocket protocol version in `hello` **(S)**
- [ ] Backward-compatible event additions; no silent field removal **(M)**
- [ ] Schema validation on every client message **(S)**
- [ ] Deprecation policy and sunset date **(S)**
- [ ] Migration path for stored records **(M)**
- [ ] Pinned LAIX version and upgrade runbook **(S)**
- [ ] Contract tests for the adapter and public API **(M)**
- [ ] Export format version in every file **(S)**
- [ ] No breaking change without a pilot gate **(S)**

## Appendix L — Definition of done

The app is full when all of these are true:

- [ ] A student can join, work, ask, consent and solve on a phone, tablet or laptop.
- [ ] A teacher can see who needs help, why, and what to do next.
- [ ] A peer can help with only the consented context.
- [ ] LAIX decides every intervention, with visible alternatives and constraints.
- [ ] The teacher can override, and the override changes the next decision.
- [ ] A helper decline or disconnect re-plans cleanly.
- [ ] Every decision has a record and an outcome.
- [ ] Consent is revocable and enforced by the host.
- [ ] No raw media goes to LAIX.
- [ ] No local LAIX copy exists; the pinned package passes contract tests.
- [ ] The fast example runs offline, covers 12 steps and starts in under three minutes.
- [ ] The 2026 direction is implemented: quiet room, one accent, type-led, accessible, motion that
  explains state.
- [ ] The stage piece runs offline in 90 seconds and resets in five.
- [ ] The 10-metre readability and five-stranger tests pass.
- [ ] The pilot measures time to help, teacher load, false positives and learning outcome.
- [ ] Security, privacy, accessibility and data-rights reviews are signed.
- [ ] Deployment, backup, restore, rollback and incident runbooks are tested.
- [ ] The docs explain what is real, what is simulated and what is not planned.
