# Daily flows

## Conventions used by every flow
- **Branches**: one branch per task, `task/<issue-number>-<short-slug>` (for example `task/12-create-appointment`). With a dev environment, task branches go by PR into `dev`, and `dev` goes by PR into `main` at release time; create `dev` from `main` right after the install commit (`git switch -c dev && git push -u origin dev`). Without a dev environment, task branches go by PR straight into `main`.
- **ADRs live inline** in the decision log note, one `## ADR-NNNN - Title` section each, newest at the bottom. The "Next number" line at the top of the log is updated every time an ADR is added.
- **The Definition of Done is the project-wide standard.** Each task checklist ends with a "DoD" item; tick it only after going through every DoD line for that task.
- **No `gh`, or no remote**: never block. Do the vault part, and write the exact command that is pending in the task note under `Pending on GitHub:` (for example `gh issue create --title "..." --label area:api`), with `Issue: pending` instead of a number. With no remote, commit locally and record `push pending (no remote)` in the Handoff. The next session with `gh`/a remote runs the pending commands first and replaces `pending` with the real numbers.

## A. Open a task
1. Create the issue (`gh issue create --title ... --body ...`) from the task issue template, set labels (area, priority), milestone, and add it to the board "To do". Without `gh`: see conventions.
2. Create the checklist note in `05-Checklists/` from the task template; put the issue number in it and the note's link in the issue body.
3. Pick the model (if roles): score with `model-routing.md` and fill the "Routing" line of the task note (scores, sum, choice).
4. Create the task branch (see conventions) from `dev` (or `main` without a dev environment), move the card to "In progress", set the state label.
5. Tick checklist items as they are done.

## B. Record a decision (ADR)
1. Read the "Next number" line of the decision log; that is the new ADR's number.
2. Append a new section to the decision log from the ADR template (status Proposed or Accepted, context, decision, alternatives, consequences), then bump "Next number".
3. Link the ADR (`[[Decision Log#ADR-NNNN - Title]]` or by number) from the issue/PR and from the affected spec or architecture note.
4. If it replaces an older ADR, set the old one's status to "Superseded by ADR-NNNN".

## C. Prepare a release
Follow `releases.md`. Before opening the `dev -> main` PR, confirm the DoD, the Changelog "Unreleased" section, and that the milestone is complete.

## D. Close the session
1. Tick every checklist item that is done; leave honest unticked items for what is not.
2. Update: Development Journal entry (date, agent/model that did the work, what, why, result including failures), Changelog if behavior changed, the module spec, Architecture if affected.
3. Add one line to the AI Session Log (date, agent/model, task, artifacts touched).
4. **Rewrite the Handoff**: in production now / in progress / waiting on the user / pending on GitHub or push / next steps in order.
5. Commit and push (a docs-only commit adds only docs). Move board cards and update state labels. Without a remote or `gh`: see conventions.
