# GitHub as the workflow

Principle: **the issue is the source of STATUS; the vault is the source of KNOWLEDGE.** An issue links to its checklist/spec note; the note links back to the issue number. Never duplicate status in notes.

Run each step only after the user confirms it. Check `gh auth status` first; if not logged in, ask the user to run `gh auth login` themselves. Wrapper: `scripts/gh_setup.sh <step> [owner/repo]`.

## 1. Labels (`labels`)
- Area: `area:<component>` (one per main component, for example `area:api`, `area:web`).
- Priority: `prio:high`, `prio:medium`, `prio:low`.
- State: `em-dev`, `esperando-ok`, `em-producao` (or `in-dev`, `awaiting-ok`, `in-production`; the script creates the English set by default and the Portuguese set with `LANG_SET=pt`).
- Type: `bug`, `feature`, `chore`, `docs`.

## 2. Milestones (`milestones`)
One per planned version (for example `v0.1.0`, `v0.2.0`).

## 3. Projects board (`project`)
Single-select `Status` field: **To do -> In progress -> In dev -> Awaiting OK -> In production**.
If the token lacks the `project` scope, tell the user to run `gh auth refresh -s project,read:project` (do not run it for them).

## 4. Templates
Copied by the scaffold: `.github/ISSUE_TEMPLATE/task.md` (from the task template) and `.github/pull_request_template.md` (Definition of Done as checkboxes).

## 5. Branch protection (`protect`)
On `main`: require a pull request, require the `tests` status check, no force-push, no deletion. With `approval=team`, require 1 review; with `approval=owner`, the owner merges. On the free plan GitHub refuses protection on private repositories (`gh_setup.sh protect` exits 3 with a clear message). Tell the user, and record in CLAUDE.md that main is protected by procedure only (never push to main; merge only through an approved PR) until they upgrade or make the repo public.

## 6. CI
`.github/workflows/tests.yml` runs only the tests on push and PR. **No secrets and no production deploy in CI**: deploy stays a human-approved step run from the tag (see `releases.md`).

## Conventions
- Branches `task/<issue>-<slug>`, one per task (see `daily-flows.md`).
- PR title in conventional-commit style; body has `Closes #<n>`, the vault note link, and the ticked DoD.
- State follows the board: merged into `dev` = in-dev; PR `dev -> main` open = awaiting-ok; deployed = in-production, then close.
