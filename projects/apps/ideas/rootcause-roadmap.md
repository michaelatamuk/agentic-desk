# RootCause — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means the compute and data never leave the factory network.
"Agent" means JiuwenSwarm orchestrates the data gathering and reasoning step.

**One line.** When a factory finds a bad part, RootCause finds the likely cause and writes the
quality report with evidence — in hours, not days.

**Buyer.** Quality manager (primary pain), plant manager (budget), manufacturing engineer (user).

**Best first industries.** Plastic injection moulding · battery cell production · electronics
assembly · metal stamping.

---

## Phase 0 — Conference demo

Goal: a working demo on a conference stage. No real factory or customer needed.
Data source: MVTec AD open dataset (free labelled defect images) + synthetic machine data CSVs.

- [ ] Load MVTec AD defect images (plastic or metal surface category) **(S)**
- [ ] Pre-load synthetic machine parameter CSV (temperature, pressure, cooling time, cycle count) **(S)**
- [ ] Pre-load synthetic maintenance log (last service dates, sensor calibrations) **(S)**
- [ ] Pre-load 6-month synthetic defect case history **(S)**
- [ ] Defect detection model: inference on pre-loaded images, bounding box on screen **(M)**
- [ ] Time-window query: pull machine data for the shift when the defect occurred **(S)**
- [ ] Cause ranking engine: pattern match across case history and current machine data **(M)**
- [ ] Agent (JiuwenSwarm): orchestrate data gathering and generate ranked hypotheses **(M)**
- [ ] Three-cause output with evidence bars (confidence %, supporting data points) **(M)**
- [ ] Quality report template: auto-fill defect, cause, evidence, corrective action draft **(M)**
- [ ] Web UI: defect image viewer with bounding box overlay **(S)**
- [ ] Web UI: cause list with evidence detail (expandable) **(S)**
- [ ] Web UI: report preview, edit and approve button **(S)**
- [ ] Case save: timestamp, approved cause, report version, engineer name **(S)**
- [ ] Runs fully offline on one laptop — no internet required on stage **(S)**
- [ ] Optional: USB camera integration for live defect detection on a physical sample part **(M)**
- [ ] Demo data package: images, CSVs, case history, ready to load **(S)**
- [ ] 90-second demo script and run-through **(S)**

---

## Phase 1 — First pilot

Goal: one real factory, one production line, one defect type, 90 days.
Prove value in production conditions. Run alongside existing process, not replacing it.

### 1.1 Data connectors

- [ ] OPC-UA connector: read 10–20 machine parameters from SCADA in real time **(M)**
- [ ] Modbus connector: fallback for older PLCs **(M)**
- [ ] Existing inspection camera output reader (Keyence, Cognex, or generic TCP/IP feed) **(M)**
- [ ] Batch record CSV import from MES or ERP **(S)**
- [ ] Historical defect data loader: 6 months from customer quality system **(M)**
- [ ] Data normalisation and cleaning pipeline (factory data is always messy) **(M)**

### 1.2 Detection and investigation

- [ ] Defect detection model fine-tuning on customer-specific defect images **(L)**
- [ ] Time-window aggregator: link defect event timestamp to machine state **(M)**
- [ ] Batch record linker: match defect timestamp to active material batch **(S)**
- [ ] Case similarity search: find past defects with matching machine state or batch **(M)**
- [ ] Agent (JiuwenSwarm): orchestrate multi-source data pull and hypothesis generation **(M)**
- [ ] Cause ranking: weighted by frequency in similar cases, machine deviation magnitude, batch match **(M)**
- [ ] Evidence package per cause: supporting charts, similar past case images, data excerpts **(M)**

### 1.3 Engineer workflow

- [ ] Mobile-friendly engineer review UI (quality engineers are on the floor) **(M)**
- [ ] Approve cause / reject cause / add manual cause **(S)**
- [ ] Inline report editing before sign-off **(S)**
- [ ] Report export in customer's existing format (PDF, Word) **(M)**
- [ ] Case database: local, on-site, append-only **(M)**
- [ ] Audit trail: who approved, when, which model version, which data sources **(S)**

### 1.4 Pilot measurement

- [ ] Baseline measurement: log current investigation time per case before go-live **(S)**
- [ ] Pilot dashboard: investigation count, cause accuracy (confirmed vs suggested), time saved **(M)**
- [ ] Weekly accuracy report for engineer feedback **(S)**
- [ ] Feedback loop: engineer corrections feed into next cause ranking iteration **(M)**

### 1.5 Deployment

- [ ] On-site server deployment (Linux, Docker) **(M)**
- [ ] NPU broker integration for image inference on Ascend hardware (optional) **(L)**
- [ ] No outbound network required after setup **(S)**

---

## Phase 2 — Production

Goal: expand within the pilot factory, support multiple lines and defect types, charge full price.

### 2.1 More defect types and lines

- [ ] Multi-defect-type model: train additional defect classifiers for the same line **(L)**
- [ ] Multi-line support: separate data channels per line, unified dashboard **(M)**
- [ ] Cross-line pattern detection: "this cause has appeared on three lines this week" **(M)**

### 2.2 More data connectors

- [ ] SAP QM (quality management module) connector **(L)**
- [ ] SAP PM (plant maintenance / maintenance records) connector **(L)**
- [ ] Rockwell FactoryTalk SCADA connector **(M)**
- [ ] Siemens S7 / TIA Portal connector **(M)**
- [ ] Generic REST and GraphQL connector for non-standard MES **(M)**
- [ ] Supplier batch and certificate of conformance import **(M)**

### 2.3 Analytics and management

- [ ] Quality manager dashboard: defect rate, top causes by line, time to resolution **(M)**
- [ ] Trend alerts: cause frequency crossing a threshold triggers a notification **(M)**
- [ ] Corrective action tracking: link a cause approval to a corrective action record **(M)**
- [ ] Cost tracking: scrap cost per defect type, savings estimate **(S)**

### 2.4 Billing and operations

- [ ] Per-line monthly subscription billing **(M)**
- [ ] Setup and integration fee pricing **(S)**
- [ ] NPU server hardware option with margin **(S)**
- [ ] Customer admin panel: user management, line configuration, data retention **(M)**

---

## Phase 3 — Scale

Goal: multiple factories, multiple customers, a connector library that makes each new deployment faster.

- [ ] Multi-factory deployment: one customer, multiple plants, unified view **(L)**
- [ ] Connector library: pre-built, tested integrations for the top 10 MES/SCADA/CMMS systems **(L)**
- [ ] Cross-factory anonymised pattern sharing (opt-in): "this cause is common in injection moulding when humidity exceeds X" **(L)**
- [ ] Mobile app for iOS and Android: photo of defect starts an investigation **(L)**
- [ ] ISO 9001 workflow integration: link case records to corrective action and audit trail **(M)**
- [ ] IATF 16949 compliance pack for automotive customers **(M)**
- [ ] FDA 21 CFR Part 11 audit trail for pharmaceutical and medical device customers **(L)**
- [ ] Multi-tenant architecture with full data isolation per customer **(L)**
- [ ] Managed NPU server offering: hardware + deployment + support **(M)**

---

## Not planned (with reasons)

- **Line control or automatic process adjustment** — liability and safety risk; the engineer always decides.
- **Automatic defect rejection** — the existing rejection system stays in place; RootCause only investigates.
- **Multi-tenant SaaS with factory data leaving the site** — data sovereignty is a core selling point.
- **Predictive maintenance** — different problem, different buyer, different product.
- **Generic AI for manufacturing platform** — focus stays on root cause and the quality report.
- **Cloud GPU inference for production** — factory data must stay on-site.

---

## Recommended order

1. **Phase 0** — build the conference demo first. Takes 4–6 weeks. Needs no customer. Tests whether the concept lands with an audience.
2. **First pilot customer** — find a quality manager at a plastic injection moulding or electronics facility. Prioritise one with Keyence cameras and OPC-UA SCADA (fastest to connect).
3. **1.1 connectors** before anything else in Phase 1 — without data, nothing else can be tested.
4. **1.2 detection and investigation** — the agent and cause ranking are the core product.
5. **1.3 engineer workflow** — mobile UI and report export are what the engineer sees. Get feedback here early.
6. **1.4 pilot measurement** — set the baseline on day 1 or the comparison has no anchor.
7. **Phase 2 connectors** only after the pilot succeeds and a second customer is signed. Do not build SAP integration speculatively.
8. **Phase 3** only after at least three customers are in production.
