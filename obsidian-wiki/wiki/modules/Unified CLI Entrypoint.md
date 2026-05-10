---
type: module
title: "Unified CLI Entrypoint"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - cli
status: active
path: "scripts/wan2gp_operator.py"
language: python
related:
  - "[[Agent Operated WanGP Workflow]]"
---

# Unified CLI Entrypoint

`scripts/wan2gp_operator.py` is the primary command surface for agents.

## Contract

Route top-level commands to dedicated scripts while keeping one stable command
surface for Codex, Claude, and documentation.

## Commands

- `assess`
- `bootstrap`
- `setup`
- `launch-ui`
- `compose`
- `models`
- `plan`
- `run`
- `diagnose`
- `updates`
- `evolve`
- `music-video`

## Related

- [[Headless Runner]]
- [[Compose Settings]]
- [[Music Video Pipeline]]
