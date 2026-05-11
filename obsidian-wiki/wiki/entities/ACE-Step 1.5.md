---
type: entity
title: "ACE-Step 1.5"
created: 2026-05-10
updated: 2026-05-10
tags:
  - entity
  - music-generation
  - audio
status: active
related:
  - "[[Music Video Pipeline]]"
  - "[[Automated Beat Editing Rubric]]"
---

# ACE-Step 1.5

ACE-Step 1.5 is the likely local music-generation source for the operator's
next music-video milestone.

## Current Fit

- Generates full stereo music with optional lyrics at 48 kHz.
- Supports local generation on consumer GPUs.
- XL variants are appropriate for RTX 4090-class machines.
- License is MIT according to the model card.
- Current WanGP v11.61 includes ACE-Step 1.5 XL defaults.

## RTX 4090 Target

Use the XL tier for serious tests:

- `ace15-xl-lm-4b`: first quality target in this operator, mapping to WanGP's
  ACE-Step 1.5 XL Turbo 4B DiT plus 4B LM preprocessing.
- `ace15-xl-lm-1-7b`: lower-overhead quality fallback that keeps the XL 4B DiT.
- Start at 120 seconds for first full-quality renders.
- Stretch to 180 seconds after 120 seconds succeeds locally.
- Avoid dropping to non-XL or no-LM variants unless debugging install health.

## Pipeline Role

ACE-Step should produce the song, lyrics, and structured song metadata. The
operator should then analyze that audio into sections, beats, downbeats, energy,
and edit density before planning WanGP/LTX video shots.
