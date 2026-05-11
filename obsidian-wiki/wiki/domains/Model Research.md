---
type: domain
title: "Model Research"
created: 2026-05-10
updated: 2026-05-10
tags:
  - domain
  - models
  - research
status: active
related:
  - "[[RTX 4090]]"
  - "[[Wan 2.2 A14B]]"
  - "[[LTX-2.3 Dev 22B]]"
  - "[[Curated Model Targets]]"
---

# Model Research

This domain tracks model recommendations and how they map into WanGP settings.

## Current Snapshot

- [[Wan 2.2 A14B]] is the clearest 128GB proof target because the full 720p path is memory hungry enough to justify the hardware.
- [[LTX-2.3 Dev 22B]] is the current creative quality target for long-coherence and audio-video experimentation.
- [[RTX 4090]] development should use LTX-2.3 distilled for iteration and explicit short LTX-2.3 dev quality tests, but keep stable runtime flags until Sage/Sage2 is locally proven.
- Tiny models remain useful only for installation sanity checks on high-memory machines.

> [!stale] Time-sensitive guidance
> Model recommendations change quickly. Run `python scripts/wan2gp_operator.py models --wan-root <WAN2GP_ROOT>` and verify current WanGP upstream notes before publishing a "latest and greatest" answer.

## Related

- [[Model Catalog]]
- [[High Memory Model Defaults]]
- [[GX10 High Memory Test Ladder]]
