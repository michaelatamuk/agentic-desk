# LAIX · StudyRoom — speaker notes

Open the deck directly in a browser. No server, build or network is required.

```text
index.html
```

Keyboard: `←` / `→` or space to move, `N` for notes, `F` for full screen, `Home` / `End`.

The deck has two lenses:

- **Managers:** slides 1–7, plus 8 for the demo and 12–14 for truth and close.
- **PPMA builders:** slides 1–5, then 9–12 and 14.

Do not try to present all 14 slides to both audiences in one pass.

---

## 20-minute manager run

| Time | Slide | What to say |
|---:|---|---|
| 0:00–0:02 | 1 | “Every app can see. Few can decide.” |
| 0:02–0:05 | 2 | Alice is stuck; the teacher cannot watch all three |
| 0:05–0:08 | 3 | LAIX answers: what should happen next? |
| 0:08–0:11 | 4 | The decision receipt |
| 0:11–0:15 | 5 | Wait, override, ask, consent, board |
| 0:15–0:17 | 6 | Less noise, consistent help, auditable trust |
| 0:17–0:19 | 7 | What it is not |
| 0:19–0:20 | 14 | Close: accountable for what it does next |

Optional: replace the slide-5 story with the safe live demo in slide 8.

### Manager talk track

> “Alice has two wrong attempts. The teacher is one person. The room can wait, hint, ask Ben, or call the teacher. This is not a content problem. It is a decision problem.”

> “LAIX returns one decision with the options it rejected, the limits that applied, how sure it is, and who must approve.”

> “The important part is not that it acts. It is that it can wait, ask and escalate — and show why.”

> “For a school, that means less noise, a consistent escalation path, and a record you can defend.”

> “One decision layer reused across apps is cheaper and safer than a different chatbot in every product.”

Close:

> “LAIX does not make the app smarter. It makes the app accountable for what it does next.”

---

## 45-minute PPMA builder run

| Time | Slide | What to say |
|---:|---|---|
| 0:00–0:03 | 1 | The decision layer, not a memory or agent platform |
| 0:03–0:08 | 3–4 | The request/decision/receipt contract |
| 0:08–0:14 | 9 | PPMA owns memory, consent and audit; LAIX owns the decision |
| 0:14–0:22 | 10 | The integration sequence; one adapter |
| 0:22–0:30 | 11 | What to implement; policy in the host |
| 0:30–0:36 | 12 | Real vs simulated; no overclaim |
| 0:36–0:42 | 13 | The 90-day pilot and measures |
| 0:42–0:45 | 14 | Close and questions |

### Builder talk track

> “PPMA owns memory, identity, consent and audit. LAIX owns the live decision. StudyRoom is the host that connects them.”

> “LAIX never calls PPMA. It never reads PPMA tables. The host asks PPMA for authorized context, passes generic constraints and options to LAIX, and routes the decision back.”

> “The adapter is the only module that knows both vocabularies. The domain policy lives in the host. LAIX owns the decision mechanics, confidence, alternatives, approval and record.”

> “The integration is a request in, a decision out, a record back. It is not a rewrite of PPMA.”

> “If LAIX is unavailable, the host waits and alerts. It does not silently switch to a second decision engine. Consent failures fail closed.”

### Builder questions

**Why not put this inside PPMA?**  
PPMA should own memory and permission. LAIX is domain-neutral and reusable across hosts. PPMA can call it without owning it.

**What does the host have to implement?**  
One adapter, one policy plugin, consent/approval handling, decision records and outcomes. Not a new memory system.

**What is the failure mode?**  
Safe wait, teacher alert, no silent fallback. Consent store unavailable means no peer help and no board sharing.

---

## The safe live demo

The current Phase 0 build has a strong live path and a few known rough edges. Use the safe path.

**Open:** `http://127.0.0.1:8000/?view=teacher`

**Manual only.** Do not use autoplay.

1. Show the teacher wall: three learners, evidence line, decision dock.
2. Alice answers incorrectly twice. LAIX waits.
3. False hand raise: LAIX proposes Ben; teacher overrides “back on task”; re-rank to wait.
4. Alice asks; Ben offers. LAIX asks both learners for consent.
5. Both accept. The shared board opens with only the current problem.
6. Stop. Say the line: “It knew when not to interrupt.”

**Do not show in the current build:**

- autoplay — it takes about 105 seconds and races with a second window;
- the alternatives drawer — the score/reason text is not trustworthy yet;
- the helper-disconnect/re-plan step — the sequence is not coherent yet;
- steps 8 and 12 — they show the previous decision rather than “no new decision.”

If someone asks about re-plan, answer with the design, not a live claim:

> “The next live moment is the helper leaving mid-explanation. LAIX re-plans to a private hint. That is designed; it is not the live proof today.”

---

## The one-sentence story

> “StudyRoom is a room that notices when a learner needs help. LAIX is the part that decides whether to wait, hint, ask a peer or call the teacher — and shows why.”

## The closing line

> “LAIX does not make the app smarter. It makes the app accountable for what it does next.”

## If StudyRoom is not running

Use the deck alone. Slide 5 is the storyboard. Slide 8 is the safe demo path. Do not claim a live run you did not do.
