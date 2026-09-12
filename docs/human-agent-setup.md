# Connect an AI Coding Agent to These Guidelines

> **Audience: human maintainers.** This page is non-normative setup
> documentation. Nothing on this page becomes an instruction for an AI coding
> agent merely because the page exists. A person must deliberately copy one of
> the templates into a location that the selected agent loads as instructions.

The coding guidelines themselves remain in the canonical
[`Sokrates1989/coding-guidelines`](https://github.com/Sokrates1989/coding-guidelines)
repository. An agent starts with `ai-agent-dev-rules.md`, which routes it to only
the pages relevant to its current task.

## Recommended setup

Clone the guidelines once on each development computer before starting an agent
run. This avoids repeated network traffic and gives local agents a stable,
checked-out rules revision.

Windows PowerShell example:

```powershell
git clone https://github.com/Sokrates1989/coding-guidelines.git D:\Development\Code\coding-guidelines
git -C D:\Development\Code\coding-guidelines remote get-url origin
```

macOS or Linux example:

```bash
git clone https://github.com/Sokrates1989/coding-guidelines.git "$HOME/Development/coding-guidelines"
git -C "$HOME/Development/coding-guidelines" remote get-url origin
```

Update this clone between agent runs when a newer rules revision is wanted. Do
not update or switch its revision while an agent is already using it for a task.

Choose one or both installation scopes:

1. Add repository instructions for a team, cloud agent, or repository-specific
   setup.
2. Add personal instructions to a desktop agent so the guidelines apply to all
   local repositories.

## Where each coding agent reads instructions

| Coding agent | Repository instructions | Personal or machine-wide instructions |
| --- | --- | --- |
| [Codex](https://developers.openai.com/codex/guides/agents-md) | `AGENTS.md` in the repository root; nested files can add narrower guidance. | `~/.codex/AGENTS.md`, or the equivalent file below the configured `CODEX_HOME`. |
| [Cursor](https://cursor.com/docs/rules) | `AGENTS.md` in the repository root; nested files are also supported. | Paste the desktop template into **Customize → Rules → User Rules**. |
| [Devin](https://docs.devin.ai/onboard-devin/agents-md) | Put `AGENTS.md` in the repository root. Devin also discovers files in subdirectories. | Prefer the committed repository file so every Devin session receives the same bootstrap. |
| [Claude Code](https://code.claude.com/docs/en/memory#agents-md) | Claude Code reads `CLAUDE.md`, not `AGENTS.md`. Add the import bridge shown below to reuse the root `AGENTS.md`. | `~/.claude/CLAUDE.md`. |

These products can also offer richer rule systems. The files and setting above
are the smallest portable integration points for this bootstrap.

## Repository and cloud setup

Repository instructions are the recommended choice for shared projects and
cloud development. Create `AGENTS.md` directly in the target repository root and
copy the complete block below into it.

```markdown
# AI Agent Development Instructions

## Mandatory canonical development rules

For every AI-assisted software-development task, load and follow the applicable
rules from the canonical repository:

`https://github.com/Sokrates1989/coding-guidelines`

The operational entry point is `ai-agent-dev-rules.md`.

## Ruleset discovery

1. Prefer an already available trustworthy local clone or copy of
   `Sokrates1989/coding-guidelines`. Check only obvious workspace, sibling, or
   explicitly configured locations; do not scan unrelated or sensitive
   directories. A common Windows location is:

   `D:\Development\Code\coding-guidelines`

2. When the candidate is a Git clone, verify that its remote identifies
   `github.com/Sokrates1989/coding-guidelines`. Use its currently checked-out
   revision for the complete agent run. Do not fetch, pull, switch, reset, or
   otherwise update it during an active task unless the user explicitly asks.

3. If no trustworthy local copy is available, use read-only access to the
   canonical GitHub repository. Resolve the current `main` branch to one commit
   SHA and read the root router and every required page from that exact revision.
   A temporary shallow clone outside the project is allowed. If Git transport is
   blocked, use `https://api.github.com` to resolve the SHA and
   `https://raw.githubusercontent.com` to read files from that revision. Do not
   vendor the rules or add them as a submodule.

4. Read `ai-agent-dev-rules.md` first and follow its selection procedure. Load
   only pages applicable to the current repository, task, files, languages,
   frameworks, repository type, and workflows. Recursively load every required
   dependency before modifying project files or performing side effects.

## Failure, authority, and completion evidence

If the root router or a required page cannot be read from either a trustworthy
local copy or the canonical GitHub source, stop before modifications and report
the inaccessible resource and attempted access methods.

System, platform, security, tool, and explicit current-user instructions retain
their normal authority. More narrowly scoped repository instructions override
broader guidance according to the canonical ruleset's precedence model.

For every file-changing task, report the rules source and revision, ruleset
version, loaded Rule IDs, and validation actually performed. Never claim
compliance with an unread page or validation that was not executed.

## Repository-specific instructions

No additional repository-specific instructions are defined here.
```

Add genuine project-specific instructions only below the final heading. Keep
them concise and do not copy individual canonical rules into every repository.

### Claude Code bridge

When the target repository also uses Claude Code, create a root `CLAUDE.md`
containing this line:

```markdown
@AGENTS.md
```

Claude Code then imports the shared repository instructions without maintaining
a second copy. Claude-specific additions may follow the import when needed.

### Restricted cloud environments

A cloud agent that has no local clone needs read-only access to the canonical
GitHub source. For Codex Cloud, the narrow allowlist described in the
[detailed bootstrap guide](https://wiki.fe-wi.com/en/dev-guide/ai-agent-repository-bootstrap)
is:

```text
github.com, api.github.com, raw.githubusercontent.com
```

Where HTTP methods can be restricted, `GET`, `HEAD`, and `OPTIONS` are
sufficient for the API and raw-file fallback. Save changed environment settings,
reset the environment or setup cache, and start a new cloud task.

## Personal desktop setup

Use this scope when one developer wants every local project to inherit the
guidelines. First create or update the local clone between agent runs. Then copy
the block below into the location listed for the selected product, replacing
`<ABSOLUTE-PATH-TO-CODING-GUIDELINES>` with the clone's actual absolute path.

For Codex, place the text in `~/.codex/AGENTS.md`. For Cursor, paste it into
**Customize → Rules → User Rules**. For Claude Code, place it in
`~/.claude/CLAUDE.md`. Devin users should normally use the repository template
instead.

```markdown
# Global Development Rules

For every AI-assisted software-development task, read and follow the local
ruleset starting at:

`<ABSOLUTE-PATH-TO-CODING-GUIDELINES>/ai-agent-dev-rules.md`

The canonical repository is:

`https://github.com/Sokrates1989/coding-guidelines`

Use the local clone as the operational copy. Start with the root router and load
only the rule pages applicable to the current task, repository, files,
languages, frameworks, and workflows. Recursively load each page's required
rules before modifying project files.

System, tool, security, and current-user instructions retain their normal
precedence. More narrowly scoped repository and path instructions override
broader global rules.

If the local root router or a required page cannot be read, stop before modifying
the project and report the inaccessible path.

Never claim compliance with an unread rule page or validation that was not
actually executed. Do not update the rules clone during an active task unless
explicitly requested.
```

For the common Windows clone location used in the examples, the first path is:

```text
D:\Development\Code\coding-guidelines\ai-agent-dev-rules.md
```

Start a new agent session after installing or changing persistent instructions.

## Verify the setup

Run a normal, small task in a disposable branch or test repository. Confirm that
the agent:

- discovers the installed instruction file without a reminder;
- starts with `ai-agent-dev-rules.md` and loads only applicable rule pages;
- uses one rules revision for the complete run;
- makes no project change before required pages are available; and
- reports the rules revision, version, loaded Rule IDs, and validation results.

The [detailed bootstrap guide](https://wiki.fe-wi.com/en/dev-guide/ai-agent-repository-bootstrap)
contains expanded GitHub Web UI instructions, Codex Cloud configuration,
security notes, verification steps, and troubleshooting.
