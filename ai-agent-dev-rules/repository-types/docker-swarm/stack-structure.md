# Docker Swarm Stack Structure

**Rule ID:** `SWARM-STACK-STRUCTURE`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing Swarm service definitions, networks, volumes, health checks, scaling, placement, or image references.  
**Required pages:** `REPO-TYPE-DOCKER-SWARM`  
**Overrides:** None.  
**Ruleset version:** `2.2.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Services and images

- Use explicit image version tags for deployment evidence and immutable digests when exact immutable image identity is required. Do not replace version variables with `latest`.
- Preserve repository variables such as `FRONTEND_IMAGE_VERSION` and `BACKEND_IMAGE_VERSION` when they own image tags.
- Set resource, restart, update, rollback, and placement policies intentionally when the repository defines them.
- Health checks MUST test a meaningful readiness or health contract and use commands available inside the image.
- Do not expose ports publicly when Traefik or an internal overlay network is the intended access path.

## Networks and storage

- Reuse the repository’s declared external Traefik network and application networks.
- A volume or Azure File Share MUST satisfy the exact repository’s resource-group and access-mode requirements.
- Stateful services require documented persistence, backup, restore, ownership, and single/multi-replica constraints.
- Avoid host-bound assumptions that break rescheduling unless placement constraints deliberately enforce them.

## Rendering and deployment command

Render and inspect the effective stack before deployment using the repository’s authoritative command or a safe equivalent. A common Bash-compatible example is:

```bash
docker stack deploy -c <(docker compose -f config-stack.yml config) <STACK_NAME>
```

Use the repository’s canonical compose file. Repository scripts, legacy `docker-compose`, PowerShell-compatible temporary rendered files, or other safe rendering workflows MAY be used when they preserve the same inspected configuration. Process substitution requires a compatible shell. Do not publish an unrendered variable-dependent stack by accident.

## Validation

Check YAML/config rendering, required variables, image tags or digests, secrets/config references, external networks, target ports, and health checks. When a rollout is performed at an authorized environment tier, also check service convergence and review `docker service ps` and service logs for failures.
