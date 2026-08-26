# Database Migration Rules

**Rule ID:** `WORKFLOW-DATABASE-MIGRATIONS`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing database schemas, migration files, persisted data transformations, or compatibility between application and database versions.  
**Required pages:** `CORE-CHANGE-SAFETY`, `QUALITY-TESTING`, `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Overrides:** None.  
**Ruleset version:** `2.9.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Migration design

- Use the repository’s migration framework and naming/order conventions.
- Prefer additive, backward-compatible expand-and-contract transitions.
- Separate schema changes from large data backfills when operational risk warrants it.
- Make destructive changes explicit and require authorization, backup, compatibility analysis, and a rollback or recovery plan.
- Avoid application deployments that require an instantaneous incompatible schema switch.

## Data safety

- Never run a migration against production or real user data without explicit authorization.
- Use transactions when the database and operation support them.
- Make long-running operations observable and resumable where practical.
- Preserve constraints, indexes, defaults, timezone semantics, and null behavior intentionally.
- Do not embed credentials or environment-specific endpoints in migrations.

## Validation

Test migration from the supported previous state, clean database creation, application compatibility, downgrade or recovery behavior where supported, and relevant data invariants. Record commands and database engine/version.

Update models, schemas, repositories, fixtures, API contracts, and documentation in the same logical change.
