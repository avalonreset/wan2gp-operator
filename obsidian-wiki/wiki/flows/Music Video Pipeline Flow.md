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
  - "[[ACE-Step 1.5]]"
  - "[[Automated Beat Editing Rubric]]"
---

# Music Video Pipeline Flow

## Steps

1. Generate or accept audio. Generated audio should use [[ACE-Step 1.5]].
2. Analyze audio for duration, BPM, beats, downbeats, sections, and energy.
3. Build a director treatment: motifs, palette, subject rules, and section intent.
4. Plan shots using the [[Automated Beat Editing Rubric]].
5. Compose settings for each shot with the selected video model.
6. Generate takes through WanGP.
7. Select takes, assemble clips, apply edit strategy, and mux audio with FFmpeg.

## Current Watchpoint

Model selection must pass through the full pipeline. The pipeline should not
silently override explicit model choices on high-memory systems.

Editing should not default to one cut per beat. Section energy and phrase
structure should control cut density and transition style.
