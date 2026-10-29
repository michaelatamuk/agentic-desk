# GeoResponse — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means imagery and compute stay inside the customer network.
"Agent" means JiuwenSwarm orchestrates context enrichment, ranking and assessment writing.

**One line.** When an area changes — flood, fire, damage or new construction — GeoResponse finds
it, ranks what matters by urgency and value, and writes the assessment with a map. Hours, not days.

**Buyer.** Head of Claims (insurer) · Asset Management Director (utility) · Emergency Management
(government, Phase 3).

**Best first market.** Property insurer — storm and flood damage assessment. Clear ROI, large
volume of claims after a single event, measurable before/after.

---

## Phase 0 — Conference demo

Goal: a working, compelling demo on a conference stage. No customer or paid imagery needed.
Data source: Copernicus Emergency Management Service (free, real disaster data with expert labels)
+ Sentinel-2 (free, 10m optical imagery, global archive) + OpenStreetMap (free context).

- [ ] Sentinel-2 before/after image pair download for a real event (2021 Germany/Belgium floods recommended) **(S)**
- [ ] GeoTIFF tiling engine: split large image into manageable tiles, normalise projection **(M)**
- [ ] Change detection model: run open-weight model (ChangeFormer or fine-tuned SAM) on tile pairs **(M)**
- [ ] Severity classification: red (severe) / orange (moderate) / yellow (minor change) **(S)**
- [ ] OpenStreetMap basemap integration: roads, building footprints, land use overlay **(S)**
- [ ] Change overlay on interactive web map (MapLibre or Leaflet) **(M)**
- [ ] Before/after image slider in the map viewer **(S)**
- [ ] Location ranking: score each flagged area by change extent and detection confidence **(M)**
- [ ] Top-10 prioritised location list with coordinates, severity, confidence **(S)**
- [ ] Agent (JiuwenSwarm): generate written assessment paragraph from ranked findings **(M)**
- [ ] Analyst review UI: approve / correct / reject per location **(M)**
- [ ] Export: GeoJSON of approved locations + PDF assessment with embedded map **(M)**
- [ ] Runs fully offline on one laptop after imagery is downloaded — no internet on stage **(S)**
- [ ] Demo data package: pre-downloaded imagery, pre-run results, ready to present **(S)**
- [ ] 90-second demo script and run-through **(S)**

---

## Phase 1 — First pilot

Goal: one property insurer, one storm or flood event, one region, 90 days.
Run the AI assessment in parallel with the analyst's manual process. Compare results.

### 1.1 Imagery pipeline

- [ ] Commercial imagery ingestion: Planet, Maxar or Airbus via SFTP or API **(M)**
- [ ] Customer drone orthophoto ingestion (GeoTIFF, LAS) **(M)**
- [ ] Sentinel-2 archive pull for before-image (free, automated by area and date) **(S)**
- [ ] Automatic tiling and projection normalisation for all input sources **(M)**
- [ ] Imagery trigger: new file delivered → pipeline starts automatically **(M)**
- [ ] Cloud-cover detection: flag tiles with >30% cloud cover, exclude from analysis **(S)**

### 1.2 Detection and context

- [ ] Damage classification model fine-tuned for storm/roof damage on customer imagery **(L)**
- [ ] OpenStreetMap building footprint matching: link detected change to a building polygon **(M)**
- [ ] Customer insured property database geocoding and polygon match **(M)**
- [ ] Asset value enrichment: attach policy value to each matched building **(S)**
- [ ] Road access check: flag locations with blocked or flooded access routes **(S)**

### 1.3 Ranking and assessment

- [ ] Ranking engine: combine detection confidence + insured value + access + change extent **(M)**
- [ ] Agent (JiuwenSwarm): pull ranked findings, context and asset data, write structured assessment **(M)**
- [ ] Assessment template: match the customer's existing claims first-notice format **(M)**
- [ ] Confidence disclosure: every finding shows the model's confidence level **(S)**

### 1.4 Analyst workflow

- [ ] Analyst review UI: map + list view, approve / flag for adjuster / reject per location **(M)**
- [ ] Inline notes per location **(S)**
- [ ] Batch approve: mark all locations above a confidence threshold in one action **(S)**
- [ ] Report export: PDF with map, ranked list and assessment text in customer format **(M)**
- [ ] Audit trail: imagery source, model version, analyst name, correction history **(S)**

### 1.5 Pilot measurement

- [ ] Baseline log: record analyst time per event before go-live **(S)**
- [ ] Accuracy tracking: compare AI-detected locations against adjuster-confirmed damage **(M)**
- [ ] False positive log: track analyst rejections by reason **(S)**
- [ ] Pilot dashboard: event count, detection accuracy, false positive rate, time saved **(M)**

### 1.6 Deployment

- [ ] On-site server or private cloud deployment (Linux, Docker) **(M)**
- [ ] NPU broker for image inference on Ascend hardware (optional, for on-site sovereignty) **(L)**
- [ ] No outbound network required after imagery is delivered **(S)**

---

## Phase 2 — Production

Goal: handle multiple event types, automate monitoring, integrate with claims systems,
charge full price.

### 2.1 More change types

- [ ] Flood inundation model: water extent mapping, not just building damage **(L)**
- [ ] Wildfire burned-area and structure-survival model **(L)**
- [ ] Construction change detection: new structures, demolition, site progression **(M)**
- [ ] Vegetation / crop health change (NDVI delta from Sentinel-2) **(M)**

### 2.2 SAR and cloud cover

- [ ] Sentinel-1 SAR ingestion: cloud-penetrating, always available after a storm **(L)**
- [ ] SAR change detection model (different architecture from optical) **(L)**
- [ ] Optical + SAR fusion: use SAR when optical is cloud-covered **(L)**
- [ ] Commercial SAR connectors: ICEYE, Capella (for higher resolution) **(M)**

### 2.3 System integrations

- [ ] Guidewire ClaimCenter API: push prioritised claim list directly **(L)**
- [ ] Duck Creek Claims API **(L)**
- [ ] Esri ArcGIS Server export and layer publish **(M)**
- [ ] QGIS project export **(S)**
- [ ] Field crew dispatch integration for utility customers **(M)**

### 2.4 Automated monitoring

- [ ] Recurring monitoring: check a corridor or region on a schedule (weekly, monthly) **(M)**
- [ ] Change alert: notify analyst when change exceeds a configured threshold **(M)**
- [ ] Historical baseline: build a normal-state model for a region, flag anomalies **(L)**

### 2.5 Accuracy and compliance

- [ ] Per-event accuracy report: precision, recall, false positive rate by change type **(M)**
- [ ] Model version pinning: every published assessment records the exact model version **(S)**
- [ ] Privacy review: confirm residential imagery handling complies with local law **(M)**

---

## Phase 3 — Scale

Goal: multiple customers and sectors, global coverage, government and agriculture markets.

- [ ] Multi-customer platform with full data isolation between tenants **(L)**
- [ ] Government / emergency management fast-track: pre-agreed data-sharing framework with civil protection agencies **(L)**
- [ ] Agriculture pack: crop health monitoring, field boundary verification, insurance **(L)**
- [ ] Mining pack: tailings dam monitoring, operational area change detection **(L)**
- [ ] Planet imagery connector (daily 3m global coverage) **(M)**
- [ ] Maxar / Airbus 30–50cm connector for detailed damage **(M)**
- [ ] IBM Maximo integration for utility asset management **(M)**
- [ ] SAP PM integration for utility maintenance workflows **(M)**
- [ ] Managed NPU server offering for customers requiring full on-site sovereignty **(M)**
- [ ] Partner programme: reinsurer introductions, imagery provider referrals **(S)**

---

## Not planned (with reasons)

- **Own satellite or imagery collection** — imagery is a commodity; the assessment is the product.
- **Live video feeds** — surveillance product, different regulation, different ethics review.
- **Automated claim approval without human review** — keep the analyst in the loop always.
- **Predictive damage before an event** — Phase 3 at earliest; requires different modelling and data.
- **Generic geospatial analytics platform** — stay focused on the assessment workflow.
- **Real-time streaming imagery processing** — latency is not the bottleneck; accuracy and analyst workflow are.

---

## Recommended order

1. **Phase 0** — build the conference demo first. Free data, no customer needed, 3–4 weeks. The 2021 Germany floods data is already publicly available from Copernicus. This is the fastest path to something showable.
2. **First pilot customer** — target a property insurer with storm exposure and an existing commercial satellite subscription. The adjuster workflow gives a measurable before/after.
3. **1.1 imagery pipeline** before anything else in Phase 1 — without imagery delivery, nothing else can be tested.
4. **1.2 detection and context** with the customer asset database — this is what turns "damaged building" into "policy XYZ, value €280k, priority HIGH".
5. **1.3 ranking and assessment** — the agent writing the assessment is what saves analyst hours.
6. **1.4 analyst workflow** — the analyst is the daily user. Their acceptance determines whether the pilot continues.
7. **1.5 pilot measurement** — set the baseline on day 1.
8. **SAR (2.2)** only after the first pilot, because cloud cover will be a problem in practice and must be solved for the product to be reliable.
9. **Claims system integration (2.3)** only after a second customer is signed. Do not build Guidewire integration speculatively.
10. **Phase 3** only after multiple customers and sectors are proven.
