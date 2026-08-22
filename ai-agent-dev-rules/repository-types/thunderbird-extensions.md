# Thunderbird Extension Repository Rules

**Rule ID:** `REPO-TYPE-THUNDERBIRD-EXTENSION`  
**Status:** Active.  
**Applies when:** Work creates, changes, reviews, packages, or releases a Thunderbird MailExtension, add-on, plugin, XPI archive, or native installer for one.  
**Required pages:** `CORE-REPOSITORY-DISCOVERY`, `WORKFLOW-SEMANTIC-VERSIONING`, `WORKFLOW-GIT-COMMITS`, `QUALITY-TESTING`, `QUALITY-DEPENDENCIES-COMPATIBILITY`, `QUALITY-LOCALIZATION`  
**Overrides:** None.  
**Ruleset version:** `2.5.0`.  
**Updated:** `2026-08-22`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Release boundary after implementation

A completed implementation that changes extension runtime behavior, UI, permissions, compatibility, packaging, or installation behavior is a release boundary unless the operator explicitly defers packaging. Documentation-only, test-only, diagnostic-only, and incomplete work is not automatically a release boundary.

For every release boundary, the agent MUST:

1. Classify the actual released impact under `WORKFLOW-SEMANTIC-VERSIONING` and update the authoritative version.
2. Synchronize every repository-owned duplicate and derived version surface.
3. Build a fresh installable XPI from the completed source.
4. Build every native installer supported by the current host and repository tooling.
5. Validate the archive and installer before committing and handing them to the operator.

MUST NOT hand off an installer from a prior version or claim that a non-built platform installer is current. If required tooling is unavailable on the host, synchronize its source metadata, report the exact unbuilt installer, and provide every successfully built artifact.

## Identity and version synchronization

- Treat the extension manifest version as authoritative unless repository evidence names another source.
- Preserve the stable Thunderbird extension ID across updates. Changing it creates a separate installation and requires explicit operator intent plus migration analysis.
- Synchronize package manifests, runtime display constants, install defaults, Windows installer definitions, macOS package metadata, tests, documentation, and artifact names that intentionally duplicate the version.
- Search the maintained source and documentation for stale prior-version references before building.
- Use a minor bump for backward-compatible new functionality and a patch bump for compatible fixes or packaging maintenance. Use a major bump only under the general SemVer rule.
- A versioned commit subject MUST use the staged authoritative version exactly.

## Installer production

- Use repository-owned build scripts; do not assemble XPI, PKG, or EXE files manually when a builder exists.
- Build from the current worktree only after focused behavior checks pass.
- A repository that promises direct native installation SHOULD provide macOS and Windows builders. Build the macOS package on macOS and the Windows installer on Windows unless the repository has a validated cross-build workflow.
- Keep generated XPI and installer binaries out of Git unless repository ownership explicitly tracks release artifacts.
- Never sign, notarize, publish, upload, tag, push, or install into the operator's live Thunderbird profile without explicit authorization. Report unsigned or unnotarized status.

## Required validation

At minimum, validate the following for each release boundary:

- Run focused tests for the implementation and the repository's broader required suite.
- Parse the source manifest and verify semantic version syntax, the stable extension ID, and supported Thunderbird bounds.
- Inspect the built XPI for the matching manifest version and ID, required scripts/resources, English and German localization, install defaults, and portable archive paths.
- Run repository installer tests in disposable profile directories. Verify first install and update replacement while preserving the stable ID and stored settings contract.
- Inspect native package metadata, payload, installer scripts, and displayed artifact version. On macOS, verify current-user scope and that installation never force-terminates Thunderbird. On Windows, verify per-user scope and update cleanup when those are the documented contracts.
- Run syntax checks for changed shell or installer sources and `git diff --check`.
- Compute and report a SHA-256 checksum for every built artifact handed to the operator.

Live installation is a separate, state-changing validation tier. Run it only when explicitly requested, identify the exact profile target, and preserve drafts and settings.

## Commit and handoff

The implementation, version synchronization, installer-source changes, tests, and release documentation SHOULD remain one coherent commit unless the repository defines a separate release commit. Generated ignored binaries remain outside the commit.

Before committing, inspect the staged version and full staged diff. The commit body MUST record the XPI and installer validation actually run, platform installers not built, compatibility boundaries, and signing or notarization limitations.

The completion report MUST include the release version, local commit ID, absolute artifact paths, SHA-256 checksums, and any platform installer that remains unbuilt.
