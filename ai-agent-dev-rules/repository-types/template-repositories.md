# Template and Generator Repository Rules

**Rule ID:** `REPO-TYPE-TEMPLATE`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing templates, generators, blueprints, recipes, golden outputs, ownership manifests, or generated application trees.  
**Required pages:** `CORE-CHANGE-SAFETY`, `QUALITY-TESTING`, `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Overrides:** None.  
**Ruleset version:** `2.4.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Source ownership

Determine which artifacts are:

- Human-owned inputs.
- Template or recipe source.
- Generator implementation.
- Generated owned files.
- Detached or hand-maintained files.
- Golden/reference outputs.

Change the owning source, not the generated result. A generated golden output is validation evidence, not an alternative template.

## Deterministic lifecycle

- Provide check, plan, or diff behavior before writes when the repository supports it.
- Require exact write intent for destructive or broad generation operations.
- Generate into explicit destinations and reject ambiguous roots.
- Preserve unowned, modified, detached, and human-maintained paths.
- Fail closed when ownership or identity cannot be proven.
- Make multi-repository operations atomic or provide exact rollback of already changed repositories.

## Golden outputs

Update golden outputs only through the generator. Review the resulting diff and run drift validation. Do not normalize unrelated files or run broad formatters from a monorepo root when generation is intended to touch one target.

## Compatibility

Version templates and recipes when generated ownership depends on them. Define migrations for supported managed updates and preserve older generated applications according to the repository’s support policy. Do not silently change package identity, bundle identity, persistence schema, auth contract, or deployment registration.

## Security

Human-owned blueprints and brand inputs contain public configuration only. Secrets, signing keys, provider administration, and deployment credentials remain environment or deployment responsibilities.
