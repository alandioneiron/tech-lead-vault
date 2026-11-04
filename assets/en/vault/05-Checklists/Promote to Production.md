---
tags: [checklist, release]
---
# Promote to Production

- [ ] All work for the version merged into `{{DEV_BRANCH}}`; milestone complete
- [ ] [[Definition of Done]] ticked for every task
- [ ] [[Changelog]] "Unreleased" lists the changes
- [ ] PR `{{DEV_BRANCH}}` to `{{MAIN_BRANCH}}` approved by the owner (this is the OK)
- [ ] Backup taken (if data is involved)
- [ ] Tag `vX.Y.Z` created; draft release with the Changelog notes
- [ ] Deploy of the TAG done
- [ ] Verification: health check, key flows, logs clean
- [ ] Release published ("Latest" = what runs in production)
- [ ] Changelog "Unreleased" renamed to the version and date
- [ ] Issues moved to in-production and closed
- [ ] [[Last Agent - Handoff]] updated

Rollback: deploy the previous tag and log it in [[Development Journal]].
