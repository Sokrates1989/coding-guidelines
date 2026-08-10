# Bash CLI Versioning

**Rule ID:** `BASH-CLI-VERSIONING`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing a Bash CLI tool version, version display, release identity, or `VERSION` handling.  
**Required pages:** `REPO-TYPE-BASH-CLI`, `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Overrides:** None.  
**Ruleset version:** `2.2.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## VERSION file

Every applicable tool repository MUST have a root `VERSION` file containing exactly one bare semantic version such as:

```text
1.2.3
```

The file MUST NOT contain a key, `v` prefix, spaces, comments, or extra blank lines. A normal final newline is valid and preferred for a text file.

## Semantic versioning

| Change | Example |
| --- | --- |
| Backward-compatible fix or documentation correction | `1.2.3 -> 1.2.4`. |
| Backward-compatible command or significant behavior | `1.2.3 -> 1.3.0`. |
| Breaking CLI, configuration, or persisted-state contract | `1.2.3 -> 2.0.0`. |

Determine the bump from the user-visible contract, not the number of changed files. Do not invent or bump a version unless requested or required by the exact repository workflow.

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

When the staged `VERSION` file contains a verified new version, the commit subject includes that version under the Git commit-message rules. The version bump remains in the same logical commit as the change that requires it unless the repository explicitly separates release commits.
