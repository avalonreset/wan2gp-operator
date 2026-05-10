---
type: module
title: "Update Checker"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - updates
status: active
path: "scripts/check_updates.py"
language: python
related:
  - "[[WanGP]]"
---

# Update Checker

`scripts/check_updates.py` checks WanGP upstream release and commit state.

## Important Context

WanGP can publish meaningful updates through README and main branch changes even
when GitHub releases are not the primary signal. The checker should account for
README-derived version data and upstream commit IDs.
