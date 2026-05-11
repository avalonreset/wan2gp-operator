# Wan2GP Performance Guide

Starter defaults by VRAM tier for stable first runs:

| VRAM | Model Target | Attention | Profile | TeaCache | Compile |
|------|---------------|-----------|---------|----------|---------|
| 6-8GB | `t2v-1-3B` or conservative Wan 14B | `sdpa` | `4` | `1.5` | Off |
| 10-12GB | Wan 2.2 14B conservative | `sdpa` | `4` | `1.5` | Off |
| 16-20GB | `ltx23-distilled-22b` or Wan 2.2 14B | `sage` | `3` | `2.0` | On |
| 24GB RTX 4090 class | `ltx23-distilled-22b` for iteration; explicit `ltx23-dev-22b` quality tests | `sdpa` | `3` | `2.0` for balanced iteration; optional for quality | Off |
| 96GB+ | `ltx23-dev-22b` quality, longer 720p tests, then Wan 2.2 A14B comparisons | `sage2` | `3` | optional | On |

## Known Tradeoffs

- `sdpa`: safest compatibility, slower than Sage/Sage2.
- `sage`/`sage2`: higher throughput, but requires dependency compatibility.
- `profile 4`: best fallback when facing OOM.
- `profile 3`: higher speed if VRAM headroom exists.
- `teacache`: speed boost with potential quality tradeoff at higher values.

## RTX 4090 Developer Path

Treat 24GB cards as a serious development tier, not the same class as a
96GB+ proof machine. Start with stable runtime flags and scale only after a
dry-run and one successful short render:

```bash
python scripts/wan2gp_operator.py compose --model ltx23-distilled-22b --quality balanced --duration-seconds 5 --prompt "<PROMPT>"
```

For quality checks, explicitly target the dev model but keep the runtime stable
until local Sage/Sage2 dependencies are proven. TeaCache can be omitted when
quality matters more than iteration speed:

```bash
python scripts/wan2gp_operator.py compose --model ltx23-dev-22b --quality quality --duration-seconds 4 --prompt "<PROMPT>"
```

## Common Fallback Path

If a run fails with OOM:
1. Switch to `--model-preset t2v-1-3B`.
2. Force `--attention sdpa --profile 4`.
3. Lower generation complexity (frames, steps, resolution) in queue/settings.

## Current High-End Path

For DGX Spark/GX10-class unified-memory machines, do not start with tiny models unless
you are only debugging installation. Start with:

```bash
python scripts/wan2gp_operator.py compose --model ltx23-dev-22b --quality quality --duration-seconds 10 --fps 24 --prompt "<PROMPT>"
```

Then compare against Wan 2.2 T2V or I2V A14B at the same prompt length and resolution:

```bash
python scripts/wan2gp_operator.py compose --model wan22-t2v-14b --quality quality --duration-seconds 10 --fps 24 --prompt "<PROMPT>"
```

If you want fast iteration while keeping the LTX-2.3 path:

```bash
python scripts/wan2gp_operator.py compose --model ltx23-distilled-22b --quality balanced --duration-seconds 10 --fps 24 --prompt "<PROMPT>"
```

## Terminal-First Tip

Use:
```bash
python scripts/wan2gp_operator.py compose --prompt "<PROMPT>" --quality draft
```
Then run dry-run before full generation.

