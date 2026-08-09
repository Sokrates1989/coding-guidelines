# Support Files

This directory contains non-normative maintenance, validation, discovery, and integration artifacts for the canonical GitHub repository.

The tracked rule-page Markdown outside `_support` is the canonical ruleset content. A local clone is the operational installation for AI agents. GitHub-rendered pages, Wiki entries, exports, caches, adapters, manifests, and checksums do not override the tracked rule pages.

- `rules-manifest.json` lists rule IDs, dependencies, repository files, page types, load triggers, and word estimates.
- `llms.txt` is a concise optional discovery index.
- `codex/AGENTS.md` is a minimal global bootstrap for the local clone. Replace the prior monolithic global instructions with this content and start a new agent run after changing it.
- `validation/validate-ruleset.py` validates page metadata, dependencies, relative links, repository coverage, and size budgets.
- `migration-map.md` maps the previous monolithic rules into the modular hierarchy for review.
- `SHA256SUMS` records tracked content checksums and is regenerated after ruleset changes.

The canonical repository is `https://github.com/sokrates1989/coding-guidelines`.
