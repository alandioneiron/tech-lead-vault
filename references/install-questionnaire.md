# Install questionnaire

Ask in this order, at most 4 questions per AskUserQuestion call. Pre-fill from detection and skip what is already known. Offer a "recommended" option first when there is a sensible default. Never ask for tokens, passwords or keys.

## Round 1 - the project
1. **Project name and one sentence about it** (free text). -> `project_name`, `project_summary`
2. **Documentation language**: English / Português (pt-BR). -> `lang` = `en` | `pt-BR`
3. **Git/GitHub**: no repo yet / local repo only / repo on GitHub. If on GitHub: account or org (`owner`), repo name (`repo`), public or private (`visibility`). If none, offer to run `git init -b main` and, later, `gh repo create` (confirmed separately).
4. **Obsidian**: use it? Vault at the repo root or in `docs/`. -> `vault_dir` = `.` or `docs`. (Without Obsidian the notes are still plain Markdown; the wikilinks degrade gracefully.)

## Round 2 - environments and approval
5. **Production**: own server over SSH / cloud / app store / none yet. -> `production` (`ssh`, `cloud`, `appstore`, `none`)
6. **Separate dev/test environment?** yes/no -> `dev_env` (bool). If yes, branch `dev` is used; if no, feature branches go straight to a PR into `main`.
7. **Who approves going to production**: only the owner / team with PR review. -> `approval` (`owner`, `team`)
8. **Test command for CI** (for example `npm test`, `pytest`, `go test ./...`; empty if none yet). -> `test_command`

## Round 3 - GitHub and agents
9. **GitHub extras**, each its own yes/no: labels, milestones, Projects board, protection of `main`. -> `use_labels`, `use_milestones`, `use_board`, `protect_main`
10. **Agent roles**: Tech Lead / Devs / QA with model routing by lowest cost, or a single AI. -> `roles` (bool)
11. **Initial version**: `v0.1.0` for a new project, `v1.0.0` if already in production. -> `initial_version`

Also derive: `date` (today, `YYYY-MM-DD`).

## Config schema (JSON)

```json
{
  "project_name": "Example Project",
  "project_summary": "One sentence.",
  "lang": "en",
  "owner": "example-owner",
  "repo": "example-project",
  "visibility": "private",
  "vault_dir": "docs",
  "production": "ssh",
  "dev_env": true,
  "approval": "owner",
  "test_command": "npm test",
  "use_labels": true,
  "use_milestones": true,
  "use_board": true,
  "protect_main": true,
  "roles": true,
  "initial_version": "v0.1.0",
  "date": "2026-01-31"
}
```

Missing keys fall back to defaults in `scripts/scaffold.py`.

## The plan to show before creating anything

List: the files and folders the scaffold will create (from `--dry-run`), the files skipped because they already exist, and each GitHub step (labels, milestones, board, issue/PR templates, branch protection, CI workflow), noting that each is confirmed again when it runs. Ask "OK to proceed?" and wait.
