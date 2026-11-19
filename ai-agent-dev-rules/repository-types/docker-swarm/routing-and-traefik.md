# Docker Swarm Routing and Traefik

**Rule ID:** `SWARM-ROUTING-TRAEFIK`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing Traefik labels, reverse-proxy behavior, host/path rules, service ports, frontend API URLs, or API route decorators in a Swarm deployment.  
**Required pages:** `REPO-TYPE-DOCKER-SWARM`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## End-to-end routing analysis

Trace every affected request through:

```text
Browser or client URL
  -> external proxy or TLS terminator
  -> Traefik router and middleware
  -> Swarm service and target port
  -> application route
```

Verify host rules, path rules, router priority, entrypoints, forwarded protocol, selected Docker network, service port, and application path together. Do not validate only the container’s internal route.

## Dedicated API domains

New public Swarm APIs MUST use a dedicated DNS hostname by default, such as
`api.example.com` or `api.site.example.com`. A new deployment that exposes
an existing API publicly follows the same rule. Configure the hostname in
the deployment profile and confirm that its DNS record targets the intended
ingress. Use an explicit Traefik HTTPS `Host` rule for the API service. Wire
clients that call the dedicated host to its HTTPS base URL and configure
CORS for the approved browser origins when the requests are cross-origin.

Same-host routing requires an explicit operator decision or a documented
gateway or compatibility contract. Keep private-only APIs on the internal
network. On a dedicated API host, expose only the intended public paths and
methods. Keep administration and internal endpoints behind their own access
controls. Verify the external hostname, the intended route, and any required
browser preflight as part of deployment acceptance.

When a service is already reached through its own API hostname, such as `api.example.com`, and the frontend base URL already includes that hostname, application routes MUST NOT add a redundant `/api` prefix unless an external compatibility contract requires it.

Prefer:

```text
/vote
/comments
/me
/health
```

over:

```text
/api/vote
/api/comments
/api/me
/api/health
```

This rule applies only to that topology. Same-domain path routing, gateways, and published APIs MAY legitimately require `/api`. Determine the deployment contract before changing routes.

Traefik can reserve or prioritize `PathPrefix("/api")` routes for internal services. A redundant application prefix can therefore send traffic to the wrong router before it reaches the API container.

## Labels and networks

- Set the router’s host/path rule, entrypoint, middleware, and service explicitly.
- Set the Traefik target port to the container’s listening port, not an arbitrary published port.
- Declare the intended external Traefik network and the corresponding Docker network label.
- Avoid overlapping routers without explicit priorities and documented ownership.
- Preserve `X-Forwarded-*` handling and trusted-proxy configuration.

## Validation

Validate both internal and external paths at the highest applicable and authorized validation tier. Static or local work checks the rendered stack, labels, target ports, and application routes. When an authorized deployed environment is available, also check Traefik router/service state, container health, and an external request. A container-local `200` does not prove external routing works.
