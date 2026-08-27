# Bash CLI Tool Testing

**Rule ID:** `BASH-CLI-TESTING`  
**Status:** Active.  
**Applies when:** Validating, planning, reviewing, or diagnosing changes to an applicable Bash CLI tool.  
**Required pages:** `REPO-TYPE-BASH-CLI`, `QUALITY-TESTING`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Mandatory static checks

Run syntax checks for every changed Bash file. When inside a Git worktree, also run whitespace validation before a commit:

```bash
bash -n <changed-script-1> <changed-script-2>
git diff --check
```

Use ShellCheck when configured or available in the repository workflow. Do not expand a glob that can pass a literal nonexistent path; build the file list safely.

## Smoke tests

Test the surfaces affected by the change, including:

- Top-level help and version output.
- Every changed command’s help.
- Unknown-command and missing-argument behavior.
- Offline behavior.
- Non-interactive behavior.
- Reset help before private configuration exists.
- Update commands bypassing the auto-update guard.
- Dry-run or plan mode before execution mode.

## Integration tests

Exact tool repository pages define server paths, backends, credentials, reset sequences, and expected artifacts. Do not reuse another tool’s integration sequence by assumption.

Integration tests MUST use a disposable or explicitly authorized target, verify persisted output and cleanup behavior, and record exact commands. Never declare a release phase complete from syntax checks alone when the changed behavior requires installation or server execution.
