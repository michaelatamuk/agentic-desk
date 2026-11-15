# What's new — process

How to write one month's edition. The output format is in `FORMAT.md`.

## Steps

1. **Read the previous edition.** Note its last commit; it is the starting point for the diff.
2. **Read the product repository.** `git log <last>..HEAD` on `main`. Group commits by theme and
   count them. Read the merge titles, not only the commit subjects.
3. **Read the platform under it.** The product may not own the engine. Check the agent platform it
   calls (for DigitalMate: WorkSwarm, and Orbit if it is still in the path), and the substrate that
   runs the containers (`agent-dx`). If you cannot read one, write it in the coverage block.
4. **Read the product's own documents.** For DigitalMate: `docs/migration_status.md`,
   `docs/architecture/server-system-overview-v3.1.md`, `harness/personal-agent/README.md`, and the
   ADRs or verification records behind anything you plan to call shipped.
5. **Check the status of every candidate.** Is it a proposal, merged, accepted or deployed? Look for
   revert commits. A merge title is not proof that users can use it.
6. **Choose three to seven big things.** Platform changes first, then user-visible features, then
   reliability. Everything else goes under "the rest, by theme".
7. **Write the edition** following `FORMAT.md`.
8. **Do the stranger pass.** Read it as someone who has never heard of the product. Every term must
   be explained in place. Replace jargon with plain words. For every sentence, check that it
   describes something a person can picture doing; if it reads like a metaphor, rewrite it as a
   step. Use the before/after table in `FORMAT.md`.
9. **Do the coverage check.** List the repositories and commits read, and state what was skipped.
10. **Link it.** Add the new edition to the "see also" list of the previous one, and add the old one
    to the new one.

## Sources, in order of trust

1. Code and the documents in the repository.
2. The repository's own architecture, migration and verification notes.
3. Merge and pull-request titles.
4. The public board, status notes and memory.

If two sources disagree, the code wins, and the disagreement is worth a sentence in the edition.

## DigitalMate specifics

- Backend state: `digitalmate/entry/src/main/ets/cloud/CloudBackendConfig.ets` says which backends
  the app accepts.
- Old names: `/orbit/ws`, `orbit.request` and the `orbit` config value are compatibility, not the
  current engine. `engine_rename.py` moves old `orbit/` and `luna/` workspaces.
- Execution: `harness/personal-agent/README.md` and `harness/workswarm/` give the pinned WorkSwarm
  build.
- Architecture: `docs/architecture/server-system-overview-v3.1.md` gives the target components;
  `docs/migration_status.md` says which path is actually supported today.

## Review before saving

- Does the coverage block say what was not read?
- Is every "new" thing actually new, and every replacement named?
- Are proposals, merges and deployments told apart?
- Could the edition stand alone as the only document a reader sees?
