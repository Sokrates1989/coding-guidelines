# Change Safety and Scope

**Rule ID:** `CORE-CHANGE-SAFETY`  
**Status:** Active.  
**Applies when:** Every task that may modify repository files, configuration, data, or environments.  
**Required pages:** `ROOT-ROUTER`, `CORE-OPERATING-CONTRACT`  
**Overrides:** None.  
**Ruleset version:** `2.7.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Preserve existing work

- When inside a Git worktree, MUST inspect `git status --short` before editing.
- When no Git worktree exists, MUST inspect the relevant directory and file state closely enough to distinguish pre-existing content from the planned changes.
- MUST preserve unrelated uncommitted and untracked work.
- MUST NOT use `git reset`, `git clean`, destructive checkout commands, forced pushes, or unsolicited stashing.
- MUST NOT revert another author’s change merely because it is unrelated or unfamiliar.
- MUST isolate edits to the requested logical change and its necessary tests, documentation, configuration, and generated outputs.

## Minimal coherent scope

- MUST NOT perform unrelated cleanup, broad reformatting, renaming, dependency upgrades, or architecture changes.
- Apply current standards to new and materially modified code.
- Report larger pre-existing problems separately unless they block the requested change.
- Existing files above a size threshold do not automatically authorize a full refactor during an unrelated fix.
- When a required fix would expand into a risky or broad migration, stop and explain the smallest safe options.

## Secrets and sensitive data

- MUST NOT expose, log, paste, commit, or echo secrets, private keys, access tokens, passwords, production connection strings, or complete private environment files.
- Use placeholders in documentation and `.env.example` or `.env.template` files.
- MUST NOT weaken authentication, authorization, TLS, CORS, validation, or secret handling merely to make a test pass.
- Inspect downloaded or elevated scripts before execution.

## Generated, vendored, and external content

- MUST NOT manually edit generated files, vendor code, build output, minified assets, lock files, snapshots, or submodule contents unless the applicable workflow explicitly requires it.
- Modify the source, template, generator, or package declaration and regenerate through the repository-defined command.
- Lock files MUST be changed only through the repository’s package manager or documented generator.
- Avoid unrelated generated diffs.

## Side effects

Before commands that can alter databases, containers, remote branches, registries, cloud resources, production systems, or user data:

1. Confirm the command is necessary for the current task.
2. Identify its target environment.
3. Prefer a plan, diff, dry-run, or read-only command first.
4. Require explicit authorization for destructive, paid, production, or externally visible actions.
