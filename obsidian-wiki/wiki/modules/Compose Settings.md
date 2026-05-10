---
type: module
title: "Compose Settings"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - settings
status: active
path: "scripts/compose_settings.py"
language: python
related:
  - "[[VRAM Aware Composition]]"
  - "[[High Memory Model Defaults]]"
---

# Compose Settings

`scripts/compose_settings.py` turns a natural-language generation request into a
WanGP settings JSON.

## Important Behavior

- Accepts explicit curated model targets through `--model`.
- Uses VRAM input or detected GPU state to select defaults.
- Produces a process JSON outside WanGP `defaults/`.
- Emits runtime flag recommendations such as attention backend, profile, TeaCache, and compile.

## High-Memory Path

For 96GB+ quality-mode composition, the current recommendation is `sage2`,
`profile 3`, and compile enabled.
