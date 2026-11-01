# Guardian — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means sensor data and decision records never leave the building network.
"LAIX" means the LAIX decision layer orchestrates the response.

**Status.** Stage spec written. Product not built.

**One line.** When a sensor fires, Guardian decides what to do, shows its evidence, and keeps a
person in charge.

**Buyer.** Facilities manager (primary user and budget), site safety officer (compliance), building
owner (risk).

**Best first industries.** Data centres · hospitals · corporate campuses · industrial sites.

**The sentence the audience repeats:** *"The building knows what's happening. It asks before it
acts."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc and acceptance tests.

---

## Phase 0A — The 90-second compound alarm

Goal: a stage piece that makes facilities managers recognise the problem and non-experts feel the
stakes, with or without narration. Time: 2 weeks to build, 1 week to rehearse. No real sensor
hardware, no live LAIX calls, no network.

**Set.** A large screen showing a floor plan of an office building. Sensors are dots on the map —
green when quiet, amber when uncertain, red when firing. The presenter has a clicker and a visible
confidence slider on screen.

**The verb.** Drag the confidence slider; watch the decision change live.

**The cold open.** The floor plan is quiet. The presenter says: *"Basement. 2am. Nobody's watching."*
A water sensor fires in the basement. Amber dot. LAIX card appears: `observe — single sensor,
confidence 0.4, no cross-confirmation`.

**The turn.** The presenter drags the confidence slider to 0.9 (second sensor confirms). Decision
flips to `act — isolate water supply, zone B`. The room sees the flip in real time. Then a second
event: electrical panel in the same zone fires. LAIX immediately re-evaluates. `act` is crossed out
with a red gate line. New decision: `escalate — water + active circuit, do not enter, call building
engineer`. The compound risk scenario is visible as two overlapping alert bubbles on the floor plan.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | Presenter describes the 2am scenario | Quiet floor plan |
| 0:10–0:25 | First touch | Water sensor fires | Amber dot, LAIX card: `observe` |
| 0:25–0:38 | Confidence drag | Presenter drags slider from 0.4 to 0.9 | Decision flips to `act`, confidence bar fills |
| 0:38–0:52 | Trust beat | AI recommends `act — cut power`; operator rejects — people in server room | Decision flips to `guide` |
| 0:52–1:08 | Compound reveal | Electrical panel fires; safety gate fires; `act` crossed out | Gate panel, compound risk overlay |
| 1:08–1:20 | Escalate | Decision: `escalate — call building engineer`; engineer paged | Pager card, case stamped |
| 1:20–1:30 | The line | Closing line; QR to demo; reset | Clean floor plan |

### The trust beat, in detail

- After the confidence drag confirms the water leak, LAIX recommends `act — cut power` in the
  basement.
- The operator rejects it for a visible reason: *"there are engineers in the server room right
  now."*
- LAIX re-ranks in the same scene: `guide — show floor warden, wait for room clearance`.
- The presenter says one sentence: *"It was confident. It was wrong. This is why the operator
  stays in charge."*
- Occupancy context updates. The new option is visible: disruption score was 0.1, now 0.8.

### Audience agency

The room chooses which second event fires:

- **A — smoke detector on floor 3, HVAC duct.** LAIX returns `observe` — HVAC false positive
  rate is high.
- **B — power anomaly on floor 4.** LAIX returns `ask — check maintenance log for scheduled
  work`.

Either path works. The presenter commits to the room's choice. Both show different verbs and
different reasons.

### Props and stagecraft

- Floor plan with animated sensor dots (CSS transitions, no JS framework required).
- A confidence slider the audience can see move.
- An alert tone on sensor fire; a gate-fire sound (a soft buzzer) on compound risk; silence under
  the trust beat.
- The safety gate panel animates: `act` appears, compound risk detected, red line through `act`,
  new decision card slides in.
- A printed floor plan handout for the front row.
- Reset: `R`, under five seconds, back to the quiet floor plan.

### Phase 0A checklist

- [ ] Animated floor plan with 10 sensor zones **(M)**
- [ ] Confidence slider wired to LAIX decision output **(M)**
- [ ] Decision flip animation: `observe` → `act` on confidence change **(M)**
- [ ] Compound risk overlay: two event bubbles merge, gate fires **(M)**
- [ ] Safety gate panel: option crossed out, new decision slides in **(M)**
- [ ] Trust beat: first recommendation shown, rejected, re-ranked **(M)**
- [ ] Escalate card with pager animation **(S)**
- [ ] Audience choice: two second-event types, either path works **(S)**
- [ ] 90-second script, word-for-word for the first 20 seconds **(S)**
- [ ] Stage mode: deterministic run, reset under five seconds **(S)**
- [ ] 90-second fallback recording and a backup laptop **(S)**
- [ ] Contrast and type test at 10 metres **(S)**
- [ ] Three full rehearsals, one with a hostile audience, one with no network **(S)**

**Do not build for 0A:** login, settings, real sensor connectors, BMS integration, multi-building,
model training, report export.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" after the stage piece. Same story, synthetic
sensor events, deterministic and offline.

Time: 3–4 weeks after 0A.

- [ ] Synthetic sensor event pack: 30 events across 5 sensor types, timestamps, severities **(S)**
- [ ] Synthetic floor plan with 20 zones, asset labels, occupancy flags **(S)**
- [ ] LAIX integration: real `DecisionRequest` objects, real safety-constrained policy **(M)**
- [ ] Compound risk model: two simultaneous events produce joint risk score **(M)**
- [ ] Full scoring breakdown visible on click: options, gates, winner, reason **(M)**
- [ ] Confidence slider wired to live LAIX re-evaluation **(M)**
- [ ] Trust beat replay: viewer can step through the re-ranking **(M)**
- [ ] Escalate card with simulated pager notification **(S)**
- [ ] Audit log: scrollable record of all decisions in the session **(M)**
- [ ] Booth mode: reset, scenario picker, 3-minute run **(S)**
- [ ] Runs fully offline on one laptop **(S)**

### Demo architecture

- Fixed seed. Every run is identical.
- All LAIX calls are real library calls — this is the honest demo of the library.
- Precomputed sensor stream; no external API calls on stage.
- The confidence slider calls LAIX live on each drag event.
- A visible "powered by LAIX" provenance panel for Q&A.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the product in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] The compound reveal lands by 30 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat.
- [ ] Reset under five seconds.
- [ ] Two volunteers complete the confidence-drag interaction unassisted.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to compound reveal: ≤ 30 s.
- Full run: ≤ 90 s.
- Volunteer success: ≥ 80%.
- Qualified conversations at the event: ≥ 10.
- LAIX library adoption inquiries: ≥ 5.

### Post-stage motion

- QR code to the LAIX repository or documentation.
- One-page "How LAIX handles compound risk" explainer.
- A 10-minute booth walkthrough of the safety gate model.
- Follow-up within 48 hours with the recording and the explainer.

---

## Phase 1 — First integration

Goal: one real building, one sensor type (water), one compound scenario, 30 days.
Run alongside the existing BMS process. Operator confirms every decision before it fires.

**Gate:** do not start the integration until the stage piece has passed all acceptance tests.

### 1.1 Sensor connectors

- [ ] BACnet/IP reader for water and electrical sensors **(M)**
- [ ] Modbus RTU fallback for older panels **(M)**
- [ ] Sensor event normaliser: map severity, zone, and type to LAIX Signal contract **(M)**
- [ ] Occupancy data reader (calendar or access control) **(S)**
- [ ] Maintenance log reader: flag zones with open work orders **(S)**

### 1.2 LAIX decision layer

- [ ] Sensor event → `DecisionRequest` adapter **(M)**
- [ ] Compound risk model: joint evaluation for co-firing sensor pairs **(L)**
- [ ] Action library: 15 standard responses with risk, disruption, reversibility scores **(M)**
- [ ] Safety gate configuration per zone class (server room, kitchen, open office) **(M)**
- [ ] LAIX policy pack: safety-constrained + escalation **(S)**
- [ ] Plain-English reason rendered for each decision **(M)**

### 1.3 Operator workflow

- [ ] Floor plan view with live sensor state and LAIX decision cards **(M)**
- [ ] Confidence indicator per zone **(S)**
- [ ] Approve / override / dismiss interaction **(S)**
- [ ] Correction captured: rejected recommendation + operator's choice **(S)**
- [ ] Building engineer pager integration **(M)**
- [ ] Append-only decision log with timestamp, sensor state, model version **(S)**

### 1.4 Pilot measurement

- [ ] Baseline: log current response time per event type before go-live **(S)**
- [ ] Pilot dashboard: events triaged, correct verb rate, time to resolution **(M)**
- [ ] Weekly accuracy report for operator feedback **(S)**
- [ ] Correction feedback loop **(M)**

### 1.5 Deployment

- [ ] On-site server (Linux, Docker), no outbound network **(M)**
- [ ] Offline-capable: decisions still run if internet is down **(S)**
- [ ] Role-based access: operator view vs. manager view **(M)**

---

## Phase 2 — Production

Goal: multiple sensor types, multiple buildings, charge full price.

- [ ] Smoke and HVAC sensor support **(M)**
- [ ] Power and access control sensor support **(M)**
- [ ] Multi-building support with separate zone channels **(M)**
- [ ] Manager dashboard: event volume, response times, safety gate activations **(M)**
- [ ] Compliance report: audit trail export for safety inspections **(M)**
- [ ] Per-building annual licence billing **(M)**

---

## Phase 3 — Scale

Goal: multiple customers, sensor connector library, LAIX adoption programme.

- [ ] Multi-tenant architecture with data isolation **(L)**
- [ ] Connector library for top 5 BMS protocols **(L)**
- [ ] Outcome learning: cross-building anonymised accuracy benchmarks, opt-in **(L)**
- [ ] LAIX SDK integration guide for BMS vendors **(M)**
- [ ] ISO 45001 and EN 54 compliance pack **(M)**

---

## Not planned (with reasons)

- **Automatic building actions without confirmation** — liability and safety risk; operator always
  decides.
- **Replacing the BMS** — Guardian sits above it, not beside it.
- **Generic IoT platform** — focus stays on the LAIX compound-risk demo.
- **Cloud sensor data** — data stays on-site.
- **Dashboard-only demo** — dashboards are for pilots, not stages.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). Build the floor plan and confidence slider first. No real
   sensor hardware needed.
2. **Rehearse and red-team** (1 week). Acceptance tests, fallback, venue test.
3. **Stage gate** — if the five-stranger test fails, do not book the next event.
4. **0B — the functional demo** (3–4 weeks) for the booth and LAIX Q&A.
5. **First integration** — one data centre with BACnet water sensors.
6. **1.1 connectors** before anything else in Phase 1.
7. **1.2 compound risk model** — this is the core LAIX demonstration.
8. **1.3 operator workflow** — the floor plan and approve flow are what the operator sees.
9. **1.4 measurement** — baseline on day one.
10. **Phase 2** only after the integration succeeds and a second building is signed.

---

## Open decisions

- Which building type is the safest first target: data centre, hospital, or office?
- What sensor protocol is most common among first customers?
- How do we simulate realistic compound sensor events for the demo?
- Should the stage piece use a real floor plan or a generic one?
- Which compound scenario has the highest trust-beat drama: water+electrical, smoke+HVAC, or
  power+access?
