# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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

[Unreleased]: https://github.com/avalonreset/wan2gp-operator/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/avalonreset/wan2gp-operator/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/avalonreset/wan2gp-operator/releases/tag/v0.1.0
