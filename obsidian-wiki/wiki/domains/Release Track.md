---
type: domain
title: "Release Track"
created: 2026-05-10
updated: 2026-05-10
tags:
  - domain
  - releases
status: active
related:
  - "[[Agent Operated Control Layer]]"
  - "[[High Memory Model Defaults]]"
---

# Release Track

## Latest Known Release

`v11.61` on 2026-05-10.

Release numbers now match the verified upstream WanGP version. The operator is
not a separate semver track for public releases; `v11.61` means this operator
snapshot was verified against WanGP `11.61`.

## Recent Release Arc

| Version | Focus |
|---|---|
| `v0.5.0` | Current model guidance, curated model catalog, `compose --model` targets |
| `v0.5.1` | Music-video pipeline passes curated model targets |
| `v0.5.2` | 96GB+ quality-mode runtime recommendation tuned for high-memory machines |
| `v0.5.3` | Public docs clarify the agent-operated WanGP workflow |
| `v11.61` | WanGP-matched release: consolidated `runtime/Wan2GP`, ACE-Step 1.5 music compose, RTX 4090 CUDA verification, clean Codex/Claude skill packaging |

## Release Rule

Every release should state what changed, what was verified, and whether actual
WanGP rendering was run or only operator command generation was verified.

Do not publish WanGP, model weights, generated outputs, or runtime environments
inside this repo. Releases may reference upstream WanGP and model provider URLs,
but third-party materials must remain governed by their own licenses and be
downloaded through the user's local WanGP workflow.
