---
type: decision
title: "Automated Beat Editing Rubric"
created: 2026-05-10
updated: 2026-05-10
tags:
  - decision
  - music-video
  - editing
status: active
related:
  - "[[Music Video Pipeline]]"
  - "[[Music Video Pipeline Flow]]"
  - "[[ACE-Step 1.5]]"
  - "[[RTX 4090]]"
---

# Automated Beat Editing Rubric

## Decision

The music-video generator should not cut on every beat by default. It should use
a hierarchy of musical events and section energy to decide shot length,
transition style, and visual intensity.

## Beat Hierarchy

1. Section boundaries: intro, verse, pre-chorus, chorus, bridge, outro.
2. Phrase boundaries: usually every 4, 8, or 16 bars.
3. Downbeats: first beat of a bar, good for major visual changes.
4. Strong beats: useful for standard cuts and action accents.
5. Microbeats: only for bursts, glitches, or rapid montage moments.

## Section Rules

- Intro: slower cuts, establishing shots, motif setup.
- Verse: medium cuts, narrative continuity, character/world building.
- Pre-chorus: shorter shots, rising motion, forward camera movement.
- Chorus/drop: highest density, hero shots, strongest subject clarity.
- Bridge: contrast, slower or stranger visual language.
- Outro: deceleration, closure, callbacks to earlier motifs.

## Transition Palette

- Hard cut: default on downbeats and strong beat accents.
- Match cut: repeated gesture, pose, color, or camera direction.
- Crossfade: slow intro/outro moments only.
- Whip/pan transition: energetic chorus or section lift.
- Flash/white cut: impact hits, snares, or drop starts.
- Speed ramp: lead into chorus or emphasize one strong movement.
- Hold/freeze: lyric emphasis or final beat of phrase.

## Shot Planning

Each shot should carry:

- musical role: intro, verse, chorus, bridge, outro
- edit role: establish, develop, impact, contrast, resolve
- cut anchor: section boundary, phrase, downbeat, beat, or offbeat
- transition after: hard, match, crossfade, whip, flash, speed-ramp, hold
- visual motif: subject, color, environment, prop, motion, or symbol
- take count: more takes for chorus/hero shots, fewer for filler shots

## Validation Goal

The first serious milestone is a five-shot proof:

- ACE-Step generated song excerpt.
- 720p LTX/WanGP visual shots on RTX 4090.
- 3 takes per hero shot.
- Preview GIFs/stills for review.
- Beat-aware assembly that uses at least three transition styles.
- Final MP4 plus a review report explaining why each take was selected.

