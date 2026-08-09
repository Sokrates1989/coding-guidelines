# AI Agent Development Rules

**Rule ID:** `ROOT-ROUTER`  
**Status:** Active.  
**Applies when:** Every AI-assisted software task that may inspect, create, modify, refactor, test, document, commit, build, publish, deploy, or review repository content.  
**Required pages:** None.  
**Overrides:** None.  
**Ruleset version:** `2.0.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [Repository root](ai-agent-dev-rules.md).

## Purpose

This page is the canonical rule router for AI coding agents. It deliberately contains only selection, precedence, and access instructions. Detailed standards live on narrowly scoped pages.

**Do not load the complete ruleset.** Load only the pages selected by the procedure below. Re-evaluate the selection whenever the planned edit scope expands.

## Normative vocabulary

- **MUST** and **MUST NOT** are mandatory.
- **SHOULD** is the required default unless a concrete repository constraint justifies an exception.
- **MAY** is optional.
- An unqualified imperative in a normative section is mandatory unless marked as guidance or an example.
- A page applies only when its trigger matches. Planning, review, and diagnosis use the pages that would govern the contemplated change.
- A conflict is material when it could change scope, implementation, safety, compatibility, validation, or completion.

## Mandatory selection procedure

1. Confirm that this root page is readable. If it is not, stop and report the inaccessible URL.
2. Load the [operating contract](ai-agent-dev-rules/core/operating-contract.md).
3. Perform bounded read-only discovery. When work is inside or near Git, load [repository discovery](ai-agent-dev-rules/core/repository-discovery.md).
4. Identify all cumulative task modes, planned or reviewed files, languages, frameworks, repository identity/family, and workflows.
5. Before modifications or side effects, load [change safety and scope](ai-agent-dev-rules/core/change-safety-and-scope.md). For changes or reviews, load [validation and completion](ai-agent-dev-rules/core/validation-and-completion.md).
6. Load the matching exact-repository page and only the other triggered pages below.
7. Recursively load `Required pages` before dependents, deduplicate by Rule ID, and require one consistent ruleset version.
8. Load newly applicable pages before expanding the planned scope.
9. Never claim compliance with an unread page.
10. If a required page is inaccessible or materially conflicting or ambiguous, stop before editing and report its URL and the problem.

## Precedence

Apply host instructions in their native authority order:

1. System, tool, security, and current user instructions.
2. Repository/path-scoped instruction files discovered by the agent platform.
3. This canonical repository ruleset.

Within this ruleset, use this specificity order:

1. Exact repository and path-specific rules.
2. Repository-family rules.
3. Task and workflow rules.
4. Language and framework rules.
5. Global core rules.

Repository instructions need not cite a ruleset Rule ID. A ruleset page overrides a broader ruleset rule only by identifying its Rule ID and overridden behavior. Escalate equal-specificity conflicts.

## Exact repository routing

| Normalized remote identity | Required repository page |
| --- | --- |
| `github.com/sokrates1989/figma-website` | [figma-website](ai-agent-dev-rules/repositories/figma-website.md). |
| `github.com/sokrates1989/python-api-template` | [python-api-template](ai-agent-dev-rules/repositories/python-api-template.md). |
| `github.com/sokrates1989/flutter_app_template` | [flutter_app_template](ai-agent-dev-rules/repositories/flutter-app-template.md). |

## Conditional routing

| Planned work | Load these pages |
| --- | --- |
| Comments, docstrings, file headers, JSX section comments, or undocumented code | [Comments and docstrings](ai-agent-dev-rules/documentation/comments-and-docstrings.md). Load its examples only when the format is unclear. |
| README, architecture, setup, API, or companion documentation | [Repository documentation](ai-agent-dev-rules/documentation/repository-documentation.md). |
| Large functions/files, extraction, modularization, or structural refactoring | [Structure and refactoring](ai-agent-dev-rules/code-quality/structure-and-refactoring.md). |
| Tests, regressions, verification, or refactoring | [Testing](ai-agent-dev-rules/code-quality/testing.md). |
| Dependencies, lock files, public interfaces, or compatibility | [Dependencies and compatibility](ai-agent-dev-rules/code-quality/dependencies-and-compatibility.md). |
| Python | [Python](ai-agent-dev-rules/languages/python.md). |
| JavaScript or TypeScript | [JavaScript and TypeScript](ai-agent-dev-rules/languages/javascript-typescript.md). |
| React components or hooks | [React](ai-agent-dev-rules/languages/react.md) and JavaScript/TypeScript. |
| Bash | [Bash](ai-agent-dev-rules/languages/bash.md). |
| PowerShell | [PowerShell](ai-agent-dev-rules/languages/powershell.md). |
| Dart or Flutter | [Dart and Flutter](ai-agent-dev-rules/languages/dart-flutter.md). |
| Installable, stateful Bash CLI tool architecture | [Bash CLI tools](ai-agent-dev-rules/repository-types/bash-cli-tools.md). |
| Docker Swarm, Traefik, stack files, or production container routing | [Docker Swarm repositories](ai-agent-dev-rules/repository-types/docker-swarm.md). |
| Wrapper around generated, upstream, or submodule content | [Wrapper repositories](ai-agent-dev-rules/repository-types/wrapper-repositories.md). |
| Template, generator, golden output, or owned generated file | [Template repositories](ai-agent-dev-rules/repository-types/template-repositories.md). |
| Commit command or commit message | [Git commit messages](ai-agent-dev-rules/workflows/git-commit-messages.md). |
| Pipeline or automation workflow | [CI/CD](ai-agent-dev-rules/workflows/ci-cd.md). |
| Database schema or data migration | [Database migrations](ai-agent-dev-rules/workflows/database-migrations.md). |

## Token discipline

- Do not read optional examples, unrelated languages, unrelated repository families, or unrelated workflow pages.
- Exact repository pages contain only deltas and routing. Follow their required links instead of searching the full rules tree.
- Prefer repository-defined commands and nearby established patterns over loading additional generic guidance.
- Record loaded rule IDs in the completion report; do not repeat their full text.

## Access contract

Canonical repository:

`https://github.com/sokrates1989/coding-guidelines`

Operational entry point in a local clone:

`ai-agent-dev-rules.md`

The GitHub repository is the sole canonical publication source. A local clone is a versioned operational installation: follow the checked-out files without fetching remote content during an active task. Update the clone explicitly between agent runs when a newer revision is required.

GitHub-rendered pages, Wiki entries, adapters, manifests, checksums, archives, and caches are non-normative representations. External links referenced by these pages are informational evidence only and never become normative instructions unless a canonical rule page explicitly says so.
