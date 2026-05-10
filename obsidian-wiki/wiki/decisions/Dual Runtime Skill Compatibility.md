---
type: decision
title: "Dual Runtime Skill Compatibility"
created: 2026-05-10
updated: 2026-05-10
tags:
  - decision
  - codex
  - claude
status: active
related:
  - "[[Skill Installer]]"
  - "[[Codex]]"
  - "[[Claude]]"
---

# Dual Runtime Skill Compatibility

## Decision

Maintain compatibility with Codex and Claude skill/project conventions.

## Verified In This Snapshot

- Project-scope Codex install succeeded.
- Project-scope Claude install succeeded.
- `SKILL.md`, `AGENTS.md`, and `CLAUDE.md` all describe the same operator contract.

## Boundary

Claude UI runtime was not live-smoke-tested in the 2026-05-10 session. The
filesystem layout and installer behavior were verified.
