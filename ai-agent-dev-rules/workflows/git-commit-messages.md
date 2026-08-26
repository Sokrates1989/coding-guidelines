# Git Commit Workflow Rules

**Rule ID:** `WORKFLOW-GIT-COMMITS`  
**Status:** Active.  
**Applies when:** A task may change files in a Git worktree, or the user asks for a commit message, commit command, staged-change review, or actual commit.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.9.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Mandatory local commits

A coherent coding session is one closed logical unit of operator-requested repository work. It includes the code, tests, documentation, configuration, and generated artifacts required to complete that task. Size does not determine coherence: a one-sentence documentation correction or another tiny change is coherent when it is the complete requested task. A conversation turn is not automatically a session boundary, and unrelated tasks MUST NOT be combined merely because they occurred during one agent run.

Unless the current operator explicitly instructs otherwise:

- After completing each coherent coding session and executing or transparently accounting for its required validation, MUST create one local commit before reporting that task complete.
- MUST commit exactly the files and hunks created, modified, or deleted during that session. MUST NOT stage or commit unrelated pre-existing, user-owned, or other-session changes.
- MUST inspect `git status --short`, the relevant working-tree diff, and the staged diff before committing. Existing staged content MUST NOT be included unless it belongs to the current session.
- When one file contains both current-session changes and unrelated pre-existing changes, MUST isolate only the current-session hunks. If safe isolation is not possible, stop and report the blocker instead of committing unrelated work.
- Read-only work, sessions with no net file changes, and incomplete units do not require a commit. MUST NOT create an empty commit merely to satisfy this rule.
- The local-commit requirement authorizes only the staging and commit operations necessary for the current session. MUST NOT push, force-push, publish, open a pull request, or otherwise transfer commits to a remote without an explicit operator request.
- After committing, MUST verify the committed scope and repository status, report the local commit identifier, and disclose any remaining unrelated changes.
- If repository state, Git identity, signing, hooks, or another technical condition blocks a safe commit, MUST report the exact blocker and leave the session changes unpushed.

An explicit operator instruction MAY opt out of the commit, defer or combine identified sessions, include identified additional files, or authorize a push. Never infer an exception from silence.

## Determine the message scope

- For an actual commit, commit command, staged-change review, or final staged message, inspect the staged diff and status. The message MUST describe all staged changes as one logical unit.
- For an unstaged proposed commit, inspect the relevant working-tree diff and state clearly that the message is based on unstaged changes.
- For a hypothetical change, use the behavior and scope supplied by the user and label material assumptions. Do not imply that a diff was inspected.
- For a partially staged change, describe only the staged portion unless the user explicitly requests a future message covering additional identified work.

Do not write a message from filenames alone when a relevant diff is available.

## Subject

Use:

```text
[VERSION | JIRA-ID | Category] Area: concise summary
```

Include metadata only when verified:

- No version or Jira ID: `[Category]`.
- Jira ID only: `[JIRA-ID | Category]`.
- Version only: `[VERSION | Category]`.
- Both: `[VERSION | JIRA-ID | Category]`.

Never invent a version or Jira ID. When version metadata is requested or present, first load the [semantic-versioning rule](semantic-versioning.md). A staged authoritative version source MAY supply the version only when an applicable repository rule defines that behavior and the staged value was read. The commit message MUST match that value; it MUST NOT independently increment or calculate a version, and creating a commit alone MUST NOT trigger a bump.

Choose one primary category. Examples include `BugFix`, `New Feature`, `Refactoring`, `Documentation`, `Tests`, `Security`, `Performance`, `Setup`, `Env`, `Build`, `CI`, `Infra`, `UI`, `Navigation`, `Translation`, `Tooling`, and `CodeVersion`.

The area is optional, at most five words, and names the main scope. The summary uses a strong technical verb and remains suitable for `git log --oneline`. It does not enumerate every secondary detail.

## Body

Every AI-prepared full commit message and actual commit MUST have a body unless the user explicitly requests a subject-only format. A trivial commit may use one to three informative lines. Larger commits use only relevant sections:

```text
Why:
Changes:
Validation:
Compatibility:
Migration:
Limitations:
```

The body explains why the change was needed, what materially changed, important behavior or architecture effects, and validation actually performed. Never claim a check that was not run.

## Bash command

```bash
git commit -F - <<'COMMIT'
[BugFix] Update guard: distinguish remote branch states

Correct the update check so it offers self-update only when the local branch
is strictly behind its configured upstream.

Changes:
- Handle equal, behind, ahead, diverged, and detached states.
- Preserve offline and non-interactive execution.

Validation:
- Ran Bash syntax validation.
- Ran git diff --check.
COMMIT
```

## PowerShell command

```powershell
$commitMessage = @'
[Documentation] AI rules: clarify repository detection

Clarify how HTTPS and SSH remotes are normalized before exact repository
rules are selected.

Validation:
- Reviewed internal rule-page links.
'@

$commitMessage | git commit --file -
```

Generate syntax for the active shell. Preserve identical message semantics across shells. If the user supplies an explicit template, follow it exactly.

## Granularity

One commit represents one coherent logical change. Do not combine unrelated cleanup. Version changes remain with the feature or fix that requires them unless the repository explicitly defines a separate release commit.
