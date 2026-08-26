# Bash CLI Auto-Update Guard

**Rule ID:** `BASH-CLI-AUTO-UPDATE`  
**Status:** Active.  
**Applies when:** Implementing, changing, planning, reviewing, or diagnosing an automatic remote update check before command dispatch.  
**Required pages:** `REPO-TYPE-BASH-CLI`, `BASH-CLI-LIFECYCLE`  
**Overrides:** None.  
**Ruleset version:** `2.9.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Safety objective

The guard MAY offer an update before an interactive command, but it MUST never misclassify branch state, break offline use, modify the working tree or current branch merely to check, or update unsafe local work. Fetching remote-tracking metadata without merging is permitted when required for ancestry checks.

## Required state detection

Identify the current branch and configured upstream. Fetch the required remote reference without merging, then distinguish:

- Equal: local and upstream point to the same commit.
- Behind: local is an ancestor of upstream.
- Ahead: upstream is an ancestor of local.
- Diverged: neither is an ancestor of the other.
- Detached: `HEAD` is not on a branch.
- Missing upstream or remote.
- Dirty working tree.
- Remote unavailable.

`git ls-remote` alone can show that object IDs differ, but it cannot prove that local is behind. Ancestry MUST be determined from fetched commit graph data, for example with `git merge-base --is-ancestor`.

## Update eligibility

Offer automatic update only when all conditions hold:

- The session is interactive.
- CI and other non-interactive modes are not active.
- The command is not `update`, `self-update`, version output, completion, or another explicitly exempt command.
- The checkout is clean.
- `HEAD` is attached to the expected branch.
- A configured upstream exists.
- The local branch is strictly behind and not ahead or diverged.
- The configured origin matches the expected repository.

Never auto-update a dirty, ahead, diverged, detached, or ambiguous checkout. Print a concise actionable notice instead when user action is required.

## Offline and frequency behavior

Missing Git, missing checkout, missing remote, authentication failure, timeout, and network failure MUST skip silently or emit only debug output. Normal offline tool use MUST continue.

Cache successful checks for a configurable interval to avoid a network request on every invocation. Do not let stale cache data authorize an update.

## Prompt and replay

The exact repository decides whether Enter defaults to update or decline. The prompt MUST show the current and available version or commit context. On acceptance, use the documented updater, then `exec` the original command with its exact argument array. On decline, continue immediately with the current version.

Preserve quoting and exit codes. Do not reconstruct arguments through a single unsafe string.
