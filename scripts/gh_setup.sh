#!/usr/bin/env bash
# One GitHub setup step per call. The assistant confirms each step with the user first.
# Usage: gh_setup.sh <status|labels|milestones|project|protect> [owner/repo]
# Env:   LANG_SET=en|pt (label names), MILESTONES="v0.1.0 v0.2.0", AREAS="api web",
#        REQUIRE_REVIEW=0|1 (protect), STATUS_CHECK=tests
set -euo pipefail

step="${1:-status}"
repo="${2:-$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)}"
[ -n "$repo" ] || { echo "pass owner/repo or run inside a cloned repo" >&2; exit 1; }
owner="${repo%%/*}"
lang="${LANG_SET:-en}"

label() { gh label create "$1" --color "$2" --description "$3" --force -R "$repo" >/dev/null && echo "label: $1"; }

case "$step" in
  status)
    gh auth status
    gh repo view "$repo" --json nameWithOwner,visibility,defaultBranchRef
    ;;
  labels)
    for a in ${AREAS:-api web}; do label "area:$a" "1d76db" "Area: $a"; done
    label "prio:high" "b60205" "High priority"
    label "prio:medium" "fbca04" "Medium priority"
    label "prio:low" "0e8a16" "Low priority"
    if [ "$lang" = "pt" ]; then
      label "em-dev" "5319e7" "Merged into dev"
      label "esperando-ok" "d93f0b" "Waiting for the owner's OK"
      label "em-producao" "0e8a16" "Running in production"
    else
      label "in-dev" "5319e7" "Merged into dev"
      label "awaiting-ok" "d93f0b" "Waiting for the owner's OK"
      label "in-production" "0e8a16" "Running in production"
    fi
    label "bug" "d73a4a" "Something is broken"
    label "feature" "a2eeef" "New capability"
    label "chore" "cfd3d7" "Maintenance"
    label "docs" "0075ca" "Documentation"
    ;;
  milestones)
    for m in ${MILESTONES:-v0.1.0}; do
      gh api "repos/$repo/milestones" -f title="$m" -f description="Release $m" >/dev/null && echo "milestone: $m"
    done
    ;;
  project)
    # needs the 'project' token scope: the user runs `gh auth refresh -s project` if missing
    title="${repo##*/} board"
    gh project create --owner "$owner" --title "$title" --format json
    echo "Add the Status options To do / In progress / In dev / Awaiting OK / In production in the project settings,"
    echo "then link it: gh project link <number> --owner $owner --repo $repo"
    ;;
  protect)
    reviews=0
    [ "${REQUIRE_REVIEW:-0}" = "1" ] && reviews=1
    check="${STATUS_CHECK:-tests}"
    if [ "$reviews" = "1" ]; then
      rr='{"required_approving_review_count":1}'
    else
      rr='{"required_approving_review_count":0}'
    fi
    gh api -X PUT "repos/$repo/branches/main/protection" --input - <<JSON
{
  "required_status_checks": {"strict": true, "contexts": ["$check"]},
  "enforce_admins": false,
  "required_pull_request_reviews": $rr,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
JSON
    ;;
  *)
    echo "unknown step: $step" >&2
    exit 2
    ;;
esac
