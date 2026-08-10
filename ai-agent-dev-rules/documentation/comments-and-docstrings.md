# Comments and Docstrings

**Rule ID:** `DOC-COMMENTS-DOCSTRINGS`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to commentable source code, comments, docstrings, components, hooks, handlers, helpers, or logical code groups.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`  
**Overrides:** None.  
**Ruleset version:** `2.2.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Named declarations

Public APIs and non-obvious named functions, methods, classes, React components, hooks, event handlers, and assigned helpers MUST have documentation in the idiomatic location for their language.

- Public APIs and non-obvious internal code require complete documentation.
- A small but meaningful named internal helper MAY use a concise one-sentence documentation block when its signature and behavior are obvious.
- Private or file-local status alone is not a reason to omit documentation when the declaration owns meaningful behavior, side effects, assumptions, or error handling.
- Tiny self-explanatory test helpers, getters, setters, callbacks, and local handlers MAY omit separate documentation when names, types, the parent declaration, or the surrounding section already explain their complete contract.
- Documentation MUST describe purpose and, when applicable, parameters, return values, defaults, side effects, errors, fallback states, assumptions, permissions, and special sentinel values.
- Do not repeat type annotations or restate the function name without adding semantic information.

Follow the existing valid documentation convention in the file. Otherwise use the language page and the [documentation examples](comments-and-docstrings/examples.md).

## File-level documentation

Every public module and every hand-maintained commentable code file with a non-obvious responsibility or architectural boundary MUST contain an idiomatic file-level or module-level documentation block describing:

- Its primary responsibility.
- Important architectural boundaries or invariants.
- Significant side effects or runtime dependencies.
- Safe extension points when they are not obvious.

Small single-purpose internal files MAY omit a file-level block when their path, name, declarations, and repository convention already make their responsibility complete and unambiguous. Do not require author, creation date, file version, routine import lists, or dependency versions. Git and package manifests own that information. Generated files and files whose format forbids comments are exempt.

## Logical group comments

Use concise group comments when declarations, statements, or JSX form a non-obvious logical section whose purpose, lifecycle, ownership, or relationship is not clear from names and structure alone. Blank-line separation by itself does not require a comment.

- A single word or very short heading is valid when it clearly names the group.
- Human-language explanatory comments SHOULD end with a sentence mark such as `.`, `!`, or `?`.
- Shebangs, pragmas, directives, formatter or linter controls, ShellCheck annotations, labels, generated markers, separators, and tool-required comments are exempt from prose and punctuation rules.
- Larger or non-obvious groups MUST use a visually prominent multi-line block that explains the group’s purpose, relationship, lifecycle, or invariant.
- Group comments are structural navigation and MAY be concise even when the underlying code is obvious.
- Comments MUST remain synchronized when the group moves, changes responsibility, or is removed.

## Visibility

Use one-line comments for one immediate line or one tiny group of at most three closely related lines. Use prominent multi-line comments for larger sections. Use full documentation blocks for declarations that require complete documentation under the named-declaration rule.

Comments inside JSX MUST explain purpose, state dependency, accessibility, permissions, or layout reasoning. They MUST NOT merely repeat tag names. Large JSX return blocks MUST be extracted into named internal render helpers or components when comments alone no longer make the structure easy to scan.

## Non-commentable files

Add or update a companion Markdown document only when a created or substantially changed non-commentable file has lasting, non-obvious ownership, schema, generation, or safe-editing rules.

Appropriate examples include custom policy JSON, custom schemas, complex deployment data, and grouped configuration contracts. Do not create companion documents for lock files, generated files, test snapshots, standard package manifests, small translation dictionaries, or self-explanatory data.

Use `<filename>.md` for one file or `README.md` for a coherent group.

## Maintenance

Documentation changes in the same logical change as behavior. Update parent documentation after extraction, remove stale statements, and never delete useful documentation merely to satisfy a line limit.
