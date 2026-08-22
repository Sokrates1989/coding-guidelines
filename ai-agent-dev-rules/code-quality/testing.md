# Testing

**Rule ID:** `QUALITY-TESTING`  
**Status:** Active.  
**Applies when:** Tests are created, changed, run, reviewed, or required to validate a code change.  
**Required pages:** `CORE-VALIDATION-COMPLETION`, `CORE-CHANGE-SAFETY`  
**Overrides:** None.  
**Ruleset version:** `2.5.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Test intent

- Test observable behavior and stable contracts rather than implementation trivia.
- Add or update tests for new behavior, fixed regressions, error paths, and compatibility-sensitive changes.
- Preserve or improve meaningful coverage; do not chase a numeric target with low-value assertions.
- Do not delete or weaken a failing test merely to make the suite pass unless the tested contract intentionally changed and the reason is documented.

## Before and after

Run a baseline before risky refactors or broad changes when it helps identify pre-existing failures. After changes, run the most focused relevant tests, then broader repository-required checks.

For failures:

1. Capture the exact command and failure.
2. Determine whether it reproduces on the unchanged baseline when feasible.
3. Fix failures introduced by the change.
4. Report confirmed pre-existing or environment-blocked failures without concealing them.

## Test safety

- Default to isolated local test resources, fixtures, and mocks at external boundaries.
- Do not connect tests to production services or real customer data.
- Destructive integration tests require an explicit disposable target and authorization.
- Do not require unavailable credentials for unit tests.
- Avoid flaky timing, network, timezone, locale, and order dependencies.

## Refactors and extraction

Verify imports, circular dependencies, public APIs, configuration, and integration points after code moves. Update test paths and fixtures without changing their behavioral meaning unless required by the task.
