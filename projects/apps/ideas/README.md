# Agentic App Lab

Nine app concepts, each with a **playable demo** you manipulate and a **productive studio** you work in.

**Live site:** <https://michaelatamuk.github.io/agentic-desk/>

All data, results and agents are simulated. No backend is required.

## Structure

```
ideas/
├── index.html          demo home (deployed as the site root)
├── start-demos.cmd     one-click local server + browser
├── play/               9 playable demos, one per app
├── studio/             9 productive studio demos, one per app
├── docs/
│   ├── concepts/       one-page concept note per app
│   ├── roadmaps/       phase-by-phase roadmaps
│   └── ideation/       wider idea lists
├── assets/             images and portfolio overview renders
├── tools/              render scripts
└── archive/            older prototypes, pitches and the app suite
```

File names are consistent across `play/`, `studio/` and `docs/concepts/`:

`rootcause` · `aifilm` · `georesponse` · `imaging` · `labloop` · `twin` · `synthetic` · `cyber` · `architecture`

## The nine apps

| App | Play verb | Play | Studio |
|---|---|---|---|
| RootCause | Inspect a failed part and reconstruct the cause | [play](play/rootcause.html) | [studio](studio/rootcause.html) |
| AI Film Studio | Compose and shoot a film frame | [play](play/aifilm.html) | [studio](studio/aifilm.html) |
| GeoResponse | Move time, assign teams, run the assessment | [play](play/georesponse.html) | [studio](studio/georesponse.html) |
| Imaging Assistant | Scroll a CT stack and compare a nodule over time | [play](play/imaging.html) | [studio](studio/imaging.html) |
| Lab Loop | Steer an experiment cloud toward the yield peak | [play](play/labloop.html) | [studio](studio/labloop.html) |
| Digital Twin | Balance a production line and remove the bottleneck | [play](play/twin.html) | [studio](studio/twin.html) |
| Synthetic World | Paint a generated world, then release the car | [play](play/synthetic.html) | [studio](studio/synthetic.html) |
| Cyber Range | Harden nodes and hold the core for 40 seconds | [play](play/cyber.html) | [studio](studio/cyber.html) |
| Architecture Studio | Drag the sun and watch the tower shade the plaza | [play](play/architecture.html) | [studio](studio/architecture.html) |

## Run locally

Double-click `start-demos.cmd`, or:

```powershell
cd projects/apps/ideas
py -m http.server 8765 --bind 127.0.0.1
```

Then open <http://127.0.0.1:8765/index.html> in Chrome or Edge.

## Deploy

GitHub Pages is built by `.github/workflows/pages.yml`, which publishes this folder as the site root on every push that touches it.

- Source: `main`
- Build: GitHub Actions
- Artifact: `projects/apps/ideas`

## Notes

- **Play** demos are self-contained HTML/CSS/JS with no external assets or network calls.
- **Studio** demos are the productive workbench versions. Most share a shell; Lab Loop is the deepest.
- **Docs** cover the buyer, problem, product loop, NPU role, business case and risks.
- **Archive** keeps earlier pitches, prototypes and the 9-app suite for reference only.
