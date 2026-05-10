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
  - "[[Wan 2.2 A14B]]"
  - "[[LTX-2.3 Dev 22B]]"
---

# High Memory Model Defaults

## Decision

For 96GB+ and 128GB-class machines, do not default to tiny low-VRAM models except
for install sanity checks. Recommend serious targets first.

## Current Defaults

- Use [[Wan 2.2 A14B]] for the clean high-memory 720p proof.
- Use [[LTX-2.3 Dev 22B]] for creative quality and longer-coherence tests.
- For quality-mode 96GB+ composition, recommend `sage2`, `profile 3`, and compile.

## Rationale

High-memory users need a path that uses the hardware. Low-VRAM survival defaults
are still valuable, but they should not be the first recommendation for GX10 or
DGX Spark-class machines.
