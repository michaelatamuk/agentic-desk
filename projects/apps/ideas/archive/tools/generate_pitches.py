from pathlib import Path
from string import Template

# Legacy generator for the original template pitches. Not used by the current site.
BASE = Path(__file__).parent
OUT = BASE.parent / "pitches"
OUT.mkdir(exist_ok=True)

APPS = [
    {
        "id": "geo",
        "name": "GeoResponse",
        "tag": "Geospatial",
        "accent": "#22d3ee",
        "headline": "The flood is moving.<br>The map is two days old.",
        "sub": "Satellite imagery arrives in minutes. The assessment takes days.",
        "metric": "2 days",
        "metric_label": "to assess 40 km2",
        "evidence_headline": "1,240 tiles. 18 places that matter.",
        "cards": [
            ("1,240", "image tiles", "checked on the NPU"),
            ("18", "priority sites", "ranked by risk and access"),
            ("96%", "detection", "on the reviewed sample"),
        ],
        "aha_headline": "The flood extent overlaps 18 priority sites.",
        "aha_text": "7 roads, 6 power assets and 5 populated blocks. Two false positives were removed before the map was sent.",
        "chips": ["42 min", "18 sites", "96% detection"],
        "outcome_headline": "42 minutes.",
        "outcome_sub": "The map and assessment are ready before the response teams arrive.",
        "outcomes": [("42 min", "to assess"), ("18", "priority sites"), ("2 days", "was the old cycle")],
        "quote": "We knew where to send the teams before the second coffee.",
        "quote_by": "Operations lead - flood response",
        "scenes": ["The problem", "The evidence", "The agent", "The outcome"],
    },
    {
        "id": "imaging",
        "name": "Imaging Assistant",
        "tag": "Medical imaging",
        "accent": "#a78bfa",
        "headline": "120 scans.<br>7 urgent findings.<br>One night shift.",
        "sub": "The queue grows. The radiologist is one person.",
        "metric": "4 h",
        "metric_label": "earlier for the urgent case",
        "evidence_headline": "The urgent case was buried at position 84.",
        "cards": [
            ("120", "studies triaged", "overnight queue"),
            ("7", "urgent flags", "with evidence"),
            ("1", "confirmed", "radiologist signed"),
        ],
        "aha_headline": "The AI read first. The doctor decided.",
        "aha_text": "The draft report had the finding, the prior study and the uncertainty. The radiologist confirmed it and signed.",
        "chips": ["25 min", "7 flags", "1 confirmed"],
        "outcome_headline": "Four hours earlier.",
        "outcome_sub": "The urgent case reached the doctor before the morning round.",
        "outcomes": [("25 min", "to urgent finding"), ("7", "flagged"), ("1", "confirmed")],
        "quote": "The urgent case reached the doctor four hours earlier.",
        "quote_by": "Radiologist - night shift",
        "scenes": ["The problem", "The evidence", "The agent", "The outcome"],
    },
    {
        "id": "lab",
        "name": "Lab Loop",
        "tag": "Autonomous lab",
        "accent": "#4ade80",
        "headline": "Six weeks per cycle.<br>We can do three days.",
        "sub": "A scientist designs a batch, waits, analyses and repeats.",
        "metric": "6 weeks",
        "metric_label": "per optimization cycle",
        "evidence_headline": "5,000 candidates scored while the lab slept.",
        "cards": [
            ("5,000", "candidates", "scored on the NPU"),
            ("+9.4%", "yield", "best batch"),
            ("3 days", "cycle", "was 6 weeks"),
        ],
        "aha_headline": "The next batch was ready in the morning.",
        "aha_text": "The agent proposed a batch, the NPU scored it, and the result changed the next proposal. The scientist approved batch 2.",
        "chips": ["5,000 scored", "+9.4% yield", "3 days"],
        "outcome_headline": "Three days.",
        "outcome_sub": "A six-week loop becomes a weekend.",
        "outcomes": [("3 days", "cycle"), ("+9.4%", "yield"), ("5,000", "candidates")],
        "quote": "It found a better formulation while we slept.",
        "quote_by": "Principal scientist",
        "scenes": ["The problem", "The evidence", "The loop", "The outcome"],
    },
    {
        "id": "twin",
        "name": "Digital Twin",
        "tag": "Optimization",
        "accent": "#38bdf8",
        "headline": "1,000 simulations.<br>One better setting.",
        "sub": "Engineers try a few settings. The plant runs on good enough.",
        "metric": "15%",
        "metric_label": "energy target",
        "evidence_headline": "Option B: less energy, same yield.",
        "cards": [
            ("1,000", "simulations", "in 8 minutes"),
            ("-12.8%", "energy", "no yield loss"),
            ("4 mo", "payback", "option B"),
        ],
        "aha_headline": "The engineer approves. The line changes tomorrow.",
        "aha_text": "The agent ran the search, stress-tested the top three options and showed the trade-offs. Option B was the best balance.",
        "chips": ["1,000 sims", "-12.8% energy", "4 mo payback"],
        "outcome_headline": "12.8% less energy.",
        "outcome_sub": "No yield loss. Payback in about four months.",
        "outcomes": [("-12.8%", "energy"), ("+0.6%", "yield"), ("4 mo", "payback")],
        "quote": "Run option B on line 3 tomorrow.",
        "quote_by": "Plant director",
        "scenes": ["The problem", "The evidence", "The decision", "The outcome"],
    },
    {
        "id": "synthetic",
        "name": "Synthetic World",
        "tag": "Training data",
        "accent": "#facc15",
        "headline": "The model fails at night.<br>You cannot film the night.",
        "sub": "Rare cases are expensive, slow or unsafe to collect.",
        "metric": "61%",
        "metric_label": "coverage of rare cases",
        "evidence_headline": "The agent found the gaps and filled them.",
        "cards": [
            ("300", "rare cases", "generated"),
            ("94%", "coverage", "was 61%"),
            ("+8.2", "model points", "on the test set"),
        ],
        "aha_headline": "Night, glare, occlusion. 300 variants.",
        "aha_text": "The agent designed the missing scenarios, the NPU generated them, and the model improved by 8.2 points.",
        "chips": ["300 variants", "94% coverage", "+8.2 pts"],
        "outcome_headline": "94% coverage.",
        "outcome_sub": "The safety case moves forward without a film crew.",
        "outcomes": [("300", "rare cases"), ("94%", "coverage"), ("+8.2", "model points")],
        "quote": "This unblocks our safety case.",
        "quote_by": "Head of perception",
        "scenes": ["The problem", "The evidence", "The generation", "The outcome"],
    },
    {
        "id": "cyber",
        "name": "Cyber Range",
        "tag": "Security",
        "accent": "#f87171",
        "headline": "The attacker does not<br>follow the script.",
        "sub": "Static exercises cannot measure readiness.",
        "metric": "4m 12s",
        "metric_label": "to detect the first anomaly",
        "evidence_headline": "The attacker changed tactic. The defender adapted.",
        "cards": [
            ("4m 12s", "detection", "first anomaly"),
            ("6m", "response", "host isolated"),
            ("3", "gaps", "in one exercise"),
        ],
        "aha_headline": "Three real gaps in one exercise.",
        "aha_text": "The NPU flagged the login pattern, the defender isolated the host, and the attacker moved again. The score showed what to fix.",
        "chips": ["4m 12s detect", "6m response", "3 gaps"],
        "outcome_headline": "Measured readiness.",
        "outcome_sub": "Not a tabletop opinion.",
        "outcomes": [("4m 12s", "detection"), ("6m", "response"), ("3", "gaps")],
        "quote": "We measured readiness, not opinions.",
        "quote_by": "CISO - financial services",
        "scenes": ["The problem", "The evidence", "The exercise", "The outcome"],
    },
    {
        "id": "arch",
        "name": "Architecture Studio",
        "tag": "Design",
        "accent": "#fb7185",
        "headline": "Three costed options.<br>Before the client call.",
        "sub": "Feasibility studies take days. Energy rules are tighter.",
        "metric": "3",
        "metric_label": "options in one hour",
        "evidence_headline": "Option 2: 18% less energy, inside budget.",
        "cards": [
            ("3", "layouts", "generated"),
            ("-18%", "energy", "vs baseline"),
            ("EUR 280k", "budget", "within target"),
        ],
        "aha_headline": "The architect signs the design.",
        "aha_text": "The agent generated, scored and improved the best layout. The architect checked daylight and circulation, then selected option 2.",
        "chips": ["3 options", "-18% energy", "EUR 280k"],
        "outcome_headline": "Option 2.",
        "outcome_sub": "Costed, scored and ready for the client.",
        "outcomes": [("3", "options"), ("-18%", "energy"), ("EUR 280k", "budget")],
        "quote": "Three costed options before the client call.",
        "quote_by": "Principal architect",
        "scenes": ["The problem", "The evidence", "The design", "The outcome"],
    },
]

TEMPLATE = Template(r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$name - Pitch</title>
<style>
  :root { --accent: $accent; --bg: #07040d; --ink: #f8fafc; --muted: #a1a1aa; --soft: #64748b; }
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; }
  body { font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif; background: var(--bg); color: var(--ink); overflow: hidden; }
  button, a { font: inherit; }
  .stage { height: 100vh; display: flex; flex-direction: column; position: relative; overflow: hidden; }
  .stage::before { content: ""; position: fixed; inset: -20%; background: radial-gradient(40% 40% at 18% 18%, color-mix(in srgb, var(--accent) 34%, transparent), transparent 70%), radial-gradient(38% 42% at 82% 22%, rgba(236,72,153,.18), transparent 70%), radial-gradient(40% 44% at 58% 90%, rgba(34,211,238,.12), transparent 72%); filter: blur(70px); opacity: .75; pointer-events: none; }
  .grid { position: fixed; inset: 0; background-image: linear-gradient(rgba(148,163,184,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(148,163,184,.05) 1px, transparent 1px); background-size: 64px 64px; mask-image: radial-gradient(circle at 50% 40%, black, transparent 78%); pointer-events: none; }
  .topbar { height: 60px; flex: none; display: flex; align-items: center; gap: 16px; padding: 0 26px; position: relative; z-index: 5; }
  .brand { display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 800; }
  .mark { width: 26px; height: 26px; border-radius: 50%; background: conic-gradient(from 210deg, var(--accent), #ec4899, #8b5cf6, var(--accent)); box-shadow: 0 0 18px color-mix(in srgb, var(--accent) 50%, transparent); }
  .brand span { color: var(--soft); font-weight: 500; }
  .progress { display: flex; gap: 4px; margin-left: auto; margin-right: auto; }
  .progress button { width: 30px; height: 3px; border: 0; padding: 0; background: rgba(255,255,255,.16); border-radius: 999px; cursor: pointer; }
  .progress button.active { width: 46px; background: var(--accent); }
  .progress button.done { background: rgba(255,255,255,.3); }
  .auto { border: 1px solid rgba(255,255,255,.14); background: rgba(255,255,255,.04); color: var(--muted); border-radius: 999px; padding: 6px 10px; font-size: 9px; font-weight: 700; cursor: pointer; }
  .auto.on { color: #fff; border-color: var(--accent); }
  .scenes { flex: 1; position: relative; overflow: hidden; }
  .scene { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; padding: 28px 54px 76px; opacity: 0; transform: translateY(18px); transition: .5s ease; pointer-events: none; }
  .scene.active { opacity: 1; transform: none; pointer-events: auto; }
  .inner { width: min(1120px,100%); }
  .eyebrow { display: flex; align-items: center; gap: 9px; font-size: 10px; letter-spacing: .16em; text-transform: uppercase; color: var(--soft); font-weight: 800; margin-bottom: 16px; }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 14px var(--accent); }
  h1, h2 { margin: 0; letter-spacing: -.045em; line-height: .94; font-weight: 800; text-wrap: balance; }
  h1 { font-size: clamp(48px, 8vw, 104px); }
  h2 { font-size: clamp(36px, 5.6vw, 72px); }
  .accent { color: var(--accent); }
  .lede { color: var(--muted); font-size: clamp(14px, 1.4vw, 18px); line-height: 1.55; max-width: 650px; margin: 20px 0 0; }
  .big { margin-top: 28px; font-size: clamp(40px, 6vw, 72px); font-weight: 800; letter-spacing: -.05em; line-height: 1; color: var(--accent); }
  .big small { display: block; color: var(--muted); font-size: 10px; letter-spacing: .12em; text-transform: uppercase; margin-top: 8px; font-weight: 700; }
  .cards { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-top: 28px; }
  .card { border: 1px solid rgba(255,255,255,.12); background: rgba(255,255,255,.04); border-radius: 12px; padding: 14px; border-top: 2px solid var(--accent); }
  .card b { display: block; font-size: 26px; font-weight: 800; letter-spacing: -.04em; }
  .card span { display: block; font-size: 10px; font-weight: 700; color: #e4e4e7; margin-top: 3px; }
  .card small { display: block; font-size: 9px; color: var(--soft); margin-top: 5px; }
  .chips { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 20px; }
  .chip { border: 1px solid rgba(255,255,255,.14); background: rgba(255,255,255,.04); border-radius: 999px; padding: 5px 9px; font-size: 9px; color: var(--muted); font-weight: 700; }
  .chip b { color: var(--ink); }
  .quote { margin-top: 24px; border-left: 2px solid var(--accent); padding-left: 12px; color: #e4e4e7; font-size: 13px; line-height: 1.5; }
  .quote small { display: block; color: var(--soft); font-size: 9px; margin-top: 3px; }
  .metrics { display: grid; grid-template-columns: repeat(3,1fr); gap: 12px; margin-top: 26px; max-width: 760px; }
  .metric { border-top: 1px solid rgba(255,255,255,.16); padding-top: 9px; }
  .metric b { display: block; font-size: 28px; font-weight: 800; letter-spacing: -.04em; }
  .metric span { display: block; font-size: 9px; color: var(--soft); text-transform: uppercase; letter-spacing: .1em; margin-top: 2px; }
  .cta-row { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 26px; }
  .cta { display: inline-flex; align-items: center; gap: 6px; border: 0; border-radius: 8px; background: var(--accent); color: #120a05; font-size: 11px; font-weight: 800; padding: 10px 14px; text-decoration: none; cursor: pointer; }
  .cta.secondary { background: transparent; color: var(--muted); border: 1px solid rgba(255,255,255,.14); }
  .nav { height: 56px; flex: none; display: flex; align-items: center; gap: 10px; padding: 0 26px; border-top: 1px solid rgba(255,255,255,.08); background: rgba(7,4,13,.55); backdrop-filter: blur(10px); position: relative; z-index: 5; }
  .nav-btn { border: 1px solid rgba(255,255,255,.14); background: rgba(255,255,255,.04); color: #e4e4e7; border-radius: 7px; padding: 7px 11px; font-size: 10px; font-weight: 700; cursor: pointer; }
  .nav-btn[disabled] { opacity: .3; cursor: default; }
  .scene-name { font-size: 9px; color: var(--soft); letter-spacing: .12em; text-transform: uppercase; font-weight: 700; }
  .nav-right { margin-left: auto; color: var(--soft); font-size: 9px; }
  @media (max-width: 820px) { .cards, .metrics { grid-template-columns: 1fr; } .scene { padding: 22px 22px 76px; overflow-y: auto; } .progress { display: none; } }
</style>
</head>
<body>
<div class="stage">
  <div class="grid"></div>
  <header class="topbar">
    <div class="brand"><div class="mark"></div>$name <span>| pitch</span></div>
    <div class="progress" id="progress"></div>
    <button class="auto" id="autoBtn">Auto play</button>
  </header>
  <main class="scenes" id="scenes">
    <section class="scene active" data-scene="0">
      <div class="inner">
        <div class="eyebrow"><span class="dot"></span>$tag | 01</div>
        <h1>$headline</h1>
        <p class="lede">$sub</p>
        <div class="big">$metric<small>$metric_label</small></div>
      </div>
    </section>
    <section class="scene" data-scene="1">
      <div class="inner">
        <div class="eyebrow"><span class="dot"></span>The evidence</div>
        <h2>$evidence_headline</h2>
        <div class="cards">$cards</div>
      </div>
    </section>
    <section class="scene" data-scene="2">
      <div class="inner">
        <div class="eyebrow"><span class="dot"></span>The agent</div>
        <h2>$aha_headline</h2>
        <p class="lede">$aha_text</p>
        <div class="chips">$chips</div>
      </div>
    </section>
    <section class="scene" data-scene="3">
      <div class="inner">
        <div class="eyebrow"><span class="dot"></span>The outcome</div>
        <h1>$outcome_headline</h1>
        <p class="lede">$outcome_sub</p>
        <div class="metrics">$outcomes</div>
        <div class="cta-row">
          <a class="cta" href="$id-studio.html">Open the studio -></a>
          <button class="cta secondary" id="replayBtn">Replay</button>
        </div>
        <div class="quote">$quote<small>$quote_by</small></div>
      </div>
    </section>
  </main>
  <footer class="nav">
    <button class="nav-btn" id="backBtn"><- Back</button>
    <span class="scene-name" id="sceneName">$first_scene</span>
    <button class="nav-btn" id="nextBtn">Next -></button>
    <span class="nav-right">Use left/right arrows</span>
  </footer>
</div>
<script>
  const scenes = Array.from(document.querySelectorAll(".scene"));
  const names = $scene_names;
  const progress = document.getElementById("progress");
  const sceneName = document.getElementById("sceneName");
  const backBtn = document.getElementById("backBtn");
  const nextBtn = document.getElementById("nextBtn");
  const autoBtn = document.getElementById("autoBtn");
  let current = 0;
  let autoTimer = null;
  progress.innerHTML = names.map((n, i) => '<button data-go="' + i + '"></button>').join("");
  const dots = Array.from(progress.querySelectorAll("button"));
  function go(i) {
    current = Math.max(0, Math.min(scenes.length - 1, i));
    scenes.forEach((s, n) => s.classList.toggle("active", n === current));
    dots.forEach((d, n) => { d.classList.toggle("active", n === current); d.classList.toggle("done", n < current); });
    sceneName.textContent = names[current];
    backBtn.disabled = current === 0;
    nextBtn.textContent = current === scenes.length - 1 ? "Replay" : "Next ->";
  }
  function next() { if (current === scenes.length - 1) { go(0); return; } go(current + 1); }
  function stopAuto() { if (autoTimer) clearInterval(autoTimer); autoTimer = null; autoBtn.classList.remove("on"); autoBtn.textContent = "Auto play"; }
  function startAuto() { stopAuto(); autoTimer = setInterval(() => { if (current < scenes.length - 1) go(current + 1); else stopAuto(); }, 6500); autoBtn.classList.add("on"); autoBtn.textContent = "Pause"; }
  backBtn.addEventListener("click", () => { stopAuto(); go(current - 1); });
  nextBtn.addEventListener("click", () => { stopAuto(); next(); });
  document.getElementById("replayBtn").addEventListener("click", () => { stopAuto(); go(0); });
  autoBtn.addEventListener("click", () => { autoTimer ? stopAuto() : startAuto(); });
  progress.addEventListener("click", e => { const b = e.target.closest("[data-go]"); if (b) { stopAuto(); go(Number(b.dataset.go)); } });
  document.addEventListener("keydown", e => { if (e.key === "ArrowRight" || e.key === " ") { e.preventDefault(); stopAuto(); next(); } if (e.key === "ArrowLeft") { e.preventDefault(); stopAuto(); go(current - 1); } });
  go(0);
</script>
</body>
</html>
""")

for app in APPS:
    cards = "".join(
        f'<div class="card"><b>{value}</b><span>{label}</span><small>{note}</small></div>'
        for value, label, note in app["cards"]
    )
    chips = "".join(f'<span class="chip">{chip}</span>' for chip in app["chips"])
    outcomes = "".join(
        f'<div class="metric"><b>{value}</b><span>{label}</span></div>'
        for value, label in app["outcomes"]
    )
    scene_names = "[" + ",".join('"' + name + '"' for name in app["scenes"]) + "]"
    html = TEMPLATE.substitute(
        name=app["name"],
        tag=app["tag"],
        accent=app["accent"],
        headline=app["headline"],
        sub=app["sub"],
        metric=app["metric"],
        metric_label=app["metric_label"],
        evidence_headline=app["evidence_headline"],
        cards=cards,
        aha_headline=app["aha_headline"],
        aha_text=app["aha_text"],
        chips=chips,
        outcome_headline=app["outcome_headline"],
        outcome_sub=app["outcome_sub"],
        outcomes=outcomes,
        quote=app["quote"],
        quote_by=app["quote_by"],
        id=app["id"],
        first_scene=app["scenes"][0],
        scene_names=scene_names,
    )
    (OUT / f'{app["id"]}-pitch.html').write_text(html, encoding="utf-8", newline="\n")
    print("wrote", app["id"] + "-pitch.html")
