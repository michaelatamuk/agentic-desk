# CUE — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means artist content and compute stay inside the production network.
"Agent" means JiuwenSwarm orchestrates look suggestions, checks and cue-sheet drafting.

**Status.** Concept + stage plan. No playable proof yet. Concept note: [cue.md](../concepts/cue.md).

**One line.** CUE designs the show before the lights go down — stage, looks, video, cues and budget in
one workspace.

**Buyer.** Production companies, touring artists, venues, festivals and brand-experience agencies.

**User.** Creative director, production designer, lighting designer, video designer, tour manager.

**The sentence the audience repeats.** *"The show is designed before the lights go down."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc, trust beat, acceptance tests and stagecraft.

Phases 4–6 adapt the proactive readiness, 2026 product-experience and production-wiring patterns
proven in the developed RootCause and GeoResponse roadmaps.

---

## What CUE is

A **pre-production design workspace** for live shows. It connects concept, stage, light, video,
blocking, setlist, cue sheet and cost on one timeline, and exports into the tools the crew already
uses.

## What CUE is not

- **Not a lighting console.** No DMX, no live show control.
- **Not a renderer replacement.** Depence², WYSIWYG, Capture, Vectorworks Spotlight, disguise and
  Notch remain the previz and media tools.
- **Not a music generator.** It works with the artist's track.
- **Not a CAD replacement.** It is the design layer above the drafting and previz tools.
- **Not autonomous.** The designer authors; the AI proposes and checks.

## Cadence

- **Freelance designer:** daily during pre-production, idle between shows.
- **Production company / venue / tour:** daily across a slate of shows.
- **The daily user is the production office.** Sell to the company, not only the creative.

---

## Phase 0A — The 90-second drop

Goal: a stage piece that makes the room feel the show before it exists.
Time: 2 weeks to build, 1 week to rehearse. No real rig, no console, no network.

**Set.** A black stage on screen, one practical lamp, a small moving light or set model on the desk,
headphones, and a printed cue sheet. The screen is the previz.

**The verb.** Scrub the track and drag a look onto the build.

**The cold open.** Blackout. One light. A song intro. *"The tour starts in six days. The drop isn't
landing."*

**The turn.** The designer finds a look that lands, rejects a spectacular but unsafe one, and hands
the crew a cue sheet that matches the show.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | One light, a track intro, six days to the tour | Stage blackout, setlist |
| 0:10–0:25 | First touch | Scrub the track; drag a lighting look onto the build | Previz, cost meter |
| 0:25–0:45 | Agent works | Three looks, a video transition, a set move; sightline/power flags | Looks, rig, cue timeline |
| 0:45–1:05 | Trust beat | AI's 12-fixture look blinds the front row and exceeds rig power; designer rejects it | Rig warning, glare cone, simpler look |
| 1:05–1:20 | Audience choice | Light drop or video drop; the room votes | Two drops, energy and cost |
| 1:20–1:30 | The reveal | The show plays; cue sheet prints; reset | Final 20 seconds, cue sheet |

### The trust beat, in detail

- The AI proposes a **12-fixture aerial beam look**. In previz it is spectacular.
- It has two visible problems: it **exceeds the rig's power/weight budget**, and it **blinds the
  front row** at the height of the drop.
- The designer rejects it. The system keeps the rejection and re-ranks.
- A **six-fixture look with one video moment** lands harder. The presenter says: *"It was
  spectacular. It was wrong. The show is not the rig."*

This is the product in one minute: creativity, evidence, a human decision, and a system that updates.

### Audience agency

The room chooses the drop:

- **Light drop** — high energy, higher rig cost.
- **Video drop** — cheaper rig, more content and cue complexity.

Both are defensible. The screen shows the trade-off; the presenter commits to the room's choice and
plays 20 seconds of the show.

### Props and stagecraft

- A small moving light or a scale set model on the desk.
- A practical lamp for the cold open.
- Headphones for the track; studio monitors for the reveal.
- A printed cue sheet and a blackout cue.
- One low sub hit at the drop; silence under the trust beat.
- Reset: `R`, under five seconds.

### Phase 0A checklist

- [ ] One licensed or generated 20-second track, cleared for public demo **(S)**
- [ ] Stage blockout: set, risers, screen, entrances **(M)**
- [ ] Three lighting looks on a timeline **(M)**
- [ ] One video moment with mapping/transition **(M)**
- [ ] Scrub-to-any-second previz with sound **(M)**
- [ ] Cost meter that responds to rig, crew and power **(M)**
- [ ] Sightline, glare and power checks that flag the hero look **(M)**
- [ ] Trust beat: reject the 12-fixture look; re-rank to the six-fixture look **(M)**
- [ ] Audience choice: light drop vs video drop **(S)**
- [ ] Cue sheet export/print **(M)**
- [ ] Deterministic stage mode, reset under five seconds **(S)**
- [ ] 90-second fallback recording and backup laptop **(S)**
- [ ] Contrast and legibility test at 10 metres **(S)**
- [ ] Artist/venue data rights and provenance sheet **(S)**
- [ ] Three rehearsals, one with a hostile audience, one with no network **(S)**

**Do not build for 0A:** console control, DMX, multi-user, asset marketplace, full CAD, music
generation.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" Same story, editable project, still deterministic
and offline.

Time: 3–4 weeks after 0A. It can reuse the stage piece as its shell.

- [ ] Import a licensed track and a stage blockout **(M)**
- [ ] Setlist with timings and transitions **(S)**
- [ ] Lighting looks, palettes and cue list **(M)**
- [ ] Video content, mapping and transitions **(M)**
- [ ] Blocking for artist, dancers and camera **(M)**
- [ ] Timeline scrub with audio and previz **(M)**
- [ ] Rig, crew, power and budget model **(M)**
- [ ] Sightline, glare and rigging checks **(M)**
- [ ] Agent look/cue suggestions with reasons **(M)**
- [ ] Cue-sheet export and print **(M)**
- [ ] Versioning for venue and tour leg **(S)**
- [ ] Booth mode: scenario picker, 3-minute run, reset **(S)**
- [ ] Runs fully offline on one laptop/GPU **(S)**

### Demo architecture

- Fixed track and fixed stage; every run is identical.
- Precomputed previz and look suggestions; no cloud model calls.
- All audio, video, models and fonts local.
- Stage mode and booth mode are separate routes.
- A provenance panel for Q&A: track licence, assets, model, simulated vs real.

### Data rights

- **Music:** the public demo uses a licensed or generated track, never an uncleared commercial song.
- **Artist content:** unreleased material stays local; no upload without written permission.
- **Venue/rig data:** customer confidential.
- **AI-generated looks/video:** ownership and disclosure terms must be explicit.
- Keep a provenance sheet for every asset.

### Compute and NPU

- GPU/CPU is the core: previz, playback, encoding.
- NPU is optional local inference: look/video suggestions, beat analysis, pose from rehearsal
  footage.
- Do not sell the NPU as the hero. If used, sell it as **on-site privacy for unreleased artist
  content**.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain CUE in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] The drop lands by 30 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat and the vote.
- [ ] Reset under five seconds.
- [ ] Two volunteers can change a look or vote without help.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to the drop: ≤ 30 s.
- Full run: ≤ 90 s.
- Volunteer completion: ≥ 80%.
- Qualified production-company conversations: ≥ 15.
- Pilot intros booked: ≥ 5.

### Post-stage motion

- QR to the playable demo, not a signup form.
- One-page "one tour, 90 days" pilot offer.
- A 10-minute booth version: one song, one drop.
- Follow-up within 48 hours with the recording and the one-pager.
- Capture 15 named production and venue leaders.

---

## Phase 1 — First pilot

Goal: one production company, three shows, 90 days. Run alongside the existing design process.

**Gate:** do not start the pilot until the stage piece has passed all acceptance tests.

### 1.1 Project and import

- [ ] Track and setlist import **(S)**
- [ ] Stage blockout **(M)**
- [ ] Venue profile: stage dimensions, rig, power, load-in, sightlines **(M)**
- [ ] Existing CAD/previz import or reference **(M)**
- [ ] Lighting/video asset import **(M)**
- [ ] Rights and provenance register for the track and assets **(S)**

### 1.2 Design

- [ ] Looks, palettes and cue list **(M)**
- [ ] Video mapping and transitions **(M)**
- [ ] Blocking and camera plan **(M)**
- [ ] Setlist timing and energy curve **(S)**

### 1.3 Validation

- [ ] Sightline and glare check **(M)**
- [ ] Rigging, weight and power check **(M)**
- [ ] Budget and crew estimate **(M)**
- [ ] Collision/blackout checks between set, light and video **(M)**
- [ ] Laser, structural load and load-in/changeover constraints **(M)**
- [ ] Human safety sign-off before any cue is released to the venue **(S)**

### 1.4 Cue sheet and export

- [ ] Cue-sheet editor and print **(M)**
- [ ] Export to the venue's format **(M)**
- [ ] Export to the previz/console tool used by the pilot **(M)**
- [ ] Cue-sheet diff and approval before export **(S)**
- [ ] Version per venue and tour leg **(S)**

### 1.5 Collaboration and approval

- [ ] Comments and review links **(S)**
- [ ] Designer/producer approval **(S)**
- [ ] Change log and immutable approval audit per show version **(S)**

### 1.6 Pilot measurement

- [ ] Baseline: previz iterations and rehearsal changes before go-live **(S)**
- [ ] Measure: iterations to approval, cue-sheet changes, rig cost avoided, rehearsal time **(M)**
- [ ] Weekly review with the production team **(S)**

### 1.7 Deployment

- [ ] Local/offline deployment for the production office **(M)**
- [ ] Optional on-site inference for unreleased content **(M)**
- [ ] Role-based access and signed exports **(M)**
- [ ] No outbound network required during a show week **(S)**

---

## Phase 2 — Production

Goal: multiple shows and venues, integrations with the tools crews already use, paid seats.

### 2.1 Integrations

- [ ] Vectorworks Spotlight import/export **(L)**
- [ ] WYSIWYG / Capture / Depence² previz exchange **(L)**
- [ ] grandMA3 cue import/export **(L)**
- [ ] disguise / Notch / Resolume video exchange **(L)**
- [ ] Budget and crew systems **(M)**

### 2.2 Libraries and reuse

- [ ] Look library and palette presets **(M)**
- [ ] Venue profiles and rig templates **(M)**
- [ ] Tour templates and setlist presets **(S)**
- [ ] Asset and content library **(M)**

### 2.3 Collaboration

- [ ] Multi-user projects and roles **(M)**
- [ ] Review links and annotations **(M)**
- [ ] Version comparison **(M)**
- [ ] Approval workflow **(S)**

### 2.4 Business

- [ ] Per-show and per-seat billing **(M)**
- [ ] Production-company accounts **(M)**
- [ ] Sponsorship/brand-experience projects **(S)**
- [ ] Setup and integration fees **(S)**

---

## Phase 3 — Scale

Goal: a touring network, a venue graph, and a marketplace of reusable looks and assets.

- [ ] Touring network: multiple cities, venues and crews **(L)**
- [ ] Venue database with rig, power and sightline profiles **(L)**
- [ ] Marketplace for looks, video content and set templates **(L)**
- [ ] Festival and multi-stage support **(L)**
- [ ] Brand-experience and product-launch pack **(M)**
- [ ] Real-time remote collaboration **(L)**
- [ ] Energy and sustainability reporting per show **(M)**
- [ ] Partner programme with previz, console and video vendors **(S)**

---

## Phase 4 — Tour readiness (proactive)

Goal: make CUE the production office's daily readiness desk. Catch venue, rig, rights and asset
problems before load-in, not on stage.

**Contract:** recommendations only. No live control, no automatic cue changes, no automatic release.

### 4.0 Scope and guardrails

- [ ] Watched object: tour, show, tour leg, venue, asset package and rights window **(M)**
- [ ] Separate **Show watch** from **Show design** in navigation, permissions and data model **(M)**
- [ ] Readiness plan per tour: dates, venues, rig, crew, content, rights and approvals **(M)**
- [ ] Freshness contract for venue, rig, cue and asset data; define what happens when data is stale **(S)**
- [ ] Coverage contract: which venues are watched, best-effort or blind spots **(S)**
- [ ] Define "no action" as a valid, recorded outcome **(S)**
- [ ] Onboarding: tour dates → venues → rig → content → approvals → test check **(M)**
- [ ] Subscription tiers: per show, per tour, per venue, per season **(S)**
- [ ] Pause / resume / kill switch per tour, visible to the production office **(S)**
- [ ] Start with one tour, one venue and one risk type; resist a portfolio-wide launch **(S)**

### 4.1 Show data and scheduling

- [ ] Tour calendar and venue date import **(M)**
- [ ] Venue profile: stage dimensions, rig, power, load-in, sightlines, last verified date **(M)**
- [ ] Setlist, cue and content version tracking **(M)**
- [ ] Rights windows: music, video, likeness, territory and expiry **(M)**
- [ ] Asset readiness: missing video, stale cue, outdated rig profile **(M)**
- [ ] Crew roles, approvals and named owners **(S)**
- [ ] Change detection when a date, venue, setlist, cue or asset changes **(M)**
- [ ] Data quality: stale venue profile, missing power data, missing rights, broken asset link **(S)**
- [ ] Provenance attached to every readiness check **(S)**

### 4.2 Readiness detection and alerting

- [ ] Venue compatibility: rig weight, power, stage dimensions and sightlines **(M)**
- [ ] Cue/asset drift: a cue references a missing asset or an outdated look **(M)**
- [ ] Budget drift: a look, rig or content change exceeds the approved budget **(M)**
- [ ] Rights expiry and territory mismatch **(M)**
- [ ] Schedule compression: load-in/rehearsal time versus cue complexity **(M)**
- [ ] Multi-show confirmation before raising a readiness risk **(S)**
- [ ] Adaptive thresholds by venue, tour and show type **(S)**
- [ ] Deduplicate and group risks by tour, venue and pattern **(S)**
- [ ] Human-readable readiness summary from evidence **(M)**
- [ ] Suggested check/fix per risk with effort, owner and cost impact **(M)**
- [ ] Estimate load-in time, rig cost or rights exposure at risk, labelled as an estimate **(M)**
- [ ] Near-miss capture: a cue miss, load-in delay or last-minute asset change **(S)**
- [ ] "Why now?" evidence pack: the factor, the source and what would falsify it **(S)**

### 4.3 Anticipation

- [ ] 14 / 7 / 3-day readiness checks before each show **(M)**
- [ ] New date or venue change triggers an automatic re-check **(S)**
- [ ] Rights expiry and content-delivery countdown **(S)**
- [ ] Crew approval and travel deadline tracking **(S)**
- [ ] Rehearsal schedule risk against cue complexity **(M)**
- [ ] "What changed since your last look" digest per tour **(S)**
- [ ] Backtest readiness checks over past tours before live alerts **(M)**
- [ ] Recommendations only; no automatic changes to the show **(S)**

### 4.4 Readiness lifecycle

- [ ] Risk states: new → acknowledged → assigned → investigating → resolved / dismissed **(M)**
- [ ] Dismissal reason taxonomy, visible in reporting **(S)**
- [ ] Assignment and routing by tour, venue and role **(M)**
- [ ] SLA timers for load-in, rehearsal and approval deadlines **(M)**
- [ ] Incident timeline combining risks, notes, assets and decisions **(M)**
- [ ] "Why this risk" panel: factors, source, confidence and history **(S)**
- [ ] Create task, approval or review from a readiness risk **(M)**
- [ ] Post-fix verification: re-check the venue/cue/asset and reopen if the risk returns **(M)**
- [ ] "Fixed but not verified" items surfaced on the show-week brief **(S)**
- [ ] Risk-fatigue budget per producer per week with a digest fallback **(S)**
- [ ] Handoff to design without re-uploading assets **(S)**
- [ ] Mobile readiness card and acknowledge action **(S)**

### 4.5 Notifications and integrations

- [ ] Email notifications with a signed deep link **(S)**
- [ ] Slack / Microsoft Teams with acknowledge and assign **(M)**
- [ ] SMS / pager escalation for critical show-week risks **(S)**
- [ ] Calendar sync for tour dates, load-in and rehearsal **(M)**
- [ ] Jira / Asana / Linear task creation and status sync **(M)**
- [ ] Budget and accounting export **(M)**
- [ ] DAM/asset-library link and freshness check **(M)**
- [ ] Generic webhook with HMAC signature and retry **(S)**
- [ ] Per-tenant notification isolation **(S)**

### 4.6 Trust, governance and safety

- [ ] Immutable audit of readiness checks, approvals, dismissals and exports **(M)**
- [ ] Model, rule and data-version pinned on every readiness risk **(S)**
- [ ] Explainability per risk class **(M)**
- [ ] False-alarm cost and trend by venue, tour and reason **(M)**
- [ ] Human-override analysis: where designers/producers disagree and why **(M)**
- [ ] Safety sign-off: rigging, power, laser, sightlines and structural load; never automatic **(M)**
- [ ] Privacy review for unreleased artist content **(M)**
- [ ] Data-rights annex for venue, artist and content data **(M)**
- [ ] Per-tenant encryption and storage isolation **(M)**
- [ ] No customer-facing readiness risk before the producer validates the first N per tour **(S)**
- [ ] Kill switch and stop-all-readiness runbook **(S)**
- [ ] Explicit non-goals enforced: no live control, no automatic cue release **(S)**

### 4.7 Readiness UI

- [ ] Tour readiness board: dates, venues, status, owner and next action **(M)**
- [ ] Venue readiness card: rig, power, sightlines, load-in and last verified **(M)**
- [ ] Cue, asset, rights and budget drift views **(M)**
- [ ] Daily / weekly digest for the production office **(S)**
- [ ] Notification preferences page **(S)**
- [ ] One-click acknowledge / assign / dismiss with reason **(S)**
- [ ] "Why this risk" drawer with source and evidence **(S)**
- [ ] Readiness dashboard: open risks, time-to-load-in, precision, cost avoided **(M)**
- [ ] Mobile readiness card and deep link **(S)**
- [ ] Show-week brief: top risks, approvals due and open items **(M)**

### 4.8 Commercial motion

- [ ] Per-tour, per-season and per-show pricing **(M)**
- [ ] SLA tiers: weekly readiness, show-week readiness, 24/7 tour watch **(S)**
- [ ] 90-day readiness pilot: one tour, one venue, shadow mode first **(M)**
- [ ] Pilot measurement: missed risks, time saved, rig cost avoided, approvals on time **(M)**
- [ ] Renewal criteria and conversion credit from the pilot fee **(S)**
- [ ] Partner motion with production companies and venues **(S)**
- [ ] One-page "tour readiness in 90 days" offer **(S)**
- [ ] Security/procurement package for artist content **(M)**
- [ ] Reference case with measured load-in readiness **(S)**

### 4.9 Platform and operations

- [ ] PostgreSQL state store for tours, venues, risks and approvals **(M)**
- [ ] Object storage for assets, exports and evidence packs **(M)**
- [ ] Job queue and scheduler for readiness checks and notifications **(M)**
- [ ] Multi-tenant configuration and quotas **(M)**
- [ ] Secrets vault for venue, DAM and calendar credentials **(S)**
- [ ] Observability: metrics, logs, traces and delivery dashboards **(M)**
- [ ] Backup/restore and disaster-recovery drill **(M)**
- [ ] Offline/air-gapped readiness queue **(M)**
- [ ] Retention per tour and per asset **(S)**
- [ ] Load test at 500 tours, 5,000 shows and 100 producers **(L)**
- [ ] Cost observability per tour and venue **(S)**

### 4.10 Pilot measurement and gates

- [ ] Baseline missed readiness items per tour before the pilot **(S)**
- [ ] Time saved per producer per show week **(S)**
- [ ] Readiness risk precision and recall against confirmed issues **(M)**
- [ ] Risks per producer per day and time-to-acknowledge **(S)**
- [ ] Action conversion: risks that led to a rig, rights or content fix **(S)**
- [ ] Cost per show and cost per actionable risk **(S)**
- [ ] **Gate 1** — four-week shadow mode; no customer-facing risks; measure precision and fatigue **(S)**
- [ ] **Gate 2** — 90-day tour pilot: precision ≥ 0.80, actionable rate ≥ 25%, no missed load-in **(M)**
- [ ] **Gate 3** — production launch after two green months and a signed data-rights annex **(S)**
- [ ] Kill criteria written before launch: precision < 0.60, alert fatigue above budget, unsafe routing **(S)**

---

## Phase 5 — Product experience (2026, planned)

Goal: the desk the production office lives in every day. The stage piece stays intact; this phase is
the product, not the demo.

### 5.0 Audit and principles

- [ ] Screen-by-screen audit at 1440, 1024 and 390 px **(S)**
- [ ] Inventory every legacy tell: tiny type, permanent panels, fixed desktop, missing states **(S)**
- [ ] Interview five users per role: designer, producer, venue crew, tour manager **(M)**
- [ ] Write the 2026 principles and anti-patterns into the design brief **(S)**
- [ ] Baseline task metrics: time to a look, time to a cue sheet, time to approve a version **(M)**

### 5.1 Brand and design system

- [ ] Logotype and app mark that work at 16 px, 32 px and stage scale **(M)**
- [ ] One accent colour; semantic colour reserved for safety, rights and budget meaning **(S)**
- [ ] Light, dark and high-contrast themes designed together **(M)**
- [ ] Colour-blind-safe palette for cues, rigs and risk **(S)**
- [ ] Design tokens: colour, type, space, radius, shadow, motion **(M)**
- [ ] Accessible primitives for dialogs, menus, tabs, tooltips and comboboxes **(M)**
- [ ] Core components: button, input, timeline, cue row, look card, venue card, chart frame **(L)**

### 5.2 Information architecture and command

- [ ] Project home as the default: shows, versions, approvals, budgets and readiness **(M)**
- [ ] Stage canvas as the primary workspace; panels are contextual **(M)**
- [ ] Global command palette (`Cmd/Ctrl+K`) with actions, search and recent **(M)**
- [ ] Role-based navigation that hides what the role cannot act on **(M)**
- [ ] Context rail: looks, cues, assets, rights, budget, readiness in one predictable place **(M)**
- [ ] Project home, cue sheet editor, budget/rig dashboard and version comparison **(M)**
- [ ] Mobile review for producers and tour managers **(S)**
- [ ] Asset and venue library **(M)**

### 5.3 Spatial canvas and timeline craft

- [ ] 3D stage with camera, set, risers, screen and performer blocking **(L)**
- [ ] Lighting and video layers that can be soloed, compared and scrubbed **(L)**
- [ ] Timeline with setlist, cues, energy curve and budget markers **(L)**
- [ ] Label hierarchy and decluttering that stay readable at 10 metres **(M)**
- [ ] Offline stage pack with a size budget **(M)**
- [ ] Presenter mode: large type, keyboard-only, no accidental edits **(M)**

### 5.4 AI-native interaction

- [ ] Natural-language commands: "make the drop warmer", "show rig conflicts on this leg" **(L)**
- [ ] Intent parser with suggestions, clarification and safe fallbacks **(M)**
- [ ] Agent sidecar that reads the current show context without being asked twice **(M)**
- [ ] Tool calls rendered as inspectable steps, not hidden magic **(M)**
- [ ] "Why this look?" and "why this risk?" with citations to the source assets **(M)**

### 5.5 Role flows and mobile

- [ ] Designer flow: concept → look → cue sheet in ≤ 3 interactions per decision **(M)**
- [ ] Producer flow: budget, approvals, readiness and change log in one view **(M)**
- [ ] Venue crew flow: cue sheet, rig check and sign-off on a phone **(M)**
- [ ] Tour manager flow: dates, load-in, travel and approvals **(S)**
- [ ] Mobile-first layouts at 390 and 768 px, not squeezed desktop **(M)**
- [ ] Installable PWA with offline shell and cached show pack **(S)**
- [ ] Bottom sheets, sticky actions and 44 px touch targets **(S)**

### 5.6 Accessibility and performance

- [ ] WCAG 2.2 AA audit with fixes **(M)**
- [ ] Full keyboard path for every action; visible focus ring **(M)**
- [ ] Reduced-motion mode for camera and cue transitions **(S)**
- [ ] Performance budgets in CI: bundle, LCP, INP, CLS and 3D frame time **(M)**
- [ ] Route-level code splitting and lazy 3D/video workers **(M)**
- [ ] Virtualized cue and asset lists at 10k items **(M)**
- [ ] No external font or CDN calls **(S)**

### 5.7 Content, localisation and trust

- [ ] Voice and tone guide for designers, producers and crew **(S)**
- [ ] Plain-language errors, empty states and disclaimers **(M)**
- [ ] Terminology glossary: cue, look, rig, venue, leg, load-in, changeover **(S)**
- [ ] Date, time, unit and currency formatting per locale **(S)**
- [ ] English and Chinese UI copy from one source **(M)**
- [ ] Provenance visible on every look, cue, asset and export **(S)**
- [ ] AI-generated look/video labelled and attributable **(S)**
- [ ] Human signature visible on cue sheets and approvals **(S)**
- [ ] Audit trail accessible from the UI, not just the API **(M)**

### 5.8 Engineering and assets

- [ ] React + Vite + strict TypeScript with no `any` in product code **(M)**
- [ ] Tokens compiled from one source into CSS and TS **(M)**
- [ ] Design-system package consumed by stage, desk and mobile **(M)**
- [ ] Unit tests for cue math, budget math and rights expiry **(M)**
- [ ] Final logo, icons, stage assets and licensed demo track **(M)**
- [ ] Seeded demo pack with a repeatable reset **(S)**

### 5.9 Research, rollout and gates

- [ ] Baseline SUS, task success and time-to-decision per role **(M)**
- [ ] Five-second test: "what does this product do?" **(S)**
- [ ] Five users per role complete the core task unaided **(M)**
- [ ] Design spike: shell, type, theme and command palette **(M)**
- [ ] Token and component foundation before screen rewrites **(M)**
- [ ] Rebuild the shell and navigation first **(M)**
- [ ] Migrate project home, stage canvas, cue sheet and readiness **(M)**
- [ ] No text below 11 px in product chrome **(S)**
- [ ] Light, dark and high-contrast themes pass contrast **(M)**
- [ ] WCAG 2.2 AA signed off; keyboard reachability 100% **(M)**
- [ ] Time to first decision drops ≥ 30% against the baseline **(M)**
- [ ] SUS ≥ 80 with five pilot users **(M)**
- [ ] Keep the 90-second stage piece intact; do not force the daily desk onto it **(S)**

---

## Phase 6 — Production wiring

Goal: the code and integrations that make CUE real for one tour, not a demo shell.

### 6.1 Agent runtime

- [ ] `DeepAgent` adapter with a show-scoped tool set **(M)**
- [ ] Tools: setlist, stage, looks, video, cue sheet, budget, venue profile, rights **(M)**
- [ ] System prompt: cite sources, admit missing evidence, never change a cue or approve safety **(S)**
- [ ] `/api/agent/status` reports configured/available/backend/model **(S)**

### 6.2 Render and inference

- [ ] GPU renderer path with explicit device and quality settings **(L)**
- [ ] Optional ONNX/NPU path for local look and video inference **(M)**
- [ ] Refuse a missing model or GPU with an explicit error, never a silent fallback **(S)**
- [ ] Local/offline render and inference for unreleased content **(M)**
- [ ] Frame-time and export-time budgets on the pilot laptop **(M)**

### 6.3 Live integrations

- [ ] Depence² / Capture / WYSIWYG previz exchange **(L)**
- [ ] grandMA3 cue import/export **(L)**
- [ ] disguise / Notch / Resolume video exchange **(L)**
- [ ] DAM/asset-library connector **(M)**
- [ ] Calendar connector for tour dates and load-in **(M)**
- [ ] Budget/accounting export **(M)**

### 6.4 Customer data and storage

- [ ] Show store with versions, approvals and immutable audit **(M)**
- [ ] Per-tenant isolation and encryption keys **(M)**
- [ ] Artist content stays local by default; explicit permission for any upload **(S)**
- [ ] Provenance, model version and source IDs on every asset and cue **(S)**
- [ ] Retention and deletion policy per tour **(S)**

### 6.5 Security and operations

- [ ] OIDC/SSO and server-side role enforcement **(L)**
- [ ] Signed exports and share links with expiry **(S)**
- [ ] Backup/restore and disaster-recovery drill **(M)**
- [ ] Observability: render failures, export failures and agent errors **(M)**
- [ ] Offline queue for show week **(S)**

### 6.6 End-to-end production gate

- [ ] One real tour, one venue and 90 days running **(L)**
- [ ] Track → stage → looks → cue sheet → crew → show, with no synthetic records **(L)**
- [ ] Designer, producer and venue crew accept the cue sheet and readiness output **(M)**
- [ ] Safety sign-off is recorded and never automated **(S)**
- [ ] Agent citation coverage ≥ 95% on the pilot assets **(M)**

---

## Not planned (with reasons)

- **Live show control / DMX / console** — safety and liability; CUE designs, the crew runs.
- **Music generation** — the artist's track is the source of truth.
- **Full CAD replacement** — Vectorworks and others already own drafting.
- **Full renderer replacement** — Depence², WYSIWYG and Capture are strong; integrate, don't clone.
- **Autonomous show design** — the designer is the author.
- **Hardware** — no fixture, console or rig is required to use CUE.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). One song, one drop, one trust beat.
2. **Rehearse and red-team** (1 week). Acceptance tests, venue test, fallback.
3. **Stage gate** — if the five-stranger test fails, do not book the next conference.
4. **0B — the functional demo** (3–4 weeks) for the booth and Q&A.
5. **First pilot** — one production company, three shows, 90 days.
6. **One previz integration** (Depence², Capture or WYSIWYG) before anything else in Phase 1.
7. **One console export** (grandMA3 or Resolume) after the first pilot show.
8. **Phase 6 — production wiring** before the first paid production: agent, render, integrations, data and the end-to-end gate.
9. **Phase 4 — tour readiness** after design value is proven; this is the daily retention layer for the production office.
10. **Phase 5 — product experience** once the desk is stable; keep the 90-second stage piece intact.
11. **Phase 2 — production** only after the pilot proves fewer iterations and lower rig cost.
12. **Phase 3 — scale** only after multiple production companies are live.

---

## Open decisions

- Which production company or venue is the first pilot?
- Which track is licensed for the public demo?
- Which previz tool is integrated first: Depence², Capture or WYSIWYG?
- Which console export matters first: grandMA3, disguise or Resolume?
- Does CUE render in its own engine or orchestrate existing previz?
- Is the buyer the production company, the venue or the artist's management?
- Do we offer local/NPU inference for unreleased artist content?
- How do we handle ownership and disclosure of AI-generated looks and video?
- Is the daily user the production office, or do we also sell to freelancers?
- Which tour-readiness risks come first: rig/power, rights, asset drift or budget?
- Which integrations come first after previz and console: DAM, calendar, budget or ticketing?
- Which agent runtime and render/inference path: local GPU, ONNX, or optional NPU?
- Who signs safety, and what evidence must be attached before a cue is released?
- Does the production office or the designer own the readiness queue?
