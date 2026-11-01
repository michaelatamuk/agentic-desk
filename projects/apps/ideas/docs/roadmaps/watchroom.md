# Watchroom — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means the compute and decision records never leave the engineering network.
"LAIX" means the LAIX decision layer orchestrates the triage.

**Status.** Stage spec written. Product not built.

**One line.** When production alerts flood in, Watchroom triages each one, explains the decision,
and keeps the engineer in control.

**Buyer.** SRE / on-call engineer (primary user), engineering manager (budget), CTO (sponsor).

**Best first industries.** SaaS / cloud infrastructure · fintech · e-commerce · media streaming.

**The sentence the audience repeats:** *"Every alert, a decision. Every decision, a reason."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc and acceptance tests.

---

## Phase 0A — The 90-second ops crisis

Goal: a stage piece that makes engineers nod and non-engineers lean forward, with or without
narration. Time: 2 weeks to build, 1 week to rehearse. No real monitoring tool, no live model
calls, no network.

**Set.** A large screen showing a live ops board: left column is an alert stream, right column is
the LAIX decision for each alert. One alert is already in flight — a memory spike on a database
node. The presenter has a clicker and one keyboard shortcut.

**The verb.** Inject an alert; watch LAIX score it; see the safety gate fire.

**The cold open.** The ops board is calm. One alert streams in: `DB-PROD-03 — memory 94% — CRITICAL`.
The presenter says: *"3am. One engineer on call. This is what they see."*

**The turn.** LAIX scores `auto-restart-db` as the highest-scoring option. The safety gate fires
in the next beat: risk score 0.87 > limit 0.20. Option eliminated. LAIX falls back to
`escalate → page on-call manager`. The engineer on stage is asked: approve? They approve. Five
seconds later a verify pulse: memory stable, incident marked closed.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | Presenter describes the 3am scenario | Alert board, one live alert |
| 0:10–0:25 | First touch | Presenter injects the DB memory alert | Alert appears, LAIX scoring animation |
| 0:25–0:40 | Safety gate | `auto-restart-db` scored high; gate fires; option crossed out | Gate panel, risk score 0.87 |
| 0:40–0:52 | Trust beat | LAIX recommends `scale-up-replicas`; engineer rejects — client bug not load | Decision flips to `observe` |
| 0:52–1:08 | Approval | Engineer approves `escalate → page on-call`; pager fires | Pager card, decision stamped |
| 1:08–1:20 | Verify | Verify pulse: memory stable, incident closed | Green verify card |
| 1:20–1:30 | The line | Closing line; QR to playable demo; reset | Clean board |

### The trust beat, in detail

- The first recommendation after the gate fires is `scale-up-replicas`. It is plausible: high
  memory often means load.
- The engineer rejects it for a visible reason: *"the 5xx rate is flat — this is a client-side
  memory leak, not our load."*
- LAIX re-ranks in the same scene: `observe — watch for 2 minutes, 5xx still flat`.
- The presenter says one sentence: *"It was confident. It was wrong. This is why the engineer
  stays in charge."*
- The system saves the correction. That is the learning story.

### Audience agency

The room chooses which alert to inject next:

- **A — 5xx spike on the API gateway.**
- **B — disk full on the logging node.**

Either works. The presenter commits to the room's choice. Both show different verbs: A gets
`act → rotate log partition`, B gets `ask → page storage team`.

### Props and stagecraft

- A dark ops-board design (dark background, amber and red alert colours, monospace font).
- A real-sounding alert tone on inject; a soft confirmation tone on approval; silence under the
  trust beat.
- The safety gate panel animates: option appears, score appears, gate fires, option crossed out
  with red line.
- Reset: `R`, under five seconds, back to the cold open.
- A physical clicker the presenter uses visibly for the inject action.

### Phase 0A checklist

- [ ] Alert stream with five pre-loaded alerts, one injected on stage **(S)**
- [ ] LAIX scoring animation: options listed, scores appear, gate fires **(M)**
- [ ] Safety gate panel: risk score vs. limit, visual elimination **(M)**
- [ ] Trust beat: first recommendation shown, rejected, re-ranked **(M)**
- [ ] Approve interaction: one button, decision stamped with timestamp **(S)**
- [ ] Verify pulse: 5-second timer, green card on resolution **(S)**
- [ ] Audience choice: two alert types, either path works **(S)**
- [ ] 90-second script, word-for-word for the first 20 seconds **(S)**
- [ ] Stage mode: deterministic run, reset under five seconds **(S)**
- [ ] 90-second fallback recording and a backup laptop **(S)**
- [ ] Contrast and type test at 10 metres **(S)**
- [ ] Three full rehearsals, one with a hostile audience, one with no network **(S)**

**Do not build for 0A:** login, settings, real monitoring connectors, multi-user, model training,
runbook library, export formats, dashboard.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" after the stage piece. Same story, synthetic
alert data, deterministic and offline.

Time: 4 weeks after 0A.

- [ ] Synthetic alert pack: 20 alerts across 5 service types, timestamps, severities **(S)**
- [ ] Synthetic on-call schedule and team roster **(S)**
- [ ] LAIX integration: real `DecisionRequest` objects, real policy pack **(M)**
- [ ] Full scoring breakdown visible on click: options, scores, gate, winner **(M)**
- [ ] Safety gate demo: side-by-side view of two alerts, one gated, one not **(M)**
- [ ] Trust beat replay: viewer can step through the re-ranking **(M)**
- [ ] Verify loop: simulated 5-second resolution pulse **(S)**
- [ ] Audit log: scrollable record of all decisions in the session **(M)**
- [ ] LAIX policy trace the audience can follow **(M)**
- [ ] Booth mode: reset, scenario picker, 3-minute run **(S)**
- [ ] Runs fully offline on one laptop **(S)**

### Demo architecture

- Fixed seed. Every run is identical.
- All LAIX calls are real library calls, not mocks — this is the honest demo of the library.
- Precomputed alert stream; no external API calls on stage.
- Stage mode and booth mode are separate routes.
- A visible "powered by LAIX" provenance panel for Q&A.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the product in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] Safety gate fires by 30 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat.
- [ ] Reset under five seconds.
- [ ] Two volunteers complete the inject-and-approve interaction unassisted.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to safety gate: ≤ 30 s.
- Full run: ≤ 90 s.
- Volunteer success: ≥ 80%.
- Qualified conversations at the event: ≥ 10.
- LAIX library adoption inquiries: ≥ 5.

### Post-stage motion

- QR code to the LAIX repository or documentation, not a signup form.
- One-page "How LAIX works in 5 minutes" explainer.
- A 10-minute booth walkthrough of the decision model.
- Follow-up within 48 hours with the recording and the explainer.

---

## Phase 1 — First integration

Goal: one real engineering team, one monitoring tool, five alert types, 30 days.
Prove LAIX makes triage faster and more consistent. Agents confirm every decision before it fires.

**Gate:** do not start the integration until the stage piece has passed all acceptance tests.

### 1.1 Monitoring connectors

- [ ] Datadog Events API reader **(M)**
- [ ] PagerDuty webhook receiver **(M)**
- [ ] Prometheus Alertmanager webhook **(M)**
- [ ] Alert normaliser: map severity, service, and source to LAIX Signal contract **(M)**
- [ ] On-call schedule reader (PagerDuty or Opsgenie) **(S)**

### 1.2 LAIX decision layer

- [ ] Alert → `DecisionRequest` adapter **(M)**
- [ ] Action library: 10 standard remediation options with risk/cost scores **(M)**
- [ ] Safety gate configuration per service class **(M)**
- [ ] LAIX policy pack selection: safety-constrained + escalation **(S)**
- [ ] Scoring explanation rendered in plain English **(M)**

### 1.3 Engineer workflow

- [ ] Decision board: live alert stream with LAIX verdicts **(M)**
- [ ] Click-through to full scoring breakdown **(S)**
- [ ] Approve / override / dismiss interaction **(S)**
- [ ] Correction captured: rejected recommendation + engineer's choice **(S)**
- [ ] On-call pager integration (PagerDuty) **(M)**
- [ ] Append-only decision log with timestamp, model version, data sources **(S)**

### 1.4 Pilot measurement

- [ ] Baseline: log current MTTR per alert type before go-live **(S)**
- [ ] Pilot dashboard: alerts triaged, correct verb rate, time saved **(M)**
- [ ] Weekly accuracy report for engineer feedback **(S)**
- [ ] Correction feedback loop: feeds LAIX outcome learning **(M)**

### 1.5 Deployment

- [ ] Runs on one laptop or a small on-site server **(S)**
- [ ] No outbound network required after setup **(S)**
- [ ] Role-based access: engineer view vs. manager view **(M)**

---

## Phase 2 — Production

Goal: support multiple teams, multiple monitoring tools, charge full price.

- [ ] Multi-team support with separate alert channels **(M)**
- [ ] OpsGenie, CloudWatch, Grafana connectors **(M)**
- [ ] Runbook library: link LAIX actions to documented procedures **(M)**
- [ ] Manager dashboard: alert volume, triage accuracy, time to resolution **(M)**
- [ ] Trend alerts: recurrent patterns flagged for review **(M)**
- [ ] Per-team subscription billing **(M)**
- [ ] SSO / OIDC **(M)**

---

## Phase 3 — Scale

Goal: multiple organisations, connector library, LAIX adoption programme.

- [ ] Multi-tenant architecture with data isolation **(L)**
- [ ] Connector library for top 8 monitoring tools **(L)**
- [ ] Outcome learning: cross-team anonymised accuracy benchmarks, opt-in **(L)**
- [ ] LAIX SDK integration guide and sample code **(M)**
- [ ] Public benchmark: LAIX triage accuracy vs. manual baseline **(M)**

---

## Not planned (with reasons)

- **Automatic remediation without confirmation** — liability; the engineer always decides.
- **Replacing PagerDuty or Datadog** — Watchroom sits above them, not beside them.
- **Generic AIOps platform** — focus stays on the LAIX decision layer demo.
- **Cloud inference for production alerts** — alert data stays inside the engineering network.
- **Dashboard-only demo** — dashboards are for pilots, not stages.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). Build the ops board first. No real connector needed.
2. **Rehearse and red-team** (1 week). Acceptance tests, fallback, venue test.
3. **Stage gate** — if the five-stranger test fails, do not book the next event.
4. **0B — the functional demo** (4 weeks) for the booth and LAIX Q&A.
5. **First integration** — one SRE team with Datadog and PagerDuty.
6. **1.1 connectors** before anything else in Phase 1.
7. **1.2 LAIX decision layer** — the adapter and action library are the core product.
8. **1.3 engineer workflow** — the board and approve flow are what the engineer sees.
9. **1.4 measurement** — baseline on day one.
10. **Phase 2** only after the integration succeeds and a second team is signed.

---

## Open decisions

- Which monitoring tool is the first integration target?
- What is the right confidence threshold for auto-act vs. confirm in the first pilot?
- How do we source a realistic synthetic alert stream for the demo?
- Should the stage piece show a dark ops board or a clean dashboard?
- Which incident scenario has the highest trust-beat drama: DB memory, 5xx spike, or disk full?
