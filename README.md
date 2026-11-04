# tech-lead-vault

A Claude Code skill that makes the AI work as the **Tech Lead** of your software project: an **Obsidian vault is the memory** (knowledge, decisions, logs, checklists) and **GitHub is the workflow** (issues, board, PRs, SemVer releases).

Portuguese version: [README.pt-BR.md](README.pt-BR.md)

## What it does

- **Guided install** (first use in a project): asks up to 4 questions at a time (project, language, GitHub account/visibility, Obsidian, production type, dev environment, who approves, test command, board and branch protection, agent roles, initial version), shows the plan, and creates things only after your OK. It never asks for or stores secrets.
- **Builds the vault**: `00-Coordination` ... `99-Templates`, with `Home`, templates (task, ADR, module spec, daily log), Definition of Done, decision log, journal, changelog, AI session log and the handoff note, linked with `[[wikilinks]]`. English or Portuguese (pt-BR).
- **Writes the project `CLAUDE.md`** with the non-negotiable rules: living docs in the same task, a checklist per process, Definition of Done, every decision as an ADR, dev to production only with your OK, handoff at the end of each session, commit and push at each step, no secrets, dates as `YYYY-MM-DD`.
- **GitHub as the workflow** (via `gh`, each step confirmed): labels, milestones, Projects board (To do, In progress, In dev, Awaiting OK, In production), issue and PR templates, branch protection, and a tests-only Actions workflow. The issue holds the status; the vault holds the knowledge.
- **Releases (SemVer)**: PR `dev` to `main` approved = the OK, tag, draft release with the changelog notes, deploy the tag, verify, publish, rollback = previous tag.
- **Daily flows**: open a task, record a decision, prepare a release, close the session.

## Install the skill

Copy the folder into your skills directory:

```bash
git clone <this-repo-url> ~/.claude/skills/tech-lead-vault
```

(Or copy the repository folder to `~/.claude/skills/tech-lead-vault`, or add it through a plugin that bundles skills.) Requirements: Python 3 for the scaffold script; `gh` (GitHub CLI, logged in with `gh auth login`) for the GitHub steps.

## Example

In a project folder, tell Claude:

> Set up this project with tech-lead-vault.

Claude asks the questions, then shows something like:

```
would create 25 files:
  + docs/Home.md
  + docs/00-Coordination/Decision Log (ADR).md
  ...
  + CLAUDE.md
  + .github/workflows/tests.yml
```

After your OK it creates the files, then walks through the GitHub steps one by one. Later:

> Open a task for the login endpoint. / Record the decision to use PostgreSQL. / Prepare release v0.2.0. / Close the session.

You can also run the scaffold directly:

```bash
python scripts/scaffold.py --config my-config.json --target . --dry-run
```

## Layout

```
SKILL.md          main instructions
references/       questionnaire, rules, GitHub workflow, releases, flows, routing
scripts/          scaffold.py, gh_setup.sh
assets/en/        vault notes, CLAUDE.md, .github files (English)
assets/pt-BR/     the same in Portuguese
```

## License

MIT, see [LICENSE](LICENSE).
