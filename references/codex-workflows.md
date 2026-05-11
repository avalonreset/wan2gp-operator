# Codex Workflows

Codex-first workflow recipes for `wan2gp-operator`.

## A. Readiness + Setup

```bash
python scripts/wan2gp_operator.py bootstrap
python scripts/wan2gp_operator.py bootstrap --execute --launch-ui
```

## B. Prompt to Render (No UI Sliders)

```bash
python scripts/wan2gp_operator.py compose --prompt "cinematic product reveal in rain" --duration-seconds 6 --quality balanced
python scripts/wan2gp_operator.py run --wan-root .\runtime\Wan2GP --process <generated-settings.json> --dry-run
python scripts/wan2gp_operator.py run --wan-root .\runtime\Wan2GP --process <generated-settings.json> --log-file runtime\logs\wan2gp.log
```

## C. Queue Processing

```bash
python scripts/wan2gp_operator.py run --wan-root .\runtime\Wan2GP --process overnight_queue.zip --output-dir .\runtime\renders --dry-run
python scripts/wan2gp_operator.py run --wan-root .\runtime\Wan2GP --process overnight_queue.zip --output-dir .\runtime\renders --log-file runtime\logs\overnight.log
```

## D. Failure Recovery

```bash
python scripts/wan2gp_operator.py diagnose --log-file logs\overnight.log
```

Then rerun with safer flags:
- `--attention sdpa`
- `--profile 4`
- `--model-preset t2v-1-3B`

## E. Update Intelligence

```bash
python scripts/wan2gp_operator.py updates --wan-root .\runtime\Wan2GP
```

## F. Recursive Improvement Loop

```bash
python scripts/wan2gp_operator.py run --wan-root .\runtime\Wan2GP --process <job.json> --log-file runtime\logs\run.log
python scripts/wan2gp_operator.py evolve --wan-root .\runtime\Wan2GP --log-file runtime\logs\run.log
```

Notes:
- `run` auto-retries once for known argument incompatibilities (for example `--teacache`).
- Learned state is persisted in `.\runtime\Wan2GP\.wan2gp_operator_state.json`.

