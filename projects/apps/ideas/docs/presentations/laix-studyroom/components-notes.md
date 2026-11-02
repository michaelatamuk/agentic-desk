# LAIX component atlas — speaker notes

Open `components.html` in Chrome or Edge.

Keyboard: `←` / `→` or space, `N` for notes, `F` for full screen.

Each component slide carries the same component map, with the current component highlighted. Use it to keep the layers and connections visible while you talk about one piece.

**The map changes by layer:** core pages show a core-only map. App-kit pages show core as the base with app-kit additions. Core pages never mention or show app kit.

## Format

21 slides:

- 1 title
- 1 orientation — host, core, app kit
- 16 component slides — one per component
- 1 Belief bridge — inside Decisions, not a separate component
- 1 Action bridge — inside Policies, not a separate component
- 1 close

**Do not present the 16 as one kind of thing.** They are:

- **2 definitions** — Contracts, Schema
- **7 decision-logic components** — Decisions, Policies, Attention, Outcome, Evaluation, Perception, Resources
- **7 integration components** — Layer, Runtime, Records, Delivery, Platform, Live Context, Bench

Contracts is code, but it is a type/schema definition you import, not a runtime component you implement.

At 3 minutes per component, the full atlas is about 50–55 minutes. For a 30-minute session, pick one track:

- **Decision track:** decisions, policies, attention, outcome, evaluation, perception, resources
- **Integration track:** Layer, runtime, records, delivery, platform, Live Context, bench
- **Definitions appendix:** Contracts, Schema
- **Accountability track:** decisions, records, outcomes, evaluation, bench

## The 16 components

| # | Component | One-line job |
|---:|---|---|
| 1 | Decisions | Request and decision shape |
| 2 | Policies | Built-in, packaged and custom rules |
| 3 | Attention | What deserves attention now |
| 4 | Outcome learning | What happened after the decision |
| 5 | Evaluation | Parity, cases and reports |
| 6 | Perception | Detector, detection and frame contracts |
| 7 | Resources | Which sensing/model call is worth making |
| 8 | Layer | The optional public entry point |
| 9 | Runtime | Observe, state, policy, execution, outcome |
| 10 | Records | What happened, who approved, undo |
| 11 | Delivery | Show, send or hold |
| 12 | Platform | Run skill, cancel, approve, state, events |
| 13 | Live Context | Cheap always; deep under budget |
| 14 | Bench | Ten suites, twenty-five cases |
| 15 | Contracts | Request, response and record shapes |
| 16 | Schema | Executable, versioned contracts |

**Action** is not one of the 16. It is an option record, a verb and a built-in policy inside Policies.

**Belief** is not one of the 16 either. It is a request record inside the Situation, defined on the bridge after Decisions.

## Talk track per component

### 1. Decisions

> “The host sends a DecisionRequest. LAIX returns a Decision. The request is the input; the decision is the answer. The answer has verb, action, score, confidence, alternatives, constraints, approval and audit. A score is policy-relative; confidence is not a probability unless calibrated says so.”

### Belief bridge / inside Decisions

> "Belief is not a 17th component. It is a request record: a proposition, a confidence and its evidence. The host puts beliefs into the Situation; a policy scores against them. A belief is what the host currently thinks, not proof — ‘learner may need help’ at 0.56 is a belief, not a fact. Perception later produces exactly this record."

### 2. Policies

> "A policy reads a request and returns a decision. Some policies are built in; eight packaged policies cover common decision classes; a custom policy carries the domain rules. One active policy at a time; the decision shape stays the same."

### Action bridge / inside Policies

> "Action is not a 17th component, and it is not the verb `act`. An Action is a candidate option: id, verb, name, benefit, risk, delay, cost, approval. The host offers a set of options; the built-in action policy selects one; the decision repeats the chosen verb and action_id. The other options become alternatives. `ActionOption(verb='ask')` becomes `Decision(verb='ask', action_id=...)`; `ActionOption(verb='act')` would produce a decision with verb act."

### 3. Attention

> “Attention answers a different question: does this deserve the user’s attention now? Severity, timing, quiet hours, dedupe and feedback. It is a decision class, not a notification setting.”

### 4. Outcome learning

> “A decision without an outcome is an opinion with a timestamp. The ledger and UCB add bounded priors. It is counting, not training. Attribution is the hard part.”

### 5. Evaluation

> “A policy change needs a fixture. Cases, rows, reports and field-level mismatches. The harness compares verb, reason, delivery, record and approval.”

### 6. Perception

> “The core defines what a detector sees. The host supplies the camera, STT or sensor. LAIX keeps the contract and the frame, not the model.”

### 7. Resources

> “Cheap detectors run always. Deep calls clear information gain, cost and latency budgets. The plan records what was skipped and why.”

### 8. Layer

> “One request in, one decision out. The host does not need to know which policy class runs behind it. That is the whole public surface.”

### 9. Runtime

> “The runtime wires the pieces: observe, state, policy, execution, outcome. Every decision gets a trace; every execution gets a receipt. The host still owns the task.”

### 10. Records

> “What happened, why, who approved, can it be undone. The lifecycle is explicit: draft, approved, executed, undone or rejected. A record that cannot be verified is not evidence.”

### 11. Delivery

> “A decision is not a delivery. LAIX can decide to guide now; the host decides which channel and whether it reaches the user.”

### 12. Platform

> “Platform is the execution seam: run a skill, cancel it, ask for approval, read state, return events. The host can wrap its own worker or openJiuwen. LAIX does not care which.”

### 13. Live Context

> “Cheap always. Deep only when it pays for itself. The host drives events; LAIX decides what to run and records what it skipped.”

### 14. Bench

> “Ten suites, twenty-five cases, Python and TypeScript. Add a case before changing behavior. Bench is the contract’s regression net.”

### 15. Contracts

> "Now that you have seen the practical pieces, these are the shared shapes underneath them. The request uses Situation, Action, Belief, Constraint, Goal and Observation; the response is Decision; the record is Outcome, Receipt and Trace. A contract is a definition, not a runtime component."

### 16. Schema

> “The schema is the contract’s executable form. It keeps Python, TypeScript and the host aligned. This is tooling, not a runtime service.”

## How to use the deck

- If the audience asks “what is in LAIX?”, show the title and close first, then jump.
- If the audience asks “how does it fit together?”, show the close map and then one or two component slides.
- If the audience is PPMA builders, start with decisions, policies, Layer, records and platform; point to Contracts and Schema when they ask about types.
- If the audience is evaluating perception, start with perception, resources and Live Context.
- If the audience is evaluating trust, start with decisions, records, outcomes and evaluation.

## Honest limitations

- The eight packaged policies are deterministic defaults.
- Scores are policy-relative, not probabilities.
- Outcome learning is bounded counting.
- LAIX does not own memory, media or task execution.
- StudyRoom Phase 0 uses core, Layer, a custom policy and records; it does not yet use Live Context or Platform.
- StudyRoom’s outcome attribution should attach to the intervention, not the final verify.

