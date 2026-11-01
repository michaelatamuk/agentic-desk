# LAIX at a glance

## The one sentence

**LAIX is the decision layer between what an app senses and what it does.**

It answers: **Given this situation, what should happen next?**

It returns one of seven answers:

```text
wait   observe   guide   ask   act   verify   escalate
```

## The decision receipt

| | |
|---|---|
| **Situation** | What the app believes, with evidence and uncertainty |
| **Options** | What could happen next |
| **Constraints** | Consent, privacy, time, risk, approval |
| **Choice** | One verb, one action |
| **Confidence** | Where it came from, calibrated or not |
| **Approval** | Who must agree |
| **Alternatives** | What lost and why |
| **Record** | What happened, who approved, what changed |

## For managers

**What changes**

- The room waits when evidence is weak.
- Help follows one policy, not the loudest voice.
- Peer help needs consent.
- Every intervention has a record.
- One decision layer is reused across apps.

**What to prove in a pilot**

- Time from struggle to help.
- Interventions avoided below the line.
- Teacher time saved.
- False positives.
- Consent coverage.
- No privacy incident.

**The ask**

One class, one subject, 90 days. Shadow mode first.

## For PPMA builders

**The boundary**

| Concern | Owner |
|---|---|
| Profiles, memory, consent, audit | **PPMA** |
| Room, exercises, media, UI | Host |
| Wording, voice, delivery | Digital Mate |
| Tools, retries, execution | JiuwenSwarm / host |
| Live situation, options, decision, record | **LAIX** |

**The integration**

```text
host event
  → PPMA authorized context
  → adapter: Situation + DecisionRequest
  → LAIX: Decision
  → host: consent / approval / execution
  → decision record + outcome
```

**The rule**

> LAIX never calls PPMA. The host adapter connects them.

## The line

> **“It knew when not to interrupt.”**

## The closing line

> **“LAIX does not make the app smarter. It makes the app accountable for what it does next.”**
