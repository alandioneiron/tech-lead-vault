# CLAUDE.md - Operating rules for "{{PROJECT_NAME}}"

> Loaded automatically by every AI session in this directory. These rules take priority over default behavior.

## What this project is
{{PROJECT_SUMMARY}}

The documentation lives in an Obsidian vault (`{{VAULT_DIR}}`), linked with `[[wikilinks]]`. Start at [[Home]].

<!-- IF:ROLES -->
## Roles and models (mandatory routing)
- **Tech Lead** (most capable model): planning, architecture, decisions, ambiguous/critical/security work, final review. Coordinates with the user.
- **Devs / QA** (cheaper models): implementation and tests of well-defined tasks.
- Before delegating, pick the cheapest model able to do the task well, following [[Model Routing]]. If delegating costs about as much as doing it, the Tech Lead does it.

<!-- ENDIF:ROLES -->
## Non-negotiable process rules

1. **Living documentation.** Whenever you write, edit or test code or configuration, update the affected docs in the SAME task, before calling it done: [[Development Journal]], [[Changelog]] (if behavior changed), the module spec in `04-Development/`, [[Architecture]] if affected, and one line in [[AI Session Log]]. If a relevant context has no doc, create it and link it.
2. **Checklists.** Every process follows a checklist in `05-Checklists/`. Tick `[x]` each item as soon as it is done, not in a batch. If there is no checklist, create one from [[Template - Task]] first.
3. **Definition of Done.** Nothing is "completed" without passing [[Definition of Done]].
4. **Decisions.** Every architecture/technology decision becomes an ADR in [[Decision Log (ADR)]] using [[Template - ADR]].
5. **Dev to production.** Every change goes through the dev flow and reaches production only after the user's OK (the approved PR into `{{MAIN_BRANCH}}`), then deploy the tag. Hotfix only with explicit OK. See [[Dev to Production Flow]] and [[Promote to Production]].
6. **Handoff.** At the end of every session, rewrite [[Last Agent - Handoff]]: what is in production, in progress, waiting on the user, next steps.
7. **Commit and push after each progress step** (together with the living docs). Docs-only commits add only the docs.
8. **Never commit secrets** (keys, tokens, credentials, `.env`). `.gitignore` must protect them.
9. **Dates** are always `YYYY-MM-DD`.

## GitHub is the workflow
The issue holds the STATUS; the vault holds the KNOWLEDGE. Link each issue to its checklist/spec note and back. Release versions follow SemVer (starting at {{VERSION}}); see [[Dev to Production Flow]].

## Start of any session
1. Read [[Home]] and [[Last Agent - Handoff]].
2. Read [[Roadmap]] and the checklist of the current phase.
3. At the end, apply rules 1-6 above.

## Conventions
- Language of the docs: English.
- Links between notes: `[[Note Name]]` (no extension).
- Recurring risks never go away; see [[Risks]].
