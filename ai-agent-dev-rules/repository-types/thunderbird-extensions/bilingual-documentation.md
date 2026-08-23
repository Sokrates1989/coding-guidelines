# Thunderbird Bilingual Documentation Rules

**Rule ID:** `REPO-TYPE-THUNDERBIRD-BILINGUAL-DOCS`  
**Status:** Active.  
**Applies when:** Documentation is created, changed, reviewed, packaged, or published in a Thunderbird extension repository.  
**Required pages:** `DOC-REPOSITORY-DOCUMENTATION`, `QUALITY-LOCALIZATION`  
**Overrides:** None.  
**Ruleset version:** `2.8.0`.  
**Updated:** `2026-08-23`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## File and language contract

- Every tracked, maintained Markdown document MUST exist in complete English and German versions. Update both in the same coherent change.
- English is canonical for default filenames: `README.md`, `docs/topic.md`, and nested `README.md` files. German siblings use `.de.md`: `README.de.md`, `docs/topic.de.md`, and nested `README.de.md` files.
- The root `README.md` MUST be English. Immediately below its title, it MUST prominently link to `README.de.md` and state that the complete README is available in German. The German README MUST provide the reciprocal English link in the same position.
- Translations MUST preserve meaning, safety warnings, commands, paths, version numbers, compatibility claims, and publication status. Product names, identifiers, code, and externally defined API terms remain exact.

## Language-preserving navigation

- English documents MUST link to English project documents. German documents MUST link to the corresponding German project documents.
- A deliberate language switch MUST target the closest counterpart, not a document in an unrelated section.
- External links MAY be shared when no language-specific official destination exists.

## Validation

- Verify complete English/German file-pair coverage for maintained Markdown documentation.
- Validate all touched relative links and reject German navigation that silently returns to an English project document, or vice versa.
- Confirm both root README language links appear before introductory, download, installation, or feature content.
