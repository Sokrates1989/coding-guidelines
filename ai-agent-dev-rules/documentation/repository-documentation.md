# Repository Documentation

**Rule ID:** `DOC-REPOSITORY-DOCUMENTATION`  
**Status:** Active.  
**Applies when:** Plans, investigations, README files, architecture documents, setup instructions, API documentation, migration guides, operational runbooks, or companion documents are created, changed, planned, reviewed, or diagnosed.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-09-10`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Source of truth

- `docs/` contains authoritative documentation of what the system currently is.
  Documentation MUST describe current implemented behavior, not intended future
  behavior.
- Commands, paths, environment variables, ports, routes, and file names MUST be verified against the repository.
- Do not duplicate detailed rules or contracts already owned by another document; link to the canonical source.
- Keep generated documentation and hand-maintained documentation clearly distinguished.

## Knowledge locations

The paths below are the default convention. A more specific repository rule MAY
define an equivalent authoritative location or structure; follow that convention
instead of creating a competing `docs/` hierarchy. In every structure, keep one
authoritative current-state documentation location, one active-plan location,
clearly separated historical material, explicitly non-authoritative and
potentially stale investigations, and disposable non-authoritative temporary
material.

- `plans/active/` contains active implementation plans describing what should
  become. Plans MUST NOT be treated as evidence of current implemented behavior.
  Completed plans move to `plans/archive/` and remain historical records rather
  than authoritative current-state documentation.
- `investigations/` contains dated, point-in-time analysis: debugging evidence,
  hypotheses, corrected assumptions, and durable investigation checkpoints.
  Investigation documents MUST distinguish verified findings from hypotheses
  and identify their date and relevant scope. They may become stale and MUST NOT
  be treated as current architectural truth.
- Before context compaction, handoff, or a session change can make a long
  investigation unreliable, persist its important evidence, corrected
  assumptions, and unresolved questions in `investigations/`. Promote stable,
  verified current-state findings to `docs/`; place actionable future work in an
  active plan.
- `temp/` is disposable, non-authoritative working material. Repositories SHOULD
  ignore the root `/temp/` directory in Git, and required evidence or knowledge
  MUST NOT exist only there.
- `AGENTS.md` and equivalent agent entry points SHOULD remain concise maps to
  authoritative rules and documentation. Link to canonical content instead of
  turning entry points into duplicated knowledge stores.

## Knowledge lifecycle

Use this flow while preserving evidence appropriate to each stage:

1. Investigate uncertain behavior and checkpoint durable findings in a dated
   `investigations/` document when the work is long-running or likely to cross a
   context boundary.
2. Move verified descriptions of the current system into `docs/`, and move
   approved actionable changes into `plans/active/`.
3. Implement from the active plan, keeping investigation evidence separate from
   current-state claims.
4. In the same coherent change, update relevant `docs/` when implementation,
   architecture, contracts, deployment, security, or documented behavior
   changes.
5. After implementation and required acceptance are complete, move the plan to
   `plans/archive/` without presenting it as current documentation.

## Plans and implementation slices

- Unless a more specific repository rule defines an equivalent location,
  implementation plans MUST be written to `plans/active/` directly under the
  root of the repository most affected by the work. A cross-repository plan MUST
  have exactly one authoritative home there; other repositories link to it
  instead of maintaining duplicate plans, status records, or acceptance
  checklists.
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
- Keep the single active plan current as work proceeds, recording evidence and
  open decisions in place. When archiving or otherwise relocating a plan, update
  references and remove the superseded copy without rewriting historical
  evidence.

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
