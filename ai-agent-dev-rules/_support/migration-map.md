# Migration Map from the Previous Rules

This support document maps the two previous monolithic documents to the new page hierarchy. It is review guidance only and is not normative agent context.

## Previous global rules

| Previous content | New canonical page | Treatment |
| --- | --- | --- |
| Overview and global applicability | `ai-agent-dev-rules.md`, `core/operating-contract.md` | Rewritten as a compact router and operating contract. |
| Mandatory docstrings, parameters, returns, errors, classes, files | `documentation/comments-and-docstrings.md` | Consolidated; complete documentation remains mandatory for public and non-obvious declarations, concise blocks remain available for small meaningful helpers, and tiny self-explanatory local declarations have a narrow omission exception. |
| Documentation examples | `documentation/comments-and-docstrings/examples.md` | Moved out of the normative page and loaded only when needed. |
| Visibility and logical-group comments | `documentation/comments-and-docstrings.md` | Narrowed to non-obvious logical sections; blank lines alone do not require comments, and machine directives, pragmas, markers, and separators are exempt from prose punctuation rules. |
| JSX documentation and extraction | `languages/react.md`, `code-quality/structure-and-refactoring.md` | Split between framework behavior and general extraction rules. |
| Internal versus separate-file extraction | `code-quality/structure-and-refactoring.md` | Consolidated into one extraction order. |
| Non-commentable companion documents | `documentation/comments-and-docstrings.md` | Narrowed to lasting, non-obvious ownership/schema/generation contracts. |
| Documentation maintenance | Documentation pages and `core/validation-and-completion.md` | Preserved without duplication. |
| File and function limits | `code-quality/structure-and-refactoring.md` | Preserved as strong review/refactoring triggers with explicit exceptions and scope control. |
| Change-impact analysis | `core/operating-contract.md`, `core/change-safety-and-scope.md` | Rewritten as observable pre-edit behavior. |
| Testing and integration verification | `code-quality/testing.md`, `core/validation-and-completion.md` | Consolidated with truthful reporting and safety requirements. |
| Dependency tracking and API compatibility | `code-quality/dependencies-and-compatibility.md` | Routine import duplication removed; compatibility behavior expanded. |
| Navigation aids and triggers | Root router and scoped pages | Converted into deterministic load triggers instead of a repeated checklist. |
| Recommended tooling table | Language and repository pages | Removed as a global mandate; agents must inspect the repository-configured toolchain. |
| CI/CD checks | `workflows/ci-cd.md` | Loaded only for pipeline work. |
| Phase-specific rules | `core/change-safety-and-scope.md` or exact repository pages | Generic task-scope behavior retained; project-phase restrictions are no longer global. |
| Quick Reference | Removed | Duplicated normative text was eliminated. |
| Commit-message style | `workflows/git-commit-messages.md` | Changed to concise subject plus mandatory informative body; output is shell-aware. |
| Absolute `/api/` prohibition | `repository-types/docker-swarm/routing-and-traefik.md` | Scoped to dedicated API-hostname topology and routing evidence. |

## Previous Bash CLI tool rules

| Previous content | New canonical page | Treatment |
| --- | --- | --- |
| Tool applicability | `repository-types/bash-cli-tools.md` | Narrowed to installable, stateful, Bash-first CLI repositories. |
| Architecture layers | `repository-types/bash-cli-tools/architecture.md` | Preserved with repository-specific optional layers. |
| Generic Bash style | `languages/bash.md` | Separated from CLI architecture. |
| `VERSION` and semver | `repository-types/bash-cli-tools/versioning.md` | Corrected examples and clarified the normal final newline. |
| Help and man pages | `repository-types/bash-cli-tools/help-and-man-pages.md` | Resolved the distinction between mandatory `man <tool>` and optional `<tool> man`. |
| Automatic update guard | `repository-types/bash-cli-tools/auto-update.md` | Corrected to distinguish equal, behind, ahead, diverged, detached, dirty, offline, and non-interactive states. |
| Reset, install, update, uninstall | `repository-types/bash-cli-tools/install-update-reset.md` | Reset now applies only to tools with persisted state and cannot silently purge remote data. |
| Bash tool tests | `repository-types/bash-cli-tools/testing.md` | Generic checks retained; `file-backup` paths and commands removed from the family rule. |
| Commit additions | `workflows/git-commit-messages.md`, `repository-types/bash-cli-tools/versioning.md` | Consolidated without repeating the full commit policy. |
| Quick Reference | Removed | Duplicated normative text was eliminated. |
| Tool-specific phases and backend checks | Exact repository pages | Must be defined only for the repository that owns them. |
