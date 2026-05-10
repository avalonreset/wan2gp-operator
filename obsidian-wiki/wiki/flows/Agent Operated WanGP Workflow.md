---
type: flow
title: "Agent Operated WanGP Workflow"
created: 2026-05-10
updated: 2026-05-10
tags:
  - flow
  - agent
status: active
related:
  - "[[Agent Operated Control Layer]]"
  - "[[Headless Runner]]"
---

# Agent Operated WanGP Workflow

## Purpose

Let Codex or Claude operate WanGP through the operator so the user does not have
to hand-pick every setting or debug every failure manually.

## Flow

1. User gives creative intent and hardware context.
2. Agent runs `assess` and `updates`.
3. Agent picks a curated model target through `models`.
4. Agent runs `compose` to create process settings.
5. Agent runs `run --dry-run`.
6. Agent runs the headless job with log capture.
7. If the run fails, agent runs `diagnose` and `evolve`.
8. Agent retries with safer settings or reports the blocker.

## Output Contract

Return the command, settings path, output directory, log path, elapsed time, and
any auto-adjustments.
