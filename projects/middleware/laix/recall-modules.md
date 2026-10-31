# RECALL → LAIX: extracted modules

**Status: draft, extracted from RECALL v1.7.0.** This is the first concrete code contribution from a
reference app into LAIX. It is deliberately small and UI-free.

## Two packages

| Package | Location | What it gives LAIX |
|---|---|---|
| `@laix/attention` | `recall/packages/laix-attention` | a timing policy: `wait / notify / ask / act / verify / escalate`, with quiet hours, interruption budget, feedback suppression and a small outcome learner |
| `@laix/decision-record` | `recall/packages/laix-decision-record` | what · why · evidence · approval · audit · undo, with a content fingerprint and JSON Schema |

Both are pure TypeScript. No React, no browser storage, no RECALL types, no PPMA memory.

## Why these two

LAIX already needs a **decision record** for Max (`projects/apps/max/architecture/laix.md`) and an
**interruption policy** for deciding which card is worth showing. RECALL implements both against a
real long-timescale, one-owner domain: meetings, promises, risks and questions.

| LAIX component | Module |
|---|---|
| Decision Engine / interruption policy | `@laix/attention` |
| Outcome Learning | `OutcomeLog` in `@laix/attention` |
| Decision record | `@laix/decision-record` |
| Grounding / safety gate | evidence refs + approval + audit in the record; not the execution safety layer |

## Contract

### Attention

```ts
decide(context, candidates, options) -> Decision[]
recordOutcome(decisionId, outcome) -> void
```

The score is inspectable:

```
severity + due urgency + confidence - interruption cost + learned adjustment
```

Defaults: notify at 48, ask at 72, escalate at 92. Critical items always reach a human. Quiet hours
and the interruption budget are hard constraints.

### Decision record

```
draft --approve--> approved --execute--> executed --undo--> undone
  |
  +--reject--> rejected
```

- at least one evidence ref with `id` and `quote` is required;
- only a draft can be approved or rejected;
- every transition appends an audit event and re-seals the fingerprint;
- `verifyRecord` detects tampering;
- the fingerprint is FNV-1a 64-bit, a **content fingerprint, not a signature**.

Schema: `recall/packages/laix-decision-record/schema/decision-record.schema.json`.

## How LAIX can take them

1. Copy the two package directories into the LAIX repository.
2. Keep the exported types and enums; they are the contract.
3. Replace `OutcomeLog` with the LAIX bandit behind `adjustment(kind)`.
4. Replace the fingerprint with a signed hash if the deployment needs signatures.
5. Move the contract tests with the packages; they do not import the app.
6. Delete the duplicate analysis from RECALL when LAIX/PPMA owns understanding.

## What LAIX still has to decide

- who owns the packages;
- whether LAIX or the platform owns experience state after a reconnect;
- the bandit and evaluation set for interruption precision;
- the signing/key story for the record;
- whether the record is LAIX-owned or app-owned with a LAIX schema.

## What this does not solve

RECALL still has its own transcript analysis. That duplicates PPMA/LAIX and should be removed once
the boundary is agreed. The packages are a clean extraction, not a full integration.

## References

- `recall/packages/laix-attention/README.md`
- `recall/packages/laix-decision-record/README.md`
- `recall/docs/laix-extraction.md`
- `recall/docs/intelligence.md`
