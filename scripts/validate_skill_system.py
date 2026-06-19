#!/usr/bin/env python3
"""Validate EvoZeus cluster skill routing contracts.

This is intentionally narrower than a Markdown linter. It checks the contracts
that keep `/skill`, installed skills, runtime routing, and component repos from
drifting apart.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MAIN_REPO = ROOT / "10-repos" / "evozeus"
MAIN_SKILLS_DIR = MAIN_REPO / "skills"
COMMUNITY_SKILL_CONTENT = (
    ROOT / "10-repos" / "evozeus-community" / "src" / "app" / "skill" / "skill-content.ts"
)
COVERAGE_DOC = ROOT / "docs" / "reference" / "skill-coverage.md"

COMPONENT_SKILLS = [
    ROOT / "10-repos" / "evozeus-infra" / "SKILL.md",
    ROOT / "10-repos" / "evozeus-factor-lab" / "SKILL.md",
    ROOT / "10-repos" / "evozeus-factors-official" / "SKILL.md",
]

EXPECTED_NAME_BY_PATH = {
    MAIN_REPO / "SKILL.md": "evozeus",
    MAIN_SKILLS_DIR / "index" / "SKILL.md": "evozeus-skill-index",
}

FORBIDDEN_ACTIVE_PATTERNS = [
    "community/#register",
    "/#register",
    "skills/evozeus-runtime/SKILL.md",
    "skills/evozeus-infra/SKILL.md",
    "# EvoZeus Agent Skill Router",
    "不是单一注册说明",
]

FORBIDDEN_EXCLUDES = {
    ROOT / "docs" / "development-direction" / "skill-system-implementation.md",
    ROOT
    / "10-repos"
    / "evozeus-community"
    / "src"
    / "app"
    / "skill"
    / "route.test.ts",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing opening frontmatter delimiter"]

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, [f"{path}: missing closing frontmatter delimiter"]

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path}: malformed frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")

    return metadata, errors


def formal_skill_paths() -> list[Path]:
    paths = [MAIN_REPO / "SKILL.md"]
    paths.extend(sorted(MAIN_SKILLS_DIR.glob("*/SKILL.md")))
    paths.extend(COMPONENT_SKILLS)
    return paths


def validate_skill_metadata(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    names: dict[str, list[Path]] = defaultdict(list)
    name_pattern = re.compile(r"^[a-z0-9][a-z0-9-]*$")

    for path in paths:
        if not path.exists():
            errors.append(f"{path}: missing formal skill file")
            continue

        metadata, parse_errors = parse_frontmatter(path)
        errors.extend(parse_errors)

        name = metadata.get("name", "")
        description = metadata.get("description", "")

        if not name:
            errors.append(f"{path}: missing frontmatter name")
        elif not name_pattern.match(name):
            errors.append(f"{path}: invalid skill name {name!r}")
        else:
            names[name].append(path)

        if not description:
            errors.append(f"{path}: missing frontmatter description")
        elif not description.startswith("Use when"):
            errors.append(f"{path}: description must start with 'Use when'")

        expected_name = EXPECTED_NAME_BY_PATH.get(path)
        if expected_name is None and path.parent.parent == MAIN_SKILLS_DIR:
            expected_name = path.parent.name
        elif expected_name is None and path in COMPONENT_SKILLS:
            expected_name = path.parent.name

        if expected_name and name and name != expected_name:
            errors.append(f"{path}: expected name {expected_name!r}, found {name!r}")

    for name, paths_for_name in sorted(names.items()):
        if len(paths_for_name) > 1:
            joined = ", ".join(str(path) for path in paths_for_name)
            errors.append(f"duplicate skill name {name!r}: {joined}")

    return errors


def validate_community_bootstrap_scope() -> list[str]:
    errors: list[str] = []
    if not COMMUNITY_SKILL_CONTENT.exists():
        return [f"{COMMUNITY_SKILL_CONTENT}: missing community skill content"]

    text = COMMUNITY_SKILL_CONTENT.read_text(encoding="utf-8")
    required_tokens = [
        "# EvoZeus Community Bootstrap Skill",
        "root \\`SKILL.md\\`",
        "不要在 bootstrap skill 里复制完整 scenario routing",
        "npm run test:infra-components",
    ]

    for token in required_tokens:
        if token not in text:
            errors.append(f"{COMMUNITY_SKILL_CONTENT}: missing bootstrap token {token!r}")

    forbidden_tokens = [
        "skills/evozeus-runtime/SKILL.md",
        "skills/evozeus-infra/SKILL.md",
        "skills/evozeus-runtime-routing",
        "EvoZeus skills inventory",
    ]

    for token in forbidden_tokens:
        if token in text:
            errors.append(f"{COMMUNITY_SKILL_CONTENT}: community bootstrap duplicates routing token {token!r}")

    return errors


def validate_docs_coverage(skill_paths: list[Path]) -> list[str]:
    errors: list[str] = []
    if not COVERAGE_DOC.exists():
        return [f"{COVERAGE_DOC}: missing skill coverage doc"]

    text = COVERAGE_DOC.read_text(encoding="utf-8")
    required_tokens = [
        "evozeus-install-registration",
        "evozeus-runtime-routing",
        "evozeus-infra/SKILL.md",
        "evozeus-factor-lab/SKILL.md",
        "evozeus-factors-official/SKILL.md",
    ]

    for token in required_tokens:
        if token not in text:
            errors.append(f"{COVERAGE_DOC}: missing coverage token {token!r}")

    main_skill_folders = {
        path.parent.name
        for path in skill_paths
        if path.parent.parent == MAIN_SKILLS_DIR and path.parent.name != "index"
    }
    for folder in sorted(main_skill_folders):
        if folder not in text:
            errors.append(f"{COVERAGE_DOC}: missing main skill row for {folder}")

    return errors


def validate_forbidden_active_references() -> list[str]:
    errors: list[str] = []
    search_roots = [
        ROOT / "00-global",
        ROOT / "docs",
        ROOT / "10-repos" / "evozeus",
        ROOT / "10-repos" / "evozeus-community" / "src" / "app",
    ]

    for search_root in search_roots:
        for path in sorted(search_root.rglob("*")):
            if path in FORBIDDEN_EXCLUDES or not path.is_file():
                continue
            if any(part in {"node_modules", ".next", ".git"} for part in path.parts):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in FORBIDDEN_ACTIVE_PATTERNS:
                if pattern in text:
                    errors.append(f"{path}: forbidden active reference {pattern!r}")

    old_runtime_skill = MAIN_SKILLS_DIR / "evozeus-runtime" / "SKILL.md"
    if old_runtime_skill.exists():
        errors.append(f"{old_runtime_skill}: old main-repo runtime skill must not exist")
    old_infra_skill = MAIN_SKILLS_DIR / "evozeus-infra" / "SKILL.md"
    if old_infra_skill.exists():
        errors.append(f"{old_infra_skill}: infra component skill must not live in main repo skills")

    return errors


def main() -> int:
    skill_paths = formal_skill_paths()
    errors: list[str] = []
    errors.extend(validate_skill_metadata(skill_paths))
    errors.extend(validate_community_bootstrap_scope())
    errors.extend(validate_docs_coverage(skill_paths))
    errors.extend(validate_forbidden_active_references())

    if errors:
        print("Skill system validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Skill system validation passed for {len(skill_paths)} formal skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
