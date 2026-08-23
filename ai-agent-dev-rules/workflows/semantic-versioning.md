# Semantic Versioning

**Rule ID:** `WORKFLOW-SEMANTIC-VERSIONING`  
**Status:** Active.  
**Applies when:** A task selects, changes, reviews, or reports a tool, application, package, release, installer, artifact, tag, or commit-message version.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`, `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Overrides:** None.  
**Ruleset version:** `2.8.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Decide whether a bump is required

- MUST NOT change a version merely because files changed, a commit is being created, or a version could be included in a commit message.
- Change the version when the operator requests it or the repository's release, packaging, or version-ownership workflow requires it for the completed change.
- When one release contains several changes, choose the highest impact required by any included change.
- An explicit valid version supplied by the operator is authoritative. Report a conflict instead of silently replacing an invalid value or a value incompatible with an explicit repository policy.

## Numeric format and arithmetic

Use `MAJOR.MINOR.PATCH`, where each component is a whole non-negative integer. Numeric components are not decimal digits and have no maximum width. They MUST NOT carry or roll over at `9`, `99`, or any other value.

| Required bump | Operation | Examples |
| --- | --- | --- |
| Patch | Preserve major and minor; increment patch by one. | `1.9.9 -> 1.9.10`; `1.9.99 -> 1.9.100`. |
| Minor | Preserve major; increment minor by one; reset patch to zero. | `1.9.0 -> 1.10.0`; `1.99.4 -> 1.100.0`. |
| Major | Increment major by one; reset minor and patch to zero. | `1.9.7 -> 2.0.0`; `9.4.2 -> 10.0.0`. |

Consequently, a change after `1.9.0` becomes `1.9.1` when it is a patch and `1.10.0` when it is a minor release. It MUST NOT become `2.0.0` merely because the minor component reached `9`. Apply the same arithmetic beyond `99` and `999`.

Unless an established repository format permits them, numeric core components MUST NOT contain leading zeroes. Preserve repository-defined pre-release and build metadata behavior; do not invent such metadata solely for a routine bump.

## Select the impact level

Use the released, externally observable contract rather than changed-line count, implementation effort, business importance, or the current component values.

### Patch

Increment `PATCH` for backward-compatible corrections and maintenance, including:

- Bug and security fixes that preserve supported public contracts.
- Small compatible behavior, styling, accessibility, performance, or reliability corrections.
- Refactoring, tests, documentation, comments, build, packaging, and dependency maintenance without a new feature or breaking contract.
- Language, translation, localization-resource, spelling, and wording-only changes.

### Minor

Increment `MINOR` for backward-compatible functionality, including:

- New features, commands, screens, options, or supported capabilities.
- Additive APIs, fields, configuration, integrations, and opt-in behavior.
- Compatible feature improvements and deprecations that retain the old contract.

Reset `PATCH` to zero even when its prior value has multiple digits.

### Major

Increment `MAJOR` only when the operator explicitly requests that major version or when repository evidence makes a backward-incompatible released contract unmistakable. Examples include removing or incompatibly changing supported APIs, commands, configuration, protocols, persisted formats, or required user workflows without a compatibility path.

A large feature, extensive refactor, important release, changed file count, or minor/patch value reaching `9` or `99` is not a major-version reason. Reset `MINOR` and `PATCH` to zero after a major bump.

## Automatic decisions and exceptional clarification

- MUST determine patch, minor, or major automatically from the requested change and repository evidence in normal cases.
- MUST NOT ask the operator merely because a component gains another digit or because the choice between patch and minor requires ordinary impact analysis.
- Ask only when inspection leaves material, genuine uncertainty about whether a supported external compatibility boundary is broken and the answer would change the result to or from a major release.
- When no breaking contract exists, resolve remaining uncertainty without escalation by choosing the smallest level that accurately represents the observable change.

## Source of truth and synchronization

- Identify the authoritative version source before editing, such as `VERSION`, `package.json`, `pyproject.toml`, `pubspec.yaml`, installer configuration, or repository release tooling.
- Modify owned sources and use repository-defined generators for derived version files, manifests, lock data, installer metadata, and artifact names.
- Synchronize every repository-required version surface. Search for stale references when versions are duplicated by necessity.
- A commit subject MAY report a version only after reading the staged authoritative value. It MUST match the staged result and MUST NOT calculate, increment, or carry a separate commit-only version.
- Do not create tags, push commits, publish releases, upload artifacts, or deploy merely because a version changed. These remote or externally visible actions require explicit operator authorization.

## Validation

Before completion:

1. Record the previous version and classify the release impact from the actual coherent change.
2. Recalculate the new version component-wise and confirm no decimal carry occurred.
3. Validate the authoritative version syntax and repository-specific version checks.
4. Confirm required generated and duplicated surfaces match and no stale artifact name was introduced.
5. Confirm any commit-message version exactly matches the staged authoritative version.
