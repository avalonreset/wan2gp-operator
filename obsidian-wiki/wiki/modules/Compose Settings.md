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
  - "[[RTX 4090]]"
---

# Compose Settings

`scripts/compose_settings.py` turns a natural-language generation request into a
WanGP settings JSON.

## Important Behavior

- Accepts explicit curated model targets through `--model`.
- Accepts `--task music` for ACE-Step 1.5 song settings.
- Uses VRAM input or detected GPU state to select defaults.
- Produces a process JSON outside WanGP `defaults/`.
- Emits runtime flag recommendations such as attention backend, profile, TeaCache, and compile.

## High-Memory Path

For 96GB+ quality-mode composition, the current recommendation is `sage2`,
`profile 3`, and compile enabled.

## RTX 4090 Development Path

For 24GB-class composition, the current recommendation is serious model targets
with stable runtime flags: `sdpa`, `profile 3`, compile disabled, and TeaCache
`2.0` for balanced iteration until Sage/Sage2 compatibility is proven locally.

For ACE-Step 1.5 music generation on RTX 4090, use `--model ace15-xl-lm-4b`
with `--quality quality`. The first full-quality target is 120 seconds; 180
seconds is a stretch target after the 120-second path succeeds.
