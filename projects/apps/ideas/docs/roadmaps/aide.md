# Aide — Roadmap

Legend: `[x]` done · `[ ]` planned · **(S)** small · **(M)** medium · **(L)** large.
"On-device" means email and calendar content never leaves the user's machine.
"LAIX" means the LAIX decision layer orchestrates attention allocation.

**Status.** Stage spec written. Product not built.

**One line.** Aide decides what needs you now, what it can handle, and what can wait — with a
reason every time.

**Buyer.** Knowledge worker / engineering manager (primary user), team lead (budget), IT /
productivity team (enterprise buyer).

**Best first industries.** Technology · consulting · legal · financial services.

**The sentence the audience repeats:** *"Your inbox, with a reason for everything."*

Read first: [The Stage Playbook](../stage-playbook.md). This roadmap follows its 10 criteria,
90-second arc and acceptance tests.

---

## Phase 0A — The 90-second inbox moment

Goal: a stage piece that makes any knowledge worker feel the relief immediately. Time: 2 weeks to
build, 1 week to rehearse. No real email integration, no live model calls, no network.

**Set.** A large screen showing a clean inbox: 20 emails, most grey (`wait`), a few with coloured
badges. A quiet-hours indicator glows in the corner. The presenter has a clicker.

**The verb.** Activate quiet hours; watch the inbox settle. Then one critical email arrives and
overrides it.

**The cold open.** The inbox is busy. 20 emails. The presenter says: *"You're in a meeting. One
email matters. Which one?"* The inbox is a wall of equal-priority noise.

**The turn.** The presenter activates quiet hours. Most emails grey out and move to a suppressed
pile. Four remain: one `act` (green — Aide has drafted a reply), one `ask` (amber — it sent a
clarifying question), one `guide` (blue — needs the presenter's decision), one `escalate` (red —
deadline today, critical sender). The audience sees the inbox transform from noise to signal in
one gesture.

Then the escalation play: Aide drafted an auto-reply for the `guide` item. The presenter rejects
it — *"this person needs a personal response."* Aide re-ranks: `guide — draft with context for
your review`. *"It was confident. It was wrong. This is why you stay in charge."*

### Beat sheet

| Time | Beat | Action | Screen |
|---|---|---|---|
| 0:00–0:10 | Cold open | Presenter shows noisy inbox — 20 equal-priority emails | Full inbox, all grey |
| 0:10–0:20 | Quiet hours | Presenter activates quiet hours | 16 emails fade, 4 remain with badges |
| 0:20–0:35 | Signal | Presenter walks through 4 remaining emails: act / ask / guide / escalate | Badge tour, one reason card per badge |
| 0:35–0:50 | Override | New email arrives during quiet hours: confidence 0.96, deadline today | Quiet hours overridden, email surfaces red |
| 0:50–1:05 | Trust beat | Aide's `act` draft is rejected; re-ranked to `guide` | Draft panel, rejection, new badge |
| 1:05–1:20 | Audit | Presenter shows audit log: every decision has a reason | Scrollable log |
| 1:20–1:30 | The line | Closing line; QR to demo; reset | Clean inbox, badges visible |

### The trust beat, in detail

- Aide drafts an auto-reply for an email flagged `guide`. It is a reasonable guess: the email
  has a clear question and a known sender.
- The presenter rejects it for a visible reason: *"this person is a key customer — a template
  will insult them."*
- Aide re-ranks in the same scene: `guide — draft personalised reply for your review`.
- The presenter says one sentence: *"It was confident. It was wrong. This is why you stay in
  charge."*
- The correction is recorded. Sender tier is now a stronger feature for this email category.

### Audience agency

The room chooses which email the presenter reviews next:

- **A — a calendar conflict with three attendees.**
- **B — a budget approval request with a deadline.**

Either works. A shows `ask — propose two alternative times`. B shows `guide — approval needs you,
here is the context`. The presenter commits to the room's choice.

### Props and stagecraft

- A minimal, calm inbox design (white, light grey suppressed pile, four vivid badge colours).
- A quiet-hours toggle button the audience can see.
- A subtle chime when an email overrides quiet hours.
- The reason card appears as a tooltip on badge hover, stays visible on click.
- The audit log is always visible in a side rail — it grows as decisions are made.
- Reset: `R`, under five seconds, back to the noisy inbox.

### Phase 0A checklist

- [ ] Inbox view with 20 pre-loaded emails and LAIX badges **(M)**
- [ ] Quiet-hours toggle wired to LAIX attention policy **(M)**
- [ ] Suppression animation: emails fade to grey pile **(M)**
- [ ] Quiet-hours override: new email arrives, surfaces red **(M)**
- [ ] Reason card on click: confidence, evidence, verb **(S)**
- [ ] Trust beat: draft shown, rejected, re-ranked **(M)**
- [ ] Audit log side rail **(S)**
- [ ] Audience choice: two email types, either path works **(S)**
- [ ] 90-second script, word-for-word for the first 20 seconds **(S)**
- [ ] Stage mode: deterministic run, reset under five seconds **(S)**
- [ ] 90-second fallback recording and a backup laptop **(S)**
- [ ] Contrast and type test at 10 metres **(S)**
- [ ] Three full rehearsals, one with a hostile audience, one with no network **(S)**

**Do not build for 0A:** login, real email integration, calendar, Slack, model training,
preference settings, multi-user.

---

## Phase 0B — The functional demo

Goal: the booth version that answers "is this real?" after the stage piece. Same story, synthetic
email data, deterministic and offline.

Time: 4 weeks after 0A.

- [ ] Synthetic email pack: 50 emails across 8 signal types, varied senders and deadlines **(S)**
- [ ] Synthetic sender profile store: tier, history, relationship flag **(S)**
- [ ] LAIX integration: real `DecisionRequest` objects with Signal contract **(M)**
- [ ] Attention policy: quiet hours, cost-of-waiting, severity gate **(M)**
- [ ] Quiet-hours override: configurable severity threshold **(M)**
- [ ] Full scoring breakdown on click: signals, weights, policy, winner **(M)**
- [ ] Trust beat replay: viewer can step through the re-ranking **(M)**
- [ ] Audit log: scrollable, filterable by verb **(M)**
- [ ] Booth mode: reset, scenario picker, 3-minute run **(S)**
- [ ] Runs fully offline on one laptop **(S)**

### Demo architecture

- Fixed seed. Every run is identical.
- All LAIX calls are real library calls — this is the honest demo of the library.
- Precomputed email stream; no external API calls on stage.
- The quiet-hours toggle calls LAIX live and re-evaluates the full inbox.
- A visible "powered by LAIX" provenance panel for Q&A.

### Stage acceptance criteria

- [ ] Five strangers: at least four can explain the product in one sentence.
- [ ] First touch within 15 seconds without instruction.
- [ ] Quiet-hours transformation is clear by 20 seconds.
- [ ] The full arc runs in 90 seconds with the trust beat.
- [ ] Reset under five seconds.
- [ ] Two volunteers complete the toggle-and-review interaction unassisted.
- [ ] Runs with the network cable unplugged.
- [ ] Seven of ten viewers can repeat the closing line.

### Demo metrics

- Time to first touch: ≤ 15 s.
- Time to quiet-hours reveal: ≤ 20 s.
- Full run: ≤ 90 s.
- Volunteer success: ≥ 80%.
- Qualified conversations at the event: ≥ 10.
- LAIX library adoption inquiries: ≥ 5.

### Post-stage motion

- QR code to the LAIX repository or documentation.
- One-page "How LAIX attention policy works" explainer.
- A 10-minute booth walkthrough of the signal scoring model.
- Follow-up within 48 hours with the recording and the explainer.

---

## Phase 1 — First integration

Goal: one real user, Gmail read-only, email only, suggestion-only mode, 14 days.
User confirms every suggestion before it fires. No auto-send.

**Gate:** do not start the integration until the stage piece has passed all acceptance tests.

### 1.1 Email connector

- [ ] Gmail OAuth read-only scope **(M)**
- [ ] Email signal extractor: sender tier, subject urgency words, deadline mentions,
  question detection, reply-chain position **(M)**
- [ ] Signal normaliser: map to LAIX Signal contract (severity, confidence, due) **(M)**
- [ ] Quiet-hours configuration per user **(S)**

### 1.2 LAIX decision layer

- [ ] Email → `DecisionRequest` adapter **(M)**
- [ ] Attention policy: quiet hours, cost-of-waiting, severity gate **(M)**
- [ ] Action library: 8 standard responses (reply now, draft, defer, ignore, ask, forward,
  flag, escalate) with cost and disruption scores **(M)**
- [ ] Quiet-hours override threshold per severity level **(S)**
- [ ] LAIX policy pack: attention + preference elicitation **(S)**
- [ ] Plain-English reason rendered for each decision **(M)**

### 1.3 User workflow

- [ ] Inbox view with LAIX badge per email **(M)**
- [ ] Click-through to full scoring breakdown **(S)**
- [ ] Confirm / override / dismiss interaction **(S)**
- [ ] Draft preview before any auto-send **(M)**
- [ ] Correction captured: dismissed suggestion + user's actual action **(S)**
- [ ] Append-only decision log with timestamp, signal snapshot, model version **(S)**

### 1.4 Pilot measurement

- [ ] Baseline: log current inbox triage time before go-live **(S)**
- [ ] Pilot dashboard: emails triaged, suggestions accepted, time saved **(M)**
- [ ] After 14 days: top 5 threshold adjustments surfaced for user review **(M)**
- [ ] Correction feedback loop → outcome learning **(M)**

### 1.5 Deployment

- [ ] Browser extension or desktop app **(M)**
- [ ] All email content processed on-device; no content sent to external servers **(M)**
- [ ] Offline mode: decisions still run if internet is down **(S)**

---

## Phase 2 — Production

Goal: calendar and Slack integration, team plan, auto-send for confirmed patterns.

- [ ] Google Calendar reader: meeting context added to email scoring **(M)**
- [ ] Slack message reader (read-only, DMs and mentions only) **(M)**
- [ ] Auto-send enabled for patterns the user has confirmed 10+ times **(M)**
- [ ] Team plan: shared quiet-hours policy, attention budget visible to team lead **(M)**
- [ ] Per-seat monthly subscription billing **(M)**

---

## Phase 3 — Scale

Goal: multiple integrations, enterprise plan, LAIX adoption programme.

- [ ] Outlook / Microsoft 365 connector **(L)**
- [ ] Slack, Teams write access (send drafts for confirmation) **(L)**
- [ ] Enterprise plan: SSO, audit export, data residency, no content leaving org **(L)**
- [ ] Outcome learning: anonymised threshold benchmarks across users, opt-in **(L)**
- [ ] LAIX SDK integration guide for productivity tool vendors **(M)**

---

## Not planned (with reasons)

- **Auto-send without any confirmation** — wrong replies damage relationships; user always
  confirms new patterns.
- **Replacing email clients** — Aide sits above them.
- **Calendar management (booking, rescheduling)** — Phase 2 calendar reading only; writing
  is a later decision.
- **Full inbox AI assistant** — focus stays on the LAIX attention policy demo.
- **Dashboard-only demo** — dashboards are for pilots, not stages.

---

## Recommended order

1. **0A — the stage piece** (2 weeks). Build the inbox and quiet-hours toggle first. No real
   email needed.
2. **Rehearse and red-team** (1 week). Acceptance tests, fallback, venue test.
3. **Stage gate** — if the five-stranger test fails, do not book the next event.
4. **0B — the functional demo** (4 weeks) for the booth and LAIX Q&A.
5. **First integration** — one user, Gmail read-only, suggestion-only mode.
6. **1.1 email connector** before anything else in Phase 1.
7. **1.2 LAIX attention policy** — quiet hours and cost-of-waiting are the core demo.
8. **1.3 user workflow** — the inbox view and confirm flow are what the user sees.
9. **1.4 measurement** — baseline on day one.
10. **Phase 2** only after 14-day integration succeeds and second user signs on.

---

## Open decisions

- Which email client is the first integration target: Gmail or Outlook?
- What is the minimum permission scope needed for suggestion-only mode?
- How do we surface threshold calibration without overwhelming the user?
- Should the stage piece use real email text or synthetic?
- Which quiet-hours scenario has the highest audience moment: deadline override or
  sender-tier override?
