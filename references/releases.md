# Releases (SemVer)

Versions are `MAJOR.MINOR.PATCH`: breaking change / new feature / fix. Tags are `vX.Y.Z`. A component with its own cadence (a mobile app, a CLI, a plugin) gets a tag prefix, for example `app-vX.Y.Z`, with its own release notes.

## Flow
1. **Collect**: all work for the version is merged into `dev`; the Changelog "Unreleased" section lists it; the milestone is complete.
2. **PR `dev -> main`**: body lists the changes and ticks the DoD. **The user's approval of this PR is the OK to go to production.** (With `approval=team`, also the required reviews.)
3. **Merge**, then create the **tag** on `main` and a **draft release** whose notes come from the Changelog:
   - `git tag -a vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z`
   - `gh release create vX.Y.Z --draft --title "vX.Y.Z" --notes-file <notes.md>`
4. **Deploy the TAG**, never a moving branch, so what runs is exactly what was approved. Use the project's deploy procedure (back up first when data is involved).
5. **Verify** with the "Promote to Production" checklist (health check, key flows, logs).
6. **Publish** the release. "Latest" on GitHub then equals what runs in production.
7. **Docs**: rename "Unreleased" to the version and date in the Changelog; update the Handoff; mark issues in-production and close them.

## Rollback
Deploy the previous tag. Record the incident in the journal, and an ADR if the cause was a decision. Never delete or rewrite published tags.

## Pre-1.0
`v0.x` means "no stability promise". Move to `v1.0.0` when the project is in production with users.
