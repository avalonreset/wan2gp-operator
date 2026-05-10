# Wan2GP Operator

Use this repository as a Claude-compatible skill suite for operating WanGP/Wan2GP from the terminal.

The intended workflow is agent-operated. The human supplies creative direction and hardware context. Claude uses this repo to install or update WanGP, choose the model target, compose settings, run `wgp.py --process` headlessly, read logs, diagnose failures, and retry with safer compatibility choices.

## Command Surface

Prefer the unified entrypoint:

```bash
python scripts/wan2gp_operator.py <command> [args]
```

Important commands:
- `models`: show current model guidance and the curated operator targets
- `updates`: check live WanGP upstream version and highlights
- `compose`: generate a WanGP settings JSON from a prompt
- `run`: execute or dry-run a headless `wgp.py --process` job
- `diagnose`: analyze logs after a failed run
- `evolve`: record learned compatibility issues for future retries

## Current Model Guidance

As of 2026-05-10, treat LTX-2.3 22B as the hot general open-source audio-video target and Wan 2.2 14B as the strongest Wan-family workhorse. For high-memory machines, do not default to tiny demo models unless debugging install health.

Use:

```bash
python scripts/wan2gp_operator.py compose --model ltx23-dev-22b --quality quality --prompt "<PROMPT>"
```

For fast iteration:

```bash
python scripts/wan2gp_operator.py compose --model ltx23-distilled-22b --quality balanced --prompt "<PROMPT>"
```

## Safety Rules

- Run `run --dry-run` before full rendering unless the user explicitly skips it.
- Check `updates` before claiming WanGP is current.
- Prefer `models` before making recommendations about the best current model.
- Keep generated settings outside WanGP `defaults/`.
