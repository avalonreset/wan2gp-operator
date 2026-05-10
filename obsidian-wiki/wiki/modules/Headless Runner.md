---
type: module
title: "Headless Runner"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - headless
status: active
path: "scripts/run_headless.py"
language: python
related:
  - "[[Headless Process Runs]]"
  - "[[Learned Compatibility State]]"
---

# Headless Runner

`scripts/run_headless.py` executes WanGP headless jobs through `wgp.py --process`.

## Contract

- Resolve WanGP root and process file.
- Build the `wgp.py --process` command.
- Support `--dry-run`.
- Capture logs.
- Retry once for known incompatibility signatures.
- Persist learned unsupported flags or attention modes.

## Failure Handling

The runner learns issues such as unsupported TeaCache, compile failures, or
attention backend incompatibility and can fall back to safer choices.
