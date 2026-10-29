# RootCause — Full Roadmap

*Status: recommended to build. Not started.*

---

## The one line

When a factory finds a bad part, RootCause finds the likely cause and writes the quality report
with evidence — in hours, not days.

---

## The problem, precisely

A camera can see a defect in one second. Finding why it happened takes days.

An engineer searches machine settings, material batch records, maintenance logs and past defect
reports — across four or five separate systems. Then a group meets, guesses, argues, tests, and
someone writes a report by hand. The whole investigation depends on one or two experienced people.
When they leave, the knowledge leaves with them.

This happens dozens of times a month in any active production facility. Each investigation costs
engineer hours. Each day of delay risks more bad parts. Each wrong conclusion risks a recall.

---

## Who buys it and why

**Primary buyer: Quality Manager**
Owns scrap rate, rework cost and customer complaints. Measured on defect rate and report speed.
Feels the pain of every investigation that takes too long.

**Economic buyer: Plant Manager or VP Operations**
Owns production cost and downtime. Approves the budget. Cares about numbers:
scrap cost, rework hours, line downtime, recall risk.

**User: Manufacturing Engineer / Quality Engineer**
Runs the investigation. Does the searching. Writes the report. Will either adopt or reject the tool
based on whether it makes their job easier or harder.

**Best first industries:**
- Plastic injection moulding — visible surface defects, rich machine data, high scrap cost
- Battery cell production — expensive materials, tight tolerances, regulatory pressure
- Electronics assembly — high value per unit, multiple process steps, lots of sensor data
- Metal stamping — consistent defect types, measurable machine parameters

---

## What success looks like

### Pilot metrics (one factory, one line, 90 days)
- Time from defect found to root cause identified: from days → under 4 hours
- Engineer hours per investigation: measure baseline before, target 60% reduction
- Cause accuracy: actual root cause in the AI's top 3 suggestions, ≥ 70% of cases
- Report completion time: from hours of writing → under 30 minutes
- Engineer acceptance: at least 2 of 3 engineers on the line use it by end of pilot

### Business metrics
- Cost per investigation (before vs after)
- Scrap rate change after implementing corrective actions from AI suggestions
- Number of repeat defects (same cause appearing again)

---

## Technical architecture

```
[Camera / Inspection System]
         |
    [NPU — on-site]
    Defect detection
    Image classification
         |
    [Data Aggregator]
    Pulls in parallel:
    - Machine parameters (SCADA / OPC-UA)
    - Material batch records (MES / ERP)
    - Maintenance logs (CMMS)
    - Past defect cases (case database)
         |
    [Agent — JiuwenSwarm]
    Finds patterns across data
    Generates hypotheses
    Ranks causes by evidence
    Drafts quality report
         |
    [Engineer Review UI]
    Approve / reject / comment
    Sign the report
         |
    [Case Store — on-site]
    Saves every case
    Feeds future pattern matching
```

**Key technical decisions:**
- All compute on-site. Factory data never leaves the factory network.
- NPU for image inference (fast, on-site, handles many cameras).
- JiuwenSwarm as the agent that orchestrates data gathering and reasoning.
- Case store is local — becomes more valuable with every investigation saved.
- No line control. No automatic changes. Read-only access to factory systems.

---

## Phase 0 — Conference Demo

**Goal:** a working demo for a conference stage. No real factory needed.

**Duration:** 4–6 weeks

**What to build:**
- Pre-load 50–100 labelled defect images (plastic injection moulded parts — publicly available
  datasets exist, e.g. MVTec AD dataset)
- Pre-load a CSV of machine parameters (temperature, pressure, cooling time, cycle time) for the
  same time window — synthetic but realistic
- Pre-load a maintenance log (last service, sensor calibrations) — synthetic
- Pre-load 6 months of past defect cases — synthetic
- Defect detection model: run on the pre-loaded images, mark the defect on screen
- Cause engine: pattern match across the data, output 3 hypotheses with evidence
- Report template: structured quality report, auto-filled, ready for engineer to edit and sign
- Simple web UI: defect image → data summary → 3 causes with evidence bars → draft report →
  approve button

**Demo script (90 seconds on stage):**
1. Screen shows a camera feed (pre-recorded) — a surface defect appears on a part
2. NPU flags it, bounding box appears
3. AI gathers: machine data for that shift, batch record for that material, last maintenance log
4. Three causes appear with evidence: "High melt temperature (shift avg +8°C above spec) — 61%
   confidence", "Material batch MX-2240 — 3 of last 5 defects on same batch — 24%", "Cooling
   time deviation — 12% shorter than baseline — 15%"
5. Draft quality report appears, pre-filled
6. Engineer clicks Approve — case saved, report timestamped

**What you need for the demo:**
- One laptop or small server
- Optional: USB camera pointed at a physical sample part with a visible defect (dramatically
  improves the live feel)
- Web UI running locally
- No internet connection required — all on-site

---

## Phase 1 — First Pilot

**Goal:** one real factory, one production line, one defect type, three months.
Prove the core value in production conditions.

**Duration:** 3 months

**Prerequisites:**
- One pilot customer signed (quality manager + plant manager)
- Access to: inspection camera output, one machine data source (SCADA or OPC-UA), one batch
  record system
- 6 months of historical defect data from that line

**What to build:**

*Week 1–2: Data connectors*
- Camera integration: connect to the existing inspection camera system (most factories already have
  Keyence, Cognex or similar — read their output, do not replace them)
- SCADA connector: OPC-UA or Modbus read for 10–20 key machine parameters
- Batch record import: CSV or API from their MES or ERP for material batch data

*Week 3–4: Historical data load*
- Load 6 months of past defect cases from their quality system
- Clean and normalise — factory data is always messy
- Tag causes where known (engineers know many from memory)
- Build the initial case database

*Week 5–8: Agent and UI*
- Defect detection: run on the camera feed, on-site NPU
- Data aggregator: pull the right time window of machine data and batch records when a defect is
  detected
- Cause engine: pattern matching across historical cases + current data
- Report generator: match their existing quality report format (they always have one)
- Engineer UI: mobile-friendly (quality engineers are on the floor, not at a desk)

*Week 9–12: Trial and tuning*
- Run alongside their existing process — do not replace it yet
- Engineer uses both their current method and RootCause in parallel
- Compare: was the AI's top cause correct? How long did each take?
- Tune the cause ranking based on feedback
- Fix integration issues (there will be many)

**Pilot success criteria:**
- System runs for 4 weeks without downtime
- 20+ investigations completed
- Cause accuracy ≥ 65% (top 3)
- At least 2 engineers use it voluntarily by week 10

---

## Phase 2 — Production

**Goal:** expand within the pilot factory, make the product robust, charge for it.

**Duration:** 3–6 months after pilot

**What changes:**
- More defect types on the same line
- More production lines in the same factory
- Maintenance records connector (CMMS — often SAP PM or a standalone system)
- Supplier record connector: link batch defects back to supplier
- Pattern detection over time: "this cause has appeared 3 times this month"
- Analytics dashboard for the quality manager: defect rate, top causes by line, time to resolution
- Formal subscription contract: per-line monthly fee + NPU server optional

**New integrations to build:**
- SAP QM (quality management module — very common in manufacturing)
- SAP PM (plant maintenance — for maintenance records)
- Rockwell FactoryTalk (common SCADA in North America)
- Siemens MindSphere or TIA Portal (common in Europe)
- Generic OPC-UA for everything else

**Pricing model:**
- Per production line per month: €2,000–4,000
- Setup and integration fee: €15,000–40,000 depending on complexity
- Optional on-site NPU server: hardware + 20% margin

---

## Phase 3 — Scale

**Goal:** multiple factories, multiple customers, a connector library that accelerates every new
deployment.

**Duration:** 6–18 months after production

**What changes:**
- Multi-factory deployment: one customer, five factories, one dashboard
- Connector library: pre-built integrations for the top 10 MES/SCADA/CMMS systems — each new
  factory takes weeks, not months
- Cross-factory learning: anonymised patterns across customers (with consent) — "this cause is
  common in injection moulding when humidity exceeds X"
- Mobile app: quality engineer on the floor, photo of defect → investigation started
- Integration with quality standards workflows: ISO 9001, IATF 16949 (automotive), FDA 21 CFR
  Part 11 (pharma)

---

## Go-to-market

**First customer approach:**
Do not sell to procurement. Sell to the quality manager.

Find quality managers at mid-size manufacturers (200–2,000 employees). The sweet spot is a factory
that:
- Already has inspection cameras (so integration is easier)
- Has a scrap problem they are trying to solve (ask for their scrap rate)
- Uses SAP or a common MES (easier to integrate)
- Is not a tier-1 automotive (too slow) or a tiny shop (too small a budget)

**How to find them:**
- Manufacturing trade shows: Quality Expo, IMTS, Hannover Messe
- LinkedIn: search "quality manager" + factory size
- Through equipment vendors: camera and sensor companies (Keyence, Cognex, Balluff) sell to the
  same buyers — partnership or referral

**First conversation:**
"How many defect investigations do your engineers do per month? How long does each one take? What
does a bad month look like in scrap cost?"

If the answers are "20+ investigations, 2+ days each, scrap costs us €50k+ per month" — that is a
customer.

---

## Risks and how to handle them

| Risk | How to handle it |
|---|---|
| Factory data is messy and inconsistent | Expect 2–3 weeks of data cleaning in every pilot. Price it in. |
| MES/SCADA integration is slow and custom | Build generic OPC-UA and CSV connectors first. Avoid proprietary APIs until you have 3 customers using the same system. |
| Engineers do not trust AI suggestions | Start with "advice only". The engineer always decides. Show evidence, not just conclusions. |
| False positives erode trust fast | Set a confidence threshold. If not confident, say so. Do not guess. |
| Sales cycles in manufacturing are long | Start with a 30-day paid proof-of-concept at fixed cost. Remove the risk from the buyer. |
| A wrong root cause leads to more defects | Make it clear in the UI: "These are hypotheses, not diagnoses. The engineer approves." Never auto-apply. |

---

## What not to build (ever, until much later)

- Line control or automatic process adjustment
- Automatic defect rejection (keep the existing rejection system)
- Multi-tenant SaaS with factory data leaving the site
- Predictive maintenance (different product, different buyer)
- A generic "AI for manufacturing" platform

Stay focused: one problem, one deliverable (the quality report), one buyer (quality manager).

---

## Smallest possible first version (4 weeks)

1. Load 6 months of defect images and machine data from one line (CSV export from their system)
2. Detect the defect type (pre-trained model, no custom training yet)
3. Pull machine parameters for the relevant time window
4. Match against past cases
5. Output 3 probable causes with evidence
6. Pre-fill a quality report template
7. Engineer approves → saved

No camera integration. No live data. No line connection. Just: data in → causes + report out.
If that gets used 5 times in the first month, build the live integration.

---

## Open questions before starting

- Which factory and which line first?
- What inspection cameras do they already have?
- What MES or SCADA system are they on?
- Do they have 6+ months of historical defect data in a usable format?
- What does their current quality report look like (template)?
- Who is the quality manager and do they have budget authority?
- What is their current scrap cost per month — the number that justifies the pilot?
