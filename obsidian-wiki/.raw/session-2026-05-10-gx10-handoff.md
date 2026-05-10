---
type: raw
title: "Session Snapshot 2026-05-10 GX10 Handoff"
created: 2026-05-10
source: chat
tags:
  - raw
  - gx10
  - handoff
---

# Session Snapshot 2026-05-10 GX10 Handoff

The project was updated and released through `v0.5.3`.

Key outcomes:

- `v0.5.0`: added current model guidance, curated model catalog, and direct `compose --model` targets.
- `v0.5.1`: passed curated model targets through the music-video pipeline so LTX-2.3 and Wan 2.2 targets can be used in sequential generation.
- `v0.5.2`: tuned high-memory quality-mode recommendations for 96GB+ machines to use `sage2`, `profile 3`, and compile.
- `v0.5.3`: clarified public docs around the agent-operated WanGP workflow for Codex and Claude.

The GX10 handoff brief positioned Wan2GP Operator as the skill suite to install
into Codex or Claude. The agent, not the human, should choose model targets,
compose settings, dry-run, run headless WanGP jobs, inspect logs, and retry with
safer settings when failures occur.

High-memory guidance:

- Wan 2.2 A14B is the cleanest 128GB proof path, especially 720p T2V and I2V.
- LTX-2.3 Dev 22B is the creative quality target for long coherence and audio-video experiments.
- Tiny models should be used only for install sanity checks on high-memory machines.
