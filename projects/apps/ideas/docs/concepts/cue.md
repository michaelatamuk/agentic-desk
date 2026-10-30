# CUE: the live show design studio

*Status: concept. No playable demo yet. Stage plan: [roadmap](../roadmaps/cue.md).*

**One line.** CUE designs the show before the lights go down — the stage, the looks, the video, the cues and the budget in one workspace.

**Buyer.** Production companies, touring artists, venues, festivals and brand-experience agencies.

**User.** Creative director, production designer, lighting designer, video designer, tour manager.

**The sentence the audience repeats.** *"The show is designed before the lights go down."*

## The problem

A live show is designed across a CAD file, a previz render, a lighting console file, a video server, a
cue sheet, a spreadsheet and a group chat. The creative idea and the technical plan live in different
places. The first time anyone sees the whole show is often the first rehearsal — or the first show.

CUE makes the show a single project: concept, stage, light, video, blocking, setlist, cue sheet and
cost, on one timeline.

## What CUE does

1. **Load the setlist.** Songs, timings, transitions, energy curve.
2. **Block the stage.** Set, risers, runway, screen positions, entrances.
3. **Design the looks.** Lighting states, colour, movement, blackouts.
4. **Design the video.** Content, mapping, transitions, camera moments.
5. **Block the performers.** Where the artist and dancers are at each beat.
6. **Scrub the timeline.** See and hear the show at any second.
7. **Check the consequences.** Sightlines, power, rigging, crew and cost.
8. **Export the cue sheet.** The technical score the venue team can run.

## The task families

| Task | What the designer does |
|---|---|
| Concept | Mood, references, narrative of the show |
| Stage | Set, risers, runway, sightlines |
| Light | Looks, cues, colour, movement |
| Video | Content, mapping, transitions |
| Choreography | Blocking, entrances, camera |
| Setlist | Timing, energy curve, transitions |
| Cue sheet | The technical score |
| Budget | Rig, crew, power, transport |

That is eight different jobs in one project. The next tour starts the cycle again.

## What the designer gets

- a **previz** of the show they can play, pause and scrub,
- a **cue sheet** for lighting, video and stage,
- a **rig and budget plan** with the cost of each look,
- **versions** for each venue, tour leg and rehearsal,
- a **record** of what changed, who approved it and why.

## Where the NPU fits — optional, not core

CUE is a GPU/CPU product: 3D previz, video playback and encoding are GPU work.

An NPU can help with local inference:

- look and video suggestions on an edge box,
- beat/stem analysis,
- pose and blocking from rehearsal footage,
- a local design assistant for unreleased artist content.

That is a privacy feature, not the product's reason to exist. CUE can run without an NPU.

## Why this is not a lighting console

- It does **not** run DMX or control the live show.
- It does **not** replace Vectorworks Spotlight, WYSIWYG, Capture, Depence², disguise, Notch or
  grandMA3. It is the design workspace above them and exchanges plans with them.
- It does **not** generate the music. It works with the artist's track.

## Who else is doing this

- **Depence², WYSIWYG, Capture, Realizzer** — previz and show design.
- **Vectorworks Spotlight** — drafting and documentation.
- **disguise, Notch, Resolume** — video and media.
- **grandMA3** — lighting control.

The incumbents are strong. CUE's wedge is not a better renderer. It is an **AI-native design layer
that connects concept, previz, cue sheet and budget**, and exports into the tools crews already use.

## Business model

- Per show and per seat for production companies and venues.
- Annual seats for touring production offices.
- Sponsorship and brand-experience projects.
- Setup/integration fee for previz and console exports.

Start with one production company and three shows, not with a whole festival.

## What to prove in a pilot

- Fewer previz iterations before approval.
- Fewer cue-sheet changes during rehearsal.
- Rig cost avoided by catching weight/power/glare problems early.
- Rehearsal time saved.
- Producers can see the cost of a creative decision in the same place as the look.

## Where to start

- Touring production companies with a slate of shows.
- Mid-size venues with a continuous calendar.
- Festivals with multiple stages.
- Brand experiences and product launches.

Not a single freelance designer between tours: the cadence is too episodic.

## The hard parts

- Integration with previz, CAD, video and console formats.
- Safety: rigging, power, lasers, sightlines. CUE advises; the crew decides.
- Music and artist rights: unreleased content is sensitive.
- Creative trust: designers do not want an AI that “designs the show.”
- The buyer is conservative and the show must not fail.

## Risks

- The incumbents add AI features faster than a new entrant adds previz depth.
- The product becomes a pretty renderer with no workflow moat.
- Venue and crew data are messy; every venue is different.
- AI-generated looks can feel generic; the designer must stay the author.
- Hardware and protocol integration is a long road.

## Smallest first version

For one tour and one venue:

1. Import a licensed track and a stage blockout.
2. Add three lighting looks and one video moment.
3. Scrub the show on a timeline.
4. See the rig and budget impact.
5. Export a cue sheet.
6. Let the designer approve or reject the AI's look.

No live console control. No full CAD. No music generation.

## The 90-second stage piece

A dark stage, one light, a song intro. The designer scrubs the track, drags a look onto the build and
sees the cost update. The AI proposes a spectacular 12-fixture look; it blinds the front row and exceeds
the rig's power, so the designer rejects it. A simpler six-fixture look lands harder. The room votes
between a light drop and a video drop; the show plays; the cue sheet prints.

*"The show is designed before the lights go down."*

Full beat sheet, trust beat and acceptance tests: [roadmap](../roadmaps/cue.md).

## Cadence: daily or episodic?

- **Freelance designer:** daily during pre-production, then idle between shows.
- **Production company / venue / tour:** daily across a slate of shows.
- **The daily user is the production office**, not only the creative.

CUE should be sold to the production company, not the freelance designer, if daily use is the goal.

The roadmap adds a **tour readiness** layer for that office: venue, rig, power, rights, asset and budget
risks before load-in. That is the daily return loop; the design workspace is the deep work.

## Open questions

- Which production company or venue is the first pilot?
- Which previz tool do we integrate first: Depence², Capture or WYSIWYG?
- Which console export matters first: grandMA3, disguise or Resolume?
- Does CUE render in its own engine or orchestrate existing previz?
- Is the buyer the production company, the venue or the artist's management?
- Which track is licensed for the public demo?
- Do we offer local/NPU inference for unreleased artist content?
