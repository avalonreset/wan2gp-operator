---
type: module
title: "Music Video Pipeline"
created: 2026-05-10
updated: 2026-05-10
tags:
  - module
  - music-video
status: active
path: "scripts/music_video.py"
language: python
related:
  - "[[Music Video Pipeline Flow]]"
  - "[[Automated Beat Editing Rubric]]"
  - "[[ACE-Step 1.5]]"
---

# Music Video Pipeline

The music-video pipeline turns an audio file into a beat-aligned generation
plan, generates clips through WanGP, and assembles the final output with FFmpeg.

## Stages

- `music-analyze`
- `music-plan`
- `music-generate`
- `music-assemble`
- `music-video`

## Recent Fix

`v0.5.1` made curated model targets flow through this pipeline so high-memory or
LTX-2.3 targets are not silently forced back into legacy Wan 2.2 behavior.

## Next Upgrade

The next milestone should add a generated-song input path through [[ACE-Step 1.5]]
and replace simple beat-aligned shot planning with the [[Automated Beat Editing Rubric]].
