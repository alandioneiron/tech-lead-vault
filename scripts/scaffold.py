#!/usr/bin/env python3
"""Build the vault, CLAUDE.md and .github files from a JSON config.

Usage:
    python scaffold.py --config cfg.json [--target DIR] [--dry-run] [--force]

Never overwrites existing files unless --force. Writes LF line endings.
Template placeholders look like {{PROJECT_NAME}}; blocks can be conditional:
    <!-- IF:ROLES --> ... <!-- ENDIF:ROLES -->   (also DEVENV)
A file whose first lines contain `requires: roles` is skipped when roles are off.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
DEFAULTS = {
    "project_name": "Example Project",
    "project_summary": "",
    "lang": "en",
    "owner": "",
    "repo": "",
    "visibility": "private",
    "vault_dir": ".",
    "production": "none",
    "dev_env": True,
    "approval": "owner",
    "test_command": "",
    "roles": True,
    "initial_version": "v0.1.0",
    "date": "",
}


def setup_steps(test_command):
    """CI preparation steps inferred from the test command (empty when unknown)."""
    cmd = (test_command or "").strip()
    first = cmd.split()[0] if cmd else ""
    steps = []
    if first in ("npm", "npx", "pnpm", "yarn", "node"):
        steps = ["- uses: actions/setup-node@v4", "  with:", "    node-version: 20"]
        if first == "pnpm":
            steps += ["- run: npm install -g pnpm", "- run: if [ -f pnpm-lock.yaml ]; then pnpm install --frozen-lockfile; else pnpm install; fi"]
        elif first == "yarn":
            steps += ["- run: if [ -f yarn.lock ]; then yarn install --frozen-lockfile; else yarn install; fi"]
        else:
            steps += ["- run: if [ -f package-lock.json ]; then npm ci; else npm install; fi"]
    elif first in ("pytest", "python", "python3", "uv"):
        steps = ["- uses: actions/setup-python@v5", "  with:", "    python-version: '3.12'",
                 "- run: if [ -f requirements.txt ]; then pip install -r requirements.txt; fi; pip install pytest"]
    elif first == "go":
        steps = ["- uses: actions/setup-go@v5", "  with:", "    go-version: stable"]
    elif first in ("dotnet",):
        steps = ["- uses: actions/setup-dotnet@v4", "  with:", "    dotnet-version: 8.0.x"]
    return "".join("      " + s + "\n" for s in steps)


def render(text, cfg):
    flags = {"ROLES": cfg["roles"], "DEVENV": cfg["dev_env"]}
    for name, on in flags.items():
        pat = re.compile(r"<!-- IF:%s -->\n?(.*?)<!-- ENDIF:%s -->\n?" % (name, name), re.S)
        text = pat.sub(lambda m: m.group(1) if on else "", text)
    values = {
        "PROJECT_NAME": cfg["project_name"],
        "PROJECT_SUMMARY": cfg["project_summary"],
        "DATE": cfg["date"],
        "VERSION": cfg["initial_version"],
        "TEST_COMMAND": cfg["test_command"] or "echo 'no tests yet'",
        "SETUP_STEPS": setup_steps(cfg["test_command"]),
        "OWNER": cfg["owner"],
        "REPO": cfg["repo"],
        "VAULT_DIR": cfg["vault_dir"],
        "MAIN_BRANCH": "main",
        "DEV_BRANCH": "dev" if cfg["dev_env"] else "main",
        "PRODUCTION": cfg["production"],
        "APPROVAL": cfg["approval"],
    }
    return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: str(values.get(m.group(1), m.group(0))), text)


def destinations(cfg, lang_dir):
    """Yield (source, relative destination) pairs."""
    vault_prefix = Path("." if cfg["vault_dir"] in (".", "") else cfg["vault_dir"])
    for src in sorted((lang_dir / "vault").rglob("*.md")):
        yield src, vault_prefix / src.relative_to(lang_dir / "vault")
    yield lang_dir / "CLAUDE.md", Path("CLAUDE.md")
    yield SKILL / "assets" / "gitignore", Path(".gitignore")
    yield SKILL / "assets" / "gitattributes", Path(".gitattributes")
    gh = lang_dir / "github"
    mapping = {
        "ISSUE_TEMPLATE/task.md": ".github/ISSUE_TEMPLATE/task.md",
        "pull_request_template.md": ".github/pull_request_template.md",
        "workflows/tests.yml": ".github/workflows/tests.yml",
    }
    for rel, dest in mapping.items():
        if (gh / rel).exists():
            yield gh / rel, Path(dest)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--target", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    # Windows consoles default to a legacy code page; accented file names must print correctly.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    cfg = dict(DEFAULTS)
    cfg.update(json.loads(Path(a.config).read_text(encoding="utf-8")))
    if not cfg["date"]:
        import datetime
        cfg["date"] = datetime.date.today().isoformat()
    lang_dir = SKILL / "assets" / cfg["lang"]
    if not lang_dir.is_dir():
        sys.exit("unknown lang %r (use en or pt-BR)" % cfg["lang"])
    target = Path(a.target).resolve()

    created, skipped, omitted = [], [], []
    for src, rel in destinations(cfg, lang_dir):
        text = src.read_text(encoding="utf-8")
        head = "\n".join(text.splitlines()[:8])
        if "requires: roles" in head and not cfg["roles"]:
            omitted.append(str(rel))
            continue
        text = render(text.replace("requires: roles\n", ""), cfg)
        dest = target / rel
        if dest.exists() and not a.force:
            skipped.append(str(rel))
            continue
        created.append(str(rel))
        if not a.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)

    verb = "would create" if a.dry_run else "created"
    print("%s %d files:" % (verb, len(created)))
    for p in created:
        print("  + " + p)
    if skipped:
        print("skipped %d existing files:" % len(skipped))
        for p in skipped:
            print("  = " + p)
    if omitted:
        print("omitted (roles disabled):")
        for p in omitted:
            print("  - " + p)


if __name__ == "__main__":
    main()
