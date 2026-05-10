# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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

[Unreleased]: https://github.com/avalonreset/wan2gp-operator/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/avalonreset/wan2gp-operator/releases/tag/v0.1.0
