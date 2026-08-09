# Git Commit Message Rules

**Rule ID:** `WORKFLOW-GIT-COMMITS`  
**Status:** Active.  
**Applies when:** The user asks for a commit message, commit command, commit review, or an actual commit.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.0.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

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

Never invent a version or Jira ID. A staged repository `VERSION` file MAY supply the version only when an applicable repository rule defines that behavior and the new value was read.

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
