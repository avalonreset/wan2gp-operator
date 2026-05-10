---
type: flow
title: "GX10 High Memory Test Ladder"
created: 2026-05-10
updated: 2026-05-10
tags:
  - flow
  - gx10
  - high-memory
status: active
related:
  - "[[Wan 2.2 A14B]]"
  - "[[LTX-2.3 Dev 22B]]"
---

# GX10 High Memory Test Ladder

## Purpose

Exercise a 128GB unified-memory machine with models that actually benefit from
memory headroom.

## Ladder

1. Assess hardware and update WanGP.
2. Prepare serious model targets: [[Wan 2.2 A14B]] and [[LTX-2.3 Dev 22B]].
3. Run Wan 2.2 A14B text-to-video at 720p, 24 fps, 12 seconds.
4. Run Wan 2.2 A14B image-to-video at 720p, 24 fps, 10 to 12 seconds.
5. Run LTX-2.3 Dev 22B at 720p, 24 fps, 16 to 20 seconds.
6. If stable, run a short 1080p stress test.
7. Build an overnight comparison queue only after the first runs produce usable logs.

## Principle

Do not start with tiny models on high-memory machines unless the goal is install
sanity checking.
