# Demo lab

The demo is a lab bench for algorithms, wearing a smart home interface.

```
scenario simulator ──▶ event stream ──▶ agent
   (or your own photo/audio)             perceive → state → predict → decide → act (mock)
                                              │
                                    decision card, why, confidence,
                                    alternatives, counterfactual
                                              │
                                    Lab: inject, replay, score
```

Three properties make it a demo of algorithms rather than a mock-up: **you can inject any scenario**,
**you can see the reasoning**, and **you can score it**.

## Screens of the demo

- **Decision card** — what, why, evidence, confidence, time to decide.
- **Why panel** — signals used, alternatives rejected, cost comparison.
- **Counterfactual** — "if I had waited 10 minutes, expected cost +€40".
- **Timeline** — scrub back through a scenario and watch the decision change as evidence arrives.
- **Lab** — pick a scenario from a menu or upload a file.
- **Scorecard** — run the evaluation set live: precision, false-alarm rate, missed-event rate, time to
  decision.
- **Case file** — the full trace of one event, exportable.

## Algorithms on show

1. Multimodal identification — model plate or error display to device, model, fault.
2. Acoustic fault classification — imbalance, bearing, pump cavitation from a phone recording.
3. Time-series anomaly — duty-cycle drift from a synthetic energy stream.
4. Baseline learning — the same house with learning off, then on.
5. Prediction with a horizon — "seal failure in ~9 days, 78%".
6. Decision under uncertainty — wait / ask / act from expected cost.
7. Constraint planning — tariff and weather in, a schedule and a saving out.
8. Retrieval with enforced citation — invented sources dropped on screen.
9. Safety gate — a gas smell withholds the step.
10. Outcome learning — the graph improving as cases accumulate.

## The five-minute run

1. **Minute 1** — Today shows three cards. Ask why on one.
2. **Minute 2** — Upload a washer recording; diagnosis, prediction, one step.
3. **Minute 3** — Replay the fridge energy stream; watch the seal prediction appear days early.
4. **Minute 4** — Tariff spike: schedule rebuilt, saving shown.
5. **Minute 5** — Gas smell and a bad photo: the agent refuses, and asks instead of guessing. Then
   the scorecard.

## Assets we already have

- 22 sourced guides (11 build, 11 fix) with a source registry and licences.
- 83 evaluation cases across identification, guide tasks, troubleshooting, replanning, photo
  verification and safety.
- Safety rules and a citation check enforced in code.
- A simulated household with three appliances.

## What to cut

Valves, locks, robots, real device integrations, continuous cameras. None is needed, and each invites
questions the demo cannot answer.
