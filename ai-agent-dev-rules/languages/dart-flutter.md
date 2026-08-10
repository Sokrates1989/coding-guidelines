# Dart and Flutter Development Rules

**Rule ID:** `LANG-DART-FLUTTER`  
**Status:** Active.  
**Applies when:** Creating, materially changing, planning, reviewing, or diagnosing changes to Dart, Flutter widgets, packages, platform integration, Flutter tests, or Flutter project configuration.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `DOC-COMMENTS-DOCSTRINGS`  
**Overrides:** None.  
**Ruleset version:** `2.2.0`.  
**Updated:** `2026-08-09`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Dart language

- Follow the repository’s Dart SDK constraint, `analysis_options.yaml`, formatter, and lints.
- Every control-flow block MUST use curly braces.
- When documentation is required by `DOC-COMMENTS-DOCSTRINGS`, use Dartdoc for classes, functions, methods, widgets, state classes, callback handlers, and helpers.
- Prefer sound null safety, immutable models, `final`, and `const` where semantics permit.
- Do not use `dynamic` to bypass a model or boundary that can be typed.

## Flutter widgets and state

- Keep widgets focused and extract coherent private widgets or render helpers before creating many separate files.
- Do not perform side effects in `build`.
- Dispose controllers, focus nodes, subscriptions, and other owned resources.
- After an `await`, check `mounted` before using a `BuildContext` or mutating state when the operation can outlive the widget.
- Preserve navigation, lifecycle, focus, accessibility, and platform behavior.
- Use the repository’s established state-management pattern; do not introduce another one for a small feature.

## Generated files and identity

Do not edit generated Dart, localization output, platform registrants, build output, or creator-owned files directly. Update the owning input or generator and regenerate through the documented workflow. Preserve Android package identity, iOS bundle identity, and app ownership contracts.

## Localization and accessibility

Use localization keys for user-visible text when localization is configured. Update every required locale. Use semantic widgets, labels, focus order, and touch targets appropriate to the supported platforms.

## Validation

Run Flutter commands from the correct app or package root. Use repository-defined versions and commands. Typical focused validation includes formatting, analysis, unit/widget tests, and a build proof for affected platforms when required.
