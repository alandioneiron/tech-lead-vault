---
tags: [coordination, process]
---
# Dev to Production Flow

How a change goes from idea to production.

## Environments
| Environment | Branch | Notes |
|---|---|---|
| Local / CI | any | automated tests, fake data |
<!-- IF:DEVENV -->| Dev | `{{DEV_BRANCH}}` | test data; the owner tries the change here |
<!-- ENDIF:DEVENV -->| Production ({{PRODUCTION}}) | `{{MAIN_BRANCH}}` | real data; only tagged releases |

## The path of a change
1. **Request** becomes a GitHub issue (see [[Template - Task]]) and a checklist note.
2. **Code** on a feature branch; tests green; a security review when it touches permissions, login, automated sending or external input.
3. **Pull request** into `{{DEV_BRANCH}}`; living docs updated; [[Definition of Done]] ticked.
4. **Approval** ({{APPROVAL}}): the approved PR `{{DEV_BRANCH}}` to `{{MAIN_BRANCH}}` is the OK to go to production.
5. **Release**: tag `vX.Y.Z`, draft release with the [[Changelog]] notes, deploy the TAG, verify with [[Promote to Production]], publish the release.
6. **Rollback** = deploy the previous tag.
7. **Docs**: [[Development Journal]], [[Changelog]], [[AI Session Log]], [[Last Agent - Handoff]].

## Rules
- Nothing reaches production without the user's OK. Exception: a hotfix with explicit OK.
- `{{MAIN_BRANCH}}` is production; no direct commits except the promotion merge and hotfixes.
- Secrets never go to git. Real data never goes to dev.
- CI runs tests only: no secrets, no production deploy.
