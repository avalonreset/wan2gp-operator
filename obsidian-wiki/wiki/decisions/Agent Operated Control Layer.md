---
type: decision
title: "Agent Operated Control Layer"
created: 2026-05-10
updated: 2026-05-10
tags:
  - decision
  - architecture
status: active
related:
  - "[[Agent Operated WanGP Workflow]]"
---

# Agent Operated Control Layer

## Decision

Wan2GP Operator is positioned as an agent-operated control layer over WanGP, not
as a standalone model or a simple settings generator.

## Rationale

The user should provide intent. Codex or Claude should handle setup, model
choice, settings generation, dry-runs, headless execution, logs, diagnosis, and
retry behavior.

## Consequences

- Documentation must describe the human-to-agent-to-WanGP loop.
- Commands must remain deterministic and log-friendly.
- Failure diagnosis and learned compatibility state are core product features.
