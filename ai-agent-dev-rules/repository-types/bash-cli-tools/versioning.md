# Bash CLI Versioning

**Rule ID:** `BASH-CLI-VERSIONING`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing a Bash CLI tool version, version display, release identity, or `VERSION` handling.  
**Required pages:** `REPO-TYPE-BASH-CLI`, `WORKFLOW-SEMANTIC-VERSIONING`  
**Overrides:** None.  
**Ruleset version:** `2.5.0`.  
**Updated:** `2026-08-10`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## VERSION file

Every applicable tool repository MUST have a root `VERSION` file containing exactly one bare semantic version such as:

```text
1.2.3
```

The file MUST NOT contain a key, `v` prefix, spaces, comments, or extra blank lines. A normal final newline is valid and preferred for a text file.

## Semantic versioning

Use `WORKFLOW-SEMANTIC-VERSIONING` to decide whether to bump and to calculate patch, minor, and major versions. In particular, CLI version components are unbounded integers: `1.9.0` advances to `1.10.0` for a minor release, never to `2.0.0` merely because the minor component reached `9`.

## Reading the version

Use the shared helper when available. Setup code that cannot load shared libraries MAY read and trim the file directly. Never hardcode the version in multiple scripts.

## Display contract

When the exact repository uses these surfaces, display the same version consistently in:

- The first line of inline top-level help.
- Guided setup introductions.
- Workflow summaries.
- Install and update completion output.
- Explicit version output.

Do not force a version line into machine-readable output whose contract forbids it.

## Commits

When the staged `VERSION` file contains a verified new version, the commit subject includes that exact version under the Git commit-message rules. The commit message MUST NOT calculate a separate next version. The version bump remains in the same logical commit as the change that requires it unless the repository explicitly separates release commits.
