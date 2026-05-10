---
type: flow
title: "Music Video Pipeline Flow"
created: 2026-05-10
updated: 2026-05-10
tags:
  - flow
  - music-video
status: active
related:
  - "[[Music Video Pipeline]]"
---

# Music Video Pipeline Flow

## Steps

1. Analyze audio for duration, BPM, beats, and sections.
2. Plan beat-aligned shots.
3. Compose settings for each shot with the selected model.
4. Generate takes through WanGP.
5. Assemble clips and mux audio with FFmpeg.

## Current Watchpoint

Model selection must pass through the full pipeline. The pipeline should not
silently override explicit model choices on high-memory systems.
