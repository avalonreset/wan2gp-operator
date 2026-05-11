---
type: concept
title: "VRAM Aware Composition"
created: 2026-05-10
updated: 2026-05-10
tags:
  - concept
  - vram
status: active
related:
  - "[[Compose Settings]]"
---

# VRAM Aware Composition

VRAM-aware composition means the operator uses available memory and quality
intent to choose model targets, resolution defaults, step counts, and runtime
flags.

## Key Rule

Hardware tiers should change recommendations. A 128GB machine should not receive
the same defaults as a 12GB or 24GB machine.

## 24GB Developer Tier

RTX 4090-class cards are a distinct tier. They should get serious model targets,
not tiny demos, but their default runtime flags should stay stable until local
attention backend compatibility is known.
