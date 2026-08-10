# CI/CD Workflow Rules

**Rule ID:** `WORKFLOW-CI-CD`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to CI pipelines, workflow automation, build gates, artifact publication, or deployment automation.  
**Required pages:** `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.1.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Scope

Do not modify CI/CD merely because application code changed. Load this page only when the task or exact repository rules require pipeline work.

## Pipeline design

- Reuse repository-defined commands so local and CI validation remain aligned.
- Pin actions, images, runtimes, and dependencies according to repository security policy.
- Use least-privilege permissions and protected secret stores.
- Keep secrets out of logs, artifacts, caches, and untrusted pull-request contexts.
- Make quality gates deterministic and fail with actionable messages.
- Separate validation, build, publication, and deployment stages.
- Preserve artifact provenance and exact version identity.

## Publication and deployment

CI MUST NOT publish or deploy when the exact repository reserves those actions for an operator-controlled workflow. Do not turn a quality-only pipeline into a release pipeline without explicit authorization.

For deployment automation, require environment protection, explicit targets, rollback behavior, concurrency control, and post-deployment verification.

## Validation

Validate workflow syntax, referenced paths, commands, permissions, conditions, matrices, caches, artifacts, and secret names. Review behavior for forks, pull requests, default branches, tags, retries, and cancellation.
