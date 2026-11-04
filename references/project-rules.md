# Project rules and why they exist

These are written into the project's `CLAUDE.md` so every future session loads them without being told.

| # | Rule | Why |
|---|---|---|
| 1 | **Living documentation**: whenever code or config is written, edited or tested, update the affected docs in the same task (journal, changelog if behavior changed, module spec, architecture if affected, session log). | Docs written "later" are never written. A fresh AI session only knows what the docs say. |
| 2 | **Checklist per process**; tick each item the moment it is done. If a process has no checklist, create one from the task template first. | Batch-ticking at the end is fiction; the checklist is only useful as live progress. |
| 3 | **Definition of Done** before "completed". | One shared bar prevents "done but untested / undocumented". |
| 4 | **Every decision becomes an ADR** (context, decision, alternatives, consequences). | Prevents re-litigating choices and explains the "why" to newcomers and to future AI sessions. |
| 5 | **Dev to production only with the user's OK.** Changes go through dev; the approved PR `dev -> main` is the OK; deploy follows. Hotfix only with explicit OK. | Production is where mistakes are expensive. |
| 6 | **Handoff**: rewrite the Handoff note at the end of every session (what is in production, in progress, waiting on the user, next steps). | The next session starts from truth, not from memory. |
| 7 | **Commit + push after each progress step.** Docs-only commits add only the docs (no blind `git add -A` while other agents edit code). | Work survives a crash and is reviewable. |
| 8 | **Never commit secrets** (keys, tokens, credentials, `.env`). Keep `.gitignore` protecting them. | A leaked secret in history is a permanent incident. |
| 9 | **Dates as `YYYY-MM-DD`.** | Unambiguous across locales and sortable. |

## Session start (goes into CLAUDE.md)
1. Read `Home` and the Handoff note.
2. Read the roadmap and the current phase's checklist.
3. At the end apply rules 1-6.

## Recurring risks
Every project has a few risks that never go away (legal, privacy, platform terms, security). Record them in `01-Planning/Risks` and re-read them when a decision touches them.
