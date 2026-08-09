#!/usr/bin/env python3
"""Validate the repository-local AI Agent Development Rules package.

The validator checks repository structure, manifest consistency, rule metadata,
dependency IDs and cycles, local Markdown links, page coverage, size budgets,
word-count estimates, and removal of obsolete Wiki source URLs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

CANONICAL_REPOSITORY = "https://github.com/sokrates1989/coding-guidelines"
RULE_ID_PATTERN = re.compile(r"\*\*Rule ID:\*\* `([^`]+)`")
VERSION_PATTERN = re.compile(r"\*\*Ruleset version:\*\* `([^`]+)`")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WORD_PATTERN = re.compile(r"\b[\w'-]+\b")
OBSOLETE_SOURCE_PATTERN = re.compile(r"https://wiki\.fe-wi\.com", re.IGNORECASE)

SIZE_LIMITS = {
    "root-router": 1100,
    "secondary-router": 700,
    "normative": 1400,
    "examples": 2000,
    "repository": 1100,
}

REQUIRED_REPOSITORY_FILES = (
    ".gitattributes",
    "README.md",
    "ai-agent-dev-rules.md",
)

REQUIRED_SUPPORT_FILES = (
    "README.md",
    "rules-manifest.json",
    "llms.txt",
    "codex/AGENTS.md",
    "migration-map.md",
    "validation/validate-ruleset.py",
)


def fail(message: str, errors: list[str]) -> None:
    """Add one validation error to the shared error collection."""
    errors.append(message)


def count_words(text: str) -> int:
    """Return a stable approximate word count for one Markdown page."""
    return len(WORD_PATTERN.findall(text))


def load_manifest(path: Path, errors: list[str]) -> dict[str, Any]:
    """Load the manifest and record a useful error when it is invalid."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Missing manifest: {path}.", errors)
        return {}
    except json.JSONDecodeError as exc:
        fail(f"Invalid manifest JSON at {path}: {exc}.", errors)
        return {}

    if not isinstance(data, dict):
        fail("Manifest root must be a JSON object.", errors)
        return {}

    return data


def detect_dependency_cycles(
    dependencies: dict[str, list[str]], errors: list[str]
) -> None:
    """Detect cycles in the required-page dependency graph."""
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(rule_id: str) -> None:
        """Visit one rule and report a cycle reached through its dependencies."""
        if rule_id in visited:
            return

        if rule_id in visiting:
            cycle_start = stack.index(rule_id)
            cycle = stack[cycle_start:] + [rule_id]
            fail(f"Dependency cycle: {' -> '.join(cycle)}.", errors)
            return

        visiting.add(rule_id)
        stack.append(rule_id)

        for dependency in dependencies.get(rule_id, []):
            if dependency in dependencies:
                visit(dependency)

        stack.pop()
        visiting.remove(rule_id)
        visited.add(rule_id)

    for rule_id in dependencies:
        visit(rule_id)


def validate_repository_structure(
    package_dir: Path, support_dir: Path, errors: list[str]
) -> None:
    """Validate required repository and support files without rejecting Git data."""
    for relative_path in REQUIRED_REPOSITORY_FILES:
        if not (package_dir / relative_path).is_file():
            fail(f"Missing repository file: {relative_path}.", errors)

    rules_dir = package_dir / "ai-agent-dev-rules"
    if not rules_dir.is_dir():
        fail("Missing rule-page directory: ai-agent-dev-rules.", errors)

    for relative_path in REQUIRED_SUPPORT_FILES:
        if not (support_dir / relative_path).is_file():
            fail(f"Missing support file: {relative_path}.", errors)


def resolve_markdown_target(source_file: Path, target: str) -> Path | None:
    """Resolve one relative Markdown rule link or return None when it is external."""
    normalized_target = target.strip().strip("<>")
    if not normalized_target or normalized_target.startswith("#"):
        return None

    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", normalized_target):
        return None

    path_part = unquote(normalized_target.split("#", 1)[0])
    if not path_part.lower().endswith(".md"):
        return None

    return (source_file.parent / path_part).resolve()


def main() -> int:
    """Validate the rules repository and return a process exit code."""
    support_dir = Path(__file__).resolve().parents[1]
    rules_dir = support_dir.parent
    package_dir = rules_dir.parent
    manifest_path = support_dir / "rules-manifest.json"
    errors: list[str] = []

    validate_repository_structure(package_dir, support_dir, errors)

    manifest = load_manifest(manifest_path, errors)
    pages = manifest.get("pages", [])
    version = manifest.get("rulesetVersion")

    if manifest.get("canonicalRepository") != CANONICAL_REPOSITORY:
        fail(
            "Manifest canonicalRepository must identify the canonical GitHub repo.",
            errors,
        )

    if not isinstance(pages, list) or not pages:
        fail("Manifest pages must be a non-empty array.", errors)
        pages = []

    ids: set[str] = set()
    manifested_files: set[Path] = set()
    dependencies: dict[str, list[str]] = {}

    for page in pages:
        if not isinstance(page, dict):
            fail("Every manifest page must be an object.", errors)
            continue

        required_keys = {
            "id",
            "title",
            "file",
            "type",
            "requires",
            "loadWhen",
            "estimatedWords",
        }
        missing_keys = required_keys - page.keys()
        if missing_keys:
            fail(
                f"Manifest page is missing keys {sorted(missing_keys)}: {page}.",
                errors,
            )
            continue

        rule_id = str(page["id"])
        file_path = (package_dir / str(page["file"])).resolve()
        page_type = str(page["type"])
        required_ids = [str(item) for item in page.get("requires", [])]

        dependencies[rule_id] = required_ids

        if rule_id in ids:
            fail(f"Duplicate rule ID: {rule_id}.", errors)
        ids.add(rule_id)

        if file_path in manifested_files:
            fail(f"Duplicate manifest file: {page['file']}.", errors)
        manifested_files.add(file_path)

        if not file_path.is_file():
            fail(f"Missing page file: {page['file']}.", errors)
            continue

        text = file_path.read_text(encoding="utf-8")
        id_match = RULE_ID_PATTERN.search(text)
        version_match = VERSION_PATTERN.search(text)

        if not id_match or id_match.group(1) != rule_id:
            fail(f"Rule ID mismatch in {page['file']}.", errors)

        if not version_match or version_match.group(1) != version:
            fail(f"Ruleset version mismatch in {page['file']}.", errors)

        if not text.endswith("\n"):
            fail(f"Missing final newline in {page['file']}.", errors)

        if OBSOLETE_SOURCE_PATTERN.search(text):
            fail(f"Obsolete Wiki source URL in {page['file']}.", errors)

        limit = SIZE_LIMITS.get(page_type)
        if limit is None:
            fail(f"Unknown page type {page_type} in {page['file']}.", errors)

        word_count = count_words(text)
        if limit is not None and word_count > limit:
            fail(
                f"Page exceeds {page_type} budget: {page['file']} has "
                f"{word_count} words; limit is {limit}.",
                errors,
            )

        if page.get("estimatedWords") != word_count:
            fail(
                f"Word estimate mismatch in {page['file']}: manifest has "
                f"{page.get('estimatedWords')}; actual is {word_count}.",
                errors,
            )

    for rule_id, required_ids in dependencies.items():
        for required_id in required_ids:
            if required_id not in ids:
                fail(f"Unknown dependency {required_id} required by {rule_id}.", errors)

    detect_dependency_cycles(dependencies, errors)

    expected_root = (package_dir / str(manifest.get("rootFile", ""))).resolve()
    if not expected_root.is_file():
        fail(f"Missing root file: {manifest.get('rootFile')}.", errors)

    actual_rule_files = {expected_root}
    actual_rule_files.update(
        path.resolve()
        for path in rules_dir.rglob("*.md")
        if "_support" not in path.parts
    )

    for path in sorted(actual_rule_files - manifested_files):
        fail(f"Unmanifested rule page: {path.relative_to(package_dir)}.", errors)

    for path in sorted(manifested_files - actual_rule_files):
        fail(f"Manifest points outside the rule-page set: {path}.", errors)

    for path in sorted(actual_rule_files):
        text = path.read_text(encoding="utf-8")
        for link_target in MARKDOWN_LINK_PATTERN.findall(text):
            resolved_target = resolve_markdown_target(path, link_target)
            if resolved_target is None:
                continue

            if resolved_target not in manifested_files:
                fail(
                    f"Unknown internal rule link in {path.relative_to(package_dir)}: "
                    f"{link_target}.",
                    errors,
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(pages)} rule pages for ruleset {version}; "
        "dependency graph and relative rule links are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
