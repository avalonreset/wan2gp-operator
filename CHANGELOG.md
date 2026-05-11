# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).
Public release numbers follow the verified upstream WanGP version.

## [Unreleased]

## [11.61] - 2026-05-10

### Added
- Added ACE-Step 1.5 XL music targets to the curated model catalog, including `ace15-xl-lm-4b` for RTX 4090-class quality song generation.
- `compose --task music` can now generate ACE-Step settings with music captions, duration, BPM, key, time signature, language, and LM preprocessing mode controls.

### Changed
- Release versioning now matches the verified upstream WanGP version; this release is aligned to WanGP `11.61`.
- Default WanGP setup path is now `./runtime/Wan2GP` so clones, venvs, logs, and generated state stay under one project runtime folder.
- Setup now installs WanGP requirements first, then applies the selected CUDA Torch stack last so requirements cannot silently replace CUDA Torch with CPU Torch.
- Added an RTX 4090/24GB developer tier so the operator uses serious LTX/Wan targets without inheriting the 96GB+ `sage2`/compile high-memory defaults.
- Skill installs now exclude `runtime/`, `logs/`, `outputs/`, and `settings/` to keep Codex and Claude skill directories clean.
- Update checks now fall back to raw README plus `git ls-remote` when the GitHub REST API is rate-limited.

### Verified
- Local WanGP root `E:\wan2gp-operator\runtime\Wan2GP` reports WanGP `11.61` at upstream commit `8387f64fe829fb0accf9d13fac65d34a25f5fc1f`.
- RTX 4090 runtime venv reports CUDA Torch: `torch 2.10.0+cu130`, `torchvision 0.25.0+cu130`, `torchaudio 2.10.0+cu130`.
- ACE-Step 1.5 XL 4B music settings dry-run passed against the active local WanGP runtime.

## [0.5.3] - 2026-05-10

### Changed
- Public docs now make the agent-operated workflow explicit: Codex or Claude installs/updates WanGP, composes settings, runs headless jobs, inspects logs, diagnoses failures, and retries with safer compatibility choices.

## [0.5.2] - 2026-05-10

### Changed
- 96GB+ quality-mode composition now recommends the high-end `sage2` / `profile 3` / compile runtime path instead of the conservative SDPA path.
- High-end performance guidance now centers GX10/DGX Spark-class tests on LTX-2.3 Dev 22B and Wan 2.2 A14B comparisons.

## [0.5.1] - 2026-05-10

### Changed
- Music-video generation now passes curated model targets into shot composition, so the sequential FFmpeg pipeline can use LTX-2.3 instead of being forced back to Wan 2.2 on high-VRAM GPUs.
- Legacy `t2v_2_2` enforcement is now opt-in through `--model-policy`, and explicit `--model` choices take precedence.

## [0.5.0] - 2026-05-10

### Added
- Current open-source model guidance command: `wan2gp_operator.py models`
- Curated model catalog for WanGP v11.61-era targets:
  - `ltx23-dev-22b`
  - `ltx23-distilled-22b`
  - `wan22-t2v-14b`
  - `wan22-i2v-14b`
  - `magi-human-15b`
- `compose --model ...` for direct LTX-2.3, Wan 2.2, and Magi Human settings generation
- `CLAUDE.md` for Claude Code/project compatibility

### Changed
- README and skill docs now position LTX-2.3 22B as the hot general open-source audio-video target and Wan 2.2 14B as the Wan-family workhorse
- High-memory guidance no longer defaults to tiny demo models except for install debugging
- Update checks now include the latest upstream main-branch commit when WanGP publishes version data through README rather than GitHub releases
- Codex skill installer now targets `.codex/skills`

## [0.4.0] - 2026-03-16

### Added
- SECURITY.md with vulnerability reporting policy and response timeline
- CITATION.cff for machine-readable citation
- CODE_OF_CONDUCT.md (Contributor Covenant v2.1)
- SUPPORT.md with help channels and diagnostic guidance
- CODEOWNERS for PR review assignment
- Issue templates (bug report and feature request YAML forms)
- Pull request template with testing checklist
- CI workflow with compile and help checks
- Devcontainer configuration (Python 3.12 with Ruff)
- Dependabot for pip and github-actions ecosystems
- Auto-generated release notes via .github/release.yml
- FUNDING.yml template
- .gitattributes for line ending normalization

### Changed
- LICENSE copyright corrected to Benjamin (avalonreset)
- CONTRIBUTING.md expanded with dev setup, code style, and PR process

## [0.3.0] - 2026-02-15

### Added
- Phase 1 music-video pipeline:
  - `music-analyze` (audio BPM/beat/section analysis)
  - `music-plan` (beat-aligned shot planning and prompts)
  - `music-generate` (multi-take Wan2GP generation with optional evolve-on-failure)
  - `music-assemble` (ffmpeg-based clip normalization, concat, and audio mux)
  - `music-video` (one-command orchestrator)
- Unified operator command map for all music-video commands
- Documentation for one-command and stage-by-stage music-video workflows

## [0.2.0] - 2026-02-15

### Added
- Quality-feedback evolution flow (`evolve --quality-feedback ...`)
- Quality recommendations output in headless runs

### Changed
- Improved compose defaults for Wan2.2 quality runs
- Safer runtime recommendations for quality-focused generation

## [0.1.0] - 2026-02-14

### Added
- Initial public release
- Bootstrap, compose, run, diagnose, updates, evolve workflows
- Codex-first skill contract and references

[Unreleased]: https://github.com/avalonreset/wan2gp-operator/compare/v11.61...HEAD
[11.61]: https://github.com/avalonreset/wan2gp-operator/compare/v0.5.3...v11.61
[0.5.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/avalonreset/wan2gp-operator/releases/tag/v0.1.0
