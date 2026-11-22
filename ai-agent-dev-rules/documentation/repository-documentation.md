# Repository Documentation

**Rule ID:** `DOC-REPOSITORY-DOCUMENTATION`  
**Status:** Active.  
**Applies when:** Plans, investigations, README files, architecture documents, setup instructions, API documentation, migration guides, operational runbooks, or companion documents are created, changed, planned, reviewed, or diagnosed, or an implementation plan is executed.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-09-26`.  
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
authoritative current-state documentation location and, when durable plans are
needed, one active-plan location. Keep historical material, explicitly
non-authoritative and potentially stale investigations, and disposable
non-authoritative temporary material separate.

- `plans/active/` contains durable active implementation plans describing what
  should become. A short internal or conversational working checklist is not a
  durable plan and need not be stored there. Plans MUST NOT be treated as
  evidence of current implemented behavior. Completed plans move to
  `plans/archive/` and remain historical records rather than authoritative
  current-state documentation.
- `investigations/` contains dated, point-in-time analysis: debugging evidence,
  hypotheses, corrected assumptions, and durable investigation checkpoints.
  Investigation documents MUST distinguish verified findings from hypotheses
  and identify their date and relevant scope. They may become stale and MUST NOT
  be treated as current architectural truth.
- Before context compaction, handoff, or a session change can make a long
  investigation unreliable, persist its important evidence, corrected
  assumptions, and unresolved questions in `investigations/`. Promote stable,
  verified current-state findings to `docs/`; place actionable future work in an
  active plan when a durable plan is warranted.
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
2. Move verified descriptions of the current system into `docs/`. When a
   durable plan is warranted, place it in `plans/active/` for review and mark
   any required approach approval as pending until obtained.
3. Implement from the active plan when one exists, keeping investigation
   evidence separate from current-state claims.
4. In the same coherent change, update relevant `docs/` when implementation,
   architecture, contracts, deployment, security, or documented behavior
   changes.
5. After implementation and required acceptance are complete, move a durable
   plan to `plans/archive/` without presenting it as current documentation.
   If manual acceptance remains pending, report implementation and validation
   status separately and keep the plan active.

## Plans and implementation milestones

- Unless a more specific repository rule defines an equivalent location,
  durable implementation plans MUST be written to `plans/active/` directly
  under the root of the repository most affected by the work. A cross-repository
  plan MUST have exactly one authoritative home there; other repositories link
  to it instead of maintaining duplicate plans, status records, or acceptance
  checklists.
- A multi-stage durable plan MUST use ordered milestones; a single-stage plan
  MAY define one milestone without artificial phases. Use as few milestones as
  possible and as many as necessary for coherent implementation and meaningful
  validation. Respect an operator's milestone limit; ask before exceeding it
  when safety or coherence requires more.
- A plan requiring operator approval MUST state the proposed approach, any
  material alternatives and trade-offs, the decision requested, acceptance
  criteria, major risks, and validation and rollback strategy. Obtain approval
  before dependent implementation unless the approach was already approved.
- Each milestone MUST define its outcome, affected areas or repositories,
  dependencies, and validation method, automated where feasible. State
  implementation boundaries, rollback, and compatibility considerations where
  material. A milestone MAY contain multiple focused commits; neither a commit
  nor a conversation turn automatically defines a milestone.
- Include operator manual testing instructions only where human observation is
  needed for a material decision or required acceptance. State what to observe,
  how to check it, and the expected result. Do not create a human checkpoint
  solely because a milestone ends.
- Plans MUST identify the human decisions and authorizations actually required,
  if any, and why. Do not add approval gates for routine milestones. Distinguish
  implementation completion, automated validation, manual acceptance, and
  deployment status. Do not skip an agreed operator checkpoint or report unrun
  acceptance as passed.
- Keep the single active plan current at material milestones and decisions,
  recording evidence and open questions in place. When archiving or otherwise
  relocating a plan, update references and remove the superseded copy without
  rewriting historical evidence.

## Recommend an execution model

Every implementation plan delivered to the operator MUST recommend a specific
model and reasoning level in both the written plan and the chat that delivers
it. Check the current models and supported reasoning levels in the intended
execution environment. Prefer its live catalog or current account-specific model
picker. If needed, consult current official provider information and identify
any account availability that still needs confirmation. Record the source and
check date. A model name from an older plan alone cannot establish availability.

Choose the least costly pair likely to implement and validate the work reliably.
Explain the choice using task complexity, failure impact, and verification needs.
State the preferred model/effort pair or range and which nearby alternatives can
safely execute with a warning. When milestones need materially different
capabilities or effort, identify each exception and its scope. Base the range
on the task independently of the model that wrote the plan.

## Execution model check

Before implementation, including delegation or any side effects, compare the
executor's actual model **and** reasoning level with the recommendation for the
current scope. Use trusted session metadata or the operator's identification
of the active selection. A catalog establishes available choices only. Recheck
on handoff, model or effort changes, and transitions to a differently rated
milestone. For an older plan with missing or obsolete guidance, derive and
report a current recommendation before executing and record it with the plan.

| Fit | Required action |
| --- | --- |
| Preferred | Proceed and record the actual pair and fit in the execution summary. |
| Nearby and viable | Proceed. Lead the execution summary with a **Model fit warning** giving the actual and preferred pairs, why the executor was sufficient, and the capability or cost trade-off. |
| Severe mismatch | Immediately stop plan execution, including delegated work on the mismatched scope. Prominently report the mismatch and the suitable replacement. Resume after the selection changes or the operator explicitly overrides this mismatch. |

A severe mismatch can mean insufficient capability or materially excessive
resource use, such as a lightweight low-effort executor assigned high-risk
authorization design, or a flagship at its highest effort assigned a simple,
low-risk change. Assess an unlisted pair against the plan's rationale. When
missing model or effort information could change the decision, obtain the
missing selection before executing. Preserve the stated range and report any
explicit override in the execution summary.

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
