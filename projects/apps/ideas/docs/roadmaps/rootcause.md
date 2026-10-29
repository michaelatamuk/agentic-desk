# RootCause — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means the compute and data never leave the factory network.
"Agent" means JiuwenSwarm orchestrates the data gathering and reasoning step.

**Status.** Stage spec + business plan. Playable proof built: [play/rootcause.html](../../play/rootcause.html).
Product not built.

**One line.** When a factory finds a bad part, RootCause finds the likely cause and writes the
quality report with evidence — in hours, not days.

**Buyer.** Quality manager (primary pain), plant manager (budget), manufacturing engineer (user).

**Best first industries.** Plastic injection moulding · battery cell production · electronics
assembly · metal stamping.

**The sentence the audience repeats:** *"It wasn't fatigue. It started in the casting."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc and acceptance tests.

---

## What changed in this revision

- **Stage first.** The old Phase 0 built a small product and hoped it would demo well. Phase 0 is
  now split into **0A (stage piece)** and **0B (functional demo)**.
- **Phase GUI retired.** It is replaced by the stage piece, plus a smaller product-UI section after
  the demo. The former GUI screens (mobile review, report export, manager dashboard) remain as
  product work, not stage work.
- **The trust beat is mandatory.** The AI is wrong once; the engineer rejects it; the system re-ranks.
- **Audience agency added.** The room chooses between surface and x-ray evidence.
- **Stagecraft, data rights, metrics and post-stage motion added.** These were missing entirely.
- **Licensing corrected.** MVTec AD is non-commercial; the public demo needs a commercial-safe pack.

**The old stage idea:**

| Old demo | 2026 stage piece |
|---|---|
| Defect image, bounding box, three cause cards, report, dashboard | Physical bracket, a lens, an x-ray reveal, a wrong first answer, an evidence web, a stamped verdict |

---

## Phase 0A — The 90-second teardown

Goal: a stage piece that makes a standing audience lean forward, with or without narration.
Time: 2 weeks to build, 1 week to rehearse. No customer, no live model training, no network.

**Set.** A real failed bracket on a black bench, a macro camera or a phone on a stand, and one large
screen. The physical part is the anchor; the screen is the lens.

**The verb.** Drag a lens across the part, then push from optical to x-ray.

**The cold open.** The presenter holds the part. *"Line 6. 1,842 hours. The report said metal fatigue."*
The screen shows the case header: `CASE 0417 · TURBINE BRACKET · UNIT 6`.

**The turn.** The engineer measures the crack origin, goes under the surface, finds the porosity
cluster, and the causal chain assembles: **gas porosity → quench crack → service growth → failure**.
The report is not the climax; the cause is.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | Presenter holds the part; the fatigue claim | Case header, part photo |
| 0:10–0:25 | First touch | Place the part; drag the lens | Loupe over the root fillet |
| 0:25–0:38 | Surface evidence | Find the crack origin and the tool mark | Finding markers, evidence chips |
| 0:38–0:52 | Trust beat | AI proposes "tool mark / operator error"; engineer rejects it | Ranking flips; confidence bars re-weight |
| 0:52–1:08 | The reveal | Push depth to x-ray; porosity cluster appears; chain assembles | X-ray, causal chain |
| 1:08–1:20 | Verdict | Cause approved; case sheet prints / stamp | White case sheet, `HYDROGEN POROSITY` |
| 1:20–1:30 | The line | "It wasn't fatigue. It started in the casting." | QR to the playable demo; reset |

### The trust beat, in detail

- The first hypothesis is **tool mark / operator error**. It is plausible: there is a machining ridge
  near the crack, and it is the kind of answer a quality manager hears every week.
- The engineer rejects it for a visible reason: **the crack starts 0.4 mm below the surface; tool
  marks are surface-only.**
- The system re-ranks in the same scene: **gas porosity, largest void 0.8 mm, aligned with the crack
  path.**
- The presenter says one sentence: *"It was confident. It was wrong. This is why the engineer stays
  in charge."*
- The system saves the correction and shows the case updated. That is the learning story without a
  fake accuracy number.

### Audience agency

The room chooses which evidence to open first:

- **A — surface:** tool mark and crack origin.
- **B — under the surface:** porosity cluster.

Either order works, but B is the reveal. The presenter commits to the room's choice, then says:
*"The tool mark is real. It is also a decoy."*

### Props and stagecraft

- Real failed bracket, painted or taped to read as line hardware.
- A physical loupe on a lanyard, used once, so the lens is not only a screen metaphor.
- A printed case sheet and an `APPROVED` stamp; the stamp is the sound cue.
- One low industrial hum; one impact sound at the reveal; silence under the trust beat.
- A red key light for the failure claim, amber for the reveal, white for the verdict.
- Reset: `R`, under five seconds, back to the cold open.

### Phase 0A checklist

- [ ] Source or fabricate one failed bracket with a visible crack and a believable root fillet **(S)**
- [ ] Macro camera / phone mount and a stable stand for the part **(S)**
- [ ] Lens interaction with optical-to-x-ray depth, tuned for a 10-metre viewing distance **(M)**
- [ ] Three findings with evidence copy: crack origin, gas porosity, tool mark **(S)**
- [ ] Cause ranking that visibly re-weights after the human rejection **(M)**
- [ ] Causal chain animation: porosity → quench crack → service growth → failure **(M)**
- [ ] Verdict card and printable/stampable case sheet **(S)**
- [ ] Audience choice: surface evidence vs under-surface evidence **(S)**
- [ ] 90-second script, word-for-word for the first 20 seconds **(S)**
- [ ] Stage mode: deterministic run, reset under five seconds **(S)**
- [ ] 90-second fallback recording and a backup laptop **(S)**
- [ ] Contrast and type test at the venue, 10 metres, 16:9 and 4:3 **(S)**
- [ ] Commercial-safe defect images and a provenance sheet **(S)**
- [ ] Three full rehearsals, one with a hostile audience, one with no network **(S)**

**Do not build for 0A:** login, settings, navigation, multi-user, model training, export formats,
the quality-manager dashboard.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" after the stage piece. Same story, real data
where possible, but still deterministic and offline.

Time: 4 weeks after 0A. It can reuse the [playable proof](../../play/rootcause.html) as its shell.

- [ ] Commercial-safe defect image pack, or synthetic defects generated in-house **(M)**
- [ ] Synthetic machine parameter CSV: temperature, pressure, cooling time, cycle count **(S)**
- [ ] Synthetic maintenance log and 6-month defect case history **(S)**
- [ ] Defect detection inference on pre-loaded images, bounding box on screen **(M)**
- [ ] Time-window query: pull machine data for the shift when the defect occurred **(S)**
- [ ] Batch record linker and similar-case search **(M)**
- [ ] Cause ranking engine with evidence per cause **(M)**
- [ ] Agent orchestration trace the audience can follow **(M)**
- [ ] Three-cause output with confidence bars and supporting data chips **(M)**
- [ ] Report template with inline edit and engineer approval **(M)**
- [ ] Case save: timestamp, approved cause, report version, engineer name **(S)**
- [ ] Booth mode: reset, scenario picker, 3-minute run **(S)**
- [ ] Runs fully offline on one laptop **(S)**

### Demo architecture

- Fixed seed. Every run is identical.
- Precomputed inference and case history; no model calls on stage.
- All assets local; no fonts, tiles or APIs from the network.
- Stage mode and booth mode are separate routes; booth mode can show more detail.
- A visible provenance panel for Q&A: data source, model, date, simulated vs real.

### Data rights

- **MVTec AD is CC BY-NC-SA 4.0 (non-commercial).** Use it for internal R&D only. For a public or
  commercial demo, use a licensed or synthetic defect pack.
- Customer images require a written demo-use permission, not just a pilot NDA.
- Keep the provenance sheet with the demo data pack.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the product in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] The x-ray reveal lands by 30 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat.
- [ ] Reset under five seconds.
- [ ] Two volunteers complete the lens-and-depth interaction unassisted.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to the reveal: ≤ 30 s.
- Full run: ≤ 90 s.
- Volunteer success: ≥ 80%.
- Qualified conversations at the event: ≥ 20.
- Pilot intros booked: ≥ 5.

### Post-stage motion

- QR code to the playable demo, not a signup form.
- One-page "RootCause pilot in 90 days" offer.
- A 10-minute booth version of the same story.
- Follow-up within 48 hours with the recording and the one-pager.
- Capture 20 named quality leaders, not badge scans.

---

## Phase 1 — First pilot

Goal: one real factory, one production line, one defect type, 90 days.
Prove value in production conditions. Run alongside the existing process, not replacing it.

**Gate:** do not start the pilot until the stage piece has passed all acceptance tests.

### 1.1 Data connectors

- [ ] OPC-UA connector: read 10–20 machine parameters from SCADA in real time **(M)**
- [ ] Modbus connector: fallback for older PLCs **(M)**
- [ ] Existing inspection camera output reader (Keyence, Cognex, or generic TCP/IP feed) **(M)**
- [ ] Batch record CSV import from MES or ERP **(S)**
- [ ] Historical defect data loader: 6 months from the customer quality system **(M)**
- [ ] Data normalisation and cleaning pipeline **(M)**

### 1.2 Detection and investigation

- [ ] Defect detection model fine-tuning on customer-specific defect images **(L)**
- [ ] Time-window aggregator: link defect timestamp to machine state **(M)**
- [ ] Batch record linker **(S)**
- [ ] Case similarity search **(M)**
- [ ] Agent orchestration for multi-source data pull and hypotheses **(M)**
- [ ] Cause ranking weighted by frequency, deviation magnitude and batch match **(M)**
- [ ] Evidence package per cause: charts, similar cases, data excerpts **(M)**

### 1.3 Engineer workflow

- [ ] Mobile-friendly review UI **(M)**
- [ ] Approve / reject / add manual cause **(S)**
- [ ] Inline report editing before sign-off **(S)**
- [ ] Report export in the customer's format (PDF, Word) **(M)**
- [ ] Local, on-site, append-only case database **(M)**
- [ ] Audit trail: who approved, when, model version, data sources **(S)**

### 1.4 Pilot measurement

- [ ] Baseline: log current investigation time per case before go-live **(S)**
- [ ] Pilot dashboard: investigations, cause accuracy, time saved **(M)**
- [ ] Weekly accuracy report for engineer feedback **(S)**
- [ ] Feedback loop: corrections feed the next ranking iteration **(M)**

### 1.5 Deployment

- [ ] On-site server deployment (Linux, Docker) **(M)**
- [ ] NPU broker integration for image inference on Ascend hardware, optional **(L)**
- [ ] No outbound network required after setup **(S)**

---

## Phase 2 — Production

Goal: expand within the pilot factory, support multiple lines and defect types, charge full price.

### 2.1 More defect types and lines

- [ ] Multi-defect-type model for the same line **(L)**
- [ ] Multi-line support with separate data channels **(M)**
- [ ] Cross-line pattern detection **(M)**

### 2.2 More connectors

- [ ] SAP QM connector **(L)**
- [ ] SAP PM connector **(L)**
- [ ] Rockwell FactoryTalk connector **(M)**
- [ ] Siemens S7 / TIA Portal connector **(M)**
- [ ] Generic REST/GraphQL connector **(M)**
- [ ] Supplier batch and certificate import **(S)**

### 2.3 Analytics and management

- [ ] Quality manager dashboard: defect rate, top causes, time to resolution **(M)**
- [ ] Trend alerts across a threshold **(M)**
- [ ] Corrective action tracking **(M)**
- [ ] Scrap cost and savings estimate **(S)**

### 2.4 Billing and operations

- [ ] Per-line monthly subscription billing **(M)**
- [ ] Setup and integration fee **(S)**
- [ ] NPU server hardware option with margin **(S)**
- [ ] Customer admin panel **(M)**

---

## Phase 3 — Scale

Goal: multiple factories, multiple customers, a connector library that shortens each deployment.

- [ ] Multi-factory deployment for one customer **(L)**
- [ ] Connector library for the top 10 MES/SCADA/CMMS systems **(L)**
- [ ] Cross-factory anonymised pattern sharing, opt-in **(L)**
- [ ] Mobile app: photo of a defect starts an investigation **(L)**
- [ ] ISO 9001 workflow integration **(M)**
- [ ] IATF 16949 compliance pack **(M)**
- [ ] FDA 21 CFR Part 11 audit trail for pharma/medtech **(L)**
- [ ] Multi-tenant architecture with full data isolation **(L)**
- [ ] Managed NPU server offering **(M)**

---

## Product UI (after the demo)

These are the former "Phase GUI" screens, correctly placed after the stage piece. They are product
work for pilots and customers, not conference work.

- [ ] Mobile-friendly engineer review: approve, reject, add a cause **(M)**
- [ ] Report preview with inline edit and sign-off **(M)**
- [ ] Report export in the customer's format **(M)**
- [ ] Quality manager dashboard: investigations this week, resolution time, scrap prevented **(M)**
- [ ] Top-causes chart and defect trend per line **(M)**
- [ ] Case history and audit trail **(M)**
- [ ] Dark industrial design language retained, but as a daily tool **(S)**

---

## Not planned (with reasons)

- **Line control or automatic process adjustment** — liability and safety risk; the engineer decides.
- **Automatic defect rejection** — the existing rejection system stays; RootCause only investigates.
- **Multi-tenant SaaS with factory data leaving the site** — data sovereignty is the selling point.
- **Predictive maintenance** — different problem, different buyer.
- **A generic AI-for-manufacturing platform** — focus stays on root cause and the quality report.
- **Cloud GPU inference for production** — factory data stays on-site.
- **A dashboard-led conference demo** — dashboards are for pilots, not stages.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). Build the 90-second teardown first. No customer needed.
2. **Rehearse and red-team** (1 week). Acceptance tests, fallback, venue test.
3. **Stage gate** — if the five-stranger test fails, do not book the next conference.
4. **0B — the functional demo** (4 weeks) for the booth and Q&A.
5. **First pilot customer** — a quality manager in injection moulding or electronics with Keyence
   cameras and OPC-UA SCADA.
6. **1.1 connectors** before anything else in Phase 1.
7. **1.2 detection and investigation** — the agent and ranking are the core product.
8. **1.3 engineer workflow** — mobile UI and export are what the engineer sees.
9. **1.4 pilot measurement** — baseline on day one.
10. **Phase 2 connectors** only after the pilot succeeds and a second customer is signed.
11. **Phase 3** only after at least three customers are in production.

---

## Open decisions

- Which real part becomes the stage prop, and can it be shown publicly?
- Does the stage piece replace the playable demo at `play/rootcause.html`, or extend it?
- Which evidence order is the default: surface first or x-ray first?
- Do we use a physical loupe, a macro camera, or both?
- Which defect pack is commercial-safe for the public demo?
- Which pilot segment gives the fastest OPC-UA access?
- What is the one accuracy number we are willing to say on stage, with provenance?
