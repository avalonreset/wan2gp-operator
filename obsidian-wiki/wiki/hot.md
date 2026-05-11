---
type: meta
title: "Hot Cache"
created: 2026-05-10
updated: 2026-05-10
tags:
  - meta
  - hot-cache
status: active
---

# Recent Context

## Last Updated

2026-05-10. Wan2GP Operator moved to `E:\wan2gp-operator` as the working project home, and this Obsidian vault was scaffolded to preserve project memory.

## Key Recent Facts

- The project direction is [[Agent Operated WanGP Workflow]]: Codex or Claude operates WanGP through the operator instead of asking the human to hand-tune settings.
- The latest shipped release target is `v11.61`, documented in [[Release Track]].
  Public release numbers now match the verified upstream WanGP version.
- High-memory guidance centers on [[Wan 2.2 A14B]] as the clean 128GB proof target and [[LTX-2.3 Dev 22B]] as the creative quality target.
- [[RTX 4090]] is now treated as a 24GB development tier: serious LTX/Wan targets are allowed, but default runtime flags stay on `sdpa`, `profile 3`, TeaCache `2.0`, and compile off until Sage/Sage2 is proven locally.
- [[ACE-Step 1.5]] is built into current WanGP. For RTX 4090 quality music generation, use `ace15-xl-lm-4b` first: ACE-Step 1.5 XL Turbo 4B DiT plus 4B LM, 120 seconds for the first full-quality target, 180 seconds only after the 120-second path is proven locally.
- [[Automated Beat Editing Rubric]] is the next creative strategy layer: edit by section, phrase, downbeat, and energy rather than cutting mechanically on every beat.
- The operator supports Codex and Claude skill installation through [[Skill Installer]].
- Future work should keep [[Model Catalog]], [[Headless Runner]], and [[Learned Compatibility State]] aligned.

## Recent Changes

- Created the development vault structure under `obsidian-wiki/`.
- Added seed pages for modules, flows, decisions, entities, concepts, domains, and source links.
- Added `AGENTS.md` guidance so future sessions read this hot cache first.
- Split RTX 4090/24GB development defaults from 96GB+ high-memory proof defaults.
- Added ACE-Step and automated beat-editing strategy pages for the next music-video milestone.
- Replaced the `runtime/Wan2GP` junction with a real in-folder WanGP clone at v11.61 and refreshed its local Python 3.11 venv.
- The active WanGP root is `E:\wan2gp-operator\runtime\Wan2GP`; do not use the old `E:\skill-forge\Wan2GP` path for new work. The old copy was archived under `E:\wan2gp-operator\runtime\archive\Wan2GP-skill-forge-previous`.
- Added ACE-Step 1.5 XL music targets and `compose --task music` controls.
- Skill installs must exclude `runtime/` so Codex and Claude receive the operator skill, not a copied WanGP runtime.

## Active Threads

- Keep the E-drive working copy current.
- Expand real render validation against a local WanGP install.
- Validate `compose --task music --model ace15-xl-lm-4b` against a real 120-second ACE-Step render.
- Upgrade `music-plan` and `music-assemble` from simple beat cuts to rubric-driven edit decisions.
- Continue refining RTX 4090 developer presets and 96GB+ high-memory presets as WanGP evolves.
