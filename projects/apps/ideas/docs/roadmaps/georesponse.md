# GeoResponse — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means imagery and compute stay inside the customer network.
"Agent" means JiuwenSwarm orchestrates context enrichment, ranking and assessment writing.

**Status.** Stage spec + business plan. Playable proof built: [play/georesponse.html](../../play/georesponse.html).
Product not built.

**One line.** When an area changes — flood, fire, damage or new construction — GeoResponse finds
it, ranks what matters by urgency and value, and writes the assessment with a map. Hours, not days.

**Buyer.** Head of Claims (insurer) · Asset Management Director (utility) · Emergency Management
(government, Phase 3).

**Best first market.** Property insurer — storm and flood damage assessment. Clear ROI, large
volume of claims after a single event, measurable before/after.

**The sentence the audience repeats:** *"We knew where to send the teams before the second coffee."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc and acceptance tests.

---

## What changed in this revision

- **Stage first.** The old Phase 0 built an analyst product and hoped the map would carry the demo.
  Phase 0 is now **0A (stage piece)** and **0B (functional demo)**.
- **The question became the product.** The stage is built around one decision: *where do we send the
  three teams?* Not a tour of a GIS dashboard.
- **Time scrub replaces the before/after slider.** The flood moves; the stakes rise.
- **The trust beat is mandatory.** One high-confidence site is a false positive; the analyst rejects
  it; ranking and team allocation update in the same scene.
- **Audience agency added.** The room decides where team 3 goes.
- **Phase GUI retired.** Analyst review, exports and dashboards are product work after the demo.
- **Stagecraft, metrics, data rights and post-stage motion added.**
- **Licensing clarified.** Sentinel is open with attribution; OSM is ODbL; Copernicus EMS maps have
  their own terms; commercial imagery needs a licence.

**The old stage idea:**

| Old demo | 2026 stage piece |
|---|---|
| Map zones, hero counters, top-10 list, before/after slider, approve/reject, dashboard | One street, a moving flood edge, three teams, a wrong site, an audience choice, a zoom-out |

---

## Phase 0A — "Where do we send the teams?"

Goal: a stage piece that turns a map into a command decision, with the room participating.
Time: 2 weeks to build, 1 week to rehearse. No customer, no live imagery download, no network.

**Set.** One large map at 14:32, a 40 km² flood event, 18 priority sites, 3 response teams. The
screen is the map; the physical props are a printed map and three metal team tokens.

**The verb.** Scrub time from 12:00 to 18:00 and watch the flood edge move. Then place the teams.

**The cold open.** *"14:32. Forty square kilometres under water. Eighteen places that matter. Three
teams."* The map is already moving.

**The turn.** The map is not the product. The decision is. By 1:20 the room sees where the teams went,
what they missed, and why 42 minutes matters.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | 40 km², 18 sites, 3 teams; the flood is moving | Full-bleed map, time 12:00 |
| 0:10–0:25 | First touch | Scrub to 18:00; the east edge advances | Flood extent, site pins wake up |
| 0:25–0:40 | Agent ranks | Pick site 1; the "why" chain appears | Road + substation + people |
| 0:40–0:55 | Trust beat | Top-ranked site is a false positive; analyst rejects it | Roof/water reflection clears; rank re-orders |
| 0:55–1:10 | Audience choice | Team 3: site A or site B? The room votes | Two candidate sites, coverage preview |
| 1:10–1:20 | The reveal | Zoom out to 40 km²; 18 sites; assessment ready | Hero map, one-page field order |
| 1:20–1:30 | The line | "Before the second coffee." QR; reset | QR + reset |

### The hero interaction

Time scrub is the spine: 12:00 → 18:00. The flood edge moves east, sites flip from *watch* to *high
risk*, and the ranking changes. The audience sees that the answer is time-dependent, not a static map.

### The trust beat, in detail

- The agent's top site is a **false positive**: a dark roof and wet pavement read as structural damage.
- The analyst opens the site and rejects it with a visible reason: **the roof edge is intact; the
  dark shape is water reflection.**
- The map updates in the same scene: the false positive drops, a previously second-ranked site rises,
  and a team is freed.
- The presenter says: *"The model was confident. The analyst was right. This is why a human signs the
  assessment."*

### Audience agency

Team 3 can go to **Site A** (dense housing, blocked access) or **Site B** (substation, open road).
Both are defensible; the room votes. The map shows coverage, response time and what stays uncovered.
The presenter commits to the room's choice and names the trade-off.

### Props and stagecraft

- A printed A1 map of the same area, with three magnetic team tokens.
- The screen mirrors the printed map; the tokens move when the audience decides.
- One low flood/rain bed; a single ping when a site flips to high risk; silence under the trust beat.
- Amber for watch, red for high risk, cyan for assigned teams.
- Reset: `R`, under five seconds, back to 12:00 with three unassigned teams.

### Phase 0A checklist

- [ ] One real event, one street, 40 km²; Sentinel-2 before/after pair cached locally **(S)**
- [ ] Flood extent animation across 12:00–18:00, with 18 site pins **(M)**
- [ ] Site detail card with the "why" chain: access + power + people **(M)**
- [ ] Ranking that visibly re-orders when the analyst rejects the false positive **(M)**
- [ ] Team assignment limited to 3, with coverage and response-time preview **(M)**
- [ ] Audience choice between two defensible sites, with visible trade-off **(S)**
- [ ] Zoom-out reveal: one street → 40 km², 18 sites, 42 minutes **(S)**
- [ ] One-page printed field order that matches the screen **(S)**
- [ ] Printed map + three team tokens **(S)**
- [ ] 90-second script, word-for-word for the first 20 seconds **(S)**
- [ ] Deterministic run, reset under five seconds **(S)**
- [ ] 90-second fallback recording and a backup laptop **(S)**
- [ ] Contrast and map legibility test at 10 metres **(S)**
- [ ] Data provenance sheet on screen and in the booth **(S)**

**Do not build for 0A:** login, settings, layer managers, layer toggles, exports, batch approval,
dashboards, analyst queues.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" Same story, real imagery, still deterministic
and offline.

Time: 3–4 weeks after 0A. It can reuse the [playable proof](../../play/georesponse.html) as its shell.

- [ ] Sentinel-2 before/after pair for a real event (2021 Germany/Belgium floods recommended) **(S)**
- [ ] GeoTIFF tiling engine with projection normalisation **(M)**
- [ ] Change detection model on tile pairs, precomputed **(M)**
- [ ] Severity classification: red / orange / yellow **(S)**
- [ ] OSM basemap: roads, buildings, land use **(S)**
- [ ] Change overlay on an interactive map (MapLibre or Leaflet) **(M)**
- [ ] Time-scrub player for flood extent **(M)**
- [ ] Location ranking: change extent, confidence, asset value, access **(M)**
- [ ] Agent assessment paragraph from ranked findings **(M)**
- [ ] Analyst review: approve / flag / reject per site **(M)**
- [ ] Export: GeoJSON + PDF one-pager **(M)**
- [ ] Booth mode: reset, scenario picker, 3-minute run **(S)**
- [ ] Runs fully offline after the data pack is cached **(S)**

### Demo architecture

- Fixed event, fixed tiles, precomputed detections; no live download on stage.
- All tiles, fonts and map styles local; no CDN.
- The time scrub is a rendering of a precomputed sequence, not a live model.
- Stage mode omits the analyst queue; booth mode can show it.
- Provenance panel: imagery source, date, model, whether the change is real or simulated.

### Data rights

- **Copernicus Sentinel** data is free and open; attribution required.
- **Copernicus EMS** maps have their own terms; check before using the published maps as the hero.
- **OpenStreetMap** is ODbL; display "© OpenStreetMap contributors".
- **Commercial imagery** (Planet, Maxar, Airbus) needs a licence even for a demo; do not assume a
  trial covers a public stage.
- Keep a provenance sheet for every tile and every label.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the decision in one sentence.
- [ ] First touch within 15 seconds; the time scrub is obvious.
- [ ] The flood-edge reveal lands by 30 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat and the vote.
- [ ] Reset under five seconds.
- [ ] Two volunteers can assign a team without help.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to the flood-edge reveal: ≤ 30 s.
- Full run: ≤ 90 s.
- Volunteer completion: ≥ 80%.
- Qualified insurer/utility conversations: ≥ 20.
- Pilot intros booked: ≥ 5.

### Post-stage motion

- QR to the playable demo, not a signup form.
- One-page "GeoResponse pilot in 90 days" offer.
- 10-minute booth version: one event, one decision.
- Follow-up within 48 hours with the recording and the one-pager.
- Capture 20 named claims and asset leaders.

---

## Phase 1 — First pilot

Goal: one property insurer, one storm or flood event, one region, 90 days.
Run the AI assessment in parallel with the analyst's manual process. Compare results.

**Gate:** do not start the pilot until the stage piece has passed all acceptance tests.

### 1.1 Imagery pipeline

- [ ] Commercial imagery ingestion: Planet, Maxar or Airbus via SFTP or API **(M)**
- [ ] Customer drone orthophoto ingestion (GeoTIFF, LAS) **(M)**
- [ ] Sentinel-2 archive pull for before-images **(S)**
- [ ] Automatic tiling and projection normalisation **(M)**
- [ ] Imagery trigger: new file → pipeline starts **(M)**
- [ ] Cloud-cover detection: exclude tiles above 30% cloud **(S)**

### 1.2 Detection and context

- [ ] Damage classification fine-tuned for storm/roof damage **(L)**
- [ ] OSM building footprint matching **(M)**
- [ ] Insured property database geocoding and polygon match **(M)**
- [ ] Asset value enrichment **(S)**
- [ ] Road access check: blocked or flooded routes **(S)**

### 1.3 Ranking and assessment

- [ ] Ranking engine: confidence + insured value + access + change extent **(M)**
- [ ] Agent assessment from ranked findings and context **(M)**
- [ ] Assessment template matching the claims first-notice format **(M)**
- [ ] Confidence disclosure on every finding **(S)**

### 1.4 Analyst workflow

- [ ] Map + list review: approve / flag for adjuster / reject **(M)**
- [ ] Inline notes per location **(S)**
- [ ] Batch approve above a confidence threshold **(S)**
- [ ] PDF export with map, ranked list and assessment **(M)**
- [ ] Audit trail: imagery, model version, analyst, corrections **(S)**

### 1.5 Pilot measurement

- [ ] Baseline analyst time per event **(S)**
- [ ] Accuracy tracking against adjuster-confirmed damage **(M)**
- [ ] False-positive log by reason **(S)**
- [ ] Pilot dashboard: events, accuracy, false positives, time saved **(M)**

### 1.6 Deployment

- [ ] On-site or private-cloud deployment (Linux, Docker) **(M)**
- [ ] NPU broker for on-site inference, optional **(L)**
- [ ] No outbound network required after imagery delivery **(S)**

---

## Phase 2 — Production

Goal: multiple event types, automated monitoring, claims integration, full price.

### 2.1 More change types

- [ ] Flood inundation extent mapping **(L)**
- [ ] Wildfire burned-area and structure-survival model **(L)**
- [ ] Construction change detection **(M)**
- [ ] Vegetation / crop health (NDVI delta) **(M)**

### 2.2 SAR and cloud cover

- [ ] Sentinel-1 SAR ingestion **(L)**
- [ ] SAR change detection **(L)**
- [ ] Optical + SAR fusion **(L)**
- [ ] Commercial SAR connectors: ICEYE, Capella **(M)**

### 2.3 System integrations

- [ ] Guidewire ClaimCenter API **(L)**
- [ ] Duck Creek Claims API **(L)**
- [ ] Esri ArcGIS Server export **(M)**
- [ ] QGIS project export **(S)**
- [ ] Field crew dispatch for utilities **(M)**

### 2.4 Automated monitoring

- [ ] Recurring monitoring for a region or corridor **(M)**
- [ ] Change alerts above a threshold **(M)**
- [ ] Historical baseline / anomaly detection **(L)**

### 2.5 Accuracy and compliance

- [ ] Per-event precision, recall and false-positive report **(M)**
- [ ] Model version pinning on every assessment **(S)**
- [ ] Privacy review for residential imagery **(M)**

---

## Phase 3 — Scale

Goal: multiple customers and sectors, global coverage, government and agriculture.

- [ ] Multi-customer platform with data isolation **(L)**
- [ ] Government / emergency management framework **(L)**
- [ ] Agriculture pack: crop health, field boundaries, insurance **(L)**
- [ ] Mining pack: tailings dams, operational change **(L)**
- [ ] Planet connector (daily 3 m) **(M)**
- [ ] Maxar / Airbus 30–50 cm connector **(M)**
- [ ] IBM Maximo integration **(M)**
- [ ] SAP PM integration **(M)**
- [ ] Managed NPU server offering **(M)**
- [ ] Partner programme: reinsurers, imagery providers **(S)**

---

## Product UI (after the demo)

Former "Phase GUI" items, correctly placed after the stage piece. These are daily analyst tools.

- [ ] Analyst review: map + list, approve / flag / reject per site **(M)**
- [ ] Inline notes and batch approval **(S)**
- [ ] PDF and GeoJSON export **(M)**
- [ ] Analyst summary dashboard: events, approved locations, area covered **(M)**
- [ ] Regional map of events by severity **(M)**
- [ ] Accuracy trend vs adjuster-confirmed damage **(M)**
- [ ] Time-to-assessment comparison vs the manual baseline **(S)**
- [ ] Audit trail and provenance panel **(S)**

---

## Not planned (with reasons)

- **Own satellite or imagery collection** — imagery is a commodity; the assessment is the product.
- **Live video feeds** — surveillance product, different regulation, different ethics review.
- **Automated claim approval without human review** — the analyst stays in the loop.
- **Predictive damage before an event** — Phase 3 at earliest.
- **A generic geospatial analytics platform** — stay focused on the assessment decision.
- **Real-time streaming imagery** — latency is not the bottleneck; accuracy and analyst workflow are.
- **A dashboard-led conference demo** — dashboards are for pilots, not stages.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). One event, one street, three teams, one vote.
2. **Rehearse and red-team** (1 week). Acceptance tests, venue test, fallback.
3. **Stage gate** — if the five-stranger test fails, do not book the next conference.
4. **0B — the functional demo** (3–4 weeks) for the booth and Q&A.
5. **First pilot customer** — a property insurer with storm exposure and a commercial imagery
   subscription.
6. **1.1 imagery pipeline** before anything else in Phase 1.
7. **1.2 detection and context** — this turns "damaged building" into "policy XYZ, value €280k,
   priority HIGH".
8. **1.3 ranking and assessment** — the agent writing the assessment is the time saving.
9. **1.4 analyst workflow** — analyst acceptance decides whether the pilot continues.
10. **1.5 pilot measurement** — baseline on day one.
11. **SAR (2.2)** only after the first pilot; cloud cover will be a practical problem.
12. **Claims integration (2.3)** only after a second customer is signed.

---

## Open decisions

- Which event and street become the stage piece: 2021 Germany/Belgium, or a live 2026 event?
- Do we use a printed map with three tokens, or keep everything on screen?
- Which two sites become the audience choice, and is the trade-off legible in five seconds?
- Which false positive is most defensible: dark roof, wet pavement, or shadow?
- Which imagery is cleared for public demo use, and with what attribution?
- Which insurer gives the first pilot data without a six-month procurement cycle?
- What accuracy number are we willing to say on stage, with provenance?
