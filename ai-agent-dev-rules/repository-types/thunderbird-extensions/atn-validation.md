# Thunderbird Add-ons Validation Rules

**Rule ID:** `REPO-TYPE-THUNDERBIRD-ATN-VALIDATION`  
**Status:** Active.  
**Applies when:** A Thunderbird extension is validated, packaged, released, or prepared for addons.thunderbird.net submission.  
**Required pages:** `CORE-VALIDATION-COMPLETION`, `WORKFLOW-CI-CD`, `QUALITY-TESTING`, `QUALITY-DEPENDENCIES-COMPATIBILITY`  
**Overrides:** None.  
**Ruleset version:** `2.10.0`.  
**Updated:** `2026-08-27`.  
**Root router:** [../../../ai-agent-dev-rules.md](../../../ai-agent-dev-rules.md).

## Packaged validation

- Run a pinned add-on linter against the built XPI before public submission or release. Validating only the source directory is insufficient.
- Review every error, notice, and warning. Eliminate actionable findings and fail the local or CI check when any unreviewed finding appears.
- Keep the linter version and reviewed warning policy in the repository so local validation and CI use the same contract.
- Validate package identity and version together with the findings; a clean report for the wrong XPI does not count.

## Thunderbird compatibility findings

Firefox-oriented validators can report documented Thunderbird-only permissions and MailExtension APIs as invalid or unsupported. For such findings:

- Verify each permission and API against current official Thunderbird documentation and confirm it is required by reachable functionality.
- Preserve necessary Thunderbird behavior. MUST NOT rename, alias, dynamically resolve, or otherwise hide API use merely to silence static analysis.
- Record exact stable fingerprints and counts in an explicit reviewed baseline. Avoid line-number-only baselines because unrelated edits make them brittle.
- Fail closed when a fingerprint or count changes. Update the baseline only with an intentional code, permission, documentation, and privacy review.
- Report validator-specific findings separately when the local generic Firefox linter and the Thunderbird Add-ons service apply different schemas.

MUST NOT baseline invalid manifests, unsafe DOM assignments, remote-code execution, obfuscation, undeclared data transfer, unnecessary permissions, or another security or privacy finding.

## Reviewer evidence

Document the remaining warning count and categories in the submission notes. Explain why each category is Thunderbird-specific, link the relevant official API or permission documentation, and provide a focused synthetic-data test that exercises the affected behavior.
