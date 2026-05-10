---
type: module
title: "Skill Installer"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - install
status: active
path: "scripts/install_skill.py"
language: python
related:
  - "[[Dual Runtime Skill Compatibility]]"
  - "[[Codex]]"
  - "[[Claude]]"
---

# Skill Installer

`scripts/install_skill.py` installs the operator into user or project skill
directories for Codex, Claude, and Gemini.

## Current Verified Targets

- Codex project install: `.codex/skills/wan2gp-operator`
- Claude project install: `.claude/skills/wan2gp-operator`

## Contract

The installer should preserve a single repo shape while installing into each
agent runtime's expected skill directory.
