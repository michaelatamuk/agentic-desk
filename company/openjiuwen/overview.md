# openJiuwen, explained simply

*As of 29 October 2026.*

openJiuwen is the company's agent platform and open-source community. It is the layer our own
projects build on.

- **Repositories:** agent-core (framework and runtime), JiuwenSwarm (the agent system), agent-dx (the
  distributed execution substrate), plus studio, memory, tools and protocol repositories under
  [openJiuwen-ai](https://github.com/openJiuwen-ai).
- **Who owns it:** the company and its community. Our team contributes to it; we do not own the
  product or its roadmap.
- **What we do in it:** file issues, write design proposals, review and merge upstream changes, and
  build LAIX, Cortex, Max and Channels on top of it. Our issues and designs are recorded in
  [`projects/openjiuwen/`](../../projects/openjiuwen/README.md), not here.
- **Release notes:** [`whats-new/`](whats-new/) records what changed in the platform since August
  2026, studied after each pull. That is product history, not our contribution log.
- **Code studies:** [`notes/`](notes/) explains how the platform works inside, one folder per
  subsystem. That is product knowledge, not our contribution log.
- **Why it matters to this folder:** it is the platform behind our projects, and the default backend
  for company siblings such as ScienceDiscovery. DigitalMate is the exception: it currently runs on
  Orbit, with a plan to move onto JiuwenSwarm.

The boundary is: **the product's home is the company; our contribution's home is `projects/`**.
