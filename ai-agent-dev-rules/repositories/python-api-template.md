# Repository Rules: python-api-template

**Rule ID:** `REPO-PYTHON-API-TEMPLATE`  
**Status:** Active.  
**Applies when:** The normalized Git remote is `github.com/sokrates1989/python-api-template`.  
**Required pages:** `REPO-TYPE-TEMPLATE`, `CORE-REPOSITORY-DISCOVERY`  
**Overrides:** None.  
**Ruleset version:** `2.6.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Identity

```text
Canonical remote: https://github.com/Sokrates1989/python-api-template.git
Normalized identity: github.com/sokrates1989/python-api-template
```

This repository is the production FastAPI backend template and Python-owned backend foundation for paired Flutter Template V2 generation.

## Ownership and generation

- The shared Flutter creator owns creation of a new paired app/backend target. The Python quick-start scripts configure and run an already selected backend checkout; they MUST NOT become a second app-pair generator.
- Preserve Template V2 check, plan, diff, create, reconcile, detach, apply, exact-intent, ownership, and rollback contracts.
- Standard generated backends use the documented Keycloak/PostgreSQL connected profile and neutral records starter. Retained compatibility profiles MUST NOT silently acquire standard-profile behavior.
- Secrets, credentials, database passwords, signing values, and provider administration remain deployment inputs, never creator inputs.

## Conditional pages

| Planned work | Load |
| --- | --- |
| FastAPI/Python application code | [Python](../languages/python.md). |
| Bash or PowerShell quick-start/tooling | [Bash](../languages/bash.md) or [PowerShell](../languages/powershell.md). |
| Docker/Swarm/routing or image release | [Docker Swarm](../repository-types/docker-swarm.md). |
| Alembic or schema changes | [Database migrations](../workflows/database-migrations.md). |
| Pipeline changes | [CI/CD](../workflows/ci-cd.md). |

## Repository-specific rules

- Use PDM and the repository’s Docker-owned dependency management workflow. Do not edit the lock file manually or introduce an undocumented local-only dependency path.
- Keep raw environment loading separate from parsing and transformation according to the existing settings/application boundary.
- Production API image planning, local proof, and publication remain operator actions through the authoritative quick-start flow. Do not publish through raw Docker commands or convert quality-only CI into a publisher.
- When changing external API routes, load `SWARM-ROUTING-TRAEFIK` and preserve the actual deployment topology rather than applying `/api` prefixes mechanically.
- Keep database access, business logic, API schemas/routes, and models in their established layers.

## Terminology evidence

Resolve terms such as “Template V2,” “connected profile,” “compatibility profile,” “release plan,” and paired lifecycle operations through the current manifests, launcher help, tests, and repository documentation. If the repository does not define a named contract, treat that omission as a material ambiguity rather than inventing behavior.

## Validation focus

Use repository-defined Docker/PDM checks, API tests, template contract tests, generated pair plans, migration tests, and image release-plan validation as applicable. Cross-repository pair changes also require the `flutter_app_template` repository page and coordinated validation.
