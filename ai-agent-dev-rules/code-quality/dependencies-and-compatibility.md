# Dependencies and Compatibility

**Rule ID:** `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Status:** Active.  
**Applies when:** Dependencies, package manifests, lock files, public interfaces, version constraints, compatibility behavior, or local identity providers may change.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Dependencies

- Inspect the repository’s package manifest, lock file, configured package manager, and existing utilities before adding a dependency.
- Prefer the standard library and an existing approved dependency when they meet the requirement.
- Add a production dependency only when its necessity, maintenance, security, license, and runtime cost are acceptable.
- Do not perform unrelated dependency upgrades.
- Update lock files only through the repository-defined package manager or generator.
- Report every new direct dependency and why it is needed.

Routine imports do not need to be repeated in every docstring. Document only non-obvious architectural, runtime, optional, or externally provisioned dependencies.

## Shared local Keycloak

- Development, demos, and manual acceptance MUST use one persistent shared
  Keycloak service per local environment. App startup MUST reuse the shared
  endpoint (`http://localhost:9090` for the standard local Keycloak stack).
- Provision each application's realm and clients on that service with the
  supported reconciliation workflow. Configure the frontend and API with the
  same realm issuer.
- A separate disposable Keycloak instance MAY run only for an isolated automated
  test that requires its own server state. The test MUST own its project, ports,
  and data and clean up its resources on success or failure.

## Compatibility

- Preserve existing public APIs, persisted formats, environment variable contracts, CLI syntax, routes, and generated ownership unless the task explicitly requires change.
- Prefer additive transitions and deprecation periods for externally consumed interfaces.
- Document breaking changes prominently and provide a migration path.
- Keep types, schemas, validation, documentation, and tests synchronized.
- Do not change a default silently when existing users can observe it.

## API administrator message status

Every API MUST offer an anonymous, read-only endpoint discoverable from its root or API documentation. Report whether administrator incident messages are enabled, the effective channels (including email and Telegram where supported), and delivery evidence per channel. Distinguish disabled, configured but unverified, provider acceptance, and failed or unavailable evidence. Include the observation time for a reported delivery result. A status read MUST NOT send a message.

The public response MUST use an explicit field allowlist. Keep recipients, addresses, chat IDs, provider configuration, raw errors and credentials out of public responses, logs and examples. Expose recipient details only to authenticated administrators of the API's own Keycloak realm, validating issuer, intended audience and administrator role. Never return credentials even to administrators. For APIs without realm-admin authorization, omit private details until that protection exists.

Test anonymous visibility, effective channel settings, failure and success evidence, and denial of recipient access for anonymous callers, ordinary users and administrators from another realm.

## Configuration

Keep raw configuration loading separate from parsing and domain transformation when the repository defines that boundary. Validate values before side effects. Never place secrets or environment-specific values into tracked defaults.
