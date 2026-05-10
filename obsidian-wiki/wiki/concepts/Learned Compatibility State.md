---
type: concept
title: "Learned Compatibility State"
created: 2026-05-10
updated: 2026-05-10
tags:
  - concept
  - compatibility
status: active
related:
  - "[[Headless Runner]]"
---

# Learned Compatibility State

Learned compatibility state records what flags, attention backends, or runtime
features failed for a WanGP install.

## File

`<WAN2GP_ROOT>/.wan2gp_operator_state.json`

## Purpose

Prevent repeated failures by allowing the operator to skip known-bad flags or
fall back to safer settings.
