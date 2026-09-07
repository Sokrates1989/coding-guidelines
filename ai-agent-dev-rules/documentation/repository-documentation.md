# Repository Documentation

**Rule ID:** `DOC-REPOSITORY-DOCUMENTATION`  
**Status:** Active.  
**Applies when:** Plans, README files, architecture documents, setup instructions, API documentation, migration guides, operational runbooks, or companion documents are created, changed, planned, reviewed, or diagnosed.
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Source of truth

- Documentation MUST describe the current implemented behavior, not intended future behavior, unless a section is explicitly labeled as a plan.
- Commands, paths, environment variables, ports, routes, and file names MUST be verified against the repository.
- Do not duplicate detailed rules or contracts already owned by another document; link to the canonical source.
- Keep generated documentation and hand-maintained documentation clearly distinguished.

## Plans and implementation slices

- Implementation plans MUST be written to `plans/` directly under the root of
  the repository most affected by the work. A cross-repository plan MUST have
  exactly one authoritative home there; other repositories link to it instead
  of maintaining duplicate plans, status records, or acceptance checklists.
- Every implementation plan MUST use ordered slices. Use as few slices as
  possible and as many as necessary for coherent architecture, focused commits,
  and meaningful testing or deployment checkpoints. Respect an operator's slice
  limit; explain why before exceeding it.
- Each slice MUST define its outcome, coherent implementation boundary, affected
  areas/repositories, dependencies, automated validation, and rollback or
  compatibility considerations where relevant. A slice may contain multiple
  focused commits; neither a commit nor a conversation turn is automatically a
  slice.
- Each slice MUST explicitly state whether meaningful operator manual testing
  is possible or advisable, what can be observed, how to run it, and what result
  confirms the intended direction. If it is only structural, say so and explain
  why moving directly to the next slice is appropriate or which check blocks it.
- Plans MUST identify review/approval checkpoints and distinguish implementation
  completion, automated validation, manual acceptance, and deployment status.
  Do not skip an agreed operator checkpoint or report unrun acceptance as passed.
- Keep the single plan current as work proceeds, recording evidence and open
  decisions in place. When relocating a plan, update references and remove the
  superseded copy without rewriting historical evidence.

## Required updates

Update relevant documentation when changing:

- Public APIs, CLI commands, options, defaults, or environment variables.
- Setup, build, test, deployment, rollback, or recovery procedures.
- Repository structure, ownership boundaries, generated paths, or extension points.
- Authentication, authorization, data handling, migrations, or compatibility requirements.
- User-visible behavior that existing documentation promises.

## Command examples

- Prefer copy-ready commands for the documented shell.
- State the required working directory and prerequisites when they are not obvious.
- Never include real secrets or production credentials.
- Do not claim a command was verified unless it was run successfully in the documented context.
- Keep Bash and PowerShell variants semantically equivalent when both are supported.

## Navigation and maintenance

Add a table of contents only when it improves navigation. Use descriptive headings and stable relative links. Validate links touched by the change. Remove stale or contradictory instructions rather than appending another competing procedure.
