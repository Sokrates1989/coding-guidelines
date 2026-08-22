# Repository Documentation

**Rule ID:** `DOC-REPOSITORY-DOCUMENTATION`  
**Status:** Active.  
**Applies when:** README files, architecture documents, setup instructions, API documentation, migration guides, operational runbooks, or companion documents are created, changed, planned, reviewed, or diagnosed.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.6.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Source of truth

- Documentation MUST describe the current implemented behavior, not intended future behavior, unless a section is explicitly labeled as a plan.
- Commands, paths, environment variables, ports, routes, and file names MUST be verified against the repository.
- Do not duplicate detailed rules or contracts already owned by another document; link to the canonical source.
- Keep generated documentation and hand-maintained documentation clearly distinguished.

## Required updates

Update relevant documentation when changing:

- Public APIs, CLI commands, options, defaults, or environment variables.
- Setup, build, test, deployment, rollback, or recovery procedures.
- Repository structure, ownership boundaries, generated paths, or extension points.
- Authentication, authorization, data handling, migrations, or compatibility requirements.
- User-visible behavior that existing documentation promises.

## Command examples

- Prefer copy-ready commands for the documented shell.
- State the required working directory and prerequisites when they are not obvious.
- Never include real secrets or production credentials.
- Do not claim a command was verified unless it was run successfully in the documented context.
- Keep Bash and PowerShell variants semantically equivalent when both are supported.

## Navigation and maintenance

Add a table of contents only when it improves navigation. Use descriptive headings and stable relative links. Validate links touched by the change. Remove stale or contradictory instructions rather than appending another competing procedure.
