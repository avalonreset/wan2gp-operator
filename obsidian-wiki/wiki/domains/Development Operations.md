---
type: domain
title: "Development Operations"
created: 2026-05-10
updated: 2026-05-10
tags:
  - domain
  - operations
status: active
related:
  - "[[Unified CLI Entrypoint]]"
  - "[[Headless Runner]]"
  - "[[Skill Installer]]"
---

# Development Operations

This domain tracks how Wan2GP Operator is developed, verified, installed, and
used by agents.

## Current Operating Rules

- Use `python scripts/wan2gp_operator.py <command>` as the primary interface.
- Run `python -m compileall scripts` after Python edits.
- Verify Codex and Claude skill installation paths after installer changes.
- Do not claim WanGP update status without running `updates`.
- Do not recommend tiny models for high-memory machines unless debugging installation health.

## Key Pages

- [[Unified CLI Entrypoint]]
- [[Skill Installer]]
- [[Update Checker]]
- [[Headless Render Flow]]
