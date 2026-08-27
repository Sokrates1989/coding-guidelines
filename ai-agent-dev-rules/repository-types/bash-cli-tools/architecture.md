# Bash CLI Architecture

**Rule ID:** `BASH-CLI-ARCHITECTURE`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing the dispatcher, workflow scripts, shared libraries, policy files, or repository structure of an applicable Bash CLI tool.  
**Required pages:** `REPO-TYPE-BASH-CLI`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Capability-dependent layers

```text
<tool>.sh              Dispatcher when the tool uses command dispatch.
scripts/*.sh           Workflow scripts when multiple workflows exist.
scripts/lib/*.sh       Shared libraries when behavior is reused.
setup/                 Install, update, and uninstall entry points when supported.
profiles/              Behavior strategies when the tool exposes profiles.
presets/               Use-case selections when the tool exposes presets.
config/                Static policy when configuration is repository-owned.
docs/                  Architecture, policies, guides, and man source as needed.
VERSION                Bare semantic version when this archetype owns release identity.
```

The established repository layout or an exact-repository page decides which layers and paths exist. Do not create an absent layer merely to match this example. When a capability exists, keep its responsibility separated according to the boundaries below.

## Boundaries

- The dispatcher resolves paths, loads minimal shared startup support, performs the update guard, and dispatches commands. It MUST NOT contain business logic.
- Workflow scripts MAY source shared libraries. Shared libraries MUST NOT call workflow scripts.
- Policy belongs in profiles, presets, configuration, or documented defaults, not duplicated throughout scripts.
- Setup scripts MUST remain operable before the installed checkout is complete and therefore MUST NOT depend on libraries that are unavailable at first install.
- Shared output, error, path, version, and command-detection behavior belongs in shared libraries.
- Avoid circular sourcing and hidden mutation of global variables.

## Command routing

The dispatcher MUST preserve the original argument list, return meaningful exit codes, and make `help`, `--help`, `-h`, `version`, update commands, and unknown-command behavior explicit. Each workflow owns argument parsing and validates before side effects.

## Repository-specific policy

Commands, phases, backends, private configuration paths, and integration sequences that belong to one tool MUST live on its exact repository page, not in this family rule.
