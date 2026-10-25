# Scenarios

Every scenario passes three tests: **no user input**, **a prediction the agent formed itself**, and
**an action within a stated time**. Nothing here needs hardware; signals are synthetic, uploaded, or
public.

Each action is a software action: notify, create a case, order a part, schedule, change a simulated
setting, escalate, or ask one question.

## Reflex — under 100 ms, on device

| Scenario | Signal | Prediction | Action |
|---|---|---|---|
| Tap left running | Simulated flow after the cycle ended | Burst or stuck inlet | Close the simulated valve, cut the circuit, notify |
| Stove unattended | Stove power + no presence for 4 minutes | Someone left the kitchen | Turn the hob off, send a clip |
| Window and child | Window sensor + pose in frame | Immediate risk | Lock the window, voice prompt in the room |

## Tactical — 1 to 5 seconds

| Scenario | Signal | Prediction | Action |
|---|---|---|---|
| Washer thumping | 10-second audio upload | Imbalance vs worn bearing vs pump | Pause the cycle, one instruction, request a second clip |
| AC with a window open | Window state + AC draw | Wasted energy | Pause the AC, say why |
| Fridge seal failing | Energy duty cycle over days | Seal failure in ~9 days, 78% | Ask for a photo of the seal, order the part |
| Fall in the next room | Impact sound + no motion for 60 s | Possible fall | Call the room speaker, then the phone, then family |
| Smoke alarm plus shower | Alarm audio + running water | Steam, not fire | Silence the alarm if allowed, start extraction, no fire call |

## Deliberate — seconds to minutes

| Scenario | Signal | Prediction | Action |
|---|---|---|---|
| Tariff spike | Price feed + load | Cost will rise 3× in 20 minutes | Rebuild the schedule, show the saving in money |
| Trip in the calendar | Calendar + device history | Empty house for 6 days | Run a pre-departure check, fix what it can, leave a report |
| Warranty about to lapse | Purchase date + logged fault | Claim lost in 30 days | Draft the claim with the fault history |

## Scenarios that show the algorithms, not the home

- **Error display photo** — device, model, manual page, one verified step. Vision plus retrieval.
- **Ambiguous photo** — Max says what it cannot see and asks for a second shot. Uncertainty as a
  feature.
- **Invented citation** — the model cites a page it never read; the app deletes it on screen. The
  trust layer, made visible.
- **Gas smell in text** — the step is withheld and escalation is shown. The safety gate, made visible.
- **Same house, twice** — run the energy stream with baseline learning off, then on. False alarms
  drop. The learning, made visible.

## The five to demo

1. Washer thumping — audio, diagnosis, predicted failure, next step.
2. Fridge seal — a slow drift, a prediction days early, a part ordered.
3. Tariff spike — a schedule rebuilt, savings in money.
4. Ambiguous photo — the agent asks instead of guessing.
5. Gas smell — the agent refuses to give a DIY step.

## Privacy rule

Prefer sensors, sound and power data over cameras. Camera only with explicit consent, processed
locally where possible, never continuous. The scenarios that survive regulation are the ones that run
on a vibration trace and a microphone.
