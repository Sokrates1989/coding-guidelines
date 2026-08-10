# JavaScript and TypeScript Development Rules

**Rule ID:** `LANG-JAVASCRIPT-TYPESCRIPT`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to JavaScript, TypeScript, Node.js tooling, frontend modules, or related tests/configuration.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.3.0`.  
**Updated:** `2026-08-10`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Control flow and typing

- Every `if`, `else`, `for`, `while`, and similar block MUST use curly braces, including single-line bodies.
- Follow the repository’s TypeScript strictness and existing formatter/linter.
- Prefer explicit domain types, discriminated unions, type guards, and `unknown` over `any`.
- Do not use non-null assertions merely to silence the type checker; prove or handle the condition.
- Preserve runtime validation at untrusted boundaries. Static types do not validate external data.

## Functions and modules

- When documentation is required by `DOC-COMMENTS-DOCSTRINGS`, use the repository’s established JSDoc or TSDoc convention and describe semantics that types alone do not express.
- Prefer `const` and immutable transformations where practical.
- Keep modules focused and avoid hidden global state.
- Use explicit exports and established index-file conventions.
- Clean up timers, subscriptions, observers, and event listeners.

## Asynchronous behavior

- Await, return, aggregate, or explicitly handle every promise.
- Fire-and-forget work MUST use an explicit convention such as `void` only when rejection, cancellation, and ownership are handled at a documented boundary.
- Handle rejected promises at the appropriate boundary.
- Preserve cancellation and stale-result protection for user-driven asynchronous work.
- Do not mix callback, promise, and async styles without a documented boundary reason.

## Browser and Node boundaries

Keep browser-only and server-only dependencies separated. Do not expose secrets in frontend bundles. Treat storage, URL, postMessage, DOM, and API data as untrusted. Preserve accessibility and security behavior when manipulating the DOM.

## User-facing text

All new or changed user-visible and AI-generated text MUST follow [Localization and User-Facing Text](../code-quality/localization.md). Do not hardcode a parallel untranslated fallback string.
