import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ── dark palette (matches reference) ─────────────────────────────────────────
BG    = '#0d1117'
CARD  = '#161b22'
CBRD  = '#30363d'
WHITE = '#e6edf3'
DIM   = '#8b949e'
SOFT  = '#21262d'

# Vivid accent colours for dark background
G  = '#3fb950'
B  = '#58a6ff'
P  = '#d2a8ff'
A  = '#ffa657'

# Dark tints (card inner highlights)
DG = '#0a1f0c'
DB = '#0c1a2e'
DP = '#1a0b2e'
DA = '#1f1408'

fig = plt.figure(figsize=(16, 9), dpi=130, facecolor=BG)
ax  = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.axis('off')
ax.set_facecolor(BG)

# ── helpers ───────────────────────────────────────────────────────────────────
def box(x, y, w, h, fc=CARD, ec=CBRD, radius=0.010, lw=0.8, zorder=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        linewidth=lw, edgecolor=ec, facecolor=fc,
        transform=ax.transAxes, clip_on=False, zorder=zorder))

def t(x, y, s, size=9, color=WHITE, ha='left', va='center',
      bold=False, italic=False, alpha=1.0, zorder=6):
    ax.text(x, y, s, transform=ax.transAxes,
            fontsize=size, color=color, ha=ha, va=va,
            fontweight='bold' if bold else 'normal',
            style='italic' if italic else 'normal',
            alpha=alpha, zorder=zorder)

def wrap(text, max_chars):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if len(test) > max_chars and cur:
            lines.append(cur.strip()); cur = w
        else:
            cur = test
    if cur: lines.append(cur.strip())
    return lines

# ── layout ────────────────────────────────────────────────────────────────────
PAD     = 0.018
COL_GAP = 0.015
ROW_GAP = 0.014
GTOP    = 0.930
GBOT    = 0.092

CW = (1.0 - 2*PAD - COL_GAP) / 2      # ≈ 0.474
CH = (GTOP - GBOT - ROW_GAP) / 2      # ≈ 0.412

positions = [
    (PAD,              GBOT + CH + ROW_GAP),
    (PAD + CW + COL_GAP, GBOT + CH + ROW_GAP),
    (PAD,              GBOT),
    (PAD + CW + COL_GAP, GBOT),
]

HBAR   = 0.062   # header height
CIRC_R = 0.014   # step circle radius

apps = [
    dict(
        name='Lab Loop', badge='L',
        sector='Pharma · Biotech · Chemistry · Materials Research',
        color=G, dark=DG,
        what='An AI experimenter that runs inside the research cycle. The scientist sets the goal and constraints; the AI proposes the next batch of experiments, runs them on an instrument or simulator, reads the results, updates its model and proposes the next batch.',
        steps=[
            ('1', 'Scientist sets\ngoal & limits'),
            ('2', 'AI proposes\nexperiment batch'),
            ('3', 'Instrument or\nsimulator runs it'),
            ('4', 'AI reads result,\nproposes next'),
        ],
        you_get=['Experiment plan', 'Full run log', 'Next recommended batch', 'Reason for each choice'],
        human='Scientist approves every proposed batch',
    ),
    dict(
        name='GeoResponse', badge='G',
        sector='Insurance · Utilities · Government · Agriculture',
        color=B, dark=DB,
        what='An AI analyst for satellite and drone imagery. When an area changes — flood, fire, building damage or new construction — it finds the change, adds context from asset records and maps, ranks locations by urgency and value, and writes the assessment.',
        steps=[
            ('1', 'Satellite or drone\nimagery arrives'),
            ('2', 'AI detects changes\nand damage'),
            ('3', 'Adds context,\nranks by urgency'),
            ('4', 'Map + written\nassessment ready'),
        ],
        you_get=['Map of changes', 'Prioritised locations', 'Evidence images', 'Written assessment'],
        human='Analyst reviews and approves before filing',
    ),
    dict(
        name='Imaging Assistant', badge='I',
        sector='Hospitals · Radiology Groups · Imaging Centres',
        color=P, dark=DP,
        what='An AI first reader for radiology. It reads every scan before the radiologist, marks possible findings on the image, pulls the patient history and prior studies for context, and produces a draft report with evidence and confidence levels for the radiologist to review and sign.',
        steps=[
            ('1', 'Scan arrives\nfrom imaging system'),
            ('2', 'AI reads it,\nmarks findings'),
            ('3', 'Pulls patient\nhistory & prior scans'),
            ('4', 'Draft report\nfor radiologist'),
        ],
        you_get=['Annotated scan image', 'Draft report', 'Confidence per finding', 'Full audit trail'],
        human='Radiologist always reviews and signs',
    ),
    dict(
        name='RootCause', badge='R',
        sector='Manufacturing · Quality · Factory Operations',
        color=A, dark=DA,
        what='An AI quality engineer for factories. When a bad part is found, it gathers machine settings, material batch records, maintenance logs and similar past defects, identifies the most likely causes ranked by evidence, and writes the quality report for the engineer to approve.',
        steps=[
            ('1', 'Defect detected\non the line'),
            ('2', 'AI gathers machine\ndata, batch & logs'),
            ('3', 'Suggests causes\nranked by evidence'),
            ('4', 'Draft quality\nreport ready'),
        ],
        you_get=['Defect photos & context', 'Causes ranked', 'Evidence charts', 'Draft quality report'],
        human='Engineer approves every cause and report',
    ),
]

# ── title ─────────────────────────────────────────────────────────────────────
t(0.50, 0.968,
  'Four AI apps that do expert work in the background',
  size=16, color=WHITE, ha='center', bold=True)
t(0.50, 0.945,
  'Research  ·  Infrastructure  ·  Healthcare  ·  Manufacturing'
  '   —   data stays on-site, human approves every output',
  size=8.5, color=DIM, ha='center')

# ── cards ─────────────────────────────────────────────────────────────────────
for app, (cx, cy) in zip(apps, positions):
    c   = app['color']
    dk  = app['dark']
    top = cy + CH

    # Card shadow (subtle)
    ax.add_patch(FancyBboxPatch((cx + 0.002, cy - 0.003), CW, CH,
        boxstyle="round,pad=0,rounding_size=0.012",
        linewidth=0, facecolor=c, alpha=0.06,
        transform=ax.transAxes, clip_on=False, zorder=1))

    # Card body
    box(cx, cy, CW, CH, fc=CARD, ec=CBRD, radius=0.012, lw=1.0, zorder=2)

    # Coloured top accent line (2px stripe)
    ax.add_patch(plt.Rectangle((cx, top - 0.005), CW, 0.005,
        transform=ax.transAxes, facecolor=c, linewidth=0, zorder=5))
    # Round top corners by drawing a rounded rect on top
    ax.add_patch(FancyBboxPatch((cx, top - 0.016), CW, 0.016,
        boxstyle="round,pad=0,rounding_size=0.010",
        linewidth=0, facecolor=c,
        transform=ax.transAxes, clip_on=False, zorder=4))

    # Header background (dark strip below the colour)
    ax.add_patch(FancyBboxPatch((cx, top - HBAR), CW, HBAR,
        boxstyle="round,pad=0,rounding_size=0.012",
        linewidth=0, facecolor=SOFT,
        transform=ax.transAxes, clip_on=False, zorder=3))
    ax.add_patch(plt.Rectangle((cx, top - HBAR), CW, HBAR / 2,
        transform=ax.transAxes, facecolor=SOFT, linewidth=0, zorder=3))

    # Badge — coloured square with letter
    bx = cx + 0.018
    by = top - HBAR * 0.72
    bsz = 0.034
    ax.add_patch(FancyBboxPatch((bx, by), bsz, bsz,
        boxstyle="round,pad=0,rounding_size=0.005",
        linewidth=0, facecolor=c, alpha=0.20,
        transform=ax.transAxes, clip_on=False, zorder=5))
    ax.add_patch(FancyBboxPatch((bx, by), bsz, bsz,
        boxstyle="round,pad=0,rounding_size=0.005",
        linewidth=1.0, edgecolor=c, facecolor='none',
        transform=ax.transAxes, clip_on=False, zorder=5))
    t(bx + bsz / 2, by + bsz / 2, app['badge'],
      size=12, color=c, ha='center', bold=True, zorder=7)

    # App name
    t(bx + bsz + 0.012, top - HBAR * 0.44,
      app['name'], size=13.5, color=WHITE, bold=True)

    # Sector
    t(bx + bsz + 0.012, top - HBAR * 0.76,
      app['sector'], size=6.5, color=DIM)

    y = top - HBAR - 0.016

    # ── WHAT IT DOES ──────────────────────────────────────────────────────────
    lines = wrap(app['what'], 74)
    LH = 0.019
    for li, line in enumerate(lines):
        t(cx + 0.018, y - li * LH, line, size=7.5, color=WHITE, alpha=0.90)
    y -= len(lines) * LH + 0.014

    # ── HOW IT WORKS ─────────────────────────────────────────────────────────
    t(cx + 0.018, y, 'HOW IT WORKS', size=6, color=c, bold=True, alpha=0.80)
    y -= 0.024

    n = len(app['steps'])
    fp = 0.020                          # flow left/right padding
    sw = (CW - 2 * fp) / n             # width per step slot

    for i, (num, label) in enumerate(app['steps']):
        sx = cx + fp + sw * i + sw / 2
        sy = y - CIRC_R - 0.002

        # Circle — tinted fill + coloured border
        ax.add_patch(plt.Circle((sx, sy), CIRC_R,
            facecolor=c, alpha=0.18,
            transform=ax.transAxes, zorder=4))
        ax.add_patch(plt.Circle((sx, sy), CIRC_R,
            facecolor='none', edgecolor=c, linewidth=1.2,
            transform=ax.transAxes, zorder=5))
        t(sx, sy, num, size=7.5, color=c, ha='center', bold=True, zorder=7)

        # Step label below circle
        for li, ll in enumerate(label.split('\n')):
            t(sx, sy - CIRC_R - 0.009 - li * 0.016,
              ll, size=6.5, color=WHITE, ha='center', va='top',
              alpha=0.88, zorder=7)

        # Arrow to next
        if i < n - 1:
            nx = cx + fp + sw * (i + 1) + sw / 2
            ax.annotate('',
                xy=(nx - CIRC_R - 0.008, sy),
                xytext=(sx + CIRC_R + 0.008, sy),
                xycoords='axes fraction', textcoords='axes fraction',
                arrowprops=dict(arrowstyle='->', color=c,
                                lw=1.2, mutation_scale=10),
                zorder=6)

    y -= CIRC_R * 2 + 0.048   # below step labels (2 label lines)

    # Divider
    ax.plot([cx + 0.018, cx + CW - 0.018], [y, y],
            transform=ax.transAxes, color=CBRD, lw=0.7, zorder=3)
    y -= 0.012

    # ── YOU GET ───────────────────────────────────────────────────────────────
    t(cx + 0.018, y, 'YOU GET', size=6, color=c, bold=True, alpha=0.80)
    y -= 0.020

    for di, item in enumerate(app['you_get'][:4]):
        col = di % 2
        row = di // 2
        ix = cx + 0.018 + col * (CW / 2 - 0.004)
        iy = y - row * 0.021
        ax.scatter([ix - 0.007], [iy], s=22, color=c, alpha=0.75,
                   zorder=6, transform=ax.transAxes)
        t(ix + 0.004, iy, item, size=7.2, color=WHITE, alpha=0.88)

    y -= 0.042 + 0.013

    # ── Human approval ────────────────────────────────────────────────────────
    NH = 0.021
    ax.add_patch(FancyBboxPatch((cx + 0.016, y - NH), CW - 0.032, NH,
        boxstyle="round,pad=0,rounding_size=0.005",
        linewidth=0.8, edgecolor=c, facecolor=dk,
        transform=ax.transAxes, clip_on=False, zorder=4))
    t(cx + CW / 2, y - NH / 2,
      '✓  ' + app['human'], size=7, color=c, ha='center', bold=True)

# ── bottom bar ────────────────────────────────────────────────────────────────
BAR_Y = 0.008
BAR_H = 0.078
box(PAD, BAR_Y, 1 - 2*PAD, BAR_H, fc=SOFT, ec=CBRD, radius=0.010, lw=0.8)

shared = [
    (G, 'Data never leaves your site',
     'Patient scans, factory data and lab results stay inside the customer network.'),
    (B, 'Human approves every output',
     'The AI gathers, analyses and drafts. The expert reads, decides and signs.'),
    (P, 'Structured deliverable — not a chat',
     'A report, a map, an experiment plan or a case file. Ready to file or audit.'),
]

BAR_W = (1 - 2*PAD) / 3
for si, (sc, title, desc) in enumerate(shared):
    sx = PAD + si * BAR_W + 0.024
    ax.scatter([sx - 0.010], [BAR_Y + BAR_H * 0.65], s=48, color=sc,
               zorder=6, transform=ax.transAxes)
    t(sx + 0.004, BAR_Y + BAR_H * 0.65, title, size=8.5, color=WHITE, bold=True)
    t(sx + 0.004, BAR_Y + BAR_H * 0.30, desc, size=7.2, color=DIM)
    if si < 2:
        vx = PAD + (si + 1) * BAR_W
        ax.plot([vx, vx], [BAR_Y + 0.010, BAR_Y + BAR_H - 0.010],
                transform=ax.transAxes, color=CBRD, lw=0.8, zorder=3)

out = '/Users/mishka/PycharmProjects/openjiuwen/agentic-desk/projects/apps/ideas/apps-overview.png'
plt.savefig(out, dpi=130, bbox_inches='tight', facecolor=BG, pad_inches=0.04)
plt.close()
print('saved:', out)
