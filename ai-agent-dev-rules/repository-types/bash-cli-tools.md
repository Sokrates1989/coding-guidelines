# Bash CLI Tool Repository Rules

**Rule ID:** `REPO-TYPE-BASH-CLI`  
**Status:** Active.  
**Applies when:** The repository is an installable, stateful, Bash-first CLI tool with a dispatcher, workflow scripts, shared libraries, setup lifecycle, and user-facing commands.  
**Required pages:** `LANG-BASH`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.3.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

This is an opinionated archetype for stateful, installable Bash CLI tools. It applies only when repository evidence or an exact-repository rule establishes this lifecycle and layering model. It does not apply to a small stateless helper script merely because it is written in Bash, and it MUST NOT be used to invent capabilities or directories that the tool does not need.

## Load by planned edit

| Planned work | Required page |
| --- | --- |
| Dispatcher, workflow layers, libraries, policy files, or directory boundaries | [Architecture](bash-cli-tools/architecture.md). |
| `VERSION`, semver, displayed versions, or release identity | [Versioning](bash-cli-tools/versioning.md). |
| `help`, `--help`, `-h`, man pages, or usage output | [Help and man pages](bash-cli-tools/help-and-man-pages.md). |
| Installer, updater, uninstaller, reset, persisted state, or guided setup | [Install, update, reset, and uninstall](bash-cli-tools/install-update-reset.md). |
| Automatic remote update check | [Auto-update guard](bash-cli-tools/auto-update.md). |
| Syntax, smoke, or integration tests | [Bash CLI testing](bash-cli-tools/testing.md). |

Load [Git commit messages](../workflows/git-commit-messages.md) only when a commit message or command is requested.
