# Proactivity

## The ladder

1. **Notice** — detect a state.
2. **Predict** — say what will happen, with a horizon and a confidence.
3. **Act** — do it, then tell.
4. **Verify** — check the result with a second signal.
5. **Escalate** — call a human, a technician, or a family member.
6. **Coordinate** — talk to another company's agent.

A notification is level 1. A demo should reach levels 3 to 5.

## Three speed tiers

| Tier | Budget | Where | Examples |
|---|---|---|---|
| Reflex | < 100 ms | On device | Close a valve, cut a circuit, lock a window |
| Tactical | 1–5 s | Edge | Pause a cycle, pause an AC, ask for a second photo |
| Deliberate | seconds–minutes | Cloud | Rebuild an energy schedule, predict a failure, file a claim |

The tier decides the model: a small local classifier for reflex, a vision or audio model for
tactical, a reasoning model for deliberate.

## The rule for acting without asking

Act when **the cost of waiting exceeds the cost of being wrong**, and the action is reversible or
bounded:

- **Act:** close a valve, pause a cycle, cut one circuit, lock a window.
- **Ask, or require a second signal:** unlock a door, spend money, cancel a service, call an
  ambulance.

Two independent signals before any irreversible action. That is how the system gets speed without a
house that panics.

## Noticing means deviation, not thresholds

Not "temperature > 26". The agent learns the baseline for this home: the fridge cycles every 40
minutes, this person is in the kitchen at 07:10, the washer sounds like this. It reports deviation
from that baseline.

That is the difference between a rule engine and an agent, and it needs history — which is also what
the failure-to-fix graph stores.

## What to measure

- **Time to action** per tier.
- **False-action rate** — acted and should not have.
- **Missed-event rate** — stayed silent and should not have.
- **Undo rate** — how often the user reversed it.

A proactive agent is judged on the last three, not on how clever the detection sounds.

## Failure modes to design for

- **Alarm fatigue** — too many nudges; solved with an interruption budget, not a mute button.
- **Confident wrongness** — a prediction stated as fact; always carry a horizon and a confidence.
- **Feedback loops** — the agent acts, the action changes the baseline, the next detection is wrong.
- **Cold start** — no baseline in a new home; fall back to suggestion-only until history exists.
- **Stale memory** — a layout or appliance changed and the model still believes the old one.
