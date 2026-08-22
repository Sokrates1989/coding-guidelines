# PowerShell Development Rules

**Rule ID:** `LANG-POWERSHELL`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to PowerShell scripts, modules, or PowerShell-owned workflows.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.5.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Script foundation

Follow the repository’s supported PowerShell version. Use strict and terminating error behavior when compatible with the existing script:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
```

Do not add strict mode blindly to a legacy script without validating all affected paths.

## Functions and parameters

- Use approved verb-noun names for reusable functions.
- Use comment-based help for exported and non-obvious functions under `DOC-COMMENTS-DOCSTRINGS`; tiny self-explanatory local helpers may use the global exception.
- Declare parameter types and validation attributes where they improve correctness.
- Use `[CmdletBinding()]` for advanced functions and scripts that need common parameters or `ShouldProcess`.
- Use `-WhatIf`/`ShouldProcess` for destructive or externally visible operations when practical.

## Reliability

- Use `Join-Path`, resolved provider paths, and explicit encodings.
- Avoid parsing formatted display output when structured objects are available.
- Preserve objects through pipelines; format only at the presentation boundary.
- Use splatting for long command invocations.
- Do not hide errors with broad `try/catch`; add context and rethrow or return a defined failure.
- Never embed secrets in scripts or command history.

## Cross-shell wrappers

When PowerShell wraps an authoritative Bash implementation, keep business logic in Bash and forward arguments without reimplementing behavior. Maintain equivalent exit codes, output contracts, and cancellation semantics.

## Validation

Parse changed scripts, run PSScriptAnalyzer when configured, and execute focused tests in the supported shell. Keep generated commit-message commands native to the active shell.
