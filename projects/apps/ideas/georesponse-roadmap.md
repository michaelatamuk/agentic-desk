# GeoResponse — Full Roadmap

*Status: recommended to build. Not started.*

---

## The one line

When an area changes — flood, fire, damage or new construction — GeoResponse finds it, ranks what
matters by urgency and value, and writes the assessment with a map. Hours, not days.

---

## The problem, precisely

A satellite or drone can image a large area in minutes. Making sense of it takes days.

An analyst opens an image viewer, scans thousands of tiles by hand, marks what looks different,
cross-checks against asset maps, writes notes, and assembles a report. During a flood or wildfire
that process costs lives. For an insurer processing storm claims it costs money and customer trust.
For a utility checking power line corridors after a storm it means sending field crews to locations
the image already shows are fine.

The problem is not the imagery. Imagery is cheap and getting cheaper. The problem is the gap
between "pixels arrived" and "decision made."

---

## Who buys it and why

**First market: Property insurers**
Use case: storm damage, flood, wildfire — roof and structure assessment.
Buyer: Head of Claims Operations or Chief Claims Officer.
Pain: large event produces thousands of claims at once, adjusters are overwhelmed, cycle times
stretch, customers complain, reserves are uncertain.
Value: faster first assessment, triage before sending adjusters, better reserve accuracy.

**Second market: Utility companies**
Use case: power line corridor and substation inspection after storms, ongoing asset monitoring.
Buyer: Asset Management Director or Head of Field Operations.
Pain: after a storm they send crews to inspect hundreds of km of lines — most are fine.
Value: AI prioritises where to send crews first, reducing truck rolls and outage time.

**Third market (later): Government / Emergency Management**
Use case: disaster response, flood extent mapping, infrastructure damage assessment.
Buyer: Emergency Management Agency, Civil Protection.
Pain: first responders need damage maps before they can deploy resources.
Value: faster situational awareness.

**Fourth market (later): Agriculture**
Use case: crop health monitoring, field boundary verification, insurance.

---

## What success looks like

### Pilot metrics (one customer, one region, 90 days)
- Time from imagery to completed assessment: from 3–5 days → under 4 hours
- Analyst hours per assessment: measure baseline, target 70% reduction
- Detection accuracy: ≥ 80% of actual changed/damaged areas found
- False positive rate: ≤ 15% (flagged locations that are not actually damaged)
- Analyst acceptance: analyst uses the AI output as the starting point, not starting from scratch

### Business metrics for the buyer
- Claims cycle time (insurer): first assessment faster → faster adjuster dispatch
- Truck rolls avoided (utility): % of lines confirmed undamaged without a field visit
- Cost per assessed area vs current

---

## Technical architecture

```
[Imagery Source]
Satellite (Sentinel-2, commercial) or customer drone
         |
    [Imagery Ingestion]
    Accept GeoTIFF, JPEG2000, orthophoto
    Split into tiles, normalise projection
         |
    [NPU — on-site or private cloud]
    Change detection model
    Damage classification
    Object detection (buildings, vehicles, power lines)
         |
    [Context Enrichment]
    OpenStreetMap: roads, buildings, land use
    Customer asset database: power lines, poles, insured properties
    Risk data: flood zones, historical damage, population
         |
    [Ranking Engine — Agent / JiuwenSwarm]
    Score each location:
    - Urgency (is it access-blocking? life-safety?)
    - Value at risk (asset value, insured value)
    - Confidence (how certain is the detection?)
    - Access (can a crew reach it?)
         |
    [Output]
    Interactive map (GeoJSON / web viewer)
    Prioritised location list (CSV / API)
    Written assessment (structured text, customer template)
    Evidence package (image crops, confidence, context)
         |
    [Analyst Review UI]
    Approve / correct / reject locations
    Add notes
    Publish final report
         |
    [Audit Trail]
    Record: imagery source, model version, analyst corrections,
    final approved assessment
```

**Key technical decisions:**
- Change detection: compare before and after image at the same location. Before image can be
  from an archive (Sentinel-2 has free global archive back to 2015).
- Context from OpenStreetMap is free and global — no customer data needed for the first version.
- Customer asset database integration makes the ranking much more useful — priority for Phase 1.
- On-site NPU for customers with data sovereignty requirements (government, some insurers).
  Private cloud deployment for others.
- JiuwenSwarm as the reasoning layer: decides what context to pull, how to rank, how to phrase
  the assessment.

---

## Phase 0 — Conference Demo

**Goal:** a working, compelling demo for a conference stage. No customer needed.

**Duration:** 4–6 weeks

**Data — all free and public:**
- **Copernicus Emergency Management Service (CEMS):** provides before/after imagery and
  activation data for real disasters free of charge. Pick any recent European flood or wildfire.
- **Sentinel-2:** free 10m resolution optical imagery, global coverage, 5-day revisit.
- **OpenStreetMap:** free road, building and land use data for context.
- Suggested event: 2021 Germany/Belgium floods (massive, well-documented, free data available
  through CEMS).

**What to build:**
- Imagery loader: accept the Sentinel-2 GeoTIFF pair (before/after)
- Tile the area of interest (e.g. 20km × 20km around the affected region)
- Change detection: pre-trained model (open-source options: ChangeFormer, BIT, or a fine-tuned
  Segment Anything Model). Run on GPU/NPU.
- Overlay on an OpenStreetMap basemap
- Colour-code by severity: red (severe change / likely damage), orange (moderate), yellow (minor)
- Ranked list: top 10 locations with highest urgency score
- Written assessment: 1–2 paragraphs generated by the agent describing what was found, how many
  buildings affected, access routes, priority areas
- Simple web map UI (Leaflet or MapLibre) with the before/after slider

**Demo script (90 seconds on stage):**
1. "This is the Ahr valley, Germany, July 2021, the morning after the flood."
2. Before image on screen (normal valley, roads, villages)
3. "GeoResponse loads the post-flood imagery."
4. After image — obviously damaged (bridges gone, roads flooded)
5. Change detection runs (10–15 seconds on NPU) — red/orange/yellow zones appear
6. Ranked list appears: "Location 7 — Schulstrasse bridge, Ahrweiler — HIGH — bridge collapsed,
   access to 340 residents cut — confidence 94%"
7. Written assessment appears: structured paragraph, analyst-ready
8. "An analyst who would have spent three days scanning this can now review and approve in one
   hour."

**What you need for the demo:**
- One laptop with GPU, or a small server
- The before/after Sentinel-2 images downloaded in advance (free)
- Pre-run the change detection so the stage demo shows results in seconds, not minutes
- Web UI running locally (no internet needed on stage)

---

## Phase 1 — First Pilot

**Goal:** one real customer, one real use case, one region, three months.
Either a property insurer (storm damage) or a utility (corridor inspection).

**Duration:** 3 months

**Recommended first customer: property insurer, storm damage**
Why: they have clear ROI (faster claims), they already have analysts doing this by hand, and the
comparison before/after is easy to measure.

**Prerequisites:**
- Customer signed for a 90-day paid pilot
- Access to: their commercial satellite subscription OR permission to use Sentinel-2 for their
  region
- Their property database (insured addresses, policy values) — this makes the ranking much better
- Their report template (they always have a format)

**What to build:**

*Week 1–2: Imagery pipeline*
- Connect to their imagery source (Planet, Maxar, Airbus, or their drone operator)
- Handle their file formats and delivery method (SFTP drop, API, S3 bucket)
- Automatic tiling and projection normalisation
- Before-image archive: pull from Sentinel-2 archive for the same area (free)

*Week 3–4: Asset context*
- Load their insured property database (CSV of addresses with policy values)
- Geocode and match to building footprints (OpenStreetMap or their GIS data)
- This step transforms "damaged building" into "policy number XYZ, insured value €280k, priority
  HIGH"

*Week 5–8: Detection and ranking*
- Fine-tune the change detection model on their specific imagery and damage types
  (storm = roof damage, not flood inundation)
- Ranking: combine detection confidence + policy value + location access
- Report generator: match their claims form format exactly
- Analyst UI: map + list + approve / flag for adjuster / reject

*Week 9–12: Trial*
- Run on one storm event, real imagery, real policies
- Compare AI assessment to analyst assessment (done in parallel, not sequentially)
- Measure: accuracy, speed, analyst corrections
- Fix issues, tune thresholds

**Pilot success criteria:**
- 1 storm event assessed end-to-end
- ≥ 80% detection accuracy
- ≤ 15% false positives
- Analyst completes review in ≤ 4 hours (vs 3 days manual)
- At least one adjuster dispatch directly informed by the AI output

---

## Phase 2 — Production

**Goal:** make the product robust, handle multiple event types, charge full price.

**Duration:** 3–6 months after pilot

**What changes:**

*More damage types:*
- Flood (different model from storm — need inundation mapping, not just roof damage)
- Wildfire (burned area detection, structure survival)
- Construction change detection (for utility corridor monitoring)

*Better imagery:*
- SAR (Synthetic Aperture Radar) — works through clouds. Essential for flood and storm response
  where cloud cover hides optical imagery. Sentinel-1 is free. Commercial SAR available from
  Capella, ICEYE.
- Fusion: combine SAR (cloud-penetrating, always available) with optical (higher resolution,
  cloud-dependent)

*Integration:*
- Claims management systems: Guidewire, Duck Creek (very common in insurance)
- GIS platforms: Esri ArcGIS, QGIS export
- Field crew dispatch systems (utility)

*Automation:*
- Trigger: new imagery arrives → pipeline starts automatically → analyst gets notification
- Recurring monitoring: imagery checked weekly or monthly, alert when change detected above threshold

*Pricing:*
- Per assessed area (km² per event): €200–500 per km² for rapid post-event
- Annual monitoring subscription per corridor or region: €50k–200k
- Setup and integration: €20k–50k

---

## Phase 3 — Scale

**Goal:** multiple customers, multiple sectors, global coverage.

**Duration:** 6–18 months after production

**What changes:**
- Multi-customer platform with isolation (each customer sees only their data)
- Government / emergency management: faster procurement via existing emergency data-sharing
  frameworks (Copernicus EMS partnership, national civil protection agencies)
- Agriculture: crop health (NDVI time series), field boundary verification for subsidies
- Mining: tailings dam monitoring, operational area change detection
- NPU server offering: for customers with strict data sovereignty (government, defence)

**Connector library:**
- Imagery: Planet, Maxar, Airbus, ICEYE, Capella, Sentinel Hub API
- Claims: Guidewire, Duck Creek, Majesco
- GIS: Esri ArcGIS Server, QGIS, QGIS Server
- Asset management: IBM Maximo, SAP PM (for utilities)

---

## Go-to-market

**First customer: find a head of claims at a property insurer with a storm or flood exposure.**

The conversation:
"After last year's storm season, how long did it take your team to complete initial assessments?
How many adjusters did you dispatch that could have been handled remotely? What would it mean to
cut that from three days to four hours?"

If they answer "two weeks of chaos and we still had 200 open claims at 30 days" — that is your
customer.

**Where to find them:**
- Insurance industry conferences: InsureTech Connect, RIMS, Demoday events at reinsurers
- Reinsurer introductions: Munich Re, Swiss Re, Gen Re all have innovation teams that introduce
  insurtechs to cedants — a single reinsurer intro can reach 20 insurers
- Catastrophe modelling firms: RMS, CoreLogic, Verisk — they serve the same buyers and may
  partner or refer

**Second path: utility companies**
- After a storm, the Head of Field Operations is desperate. That week is when to call.
- Grid modernisation teams at large utilities are already looking for AI tools.
- Trade shows: DistribuTECH, CIGRE

**What NOT to do first:**
- Do not approach government emergency management as a first customer. Procurement takes 12–18
  months and the budget cycle is rigid.
- Do not try to build the imagery supply. Use what already exists (Sentinel-2 free, commercial
  for production).
- Do not start with agriculture. It is a large market but price-sensitive and requires different
  models.

---

## Risks and how to handle them

| Risk | How to handle it |
|---|---|
| Free Sentinel-2 imagery is 10m resolution — may miss small damage | Use it for demos and discovery. Use commercial imagery (Planet, Maxar at 30–50cm) for production. Price the commercial imagery into the pilot cost. |
| Clouds hide the area after a disaster | Add SAR (Sentinel-1, free) as Phase 2. For Phase 0/1, pick demo events where the imagery is cloud-free. |
| A wrong assessment mislabels an undamaged property | Always require analyst approval before the report is final. Never publish AI output directly. |
| Labelled training data is expensive | Use CEMS-activated events (they come with expert labels). Fine-tune only after you have a paying customer who provides their validation set. |
| Insurance/government procurement is slow | Run a 30-day paid proof-of-concept for a fixed fee. Give the buyer a single event, assess it, show the comparison. |
| Privacy and ethical concerns (aerial monitoring) | Be explicit about what is and is not captured. Residential imagery is sensitive. Focus on infrastructure and commercial property first. |
| Sim-to-real gap in model accuracy | Never publish accuracy claims without customer validation on their own data. Every customer's imagery is different. |

---

## What not to build (until much later)

- Your own satellite
- A live video feed (this is surveillance — different product, different regulation)
- Predictive damage (before an event happens) — Phase 3 at earliest
- Automated claim approval (keep humans in the loop always)
- A generic "geospatial analytics platform" — stay focused on the assessment workflow

---

## Smallest possible first version (3 weeks)

1. Download a Sentinel-2 before/after pair for any real event (free, takes 30 minutes)
2. Run an open-source change detection model on it (ChangeFormer or similar — open weights exist)
3. Put the results on a Leaflet web map with colour coding
4. Rank the top 10 changed locations by area size
5. Write a two-paragraph assessment using the agent
6. Show it on a screen

That is the demo. If someone watching says "I want that for my team" — the product is real.

---

## Open questions before starting

- Which first customer: insurer or utility? (This decides the first damage type to detect.)
- What is the imagery source for the pilot? (Customer subscription, Sentinel-2, or we buy
  commercial for them?)
- Do we deploy on-site (NPU server at the customer) or in a private cloud? (Depends on their
  data sovereignty requirements.)
- What claims or asset management system do they use? (Determines Phase 1 integration priority.)
- What is their definition of "good enough" accuracy for this to replace their current process?
- Who is the analyst who will use it daily? (That person's opinion matters more than the buyer's.)
