# Dependencies and Compatibility

**Rule ID:** `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Status:** Active.  
**Applies when:** Dependencies, package manifests, lock files, public interfaces, version constraints, or compatibility behavior may change.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.3.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Dependencies

- Inspect the repository’s package manifest, lock file, configured package manager, and existing utilities before adding a dependency.
- Prefer the standard library and an existing approved dependency when they meet the requirement.
- Add a production dependency only when its necessity, maintenance, security, license, and runtime cost are acceptable.
- Do not perform unrelated dependency upgrades.
- Update lock files only through the repository-defined package manager or generator.
- Report every new direct dependency and why it is needed.

Routine imports do not need to be repeated in every docstring. Document only non-obvious architectural, runtime, optional, or externally provisioned dependencies.

## Compatibility

- Preserve existing public APIs, persisted formats, environment variable contracts, CLI syntax, routes, and generated ownership unless the task explicitly requires change.
- Prefer additive transitions and deprecation periods for externally consumed interfaces.
- Document breaking changes prominently and provide a migration path.
- Keep types, schemas, validation, documentation, and tests synchronized.
- Do not change a default silently when existing users can observe it.

## Configuration

Keep raw configuration loading separate from parsing and domain transformation when the repository defines that boundary. Validate values before side effects. Never place secrets or environment-specific values into tracked defaults.
