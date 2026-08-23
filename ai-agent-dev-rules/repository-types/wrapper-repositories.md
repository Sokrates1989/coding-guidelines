# Wrapper Repository Rules

**Rule ID:** `REPO-TYPE-WRAPPER`  
**Status:** Active.  
**Applies when:** A repository wraps generated, upstream, imported, or submodule code and adds authentication, APIs, deployment, configuration, assets, or production behavior without owning the upstream source.  
**Required pages:** `CORE-CHANGE-SAFETY`, `CORE-REPOSITORY-DISCOVERY`  
**Overrides:** None.  
**Ruleset version:** `2.7.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Ownership boundary

Identify which paths are:

- Upstream or generated source.
- Wrapper-owned runtime code.
- Wrapper-owned overrides and injected assets.
- Submodules or external repositories.
- Generated build output.

Upstream/generated paths are read-only unless the task explicitly requests a change in their owning repository or documented generation workflow.

## Preferred implementation order

1. Use existing wrapper configuration or extension points.
2. Add a wrapper-owned adapter, plugin, injected module, or override.
3. Update build or runtime integration without modifying upstream content.
4. Change upstream only in its own repository with explicit authorization.

Do not copy upstream files into the wrapper merely to patch them unless the repository defines that override mechanism. Minimize coupling to generated file layout.

## Submodules

- Inspect `.gitmodules`, `git submodule status`, and working-tree state.
- Do not commit inside a submodule when the requested change belongs to the wrapper.
- Treat a changed submodule pointer as a distinct reviewed change.
- Do not run recursive updates that move unrelated submodules without approval.
- Preserve the source repository’s independent history and remote.

## Synchronization

Wrapper changes MUST remain resilient to upstream updates. Document selectors, injection points, contracts, and assumptions that could break when upstream output changes. Add validation that fails clearly when the expected integration point disappears.

Keep wrapper and upstream concerns separate in commits and completion summaries.
