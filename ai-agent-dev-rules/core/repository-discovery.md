# Repository Discovery and Rule Selection

**Rule ID:** `CORE-REPOSITORY-DISCOVERY`  
**Status:** Active.  
**Applies when:** The task is performed inside or near a Git repository, or repository-specific rules may apply.  
**Required pages:** `ROOT-ROUTER`, `CORE-OPERATING-CONTRACT`  
**Overrides:** None.  
**Ruleset version:** `2.1.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Determine the repository root

Run from the working directory:

```bash
git rev-parse --show-toplevel
git remote get-url origin
git remote -v
```

Prefer `origin`. Inspect `upstream` when `origin` is a fork or wrapper remote. Do not use the local folder name as the primary identity.

## Normalize the remote

Treat these forms as the same identity:

```text
https://github.com/Sokrates1989/figma-website.git
git@github.com:Sokrates1989/figma-website.git
ssh://git@github.com/Sokrates1989/figma-website.git
```

Normalize by:

1. Removing the scheme and credentials.
2. Converting SCP-style `host:owner/repo` syntax to `host/owner/repo`.
3. Removing query strings, fragments, trailing slashes, and the final `.git` suffix.
4. Comparing host, owner, and repository case-insensitively.

Canonical result:

```text
github.com/sokrates1989/figma-website
```

## Fallback identification

When no remote exists, inspect repository-root manifests, README files, submodules, package metadata, and architecture documents. Use the root folder name only as supporting evidence. If the identity remains ambiguous, do not load or invent an exact repository page.

## Detect applicable technology pages

Inspect the planned files and repository configuration, including:

- `pyproject.toml`, `pdm.lock`, and Python packages.
- `package.json`, TypeScript configuration, and frontend framework files.
- `pubspec.yaml`, `analysis_options.yaml`, and Flutter app roots.
- Shell scripts and their authoritative wrappers.
- Dockerfiles, Compose files, Swarm stacks, and Traefik labels.
- Migration directories and database tooling.
- `.gitmodules`, generated ownership manifests, template inputs, and golden outputs.

Load pages for planned, reviewed, or diagnosed work, not merely for technologies present elsewhere in the repository. During planning or review, select the pages that would apply if the contemplated change were implemented.

## Scope expansion

If planned, reviewed, diagnosed, or edited scope reaches a new language, framework, workflow, repository family, submodule, or external repository, pause and load the newly applicable page before continuing.
