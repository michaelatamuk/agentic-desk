# Build plan

Five weeks, four demos. One FastAPI app: Home Manager is the shell, FixBot is the agent behind it.

| Week | Build | Show | Done when |
|---|---|---|---|
| 1 | **One app.** Merge the two services: Home Manager keeps auth, households, devices and SQLite; FixBot becomes a service behind one route. Today screen with three cards, device detail. | Log in → home → device → "something is wrong" opens Max | One process, one database, one login |
| 2 | **The repair case.** Photo or audio upload → agent turn → one step → outcome buttons: fixed / not fixed / escalated. Store model, causes, step, outcome. | Washer display photo → diagnosis → one step → "fixed" recorded | A complete case is stored and visible in Care |
| 3 | **The Lab tab.** Three injectable scenarios, a replay timeline, the why panel, and a scorecard over the 83 evaluation cases. | Inject a bad photo, watch Max ask for a better one; run the scorecard | A visitor can inject a scenario and see a score |
| 4 | **One proactive card.** Synthetic energy drift → prediction with a horizon → simulated action → verification. Decision card with a counterfactual. | "Seal failing in about 9 days, part ordered" | An event happens with no user input |
| 5 | **Make it survive the room.** Reset button, cached model responses, offline fallback, the five-minute script, a recorded backup run. | The whole run, twice, back to back | Two clean runs with no network |

## What to reuse

- **`handy-home-manager`** — auth, households, roles, device registry, SQLite, capability profiles.
- **`handy` (FixBot)** — the agent, tools, citation check, safety gate, 22 sourced guides, 83 evaluation cases, photo preparation.

Do not rewrite either. The merge is a router, a session mapping and one shared device model.

## Rules

1. **Reuse, do not rewrite.** Home Manager is the shell and the state; FixBot is the reasoning.
2. **Capture outcomes from week 2.** Counts first. That data is the only asset that compounds.
3. **No models beyond counts.** Show rankings and percentages; a bandit comes after a thousand cases.
4. **Everything is simulated.** Actions change state in the app, never hardware.
5. **Every card answers three questions:** what happened, why, what can I do.

## Not yet

Voice, mobile, multi-home, scenes editor, energy market, agent-to-agent, fine-tuning, a real bandit,
real device integrations.

## The two numbers

- Photo to first step: **under 60 seconds**.
- A clean demo run: **no failed API key, no network dependency, two runs back to back**.
