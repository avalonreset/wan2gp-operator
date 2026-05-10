---
type: domain
title: "User Handoff"
created: 2026-05-10
updated: 2026-05-10
tags:
  - domain
  - handoff
status: active
related:
  - "[[GX10 High Memory Test Ladder]]"
  - "[[Report Handoff Format]]"
---

# User Handoff

This domain tracks how the project is explained to outside users.

## Current Positioning

Install Wan2GP Operator into Codex or Claude, then let the agent operate WanGP.
The user provides creative direction. The agent handles setup, model downloads,
settings, dry-runs, headless renders, logs, diagnosis, and retries.

## Handoff Artifact

The GX10 handoff report was generated outside this repo during the project setup
session and copied to Downloads. Its core recommendation belongs here:

- Start with [[Wan 2.2 A14B]] at 720p to prove the 128GB machine matters.
- Then run [[LTX-2.3 Dev 22B]] for longer creative quality experiments.
- Use logs and diagnosis instead of guessing in the UI when something fails.
