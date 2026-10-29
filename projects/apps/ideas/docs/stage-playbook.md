# The Stage Playbook — conference style 2026

This is the bar every demo must clear before it goes on a stage. It applies to all nine apps;
RootCause and GeoResponse are the first two rewritten against it.

The rule is simple: **a demo is not a tour of a product. It is the product's argument, performed in 90 seconds.**

## The four levels

| Level | What it is | The test |
|---|---|---|
| Productive app | Workflow, tables, panels, reports | Would a user do their job in it? |
| Cinematic skin | Dark theme, hero numbers, animated cards | Does it look like a launch video? |
| Playable demo | One verb, immediate consequence | Can a stranger touch it and cause something? |
| **Stage piece** | Playable + legible agent + human trust + audience + stagecraft | Does the room react without the presenter explaining? |

We build level 4. Level 2 is the trap: it looks modern and changes nothing.

## The 10 criteria

1. **One verb.** The presenter does one physical thing — drag a lens, scrub time, move a sun, paint a world. Not a click-through.
2. **No chrome.** No dashboards, no tables, no settings, no next buttons. If it belongs in a product, it does not belong on the stage.
3. **The agent is legible.** You can see it gathering, comparing, rejecting and re-ranking. A spinner, a progress bar or a typewriter is not enough.
4. **Immediate consequence.** Something visibly changes because of the interaction. The artifact is the interface.
5. **The trust beat.** The AI is wrong once. The human rejects it. The system responds. This is the most 2026 moment available.
6. **Audience agency.** The room makes one real decision. Two options, visible consequence, no voting app required.
7. **One metaphor.** Lens, flood, shadow, evidence web, wire. The audience remembers the metaphor, not the UI.
8. **Multimodal or physical.** A real part, a live frame, a map, a sensor, a voice. A screen-only demo is weaker than a screen plus an object.
9. **Stagecraft.** Sound, lighting, a 90-second script, a fallback video, a backup laptop, and a reset under five seconds.
10. **Legible in 10, wow by 30, complete by 90.** If those three numbers fail in rehearsal, the piece is not ready.

## The 90-second arc

| Time | Beat | What happens |
|---|---|---|
| 0:00–0:10 | Cold open | The artifact and the stakes. No title slide. |
| 0:10–0:25 | First touch | The presenter (or a volunteer) does the verb. |
| 0:25–0:45 | The machine works | The agent gathers, compares and shows its thinking. |
| 0:45–1:05 | The trust beat | The AI is wrong; the human corrects it; it re-ranks. |
| 1:05–1:20 | The reveal | The cause / the decision / the consequence. |
| 1:20–1:30 | The line | One sentence the audience can repeat, then reset. |

Cut anything that is not one of these beats.

## The trust beat

A perfect AI is not credible. A corrected AI is.

- The first answer must be **plausible but wrong**.
- The human must reject it for a reason the audience can see (tool mark vs. porosity; dark roof vs. flood damage).
- The system must respond in the same scene: evidence re-weights, ranking changes, the map or case updates.
- The presenter says one sentence: “It was confident. It was wrong. This is why the human stays.”

This one beat does more for trust than any accuracy number.

## Audience agency

- One decision, two options, both defensible.
- The room votes by voice or hands; the presenter commits.
- The consequence appears in under five seconds.
- Never ask the audience to fill a form, scan a QR to vote, or wait for a backend.

## Demo architecture

- **Deterministic:** fixed seed, precomputed outputs, no live model training.
- **Offline:** all images, tiles, data and fonts local. No conference Wi-Fi.
- **Reset:** one key, under five seconds, returns to the cold open.
- **Fallback:** a 90-second recording of the same run, on the same laptop, plus a second laptop.
- **Readable:** 16:9 and 4:3 safe zones, 96 px hero type, high contrast, tested at 10 metres.
- **Fast:** every interaction responds in under 100 ms; no loading state on stage.
- **Recoverable:** if a step fails, the presenter can skip to the next beat without restarting.

## Acceptance tests

Run these before the conference, not at the conference.

- [ ] Five strangers watch once; at least four can explain the product in one sentence.
- [ ] A first-timer touches the demo within 15 seconds without instruction.
- [ ] The wow moment lands by 30 seconds.
- [ ] The full arc runs in 90 seconds, with the trust beat included.
- [ ] Reset finishes in under five seconds.
- [ ] Two volunteers complete the interaction without help.
- [ ] The demo runs with the network cable unplugged.
- [ ] The projector and the room audio are tested at the venue.
- [ ] Seven of ten people in a post-run test can repeat the closing line.
- [ ] The presenter can run it three times back-to-back without drift.

## Stagecraft

- **Script:** word-for-word for the first 20 seconds, beat cues after that.
- **Sound:** one cue for the reveal, one for the trust beat; no music under the explanation.
- **Lighting:** the physical object gets a spot; the screen is not the only light source.
- **Props:** the real part, a printed report, a stamp, a map print — something the audience can see is real.
- **Operator:** one person runs the laptop; the presenter never touches the trackpad.
- **Rehearsal:** three full runs, one with a hostile audience, one with no sound, one with a dead network.
- **Q&A:** have the provenance sheet ready — data source, model, date, what is simulated.

## Data rights

Public conference demos need commercial-safe rights.

- **MVTec AD** is **CC BY-NC-SA 4.0** — non-commercial. Do not use it in a paid or commercial conference demo without checking terms. Use a licensed or synthetic defect set for the stage.
- **Copernicus Sentinel** data is free and open; attribution is required.
- **Copernicus EMS** maps have their own terms; check before using the maps themselves as the hero visual.
- **OpenStreetMap** is ODbL; display “© OpenStreetMap contributors”.
- Keep a **provenance sheet** for every asset: source, licence, date, whether it is real or synthetic.

## Post-stage motion

Applause is not a pipeline. Plan the next 48 hours.

- QR code to the playable demo, not to a signup form.
- One-page “pilot in 90 days” offer on the booth table.
- A 10-minute booth version of the same 90-second piece.
- Capture 20 named quality/claims leaders, not badge scans.
- Follow-up within 48 hours with the recording and the one-pager.
- Track: qualified conversations, pilot intros, demo replays.

## Red team

| Failure | Mitigation |
|---|---|
| Venue Wi-Fi dies | Offline build; no network calls. |
| Model gives a different answer | Precomputed run; deterministic seed. |
| Projector washes out the palette | Test at venue; high contrast; large type. |
| Laptop dies | Backup laptop + recorded fallback. |
| Volunteer freezes | Two guided options; presenter can take over. |
| Running over time | Cut the middle, keep the trust beat and the line. |
| “Is this real?” | Show the provenance sheet and the evidence chain. |
| Licensing challenge | Commercial-safe assets; attribution on screen. |

## What not to build for the stage

Login · settings · navigation · user management · billing · full export formats · model-training UI ·
dashboards · multi-user · chat · notifications · onboarding.

Those are product features. They belong in Phase 1 or later.

## Using this for the other seven apps

Each app needs one verb, one wrong answer, one audience choice and one repeatable line. If a concept
cannot produce those four things, it is a product, not a stage piece.
