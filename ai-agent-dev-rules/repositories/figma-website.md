# Repository Rules: figma-website

**Rule ID:** `REPO-FIGMA-WEBSITE`  
**Status:** Active.  
**Applies when:** The normalized Git remote is `github.com/sokrates1989/figma-website`.  
**Required pages:** `REPO-TYPE-WRAPPER`, `CORE-REPOSITORY-DISCOVERY`  
**Overrides:** None.  
**Ruleset version:** `2.4.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Identity

```text
Canonical remote: https://github.com/Sokrates1989/figma-website.git
Normalized identity: github.com/sokrates1989/figma-website
```

This repository is a multi-site wrapper around Figma Make site submodules. It owns authentication, a FastAPI backend, shared widgets, per-site configuration and overrides, Docker development, production image construction, and Swarm deployment.

## Ownership boundaries

- `sites/` contains source-site Git submodules and MUST NOT be modified for wrapper functionality.
- Wrapper behavior belongs in `api/`, `shared-modules/`, `site-configs/`, `public-override/`, build scripts, Docker configuration, or another established wrapper-owned path.
- A submodule pointer update is a distinct reviewed change. Do not move unrelated submodules.
- Preserve plugin contracts and per-site configuration instead of hardcoding one site into shared behavior.

## Conditional pages

| Planned path or behavior | Load |
| --- | --- |
| `api/**/*.py` | [Python](../languages/python.md). |
| `shared-modules/**/*.js`, build JavaScript, or frontend integration | [JavaScript and TypeScript](../languages/javascript-typescript.md). |
| Bash scripts | [Bash](../languages/bash.md). |
| PowerShell scripts | [PowerShell](../languages/powershell.md). |
| `stack.yml`, Dockerfiles, Traefik, API hostname/path, or production routing | [Docker Swarm](../repository-types/docker-swarm.md). |
| Plugin schemas, site JSON, or companion policy documents | [Repository documentation](../documentation/repository-documentation.md). |
| Commit preparation | [Git commit messages](../workflows/git-commit-messages.md). |

## Repository-specific rules

- Prefer the repository’s quick-start and Docker-based development workflows. Do not introduce a mandatory local Node.js setup for normal development.
- Keep reusable widgets and auth behavior in shared modules; keep site-only behavior under site-specific or per-site configuration paths.
- Preserve runtime “baked defaults plus environment override” behavior for supported frontend configuration.
- When changing API routes or frontend route strings, trace external Traefik/Nginx routing and load `SWARM-ROUTING-TRAEFIK` before editing.
- Do not expose Keycloak, database, or API credentials in frontend overrides or tracked environment templates.
- Keep non-commentable custom policy files synchronized with their existing companion Markdown when one already exists.

## Terminology evidence

Resolve repository-specific terms such as “plugin contract,” “per-site configuration,” and “baked defaults plus environment override” through the current schemas, site configuration, build/runtime injection code, tests, and repository documentation. Do not infer those contracts from this summary when the owning repository evidence is missing or contradictory.

## Validation focus

Inspect submodule state, affected site/plugin contracts, Docker build/runtime injection, API tests, and rendered Swarm configuration as applicable. Test at least one affected site without moving or rebuilding unrelated sites.
