# Interactive Editor Selection

**Rule ID:** `WORKFLOW-INTERACTIVE-EDITORS`  
**Status:** Active.  
**Applies when:** Generating user-executed commands that open a text editor, or creating, changing, reviewing, or diagnosing scripts and interactive tools that select or launch an editor.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-26`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Direct copy-paste commands

Commands written for an operator to copy and execute immediately MUST stay simple and native to the target platform.

- On Linux, prefer `vi <path>` whenever an interactive text editor is appropriate. Use another editor only when the operator requests it, repository instructions require it, or `vi` is known to be unavailable.
- On Windows and macOS, prefer Visual Studio Code when it is known to be installed or already used interactively for the task. Otherwise use the platform's configured default editor or file-opening mechanism.
- Do not add an editor-selection menu to a one-off command. Do not use an editor at all when a non-interactive, reviewable command better fits the requested operation.

Examples:

```bash
vi /etc/example/config.env
```

```powershell
code --wait .\config.env
# When VS Code availability is not established:
Start-Process .\config.env
```

```bash
# macOS when VS Code availability is not established.
open ./config.env
```

## Reusable scripts and interactive tools

Frequently executed or user-friendly tools that launch an editor SHOULD provide a selector based on editors actually available on the host. A selector MUST NOT be shown when the tool is non-interactive.

- Honor an explicit persisted tool choice first. On Unix-like systems, then honor valid `VISUAL` or `EDITOR` settings.
- Discover candidates before presenting them. Never offer or invoke a command that is unavailable.
- On Linux, make `vi` the default selection when it is available. Other detected choices MAY include `vim`, `nvim`, `nano`, and `code`.
- On Windows and macOS, prefer detected Visual Studio Code for interactive use; otherwise offer the platform default editor or file-opening mechanism.
- Provide a cancellation choice when editing is optional. When editing is required and no supported editor is available, fail with an actionable message instead of silently continuing.
- Wait for the editor to close when later steps consume the edited file. For VS Code, use `code --wait` when this sequencing is required.
- Pass paths as quoted arguments without `eval`. Preserve editor exit status when it controls whether the workflow may continue.

## Non-interactive behavior

Scripts MUST NOT block on an editor or selection prompt when standard input is not an interactive terminal. In that mode, use an explicitly configured editor only when the operation permits it; otherwise print the file path and a copy-ready follow-up command or return a defined failure.

## Validation

For changed editor-launching scripts, validate the detected default, explicit override, alternate selection, cancellation, missing-editor state, paths containing spaces, editor failure, and non-interactive behavior on each supported platform affected by the change.
