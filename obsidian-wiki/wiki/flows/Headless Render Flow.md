---
type: flow
title: "Headless Render Flow"
created: 2026-05-10
updated: 2026-05-10
tags:
  - flow
  - render
status: active
related:
  - "[[Headless Runner]]"
  - "[[Dry Run First]]"
---

# Headless Render Flow

## Steps

1. Confirm WanGP root contains `wgp.py`.
2. Confirm process input exists and is JSON or queue ZIP.
3. Plan the command.
4. Run dry-run.
5. Run full render with log capture.
6. Diagnose non-zero exit status.
7. Evolve compatibility state when repeat failures occur.

## Notes

The headless path is the foundation for agent-operated workflows because it
gives the agent real commands, logs, and outputs to reason about.
