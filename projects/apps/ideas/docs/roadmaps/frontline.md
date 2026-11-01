# Frontline — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-site" means ticket data and decision records never leave the support organisation's network.
"LAIX" means the LAIX decision layer orchestrates the triage.

**Status.** Stage spec written. Product not built.

**One line.** When a ticket arrives, Frontline decides whether to act, ask, guide, or escalate —
with a written reason for every call.

**Buyer.** Customer support manager (primary user and budget), VP Customer Success (sponsor),
CCO (enterprise buyer).

**Best first industries.** SaaS · fintech · e-commerce · telecommunications.

**The sentence the audience repeats:** *"Every ticket, a decision. Every decision, a reason."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc and acceptance tests.

---

## Phase 0A — The 90-second queue moment

Goal: a stage piece that makes support managers nod and product leaders see the potential, with or
without narration. Time: 2 weeks to build, 1 week to rehearse. No real ticketing tool, no live
model calls, no network.

**Set.** A large screen showing a support queue: a list of tickets on the left, a LAIX decision
badge on the right of each row. Two tickets near the top look nearly identical. The difference
will be revealed.

**The verb.** Click a ticket; see the full scoring breakdown; watch the confidence gate fire.

**The cold open.** The queue shows 20 tickets. Most are grey (`wait`). One is green (`act`). One
is red (`escalate`). The presenter says: *"Two tickets. Same words. Different decisions."*

**The turn.** The presenter clicks the two near-identical tickets side by side. Both say *"I
can't log in."* The left ticket has a known customer, account history, clear tier. LAIX scores
`act — send password reset link, confidence 0.88`. The right ticket has no history, ambiguous
account type. Confidence gate fires: 0.52 < 0.75. Option `act` eliminated. LAIX returns `ask —
request account email first`. The audience sees the diff: two columns, one value different,
different verb, visible gate.

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | Presenter points to the two near-identical tickets | Queue with two highlighted rows |
| 0:10–0:25 | First touch | Click ticket A — known customer | Scoring breakdown: `act`, 0.88, gate clear |
| 0:25–0:38 | Gate fires | Click ticket B — unknown customer | Gate panel: 0.52 < 0.75, `act` crossed out |
| 0:38–0:52 | Trust beat | AI routes billing complaint to standard queue; agent rejects — churning customer | Decision flips to `escalate → senior rep` |
| 0:52–1:08 | Verify cycle | Auto-reply sent; ticket re-opens 24h later; LAIX escalates | Verify card, re-open animation |
| 1:08–1:20 | Audit | Presenter scrolls the audit log — every decision has a reason | Scrollable log |
| 1:20–1:30 | The line | Closing line; QR to demo; reset | Clean queue |

### The trust beat, in detail

- LAIX routes a billing complaint to the standard support queue. It is a reasonable guess: billing
  complaints are common and often have a known fix.
- The agent rejects it for a visible reason: *"this customer's usage dropped 80% last month —
  they're churning, not just billing-confused."*
- LAIX re-ranks in the same scene: `escalate → senior account manager, confidence context
  updated`.
- The presenter says one sentence: *"It was confident. It was wrong. This is why the agent stays
  in charge."*
- The correction is recorded. Churn signal is now a feature in the ranking for this customer tier.

### Audience agency

The room chooses which ticket to resolve next:

- **A — API error, enterprise customer, no prior history.**
- **B — Password reset, known customer, third request this week.**

Either works. A shows `ask — request API key`. B shows `escalate — security review, unusual
pattern`. The presenter commits to the room's choice.

### Props and stagecraft

- A clean, minimal queue design (white background, colour-coded badges, monospace confidence
  scores).
- A diff panel that lights up when two tickets are shown side by side.
- A subtle gate-fire sound when the confidence bar stops short of the threshold.
- The audit log animates: rows appear as decisions are made, reverse-chronological.
- Reset: `R`, under five seconds, back to the full queue.

### Phase 0A checklist

- [ ] Queue view with 20 pre-loaded tickets, LAIX badges **(M)**
- [ ] Side-by-side ticket diff panel **(M)**
- [ ] Scoring breakdown on click: options, confidence, gate, winner **(M)**
- [ ] Confidence gate animation: bar fills, stops short, option crossed out **(M)**
- [ ] Trust beat: routing rejected, decision re-ranked **(M)**
- [ ] Verify cycle: re-open animation and escalation **(S)**
- [ ] Audit log scroll **(S)**
- [ ] Audience choice: two ticket types, either path works **(S)**
- [ ] 90-second script, word-for-word for the first 20 seconds **(S)**
- [ ] Stage mode: deterministic run, reset under five seconds **(S)**
- [ ] 90-second fallback recording and a backup laptop **(S)**
- [ ] Contrast and type test at 10 metres **(S)**
- [ ] Three full rehearsals, one with a hostile audience, one with no network **(S)**

**Do not build for 0A:** login, settings, real ticketing connectors, multi-team routing, model
training, dashboard.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" after the stage piece. Same story, synthetic
ticket data, deterministic and offline.

Time: 4 weeks after 0A.

- [ ] Synthetic ticket pack: 50 tickets across 5 intent categories, varied history **(S)**
- [ ] Synthetic customer profile store: tier, history, open tickets **(S)**
- [ ] LAIX integration: real `DecisionRequest` objects, real attention + safety policy **(M)**
- [ ] Confidence gate: configurable threshold per intent category **(M)**
- [ ] Full scoring breakdown: options, scores, gate, winner, reason **(M)**
- [ ] Side-by-side diff view for any two tickets **(M)**
- [ ] Trust beat replay: viewer can step through the re-ranking **(M)**
- [ ] Verify cycle: configurable re-open timer **(S)**
- [ ] Audit log: scrollable, filterable by verb **(M)**
- [ ] Booth mode: reset, scenario picker, 3-minute run **(S)**
- [ ] Runs fully offline on one laptop **(S)**

### Demo architecture

- Fixed seed. Every run is identical.
- All LAIX calls are real library calls — this is the honest demo of the library.
- Precomputed ticket stream; no external API calls on stage.
- The diff panel calls LAIX live on ticket selection.
- A visible "powered by LAIX" provenance panel for Q&A.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the product in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] Gate fires and diff is clear by 30 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat.
- [ ] Reset under five seconds.
- [ ] Two volunteers complete the ticket-click interaction unassisted.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to gate reveal: ≤ 30 s.
- Full run: ≤ 90 s.
- Volunteer success: ≥ 80%.
- Qualified conversations at the event: ≥ 10.
- LAIX library adoption inquiries: ≥ 5.

### Post-stage motion

- QR code to the LAIX repository or documentation.
- One-page "How LAIX makes confidence gates visible" explainer.
- A 10-minute booth walkthrough of the routing model.
- Follow-up within 48 hours with the recording and the explainer.

---

## Phase 1 — First integration

Goal: one real support team, one ticketing tool, five intent categories, 30 days.
Agents confirm every decision before it fires.

**Gate:** do not start the integration until the stage piece has passed all acceptance tests.

### 1.1 Ticketing connectors

- [ ] Zendesk Tickets API reader **(M)**
- [ ] Intercom Conversations API reader **(M)**
- [ ] Ticket normaliser: map subject, body, customer tier, history to LAIX Signal + Belief **(M)**
- [ ] Customer profile reader: tier, open tickets, last-contact timestamp **(S)**

### 1.2 LAIX decision layer

- [ ] Ticket → `DecisionRequest` adapter **(M)**
- [ ] Intent classifier: 5 categories (auth, billing, API, account, other) with confidence scores **(M)**
- [ ] Action library: 10 standard responses with cost and disruption scores **(M)**
- [ ] Confidence gate per intent category (password reset: 0.70, billing: 0.85) **(M)**
- [ ] LAIX policy pack: active perception + safety-constrained + escalation **(S)**
- [ ] Plain-English reason rendered for each decision **(M)**

### 1.3 Agent workflow

- [ ] Queue view with LAIX verdict badges **(M)**
- [ ] Click-through to full scoring breakdown **(S)**
- [ ] Approve / override / dismiss interaction **(S)**
- [ ] Correction captured: rejected recommendation + agent's choice **(S)**
- [ ] Escalation routing to named agents or teams **(M)**
- [ ] Append-only decision log with timestamp, model version, ticket snapshot **(S)**

### 1.4 Pilot measurement

- [ ] Baseline: log current routing accuracy and resolution time before go-live **(S)**
- [ ] Pilot dashboard: tickets triaged, correct verb rate, resolution time delta **(M)**
- [ ] Weekly accuracy report for agent feedback **(S)**
- [ ] Correction feedback loop **(M)**

### 1.5 Deployment

- [ ] Hosted or on-site, configurable per customer **(M)**
- [ ] No raw ticket content leaves the customer's environment without explicit opt-in **(S)**
- [ ] Role-based access: agent view vs. manager view **(M)**

---

## Phase 2 — Production

Goal: multiple teams, multiple ticketing tools, charge full price.

- [ ] Freshdesk, Salesforce Service Cloud connectors **(M)**
- [ ] Multi-team routing with ownership rules **(M)**
- [ ] SLA-aware scoring: tickets near SLA breach get higher urgency weight **(M)**
- [ ] Manager dashboard: routing accuracy, resolution time, escalation rate **(M)**
- [ ] Per-seat monthly subscription billing **(M)**
- [ ] SSO / OIDC **(M)**

---

## Phase 3 — Scale

Goal: multiple organisations, connector library, LAIX adoption programme.

- [ ] Multi-tenant architecture with data isolation **(L)**
- [ ] Connector library for top 6 ticketing tools **(L)**
- [ ] Outcome learning: cross-team anonymised accuracy benchmarks, opt-in **(L)**
- [ ] LAIX SDK integration guide for ticketing vendors **(M)**

---

## Not planned (with reasons)

- **Automatic replies without confirmation** — wrong auto-replies damage customer relationships.
- **Replacing Zendesk or Intercom** — Frontline sits above them, not beside them.
- **Generic AI for support platform** — focus stays on the LAIX decision layer demo.
- **Sentiment analysis as primary signal** — confidence in intent, not emotion, drives routing.
- **Dashboard-only demo** — dashboards are for pilots, not stages.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). Build the queue and diff view first. No real connector
   needed.
2. **Rehearse and red-team** (1 week). Acceptance tests, fallback, venue test.
3. **Stage gate** — if the five-stranger test fails, do not book the next event.
4. **0B — the functional demo** (4 weeks) for the booth and LAIX Q&A.
5. **First integration** — one team with Zendesk and 5 intent categories.
6. **1.1 connectors** before anything else in Phase 1.
7. **1.2 LAIX decision layer** — the intent classifier and gate are the core product.
8. **1.3 agent workflow** — the queue view and approve flow are what agents see.
9. **1.4 measurement** — baseline on day one.
10. **Phase 2** only after the integration succeeds and a second team is signed.

---

## Open decisions

- Which ticketing tool is the first integration target?
- What is the right confidence threshold for `act` in the first pilot?
- How do we source labelled ticket history for threshold calibration?
- Should the stage piece show real ticket text or synthetic?
- Which ticket scenario has the highest trust-beat drama: billing, churn, or security?
