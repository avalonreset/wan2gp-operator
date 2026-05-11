---
type: decision
title: "High Memory Model Defaults"
created: 2026-05-10
updated: 2026-05-10
tags:
  - decision
  - models
status: active
related:
  - "[[GX10 High Memory Test Ladder]]"
  - "[[RTX 4090]]"
  - "[[Wan 2.2 A14B]]"
  - "[[LTX-2.3 Dev 22B]]"
---

# High Memory Model Defaults

## Decision

For 96GB+ and 128GB-class machines, do not default to tiny low-VRAM models except
for install sanity checks. Recommend serious targets first.

For RTX 4090/24GB-class development machines, also avoid tiny demos by default,
but do not inherit the 96GB+ aggressive runtime flags. Treat 24GB as a serious
developer tier with stable execution defaults.

## Current Defaults

- Use [[Wan 2.2 A14B]] for the clean high-memory 720p proof.
- Use [[LTX-2.3 Dev 22B]] for creative quality and longer-coherence tests.
- For quality-mode 96GB+ composition, recommend `sage2`, `profile 3`, and compile.
- For [[RTX 4090]] development composition, recommend `ltx23-distilled-22b` for
  iteration, explicit `ltx23-dev-22b` for short quality tests, `sdpa`,
  `profile 3`, compile off, and TeaCache `2.0` for balanced iteration.

## Rationale

High-memory users need a path that uses the hardware. Low-VRAM survival defaults
are still valuable, but they should not be the first recommendation for GX10 or
DGX Spark-class machines.

24GB developer cards need a middle path: enough ambition to exercise current
models, but not enough memory headroom to treat every run like a 96GB+ proof
machine.
