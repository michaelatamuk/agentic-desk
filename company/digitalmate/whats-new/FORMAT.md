# What's new — format

One file per product per month: `company/<product>/whats-new/whats-new-YYYY-MM.md`.

The test for every edition: **a reader who knows nothing about the product should be able to explain
what it is, what runs underneath it, and what changed this month, without opening another file.**

## Required sections, in order

1. **Title** — `# What's New in <Product> — <Month> <Year>`.
2. **Opening** — one short paragraph: the month in plain words, the two or three things that matter,
   and the commit count.
3. **`*Last updated: YYYY-MM-DD.*`**
4. **`## What <Product> is`** — three to five sentences. What the user does with it, and what the
   repository contains.
5. **`## What runs underneath`** — the stack in plain words, and what changed in it this month.
   Define every layer: product surface, engine, agent platform.
6. **`**Coverage**`** — a table of what was read (repository, commit, merge time, what it is), the
   previous edition's last commit, and an explicit **not read** line.
7. **Tag legend** — always the same four tags (below).
8. **`# The big things`** — three to seven items, most important first. Platform changes before
   feature changes; user-visible before internal. Each item says what changed, what the user sees,
   and its status.
9. **`# The rest, by theme`** — one-line bullets grouped by area. A PR number only in brackets,
   never instead of a description.
10. **`# What didn't ship`** — reverts, removals, and designs that did not land.
11. **`# See also`** — previous edition, product overview.

## Tags

- **[NEW]** — a capability that did not exist before.
- **[UPGRADE]** — an existing capability re-worked until it feels new.
- **[PROPOSAL]** — designed and reviewed, not accepted or deployed.
- **[REMOVED]** — something that was in the product and is now gone.

## Status words

Use these exactly; never write "landed", which hides which one is true.

| Word | Means |
|---|---|
| **proposal** | designed or reviewed; not accepted |
| **merged** | the code is in `main` |
| **accepted** | the owning team accepted the design or ownership |
| **deployed** | it runs in production |
| **shipped** | a user can use it |

A merge is not a deployment. A design is not a merge. If you are not sure, write "not verified".

## Style

- Plain English. Short sentences. One idea per bullet.
- Describe behaviour as steps a person can picture: "close the app, reopen it, the chat is still
  there". Do not use metaphors such as "survives", "outlives", "carries" or "joins" in place of the
  concrete action.
- Name the actor: who does what, when, and what the user sees.
- Define every term the first time it appears: engine, server, backend, protocol, adapter,
  container, skill, agent.
- No unexplained acronyms or internal codenames. Write "the server's message format", not "E2A".
- No PR number without a plain-language description; the number goes in brackets.
- Say what changed for the user before what changed in the code.
- Name the previous engine or component when something is replaced; "the app gets an engine" is
  meaningless if it already had two.
- If a source was not read, say so in the coverage block.

## Language: say what happens

Every sentence should describe something the reader can picture. A heading names the thing that
changed, not a theme or a feeling.

| Do not write | Write |
|---|---|
| "A conversation that survives leaving the app" | "Close the app, reopen it, and the same chat is there: messages, attachments and task progress" |
| "Tasks that outlive the app" | "A task keeps running after you leave the chat; you can see it in an activity panel and a notification" |
| "Progress used to live only inside the conversation" | "Progress used to be visible only while you were in the chat" |
| "Quick follow-ups join the request" | "A follow-up sent while a task is running becomes part of that task" |
| "A discovery feed joins the app" | "A new tab shows a feed of videos, articles and posts" |
| "Quoted text survived the migration" | "Quoted text still displays correctly after the migration" |
| "Orbit is the previous name of the engine" | "Orbit is a separate product; DigitalMate used it from 20 to 30 October, then replaced it" |
| "The server is being taken apart" | "The server is being split into six parts" |

Rules:

1. Say what the user does, then what they see.
2. If a sentence could describe a living thing, rewrite it: "survives", "outlives", "lives",
   "carries".
3. If a sentence needs a diagram, another document, or a second read to make sense, rewrite it as
   steps.
4. Name the actor: the phone, the app, the server, the assistant, the user.
5. Prefer concrete nouns: chat, message, task, file, notification, screen, button.
6. A heading states the change: "Your chat is still there when you come back", not "Conversation
   persistence".

## Self-check

- Could a stranger read only this file and explain the product and the month?
- Does every sentence pass the picture test: can the reader see the action?
- Is every heading a statement of what changed?
- Is every codename and acronym explained?
- Is every status word true?
- Are reverts and proposals in their own sections?
- Does the coverage block admit what was skipped?
