---
type: module
title: "Model Catalog"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - models
status: active
path: "scripts/model_catalog.py"
language: python
related:
  - "[[Curated Model Targets]]"
  - "[[Model Research]]"
---

# Model Catalog

`scripts/model_catalog.py` stores the curated targets the operator exposes.

## Current Targets

- `ltx23-dev-22b`
- `ltx23-distilled-22b`
- `wan22-t2v-14b`
- `wan22-i2v-14b`
- `magi-human-15b`

## Design Rule

The catalog should stay small. It is an operator-facing shortlist, not a mirror
of every WanGP default.

## Risk

> [!stale]
> WanGP changes quickly. This module should be refreshed whenever WanGP changes
> model defaults or adds a major new video family.
