# Repository Documentation

**Rule ID:** `DOC-REPOSITORY-DOCUMENTATION`  
**Status:** Active.  
**Applies when:** Plans, README files, architecture documents, setup instructions, API documentation, migration guides, operational runbooks, or companion documents are created, changed, planned, reviewed, or diagnosed.
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.11.0`.  
**Updated:** `2026-09-10`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Source of truth

- Documentation MUST describe the current implemented behavior, not intended future behavior, unless a section is explicitly labeled as a plan.
- Commands, paths, environment variables, ports, routes, and file names MUST be verified against the repository.
- Do not duplicate detailed rules or contracts already owned by another document; link to the canonical source.
- Keep generated documentation and hand-maintained documentation clearly distinguished.

## Knowledge lifecycle and directory conventions

- `docs/` contains authoritative documentation of what the system currently IS. This is the single source of truth for current system behavior, architecture, contracts, deployment, security, and documented operational characteristics. When implementation, architecture, contracts, deployment, security, or documented behavior changes, relevant documentation in `docs/` MUST be updated in the same change or immediately following change.
- `plans/active/` contains active implementation plans describing what SHOULD BECOME. These documents describe intended future work, not current state. Plans are working documents that may change as understanding evolves.
- Completed plans move to `plans/archive/` and remain historical records. Archived plans MUST NOT be treated as authoritative current-state documentation. They preserve decision history and implementation evidence but do not describe the current system.
- `investigations/` contains dated, point-in-time analysis, debugging evidence, hypotheses, corrected assumptions, and durable investigation checkpoints. These documents represent a snapshot of understanding at a specific time and may become stale. They MUST NOT be treated as current architectural truth.
- For long AI-agent investigations, important findings SHOULD be persisted to `investigations/` before context compaction, handoff, or session changes can make them unreliable. Stable verified findings SHOULD eventually be reflected in `docs/`; actionable future work belongs in `plans/active/`.
- `temp/` is disposable, non-authoritative working material. Files in `temp/` are normally ignored by Git and should not be used for persistent knowledge storage.
- Agent entry-point files such as `AGENTS.md` or equivalent MUST remain concise maps to authoritative rules and documentation. They MUST NOT become large duplicated knowledge stores. Point to the canonical sources in `docs/` rather than duplicating content.

## Knowledge lifecycle flow

The durable documentation lifecycle follows this pattern:

1. **Investigation** → findings are recorded in `investigations/` with clear dating and context
2. **Current documentation or plan** → stable verified findings move to `docs/` (current state) or `plans/active/` (future work)
3. **Implementation** → work follows an active plan; changes are made to code and configuration
4. **Documentation update** → as implementation changes behavior, architecture, contracts, deployment, or security, the corresponding `docs/` entries are updated
5. **Plan archive** → when a plan is completed, it moves to `plans/archive/` as historical record

This lifecycle ensures that `docs/` always reflects the current system state, `plans/active/` describes agreed future work, `investigations/` preserves analysis context without becoming stale truth, and agent entry points remain navigable maps rather than knowledge duplications.

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
