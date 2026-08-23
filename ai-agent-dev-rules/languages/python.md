# Python Development Rules

**Rule ID:** `LANG-PYTHON`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to Python source, tests, packaging, tooling, or configuration.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.7.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Style and structure

- Follow the repository’s configured Python version, formatter, linter, type checker, and dependency manager.
- Use explicit imports. Do not use wildcard imports.
- Use type annotations for public functions, non-trivial internal functions, data models, and values whose type is not obvious.
- Prefer focused modules and dependency injection at external boundaries.
- Keep import-time side effects to a minimum.

## Documentation

Use the repository’s established docstring style. Otherwise use clear PEP-compatible docstrings documenting semantics, parameters, returns, raised exceptions, side effects, and special values. Module docstrings describe responsibility and boundaries rather than author/date/version metadata.

## Errors and resources

- Raise specific exceptions with actionable messages.
- Preserve exception context with `raise ... from ...` when translating errors.
- Do not catch broad exceptions unless the boundary must log, translate, or recover; never silently swallow them.
- Use context managers for files, connections, locks, and transactions.
- Separate validation from side effects.

## Data and configuration

- Prefer typed models for structured inputs and outputs.
- Keep configuration loading, parsing, validation, and domain transformation in the repository-defined layers.
- Avoid mutable default arguments.
- Use timezone-aware dates when values cross system boundaries.

## Testing

Use repository-defined test commands. Tests should be deterministic and isolate databases, filesystems, clocks, networks, and environment variables where practical. Do not introduce local-only tooling when the repository intentionally runs Python through Docker.
