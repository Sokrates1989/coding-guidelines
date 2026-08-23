# Structure and Refactoring

**Rule ID:** `QUALITY-STRUCTURE-REFACTORING`  
**Status:** Active.  
**Applies when:** A file or function grows materially, structural extraction is implemented, planned, reviewed, or diagnosed, or the task is a refactor.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.7.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Size metrics

- **Effective code lines:** Non-empty source lines excluding comments, docstrings, and blank lines.
- **Physical lines:** All lines.

| File type | Target effective | Hard effective | Target physical | Hard physical |
| --- | ---: | ---: | ---: | ---: |
| Python | 350 | 500 | 700 | 950 |
| JavaScript / TypeScript | 350 | 500 | 750 | 1000 |
| React / UI component | 300 | 450 | 800 | 1050 |
| Java / C# | 400 | 600 | 850 | 1100 |
| Commentable configuration | 160 | 280 | 350 | 550 |
| Non-commentable data | 160 | 280 | 250 | 400 |

A target threshold triggers a structural review. A hard threshold prohibits adding further unrelated complexity without a documented extraction plan. An existing oversized file does not authorize broad refactoring during an unrelated task.

Generated files, migrations, schemas, fixtures, translations, snapshots, declarative mappings, and tool-owned outputs require explicit repository-specific interpretation. Never delete useful documentation to reduce physical line count.

## Functions and nesting

- Target one responsibility per function.
- More than 50 effective code lines or more than three nested control levels triggers extraction review.
- Framework-required declarative structures, state machines, and cohesive mappings MAY justify an exception when splitting would reduce clarity.
- Extracted helpers MUST be named by responsibility and documented.

## Extraction order

For tightly coupled code, prefer:

1. Improve names and documentation.
2. Extract large inline logic or JSX into named internal helpers, components, classes, or objects in the same file.
3. Extract shared file-local configuration in the same file.
4. Create a separate file only when reuse, size, independent responsibility, tests, state, data contracts, or dependency boundaries justify it.

Do not create many tiny files for fragments meaningful only inside one parent. Navigation cost is a design cost.

## Refactoring protocol

1. Identify the behavior and public boundaries that must remain stable.
2. Run a useful baseline when available.
3. Make one coherent structural step at a time.
4. Preserve imports, API contracts, side effects, ordering, accessibility, and error behavior.
5. Update tests and documentation with the new structure.
6. Check circular dependencies and configuration references.
7. Validate after the refactor.

Refactoring MUST NOT silently change behavior unless the task explicitly combines a refactor with a behavior change and tests document that change.
