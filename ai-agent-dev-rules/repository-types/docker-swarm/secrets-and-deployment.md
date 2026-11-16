# Docker Swarm Secrets and Deployment

**Rule ID:** `SWARM-SECRETS-DEPLOYMENT`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing secrets, configs, registry publication, deployment scripts, production rollout, or rollback behavior.  
**Required pages:** `REPO-TYPE-DOCKER-SWARM`, `SWARM-STACK-STRUCTURE`, `CORE-CHANGE-SAFETY`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Secrets and configuration

- Use the repository-approved secret mechanism for credentials and sensitive values. Use Docker Swarm secrets when Swarm owns secret distribution. Never place plaintext secrets in stack files, tracked environment files, labels, image arguments, or logs.
- Use configs or non-secret environment values for non-sensitive configuration according to repository conventions.
- Validate that secret names exist without printing secret contents.
- Preserve least privilege, file permissions, and service-specific secret mounting.

## Publication

- Build and publish only when explicitly requested and through the exact repository’s authoritative workflow.
- Use explicit version tags and record the immutable image digest when available.
- Do not make CI publish images when the exact repository reserves publication for an operator-controlled quick-start flow.
- Do not leak build secrets into image layers or logs.

## Multi-site release isolation

- Treat each deployment checkout and stack as an independent target, even when they use the same application profile. Check that a site release changes only its own image references, version floors, and release evidence unless shared changes are explicitly in scope.
- Scope site-specific paths, flags, and directory changes in operator instructions to one command or a subshell. Verify the caller's working directory and environment after the documented command exits.
- Bind automatic and inherited overrides to the active deployment checkout and stack. Ignore an inherited override for another deployment. Validate an intentional override for the active deployment before using it. Require an explicit, target-validated selection for an external backup.
- Before committing release instructions or changing a shared deployment workflow, exercise the documented target command and a second site's affected planning or update path in the same shell with isolated fixtures. Include a stale target override and verify the other site selects its own saved configuration and version metadata. Cover separate test and production checkouts when they share a profile.

## Deployment safety

Before production deployment:

1. Confirm the target Docker context and stack name.
2. Render and inspect the effective stack.
3. Confirm required secrets, configs, networks, and image tags.
4. Record the current deployed version and rollback target.
5. Deploy only with explicit authorization.
6. Monitor convergence, health, logs, and external behavior.
7. Roll back or stop when acceptance checks fail.

Never interpret a successful `docker stack deploy` command as proof that the application is healthy.

## Changes to stateful services

Back up data before destructive schema, volume, or storage changes. Define replica constraints and upgrade compatibility. Do not delete volumes, secrets, or remote data as cleanup unless the request explicitly authorizes that exact resource.
