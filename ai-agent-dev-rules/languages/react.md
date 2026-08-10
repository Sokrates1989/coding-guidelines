# React Development Rules

**Rule ID:** `FRAMEWORK-REACT`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to React components, hooks, JSX/TSX, state, context, or React tests.  
**Required pages:** `LANG-JAVASCRIPT-TYPESCRIPT`, `DOC-COMMENTS-DOCSTRINGS`, `QUALITY-STRUCTURE-REFACTORING`  
**Overrides:** None.  
**Ruleset version:** `2.4.0`.  
**Updated:** `2026-08-10`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Components and hooks

- Apply `DOC-COMMENTS-DOCSTRINGS` to components, hooks, render helpers, handlers, and assigned helpers; describe important conditional rendering, state ownership, and side effects without repeating prop types.
- Keep components focused on one UI responsibility.
- Extract large inline JSX into documented internal render helpers or internal components before creating separate files.
- Move an element to a separate file only when reuse, independent responsibility, size, state, tests, or a dependency boundary justifies it.
- Custom hooks MUST follow hook rules and expose a stable, documented contract.

## State and effects

- Derive values during rendering when they do not need independent state.
- Keep state as local as practical and avoid duplicated sources of truth.
- Effects synchronize with external systems; do not use them as a substitute for ordinary derivation.
- Declare complete dependencies and handle cleanup.
- Guard asynchronous results against unmounting or superseded requests where relevant.
- Do not add memoization by default; use it when measured cost or identity stability requires it.

## JSX structure and comments

Non-obvious JSX sections require concise comments under the global logical-group rule. Comments explain purpose, state, permissions, accessibility, or layout rationale. Blank lines alone do not require comments, and comments do not repeat tag names.

## Accessibility

Preserve semantic elements, keyboard access, focus behavior, labels, error association, and suitable ARIA semantics. Do not replace native controls with generic elements without implementing equivalent behavior.

## Text and configuration

User-visible text MUST follow [Localization and User-Facing Text](../code-quality/localization.md). Keep environment-specific frontend configuration out of source code and never expose secrets to the browser.
