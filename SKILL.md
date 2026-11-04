---
name: tech-lead-vault
description: Run a software project the way a Tech Lead would, with an Obsidian vault as the project's memory and GitHub (issues, Projects board, PRs, releases) as the workflow. Guided first-time install (asks a few questions, shows a plan, then builds the vault, CLAUDE.md, labels, board, templates, CI), plus daily flows - open a task, record a decision (ADR), prepare a SemVer release, close the session with a handoff. Use this skill whenever the user wants to set up project management, living documentation, a project vault, a CLAUDE.md with process rules, a Definition of Done, ADRs, a dev-to-production flow, a handoff between AI sessions, release notes/tags, or says things like "organize this project", "act as tech lead", "set up my repo workflow", "prepare a release", "close the session", "register this decision", even if they never name the skill. Also triggers in Portuguese - "configurar gestão do projeto", "vault do Obsidian", "fechar a sessão", "preparar release", "registrar decisão".
---

# tech-lead-vault

A method for an AI acting as **Tech Lead**: the **Obsidian vault is the memory** (knowledge, decisions, logs, checklists) and **GitHub is the workflow** (status, review, releases). The issue holds the *status*; the vault holds the *knowledge*; each links to the other.

Why this exists: AI sessions start with empty context. If knowledge lives only in chat, it is lost; if status lives only in notes, it rots. Splitting them, and forcing a handoff at the end of each session, makes any new session productive in minutes.

## Language

Instructions here are in English. Documentation the user will read is generated in the language they choose (`en` or `pt-BR`) from `assets/<lang>/`. Reply to the user in the language they use.

## Entry point: which mode?

1. No `CLAUDE.md` mentioning this method in the project, or the user asks to set up → **Install** (below).
2. Otherwise read the project's `CLAUDE.md`, the Handoff note and the checklist of the current phase, then follow the matching **Daily flow**.

## Install (first use in a project)

Never create anything before the user approves the plan. Never ask for or store secrets (tokens, passwords, keys); `gh` uses the user's own login.

1. **Detect** what exists (`git rev-parse`, `git remote -v`, `gh auth status`, existing `docs/`, `CLAUDE.md`, `.obsidian/`). Pre-fill answers from this so the user only confirms. If `gh` is missing or not logged in, say so up front: the vault and CLAUDE.md still work, but the GitHub steps need it (install from https://cli.github.com, then the user runs `gh auth login` themselves; never handle their token).
2. **Ask** the questions in `references/install-questionnaire.md`, using the AskUserQuestion tool when available, at most 4 questions per call, in the order given. Skip those already answered by detection.
3. **Write the config** as JSON (schema in the questionnaire) to a scratch location outside the repo.
4. **Show the plan**: run `python <skill>/scripts/scaffold.py --config <cfg> --dry-run` and list the GitHub steps that will run. Wait for an explicit OK.
5. **Scaffold**: run the same command without `--dry-run`. It never overwrites existing files.
6. **GitHub setup** (only if the user opted in), one step at a time, confirming each before running it. Commands and order are in `references/github-workflow.md`. Wrappers: `scripts/gh_setup.sh <step>`.
7. **Commit the scaffold first, alone** (`git add -A && git commit -m "chore: tech-lead-vault scaffold"`), before any task work, and push if a remote exists (no remote: record "push pending" in the Handoff). With a dev environment, then create `dev` from `main`. Fill the first Handoff and the first Session Log line.
8. Tell the user what was created and how to start (open the vault in Obsidian, open a first task).

## The non-negotiable rules (they go into the project's CLAUDE.md)

The generated `CLAUDE.md` is the contract future sessions load automatically. Details and the reasoning behind each rule: `references/project-rules.md`.

1. **Living documentation in the same task.** Docs change with the code, before the task is called done.
2. **A checklist per process**, ticked item by item as each is finished (not in a batch at the end).
3. **Definition of Done** before anything is "completed".
4. **Every decision becomes an ADR.**
5. **Dev → production only with the user's OK** (see flow note). Exception: hotfix with explicit OK.
6. **Handoff at the end of every session.**
7. **Commit + push after each progress step.**
8. **Never commit secrets.**
9. **Dates are `YYYY-MM-DD`.**

## Daily flows

Details for each in `references/daily-flows.md`; the short form:

- **Open a task**: create the GitHub issue from the task template (labels area/priority, milestone, board "To do"), create the checklist note in `05-Checklists/` from the task template, link both ways, choose the model by routing (`references/model-routing.md`) if roles are enabled.
- **Record a decision**: new ADR from the ADR template with the next number, append to the decision log, link it from the issue/PR and affected specs.
- **Prepare a release**: follow `references/releases.md` (SemVer, PR `dev → main`, draft release, deploy the tag, verify, publish, rollback = previous tag).
- **Close the session**: tick the checklists, update journal/changelog/spec, add one line to the AI session log, rewrite the Handoff, commit + push, move the board cards.

## Working as Tech Lead

- Plan before coding; split work into small tasks with acceptance criteria.
- When roles are enabled, delegate to the cheapest model able to do the task well; if briefing and reviewing a delegate would cost about the same as doing it, do it yourself.
- Security-, data- and money-sensitive work gets an independent review before it ships.
- Be honest in logs: record failures and partial results, not only successes.

## Bundled files

- `scripts/scaffold.py` - builds vault, CLAUDE.md and `.github/` files from a config (idempotent, `--dry-run`).
- `scripts/gh_setup.sh` - one subcommand per GitHub step (`labels`, `milestones`, `project`, `protect`, `status`).
- `references/` - questionnaire, rules, GitHub workflow, releases, daily flows, model routing, vault structure (`vault-structure.md`).
- `assets/en/`, `assets/pt-BR/` - vault notes, templates, issue/PR templates, CI workflow in each language.
