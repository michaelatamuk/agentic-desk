# LAIX technical deck — speaker notes

Open `technical.html` in Chrome or Edge. No server or network is required.

Keyboard: `←` / `→` or space, `N` for notes, `F` for full screen, `Home` / `End`.

## 30-minute builder run

| Time | Slide | What to say |
|---:|---|---|
| 0:00–0:02 | 1 | One decision layer, two surfaces |
| 0:02–0:08 | 2–3 | Core, app kit, host; the actual package map |
| 0:08–0:13 | 4–5 | What core owns; what app kit adds |
| 0:13–0:19 | 6–8 | Request shapes, flow, decision contract |
| 0:19–0:24 | 9–10 | Policies and the StudyRoom integration |
| 0:24–0:28 | 11–13 | Live Context, runtime/records, outcome/bench |
| 0:28–0:30 | 14–16 | Parity, extension points, close |

## The talk track

### 1. The boundary

> “LAIX is not a model, a memory store or an agent framework. It is the decision layer. Core owns the decision substance. App kit owns the integration plumbing. The host owns the world.”

> “PPMA is a host service. It owns memory, consent and audit. The host passes only authorized generic context to LAIX. LAIX never calls PPMA.”

This is visible on slides 2 and 7, not only in the speaker notes.

### 2. Core

> “Core has contracts, request and decision shapes, action and attention policies, eight additional policy packs, outcome learning, evaluation, perception contracts and resource admission. It imports only core.”

### 3. App kit

> “App kit is optional and frozen. It adds Layer, runtime, execution, records, delivery, platform, the live-context loop and the bench. It imports core; core never imports app kit.”

> “Optional means not required, not absent from the path. A host can call core directly. If it uses Layer, it is choosing the app-kit convenience path. Layer is not a required extra layer between core and the host.”

### 4. Request shapes

> “Layer understands two request shapes. Attention is signals plus context. Action is situation plus options. A custom policy reads request attributes. All ten decision classes return the same Decision.”

### 5. The contract

> "The host sends a DecisionRequest; LAIX returns the Decision. The decision is the answer, not the input. A score ranks inside one policy. Confidence is not a probability unless calibrated says so. The decision carries alternatives and constraints, which is what makes it explainable and auditable."

### 6. Policies

> “One active policy at a time. The built-in attention and action policies are selected by request shape. Eight more packs are explicit. A domain policy is a class with a name, a version and decide(request).”

### 7. StudyRoom

> “StudyRoom uses core contracts, Layer, a custom learning policy, and records/outcomes. It does not yet use Live Context, Platform or outcome learning. That is deliberate: Phase 0 proves the decision boundary before the media and provider stack.”

### 8. Live Context

> “The host supplies detectors and events. Cheap detectors run always. Deep detectors run only when uncertainty, gain, cost and latency justify them. The frame records what ran, what was skipped and why.”

### 9. Records and runtime

> “The decision is not the end. The host executes, records and reports an outcome. The record lifecycle is explicit: draft, approved, executed, undone or rejected. The host owns the database and media.”

### 10. Outcome and bench

> “Outcome learning is bounded counting, not model training. LAIX-Bench is ten suites and twenty-five cases across Python and TypeScript. Add a bench case before changing a policy.”

### 11. Parity and packaging

> “Python is primary. TypeScript mirrors the same core and app-kit folders. Shared contracts and test vectors keep them aligned. Hosts pin a tag and keep host translation local.”

### 12. Extension

> “Do not fork LAIX. Replace a policy, detector, execution integration, store or delivery port. The first integration is one host path, one policy, one decision record and one outcome.”

## Questions builders will ask

**Is LAIX a decision engine or a model?**  
It is a decision layer. It can host a policy backed by a model, but the contract and the record are independent of the model. The packaged policies are deterministic starting points.

**Why not put this inside PPMA?**  
PPMA owns memory, identity, consent and audit. LAIX is domain-neutral and reusable across hosts. PPMA can call it without owning it.

**Why a custom policy in StudyRoom?**  
The learning rules are domain rules. They belong in the host. LAIX owns the decision shape, confidence, alternatives, approval and record.

**How do we test a policy?**  
Unit tests for the rule, a bench case with expected verb/reason/action/approval, and a parity run in Python and TypeScript. Add the case before changing behaviour.

**How do we roll it out?**  
Add the host integration behind a flag. Run the old and new paths in shadow mode. Record both decisions. Compare verb, reason, approval and delivery. Move traffic after a quiet period.

**What happens when LAIX is unavailable?**  
The host waits and alerts. It does not silently switch to a second decision engine. Consent failures fail closed.

**How does it scale?**  
The package is stateless at the decision boundary. State and outcomes are host-owned stores. The app kit provides contracts and in-memory implementations; production stores are the host's job.

**What is not built?**  
No autonomous action. No memory in LAIX. No model training in the packaged packs. The learned decision-engine core is roadmap. StudyRoom Phase 0 does not yet use Live Context or Platform.

## Optional live technical proof

If you want one live moment, use one of these:

1. **Decision shape**: show a `Decision` from StudyRoom with `verb`, `action_id`, `alternatives`, `constraints_applied`, `confidence_source` and `requires_approval`.
2. **Bench**: run `python -m laix.appkit.bench --suite safety` and show 25/25 or the suite result.
3. **Isolation**: show that the host integration is the only path importing LAIX in the app; show no local LAIX copy.

Do not turn the technical session into a test suite tour. Use one artifact, then return to the architecture.

## Honest limitations

- The packaged policies are deterministic defaults, not trained models.
- Scores are policy-relative, not probabilities.
- Outcome learning is bounded counting.
- The host owns memory, media and permissions.
- StudyRoom Phase 0 is a decision proof, not a full classroom product.
- StudyRoom's current outcome attribution should attach to the intervention, not the final verify. Say this if asked; do not hide it.
