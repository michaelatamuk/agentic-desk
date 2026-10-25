# Surfaces

## Screens

```
Max
├─ Today        what Max noticed, decided, or needs approved
├─ Home         rooms, devices, states — the control layer
├─ Care         appliances, manuals, warranties, cases, history
├─ Activity     every decision: why, evidence, who approved, undo
└─ Settings     people, permissions, autonomy levels, budgets
```

**Ask Max** is not a tab. It is the input on every screen: type, speak, or send a photo.

## Today

Three to five cards, never more. Each card answers three questions: what happened, why, and what can
I do. Examples:

- "AC will pre-cool at 17:00 — electricity is 40% cheaper after 18:00."
- "Washer filter due. Part €8, two-minute guide."
- "Max paused the vacuum because the patio door was open."
- "Fridge seal is degrading. Photograph it and I will confirm."

## Care

The repair bench, with a home around it:

- appliance list: model, install date, warranty, manual
- open cases: symptom → what Max thinks → one step at a time
- the record: what broke before, what fixed it, which part was replaced
- maintenance schedule generated from the manual, not from a generic list

## Activity

The trust surface. One line per decision: what, why, source, who approved, undo. Autonomy is only
acceptable if this screen exists.

## Settings

Authority, not preferences:

- autonomy per domain: observe / suggest / ask / act within limits
- budgets: money per month, energy per day, interruptions per day
- people: who may approve what
- privacy: what stays local, what may leave the device

## Decision domains

| Domain | What Max decides | Risk |
|---|---|---|
| Comfort | Climate, light, scenes | Low — may act alone |
| Energy | Shift load, cheap or green hours, battery | Low, measurable |
| Maintenance | Filters, service, warranty, parts | Low — propose, then act |
| Safety | Leaks, stove, doors, smoke | High — tell a human, never act silently |
| Repair | Diagnose, guide one step, order part, escalate | High — citations and confirmation |

## Content types

- **Nudge** — one line and one action.
- **Decision record** — what was done, why, evidence, undo.
- **Case** — a fault, its diagnosis, its steps, its outcome.
- **Report** — weekly digest, savings, home health.
- **Record entry** — install, repair, part, warranty, service.
- **Guide** — repair or build instructions, always with a source.

## v1

In: Today, Care, Activity, Ask Max with photo or audio, a minimal Home, authority settings, one
working repair case, one energy decision, one safety check, the Lab tab.

Out: scenes editor, chart-heavy dashboards, marketplace, video generation, social features, build
mode, multi-home.
