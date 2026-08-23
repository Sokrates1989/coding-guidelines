# Thunderbird Extension Repository Rules

**Rule ID:** `REPO-TYPE-THUNDERBIRD-EXTENSION`  
**Status:** Active.  
**Applies when:** Work creates, changes, reviews, packages, or releases a Thunderbird MailExtension, add-on, plugin, XPI archive, or native installer for one.  
**Required pages:** `CORE-REPOSITORY-DISCOVERY`, `WORKFLOW-SEMANTIC-VERSIONING`, `WORKFLOW-GIT-COMMITS`, `WORKFLOW-CI-CD`, `QUALITY-TESTING`, `QUALITY-DEPENDENCIES-COMPATIBILITY`, `QUALITY-LOCALIZATION`, `REPO-TYPE-THUNDERBIRD-BILINGUAL-DOCS`  
**Overrides:** None.  
**Ruleset version:** `2.8.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Release boundary after implementation

A completed implementation that changes extension runtime behavior, UI, permissions, compatibility, packaging, or installation behavior is a release boundary unless the operator explicitly defers packaging. Documentation-only, test-only, diagnostic-only, and incomplete work is not automatically a release boundary.

For every release boundary, the agent MUST:

1. Classify the actual released impact under `WORKFLOW-SEMANTIC-VERSIONING` and update the authoritative version.
2. Synchronize every repository-owned duplicate and derived version surface.
3. Build a fresh installable XPI from the completed source.
4. Build every native installer supported by the current host and repository tooling.
5. Validate the archive and installer before committing and handing them to the operator.
6. For repositories that publish installers for more than one operating system, verify that the release workflow builds every supported installer on its native operating-system runner before publication.

MUST NOT hand off an installer from a prior version or claim that a non-built platform installer is current. If required tooling is unavailable on the host, synchronize its source metadata, report the exact locally unbuilt installer, and identify the validated native-runner workflow that will build it before publication.

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
- Do not require a developer workstation to emulate the other operating system merely to satisfy a multi-platform release. Prefer native macOS and Windows CI runners, and execute the same repository-owned builders and installer tests used locally.
- Keep generated XPI and installer binaries out of Git unless repository ownership explicitly tracks release artifacts.
- Never sign, notarize, publish, upload, tag, push, or install into the operator's live Thunderbird profile without explicit authorization. Report unsigned or unnotarized status.

## Required validation

At minimum, validate the following for each release boundary:

- Run focused tests for the implementation and the repository's broader required suite.
- Parse the source manifest and verify semantic version syntax, the stable extension ID, and supported Thunderbird bounds.
- Inspect the built XPI for the matching manifest version and ID, required scripts/resources, English and German localization, install defaults, and portable archive paths.
- Run repository installer tests in disposable profile directories. Verify first install and update replacement while preserving the stable ID and stored settings contract.
- Native-companion tests that generate or convert synthetic email, Office, image, or PDF fixtures MUST use the operating system temporary area, not a protected Documents checkout or repository-local base-temporary directory. This reduces anti-ransomware false positives and keeps generated documents out of source trees.
- Inspect native package metadata, payload, installer scripts, and displayed artifact version. On macOS, verify current-user scope and that installation never force-terminates Thunderbird. On Windows, verify per-user scope and update cleanup when those are the documented contracts.
- Run syntax checks for changed shell or installer sources and `git diff --check`.
- Compute and report a SHA-256 checksum for every built artifact handed to the operator.

Live installation is a separate, state-changing validation tier. Run it only when explicitly requested, identify the exact profile target, and preserve drafts and settings.

## Commit and handoff

The implementation, version synchronization, installer-source changes, tests, and release documentation SHOULD remain one coherent commit unless the repository defines a separate release commit. Generated ignored binaries remain outside the commit.

Before committing, inspect the staged version and full staged diff. The commit body MUST record the XPI and installer validation actually run, platform installers not built, compatibility boundaries, and signing or notarization limitations.

The completion report MUST include the release version, local commit ID, absolute artifact paths, SHA-256 checksums, and any platform installer that remains unbuilt.

## Public repository and release standard

Before the first public release, the agent MUST verify or prepare:

- A permanent extension ID using a domain controlled by the maintainer or another identity accepted by addons.thunderbird.net. A placeholder domain MUST NOT be published. Changing an already published ID is a breaking installation boundary.
- An OSI-approved open-source license selected by the operator, included at the repository root, in every XPI, and in every native installer payload. Package metadata and documentation MUST identify the same SPDX license expression. If requested restrictions conflict with open source, stop and explain the conflict before choosing a license.
- Native Windows and macOS installers that display the project license before installation and require the installer’s standard acknowledgement to continue. This acknowledgement MUST NOT add an EULA or restrictions beyond the selected license.
- A public README with latest-release, complete release-history, stable installer, build, privacy, support, contribution, and license links. Projects that process or transfer personal data MUST publish an accurate privacy policy. Public repositories SHOULD also provide contribution and security policies.
- Reviewer-ready source, deterministic build instructions, English and German listing text, screenshots, permission explanations, external-service or native-companion disclosures, and test instructions for addons.thunderbird.net.

GitHub release history MUST use the repository’s /releases page and the current release MUST use /releases/latest. Every release MUST retain versioned XPI and installer assets plus SHA-256 checksums. It MUST also upload byte-identical stable aliases for the current supported installers so README links can use /releases/latest/download/<stable-name> without changing on every version.

A public project that supports native installers on more than one operating system MUST automate the complete release on native CI runners. A push to the documented release branch MAY be the operator-controlled publication trigger when the operator explicitly authorizes that contract. The workflow MUST read the authoritative extension version, skip publication when that version already has a release, build and test every supported native installer, publish all platform assets together, create the matching version tag and latest release, and fail instead of publishing a partial release. A local build, an unchanged-version push, pull request, or fork MUST NOT publish. Document required repository permissions and any one-time GitHub Actions enablement so the operator knows that the triggering push is externally visible publication.

Before changing a private repository to public, inspect tracked files and relevant history for secrets and private data. Repository visibility, tags, pushes, GitHub Releases, store submissions, signing, and notarization remain externally visible publication actions and require explicit operator authorization.

## Store and platform trust

The Thunderbird Add-ons listing distributes the XPI, not a native companion. A project that requires native messaging MUST publish the companion installers separately and disclose that dependency prominently to users and reviewers. An add-on that sends data to an AI or other remote service MUST disclose the exact data categories, trigger, provider, credential model, retention boundary, and any paid-service requirement before submission.

Public native installers SHOULD be code signed. For macOS, sign nested executables where applicable, sign the flat package with the correct Developer ID identities, submit it with the current Apple notarization workflow, staple the ticket, and validate with Gatekeeper tooling. For Windows, Authenticode-sign and timestamp the final installer. When credentials or certificates are unavailable, keep them out of the repository, hand off unsigned artifacts only as clearly labeled test builds, and document the resulting Gatekeeper or SmartScreen warning.
