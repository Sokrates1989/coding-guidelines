# Validation and Completion

**Rule ID:** `CORE-VALIDATION-COMPLETION`  
**Status:** Active.  
**Applies when:** Every task that changes or reviews repository content.  
**Required pages:** `ROOT-ROUTER`, `CORE-OPERATING-CONTRACT`  
**Overrides:** None.  
**Ruleset version:** `2.6.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Validation selection

- Use repository-defined commands before inventing generic commands.
- Run the smallest set that proves the changed behavior, then broader checks when risk or repository policy requires them.
- Run a baseline before a refactor when it is necessary to distinguish pre-existing failures from introduced failures.
- Do not run destructive, production-connected, credential-requiring, unusually expensive, or externally publishing checks without authorization.
- Validate documentation links, configuration syntax, generated ownership, migrations, routes, and deployment manifests when those areas change.

## Validation tiers

Use the lowest tier that provides sufficient evidence for the changed or reviewed behavior, then move upward only when risk, acceptance criteria, or repository policy requires it:

1. Static and local checks: parsing, linting, typing, unit tests, rendering, and local build proof.
2. Disposable integration checks: isolated containers, temporary databases, generated targets, and test services that cannot affect persistent or shared data.
3. Staging or shared-environment checks: externally visible or shared resources used only with an identified target and applicable authorization.
4. Production checks: production-connected validation performed only when explicitly requested and authorized.

Passing a lower tier MUST NOT be reported as evidence that an unexecuted higher tier succeeded.

## Truthful reporting

- MUST record the exact commands actually run.
- MUST distinguish passing checks, failing checks, skipped checks, and checks blocked by the environment.
- MUST distinguish confirmed pre-existing failures from failures introduced by the change.
- MUST NOT say “all tests pass,” “build succeeds,” or equivalent when the complete referenced command was not run successfully.
- When validation cannot be completed, state precisely what prevented it and what remains unverified.

## Completion record

Finish code-changing work with a concise record in this form:

```text
Rules loaded:
Files changed:
Validation run:
Validation not run:
Known limitations:
```

List rule IDs rather than repeating rule text. Mention only material files and checks. Do not hide warnings, partial validation, or scope deviations.

## Definition of done

Work is complete only when:

- The requested behavior and acceptance criteria are satisfied.
- Applicable documentation and tests are synchronized.
- No known unrelated changes were introduced.
- Required validation was executed or transparently reported as unavailable.
- The final summary accurately describes the resulting repository state.
