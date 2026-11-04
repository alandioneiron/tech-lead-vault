# Daily flows

## A. Open a task
1. Create the issue (`gh issue create --title ... --body ...`), set labels (area, priority), milestone, and add it to the board "To do".
2. Create the checklist note in `05-Checklists/` from the task template; put the issue number in it and the note's link in the issue body.
3. Pick the model (if roles): score with `model-routing.md`, record the sum and the choice.
4. Create the branch, move the card to "In progress".
5. Tick checklist items as they are done.

## B. Record a decision (ADR)
1. Find the highest existing ADR number in the decision log; use the next one.
2. Create the ADR from the ADR template (status Proposed or Accepted, context, decision, alternatives, consequences).
3. Add a one-line entry to the decision log and link the ADR from the issue/PR and from the affected spec or architecture note.
4. If it replaces an older ADR, set the old one's status to "Superseded by ADR-<n>".

## C. Prepare a release
Follow `releases.md`. Before opening the `dev -> main` PR, confirm the DoD, the Changelog "Unreleased" section, and that the milestone is complete.

## D. Close the session
1. Tick every checklist item that is done; leave honest unticked items for what is not.
2. Update: Development Journal entry (what, why, result including failures), Changelog if behavior changed, the module spec, Architecture if affected.
3. Add one line to the AI Session Log (date, agent/model, task, artifacts touched).
4. **Rewrite the Handoff**: in production now / in progress / waiting on the user / next steps in order.
5. Commit and push (docs-only commit adds only docs). Move board cards and update state labels.
