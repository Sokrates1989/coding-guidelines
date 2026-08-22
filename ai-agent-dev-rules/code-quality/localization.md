# Localization and User-Facing Text

**Rule ID:** `QUALITY-LOCALIZATION`  
**Status:** Active.  
**Applies when:** Creating, changing, planning, reviewing, or diagnosing user-facing text, messages, labels, errors, notifications, accessibility copy, localization resources, locale behavior, or localization providers.  
**Required pages:** `CORE-OPERATING-CONTRACT`, `CORE-CHANGE-SAFETY`, `CORE-VALIDATION-COMPLETION`  
**Overrides:** None.  
**Ruleset version:** `2.6.0`.  
**Updated:** `2026-08-10`.  
**Root router:** [../../ai-agent-dev-rules.md](../../ai-agent-dev-rules.md).

## Non-negotiable translation boundary

User-facing text includes visible UI copy, dialogs, validation and error messages, notifications, onboarding and tutorial text, legal and reward copy, accessibility labels, user-visible CLI output, emails, and other content presented to an end user.

- MUST NOT hardcode user-facing text directly in application code, UI markup, templates, or business logic. Literal copy belongs in localization resources or their tool-owned source files.
- Every new or changed user-facing key MUST include complete English (`en`) and German (`de`) translations by default, plus every additional locale the repository requires to remain complete.
- MUST NOT add an untranslated fallback string beside a localization lookup. Missing-key behavior uses the configured fallback locale and is validated rather than hidden with duplicate hardcoded copy.
- Internal identifiers, protocol error codes, developer-only logs, and test descriptions that users cannot see are not user-facing text. Translate an internal error at the presentation boundary; do not expose raw implementation messages to users.
- When the requested change touches existing hardcoded user-facing text, migrate that text into the localization system. Report broader violations outside the requested scope instead of silently expanding into a repository-wide migration.

## Provider selection

- Inspect the repository’s language, framework, existing localization provider, supported platforms, build tooling, generated-file ownership, and dependency policy before choosing an implementation.
- Reuse an established supported localization system. MUST NOT introduce a parallel provider merely because another library is generally preferred.
- When establishing or intentionally replacing a provider, the AI MUST select the best supported option for that tool and briefly report the evidence behind the choice.
- For Flutter, SHOULD prefer `easy_localization` when it is compatible with the repository and supported targets. For most other projects, SHOULD prefer the ecosystem’s established i18n solution. When those options are unsupported or unsuitable, MUST use the best maintained framework-native or ecosystem-supported localization mechanism instead.
- If provider selection adds or changes a dependency, load and follow [Dependencies and Compatibility](dependencies-and-compatibility.md) before editing manifests or lock files.
- Update generated localization output only through the repository’s supported generator or build command.

## Translation catalog layout

- Default to one logical global translation source per locale, such as `en.json` and `de.json` or the provider’s idiomatic equivalent. Adding a language SHOULD normally require adding and translating one corresponding global locale file.
- Organize keys with stable semantic namespaces inside the global file. MUST NOT create separate catalogs for every screen or component by default.
- A separate localization file SHOULD be introduced only when both the domain boundary is obvious and cohesive and the translation volume is substantial enough to make the global catalog difficult to maintain. Suitable examples include legal documents, tutorials or onboarding, and rewards content.
- Every extracted catalog MUST have the same ownership, loader registration, key structure, and locale coverage across English, German, and all other required locales.
- Follow a provider-mandated catalog structure when it cannot support the preferred global-per-locale layout safely.

## Message construction

- Use stable semantic keys rather than English source sentences as identifiers.
- Use provider-supported interpolation, pluralization, selection, date, number, and currency formatting. MUST NOT assemble translated sentences through string concatenation.
- Keep placeholders, plural branches, markup, and formatting semantics compatible across English and German.
- Write natural, context-appropriate translations. Preserve meaning, tone, accessibility, and action labels rather than translating isolated words mechanically.

## Validation

- Verify that every added or changed key exists in English and German and that required locale key sets remain synchronized.
- Check placeholder and plural parity, fallback behavior, locale switching, text expansion, and affected accessibility labels as applicable.
- Run the repository’s localization linter, generator, tests, or missing-key checks. Add focused validation when the repository lacks coverage for a new localization contract.
- Search the modified scope for hardcoded user-facing text and remove any fallback copy that bypasses the localization provider.
