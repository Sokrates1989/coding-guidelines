# Bash CLI Help and Man Pages

**Rule ID:** `BASH-CLI-HELP-MAN`  
**Status:** Active.  
**Applies when:** Changing, planning, reviewing, or diagnosing inline help, command help, usage output, or installed man pages for an applicable Bash CLI tool.  
**Required pages:** `REPO-TYPE-BASH-CLI`, `BASH-CLI-VERSIONING`, `DOC-REPOSITORY-DOCUMENTATION`  
**Overrides:** None.  
**Ruleset version:** `2.7.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Inline help

These invocations MUST provide the same complete top-level inline reference and exit successfully:

```text
<tool> help
<tool> --help
<tool> -h
```

`help` MUST be handled as an explicit command as well as a flag path. Inline help covers every supported command, options and defaults, aliases, relevant environment requirements, and a short example. Include first-run, re-test, and private-configuration sections only when the tool actually supports those workflows.

Each command MUST provide focused command help through the repository’s established form, normally `<tool> <command> --help`.

## Real man page

When an installable tool targets environments that provide `man(1)`, it MUST provide a real man page. Use repository-defined source and installation prefixes. A conventional layout is:

```text
Source:  docs/man/<tool>.1
Install: /usr/local/share/man/man1/<tool>.1.gz
```

Minimum sections:

```text
NAME
SYNOPSIS
DESCRIPTION
COMMANDS
OPTIONS
ENVIRONMENT
FILES
EXAMPLES
AUTHOR
```

Add first-run or recovery sections when applicable.

The installer compresses or installs the source according to the target platform and runs `mandb --quiet` when available. Missing `mandb` MUST NOT fail installation. The uninstaller removes only tool-owned installed forms from the configured prefix and refreshes `mandb` when available.

## Distinct interfaces

```text
<tool> --help   Inline CLI reference.
man <tool>      Installed man page through man(1).
whatis <tool>   One-line mandb description.
```

`<tool> man` is an optional convenience alias that MAY page inline help. It MUST NOT replace the real man page.

Keep inline help, command behavior, README examples, and the man page synchronized in the same change.
