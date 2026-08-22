# Bash CLI Install, Update, Reset, and Uninstall

**Rule ID:** `BASH-CLI-LIFECYCLE`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing installation, manual update, persisted setup state, reset, guided configuration, or uninstall behavior.  
**Required pages:** `REPO-TYPE-BASH-CLI`, `CORE-CHANGE-SAFETY`  
**Overrides:** None.  
**Ruleset version:** `2.5.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Installation

The installer MUST be idempotent and explicit about installation root, binary link, configuration directory, permissions, installed version, and optional setup. It MUST validate prerequisites before partial writes and preserve existing private configuration unless migration is intentional.

Setup scripts that run before a checkout exists MUST remain self-contained. Do not source unavailable runtime libraries.

## Manual update

A manual update command MUST identify the configured repository and branch, protect dirty or diverged work, update code safely, refresh links and permissions, preserve private configuration and generated outputs, and report the old and new version. It MUST NOT silently discard local commits or modifications.

## Reset

Require a reset command only for tools that persist configuration, credentials, caches, setup state, or generated output.

Reset MUST:

- Remove only documented local setup state by default.
- Preserve the repository checkout and executable code.
- Work before first setup and when optional files are absent.
- Prompt for confirmation unless `--yes` is supplied.
- Support documented path overrides when the tool exposes them.
- Never delete remote data, repositories, backups, or services without a distinct explicit purge option.

Distinguish reset, purge, and uninstall. A generic reset MUST NOT become an undisclosed remote-data deletion operation.

## Uninstall

Uninstall removes installed links, tool-owned runtime files, and man pages. Private configuration is preserved by default unless an explicit purge option is supplied. Show the exact scope before destructive removal.

## Privilege boundaries

Use elevated privileges only for paths and operations that require them. Do not run the entire workflow as root when a narrow installation step is sufficient. Preserve the invoking user’s ownership for user-scoped output.
