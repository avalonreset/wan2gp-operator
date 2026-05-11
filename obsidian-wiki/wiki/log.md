---
type: meta
title: "Wiki Log"
created: 2026-05-10
updated: 2026-05-10
tags:
  - meta
  - log
status: active
---

# Wiki Log

## 2026-05-10 - Initial development vault scaffold

Created `obsidian-wiki/` inside `E:\wan2gp-operator` using the Codex Obsidian
wiki scaffold pattern.

Created:

- Root vault files: `CODEX.md`, `README.md`, `.obsidian/snippets/vault-colors.css`
- Core pages: [[overview|Wan2GP Operator Overview]], [[index|Wiki Index]], [[hot|Hot Cache]]
- Domains: [[Development Operations]], [[Model Research]], [[Release Track]], [[User Handoff]]
- Modules: [[Unified CLI Entrypoint]], [[Model Catalog]], [[Compose Settings]], [[Headless Runner]], [[Music Video Pipeline]], [[Skill Installer]], [[Update Checker]]
- Flows: [[Agent Operated WanGP Workflow]], [[GX10 High Memory Test Ladder]], [[Headless Render Flow]], [[Music Video Pipeline Flow]]
- Decisions: [[Agent Operated Control Layer]], [[High Memory Model Defaults]], [[Dual Runtime Skill Compatibility]], [[Report Handoff Format]]
- Source summaries and raw snapshots for the GX10 handoff session.

## 2026-05-10 - RTX 4090 development tier

Split RTX 4090/24GB behavior from 96GB+ high-memory proof behavior.

The live local assessment detected an NVIDIA GeForce RTX 4090 with 24.0GB VRAM,
driver 596.21, 127.8GB system RAM, and 138.4GB free disk. The operator now treats
that as a 24GB development tier:

- Use `ltx23-distilled-22b` for iteration.
- Allow explicit short `ltx23-dev-22b` quality tests.
- Recommend `sdpa`, `profile 3`, compile off, and TeaCache `2.0` for balanced
  iteration by default.
- Keep `sage2` and compile as the 96GB+ high-memory proof path unless local
  compatibility is proven.

## 2026-05-10 - ACE-Step and editing rubric strategy

Added a planning direction for the next music-video milestone:

- Use [[ACE-Step 1.5]] for local song generation.
- Treat ACE-Step XL Turbo as the RTX 4090 daily-driver music source.
- Treat ACE-Step XL SFT as the quality rerender path.
- Upgrade the current music-video pipeline from simple beat-aligned clips to the
  [[Automated Beat Editing Rubric]].
- First target is a five-shot proof: generated song excerpt, 720p LTX/WanGP
  shots, multiple takes for hero sections, preview artifacts, and final MP4.

## 2026-05-10 - ACE-Step 1.5 RTX 4090 quality path

Confirmed the local WanGP install is now available through `runtime/Wan2GP` and
updated it from v10.84 to v11.61. Requirements were refreshed in the local WanGP
venv, and the stack reports `mmgp 3.7.6`, `torch 2.10.0+cu130`, CUDA available,
and NVIDIA GeForce RTX 4090.

Added first-class operator settings composition for ACE-Step 1.5:

- `ace15-xl-lm-4b`: quality target for RTX 4090, using ACE-Step 1.5 XL Turbo
  4B DiT plus the 4B LM preprocessing path.
- `ace15-xl-lm-1-7b`: lower-overhead XL fallback while staying in the quality
  model family.
- `compose --task music` now accepts music captions, duration, BPM, key, time
  signature, language, and ACE LM preprocessing mode.

Best-practice default: start with `ace15-xl-lm-4b`, `--quality quality`, and 120
seconds. Treat 180 seconds as a stretch test after 120 seconds succeeds locally.

## 2026-05-10 - WanGP runtime consolidated under operator workspace

Replaced the `runtime/Wan2GP` junction with a real fresh clone of
`deepbeepmeep/Wan2GP` inside `E:\wan2gp-operator\runtime\Wan2GP`.

Verification:

- Upstream main commit: `8387f64fe829fb0accf9d13fac65d34a25f5fc1f`.
- Local WanGP commit: `8387f64fe829fb0accf9d13fac65d34a25f5fc1f`.
- WanGP version: `11.61`.
- Update checker: `update_available: false`.
- Local venv: `E:\wan2gp-operator\runtime\Wan2GP\wan2gp`.
- Python stack: `mmgp 3.7.6`, `torch 2.10.0+cu130`,
  `torchvision 0.25.0+cu130`, `torchaudio 2.10.0+cu130`.
- CUDA: available, GPU `NVIDIA GeForce RTX 4090`.
- ACE-Step 1.5 XL dry-run: passed from the in-folder WanGP root.

Going forward, use only `E:\wan2gp-operator\runtime\Wan2GP` as the active WanGP
root. The old `E:\skill-forge\Wan2GP` path is no longer the operator working
root.

## 2026-05-10 - WanGP-matched release scheme

The project release track now follows the verified upstream WanGP version.
The next public release target is `v11.61`, matching WanGP `11.61`.

Release-readiness fixes for this pass:

- Default setup/bootstrap path is `./runtime/Wan2GP`.
- `runtime/`, logs, outputs, and settings are excluded from Codex/Claude skill installs.
- Setup installs WanGP requirements first, then applies the CUDA Torch stack last.
- The update checker falls back to raw README plus `git ls-remote` when the GitHub REST API is rate-limited.
- Added a release compliance boundary: the repo ships the operator, not WanGP,
  model weights, generated outputs, or local runtime environments.
