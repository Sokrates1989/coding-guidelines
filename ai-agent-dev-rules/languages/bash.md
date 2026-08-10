# Bash Development Rules

**Rule ID:** `LANG-BASH`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to Bash scripts or Bash-owned shell workflows.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.4.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Script foundation

Use the repository’s established shebang. For new portable Bash scripts, prefer:

```bash
#!/usr/bin/env bash
#
# One-line responsibility.
#
# Longer boundary or side-effect description when required.
#
set -euo pipefail
```

Do not replace a repository-required `#!/bin/bash` convention without explicit reason.

## Safety and quoting

- Quote expansions unless intentional splitting or globbing is documented.
- Use arrays for command arguments and lists.
- Declare function-local values with `local`; initialize arrays explicitly.
- Use `${value:-default}` for potentially unset optional values.
- Validate arguments before side effects.
- Prefer `printf` over ambiguous `echo` behavior.
- Use `--` before user-controlled path operands when supported.
- Create temporary files with `mktemp` and clean them with traps.

## Functions and errors

When a function requires documentation under `DOC-COMMENTS-DOCSTRINGS`, use the repository’s block format and state arguments, outputs, global state, return codes, and exits when applicable.

Use a shared fatal-error helper when the repository provides one. Do not silently ignore failures. Guard optional commands and provide clear fallback behavior. Avoid pipelines whose failure semantics are unclear.

## Paths and sourcing

Resolve script locations through `BASH_SOURCE` when scripts may be sourced or invoked through symlinks. Source only trusted repository files. Use ShellCheck source annotations where static resolution is impossible.

## Validation

At minimum, run `bash -n` on every changed shell script. When inside a Git worktree, also run `git diff --check`. Run ShellCheck when configured or available in the repository workflow. Execute behavior tests in a disposable environment when the script has side effects.
