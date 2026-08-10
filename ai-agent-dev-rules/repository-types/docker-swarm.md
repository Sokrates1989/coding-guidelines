# Docker Swarm Repository Rules

**Rule ID:** `REPO-TYPE-DOCKER-SWARM`  
**Status:** Active.  
**Applies when:** The task changes, plans, reviews, or diagnoses Docker Swarm stacks, Traefik routing, container images, secrets, configs, deployment scripts, or production container topology.  
**Required pages:** `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.1.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Load by planned edit

| Planned work | Required page |
| --- | --- |
| Router rules, host/path matching, service ports, middleware, or API paths | [Routing and Traefik](docker-swarm/routing-and-traefik.md). |
| Stack YAML, networks, services, health checks, scaling, or image tags | [Stack structure](docker-swarm/stack-structure.md). |
| Secrets, configs, deployment, publication, rollback, or production commands | [Secrets and deployment](docker-swarm/secrets-and-deployment.md). |

Load language pages for scripts or application code changed alongside the stack. Load CI/CD only when automation workflows change.
