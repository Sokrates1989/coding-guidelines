# Global Development Rules

At the start of every new AI-assisted software-development agent run, read and follow:

`D:\Development\Code\coding-guidelines\ai-agent-dev-rules.md`

The canonical repository is `https://github.com/sokrates1989/coding-guidelines`. Use the local clone as the operational rules installation. Do not browse or fetch the remote repository during an active task merely to reload rules.

Use the root file as a router and load only the local pages applicable to the current task, repository, files, languages, frameworks, and workflows. After loading the root and operating contract, perform the minimum read-only repository discovery needed to select additional pages. Do not modify project files until every required page has been read.

Within one continuous agent run, retain already-loaded unchanged pages while their content, Rule IDs, and ruleset version remain reliably available in context. A new operator message alone is not a reload trigger. On follow-up messages, re-evaluate the scope and load only newly applicable pages and their required dependencies.

Reload the root and applicable pages when the operator says the rules changed or requests a refresh, the checked-out rules revision changed, compaction or handoff no longer preserves the required content, or the loaded version or requirements are uncertain. Strict adherence takes priority over avoiding a repeated read.

Re-evaluate applicable pages before expanding the planned scope. Never claim compliance with a page that was not read or validation that was not executed.

System, tool, security, current user, and more narrowly scoped repository instructions retain their normal precedence.

If the local root router or a required page cannot be read, stop before modifying the project and report the inaccessible path. Update the rules clone only when explicitly requested and preferably between agent runs.
