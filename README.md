# Coding Guidelines for AI Agents

This repository is the canonical source for modular development rules used by
AI coding agents.

Start with the [AI Agent Development Rules router](ai-agent-dev-rules.md). The
router selects only the rule pages needed for the current repository and task.

The files in a local clone are the operational rules installation. Update the
clone between agent runs rather than changing its revision during active work.

## Setup for human maintainers

The setup material below is documentation for people who want to connect an AI
coding agent to this ruleset. It is non-normative and does not change agent
behavior unless a person copies a template into a location that their coding
agent treats as instructions.

- [Human setup guide](docs/human-agent-setup.md): copy-ready repository, cloud,
  and desktop instructions for Codex, Cursor, Devin, and Claude Code.
- [Detailed repository and Codex Cloud bootstrap](https://wiki.fe-wi.com/en/dev-guide/ai-agent-repository-bootstrap):
  expanded setup, security, verification, and troubleshooting guidance.
