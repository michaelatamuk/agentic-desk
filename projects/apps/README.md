# apps

Apps we build on top of an agentic platform. The platform is a black box here: the app may use the
interface in `contract.md` and nothing else. That is what allows the same app to move to a different
platform without a rewrite.

| Path | Contents |
|---|---|
| `pitch.md` | The short pitch for the apps platform |
| `building-blocks.md` | The pieces every agentic app needs |
| `stack.md` | What we build on top of the platform |
| `contract.md` | The only platform interface an app may rely on |
| `multimodal-agent-apps.pptx` | Portfolio deck |
| `ideas/` | Concepts, not yet built |
| `builds/` | One build specification per app |
| `publishing/` | How an app gets published and distributed |

## The black-box rule

No document in this folder may depend on an internal of the platform underneath. If a sentence only
makes sense because of how openjiuwen works inside, it belongs in `projects/openjiuwen/`, not here.

Naming the current implementation is allowed in one place: a short *Current implementation* note at
the end of a build specification, saying which platform the app runs on today. Anything beyond that
note is a portability bug.

## Pipeline

An idea moves through three stages, and the file moves with it:

1. `ideas/` — the concept: what it does, who wants it, why it is worth two days.
2. `builds/` — the specification: structure, data, agent behaviour, failure modes.
3. Published — the app leaves this repository and gets a code repository of its own. What stays here
   is the narrative and the deck.
