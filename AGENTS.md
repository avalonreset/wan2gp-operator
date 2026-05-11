# Wan2GP Operator

Codex-first terminal operations layer for Wan2GP.

This repo is meant to let Codex operate WanGP for the user. The user provides
intent; Codex handles install/update checks, model selection, settings
composition, dry-runs, headless execution, log diagnosis, and corrective retries.

## Unified Interface

Use one command surface:
```bash
python scripts/wan2gp_operator.py <command> [args]
```

Commands:
- `bootstrap`: assess + setup plan (or execute) + optional UI launch
- `assess`: machine readiness and install-worth-it verdict
- `setup`: plan or execute installation/update workflow
- `launch-ui`: open Wan2GP web UI from terminal
- `compose`: create Wan2GP settings JSON from natural-language prompt
- `models`: show current open-source video model guidance and curated targets
- `plan`: build validated `wgp.py --process` command
- `run`: execute headless job with optional dry-run and log capture
- `diagnose`: analyze failures from logs/text
- `updates`: check latest Wan2GP release and summarize highlights

## Typical Flow

1. `python scripts/wan2gp_operator.py assess`
2. `python scripts/wan2gp_operator.py bootstrap --execute --launch-ui`
3. `python scripts/wan2gp_operator.py compose --prompt "<PROMPT>"`
4. `python scripts/wan2gp_operator.py run --wan-root <WAN2GP_ROOT> --process <SETTINGS_JSON> --dry-run`
5. `python scripts/wan2gp_operator.py run --wan-root <WAN2GP_ROOT> --process <SETTINGS_JSON> --log-file logs/wan2gp.log`
6. If failed: `python scripts/wan2gp_operator.py diagnose --log-file logs/wan2gp.log`

## Operating Rules

- Run dry-run before full render unless user explicitly opts out.
- Prefer conservative profile on unknown hardware (`sdpa`, profile `4`).
- Do not claim update status without running `wan2gp_operator.py updates`.
- Do not recommend tiny demo models on high-memory machines unless debugging install health.
- Use `wan2gp_operator.py models` before making "best current model" recommendations.
- Keep local WanGP installs under `runtime/Wan2GP` by default; do not scatter
  clones, venvs, logs, or model state into unrelated folders.

## Development Wiki

Path: `obsidian-wiki/`

When work depends on prior project decisions, release history, model guidance,
or agent workflow design:
1. Read `obsidian-wiki/wiki/hot.md` first.
2. If more context is needed, read `obsidian-wiki/wiki/index.md`.
3. Then drill into domain, decision, flow, or module pages.

Keep the wiki current after significant project changes by updating
`wiki/log.md`, `wiki/hot.md`, and any affected index pages.

