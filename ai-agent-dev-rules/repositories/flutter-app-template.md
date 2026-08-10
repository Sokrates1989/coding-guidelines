# Repository Rules: flutter_app_template

**Rule ID:** `REPO-FLUTTER-APP-TEMPLATE`  
**Status:** Active.  
**Applies when:** The normalized Git remote is `github.com/sokrates1989/flutter_app_template`.  
**Required pages:** `REPO-TYPE-TEMPLATE`, `CORE-REPOSITORY-DISCOVERY`  
**Overrides:** None.  
**Ruleset version:** `2.2.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Identity

```text
Canonical remote: https://github.com/Sokrates1989/flutter_app_template.git
Normalized identity: github.com/sokrates1989/flutter_app_template
```

This repository is the production Flutter app creator and owns Template V2 inputs, recipes, generator lifecycle, generated ownership, golden outputs, app registrations, and optional paired Python backends.

## Ownership boundaries

- `apps/starter_app` is generated golden output, not template source. Do not edit it manually.
- Human-owned inputs live under the documented example/input roots. Generated paths are governed by `.template_v2/ownership.json`.
- Modified, missing, detached, and unowned paths MUST fail closed or remain preserved according to the lifecycle contract.
- `quick-start.ps1` is a WSL adapter for the authoritative `quick-start.sh`. Keep business logic in Bash and forward arguments from PowerShell.

## Safe creator lifecycle

- Run check/plan/diff before write operations.
- Supply the exact documented write intent for author, create, apply, pair-apply, or detach operations.
- Keep app and backend destinations explicit.
- Preserve atomic cross-repository behavior and exact rollback when a late operation fails.
- Blueprints contain public OIDC identity only; never add secrets, signing keys, database credentials, or provider-administration values.

## Terminology evidence

Resolve terms such as “Template V2,” “exact intent,” “ownership,” “golden drift,” “creator matrix,” and lifecycle operation names through the current ownership manifests, launcher help, tests, and repository documentation. If the repository does not define a named contract, treat that omission as a material ambiguity rather than inventing behavior.

## Conditional pages

| Planned work | Load |
| --- | --- |
| Dart, Flutter apps, packages, or widgets | [Dart and Flutter](../languages/dart-flutter.md). |
| Python creator tooling | [Python](../languages/python.md). |
| Authoritative launcher | [Bash](../languages/bash.md). |
| PowerShell adapter | [PowerShell](../languages/powershell.md). |
| Paired backend work | [python-api-template](python-api-template.md). |
| Release/container/Swarm work | [Docker Swarm](../repository-types/docker-swarm.md). |

## Validation focus

Run Flutter commands from the affected app or package root, never blindly from the monorepo root. For creator changes, use the repository’s golden drift, governance, release-evidence, creator matrix, unit-test discovery, and architecture validation commands. Generate all supported profiles in temporary targets when the changed contract requires it.

Do not run broad formatting or generation that rewrites unrelated applications.
