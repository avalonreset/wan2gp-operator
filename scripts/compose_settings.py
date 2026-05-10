#!/usr/bin/env python3
"""
Compose a Wan2GP settings JSON from plain-language intent.

Usage:
  python scripts/compose_settings.py --prompt "cinematic drone shot at sunset"
  python scripts/compose_settings.py --prompt "animate this character" --task i2v --image-start ./hero.png
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Any

from detect_gpu import build_report
from model_catalog import MODEL_TARGETS, auto_model_key, get_model_target


def _parse_args() -> argparse.Namespace:
    """Parse CLI args."""
    parser = argparse.ArgumentParser(description="Compose Wan2GP settings JSON")
    parser.add_argument("--prompt", required=True, help="Primary generation prompt")
    parser.add_argument("--negative-prompt", default="", help="Optional negative prompt")
    parser.add_argument("--task", choices=["auto", "t2v", "i2v", "vace"], default="auto")
    parser.add_argument(
        "--model",
        choices=["auto", *sorted(MODEL_TARGETS.keys())],
        default="auto",
        help="Curated model target. Use ltx23-dev-22b for the hottest quality target.",
    )
    parser.add_argument("--quality", choices=["draft", "balanced", "quality"], default="balanced")
    parser.add_argument("--duration-seconds", type=float, default=5.0, help="Target clip duration")
    parser.add_argument("--fps", type=int, default=16, help="FPS estimate for frame planning")
    parser.add_argument(
        "--resolution",
        default="832x480",
        help="Output resolution as WIDTHxHEIGHT (default: 832x480)",
    )
    parser.add_argument("--seed", type=int, default=-1, help="Seed value (-1 random)")
    parser.add_argument("--image-start", help="Start image path (for i2v/vace)")
    parser.add_argument("--audio-source", help="Optional audio path for audio-conditioned models")
    parser.add_argument("--vram-gb", type=float, help="Override detected VRAM")
    parser.add_argument("--output", help="Output JSON file path")
    return parser.parse_args()


def _max_frames_for_vram(vram_gb: float) -> int:
    """Frame budget by VRAM tier."""
    if vram_gb <= 8:
        return 81
    if vram_gb <= 12:
        return 121
    if vram_gb <= 20:
        return 161
    if vram_gb >= 96:
        return 481
    return 241


def _steps_for_quality(quality: str, vram_gb: float) -> int:
    """Infer denoise steps from quality target and hardware tier."""
    base = {"draft": 12, "balanced": 20, "quality": 30}[quality]
    if vram_gb <= 8:
        return min(base, 20)
    return base


def _detect_vram(override_vram: float | None) -> float:
    """Resolve VRAM from override or GPU report."""
    if override_vram is not None:
        return override_vram
    report = build_report()
    gpus = report.get("gpus", [])
    return max((float(g.get("vram_gb", 0)) for g in gpus), default=8.0)


def _select_model(task: str, has_image: bool, vram_gb: float, quality: str) -> str:
    """Choose Wan2GP model_type for the requested task."""
    normalized = task
    if normalized == "auto":
        normalized = "i2v" if has_image else "t2v"

    if normalized == "i2v":
        return "i2v"
    if normalized == "vace":
        return "vace_14B" if vram_gb >= 12 and quality != "draft" else "vace_1.3B"
    if vram_gb >= 20 and quality == "quality":
        return "t2v_2_2"
    return "t2v" if vram_gb >= 12 and quality != "draft" else "t2v_1.3B"


def _select_model_key(args: argparse.Namespace, vram_gb: float) -> str:
    """Choose a curated model key, preserving legacy auto behavior where needed."""
    if args.model != "auto":
        return args.model
    return auto_model_key(args.task, bool(args.image_start), vram_gb, args.quality)


def _recommended_runtime_flags(vram_gb: float, quality: str) -> dict[str, Any]:
    """Recommend headless runtime flags matching hardware tier."""
    if quality == "quality":
        if vram_gb <= 12:
            return {"attention": "sdpa", "profile": "4", "teacache": 1.5, "compile": False}
        if vram_gb >= 96:
            return {"attention": "sage2", "profile": "3", "teacache": None, "compile": True}
        # Mid-tier quality runs bias toward the safest backend to avoid wasting long jobs.
        return {"attention": "sdpa", "profile": "3", "teacache": None, "compile": False}
    if vram_gb <= 8:
        return {"attention": "sdpa", "profile": "4", "teacache": 1.5, "compile": False}
    if vram_gb <= 12:
        return {"attention": "sdpa", "profile": "4", "teacache": 1.5, "compile": False}
    if vram_gb <= 20:
        return {"attention": "sage", "profile": "3", "teacache": 2.0, "compile": True}
    return {"attention": "sage2", "profile": "3", "teacache": 2.0, "compile": True}


def _parse_resolution(resolution: str) -> tuple[int, int]:
    """Parse WIDTHxHEIGHT and validate positive dimensions."""
    match = re.fullmatch(r"\s*(\d+)\s*x\s*(\d+)\s*", resolution)
    if not match:
        raise ValueError("Resolution must be in WIDTHxHEIGHT format (example: 832x480).")
    width = int(match.group(1))
    height = int(match.group(2))
    if width <= 0 or height <= 0:
        raise ValueError("Resolution width and height must be positive.")
    return width, height


def _prompt_quality_warnings(prompt: str) -> list[str]:
    """Return quality warnings for prompt patterns that often fail in base t2v."""
    lowered = prompt.lower()
    warnings: list[str] = []
    risky_terms = ("logo", "text", "typography", "website", "url", ".com", ".pro", "domain")
    if any(term in lowered for term in risky_terms):
        warnings.append(
            "Prompt asks for readable text/logo/website content; base t2v often degrades. "
            "Prefer clean visual prompts or use i2v + external text overlay."
        )
    return warnings


def _build_legacy_wan_settings(args: argparse.Namespace, vram_gb: float) -> dict[str, Any]:
    """Build the pre-catalog Wan settings payload for backwards compatibility."""
    width, height = _parse_resolution(args.resolution)
    frames_raw = max(16, int(round(args.duration_seconds * args.fps)))
    frame_cap = _max_frames_for_vram(vram_gb)
    frames = min(frames_raw, frame_cap)
    steps = _steps_for_quality(args.quality, vram_gb)
    model_type = _select_model(args.task, bool(args.image_start), vram_gb, args.quality)

    settings: dict[str, Any] = {
        "type": "WanGP settings",
        "model_type": model_type,
        "base_model_type": model_type,
        "prompt": args.prompt.strip(),
        "resolution": f"{width}x{height}",
        "num_inference_steps": steps,
        "video_length": frames,
        "seed": args.seed,
        "repeat_generation": 1,
    }
    if args.image_start:
        settings["image_start"] = str(Path(args.image_start).expanduser().resolve())
    if model_type == "t2v_2_2":
        settings["guidance_phases"] = 2
        settings["guidance_scale"] = 4.5
        settings["guidance2_scale"] = 3.0
        settings["switch_threshold"] = 875
        settings["flow_shift"] = 5
        if steps < 24:
            settings["num_inference_steps"] = 24
    return settings


def _build_catalog_settings(args: argparse.Namespace, vram_gb: float) -> tuple[dict[str, Any], str]:
    """Build settings from the curated current-model catalog."""
    model_key = _select_model_key(args, vram_gb)
    target = get_model_target(model_key)
    resolution = args.resolution
    if resolution == "832x480":
        resolution = str(target["default_resolution"])
    width, height = _parse_resolution(resolution)
    frames_raw = max(16, int(round(args.duration_seconds * args.fps)))
    frames = min(frames_raw, _max_frames_for_vram(vram_gb))

    settings = target["settings"]
    settings.update(
        {
            "type": "WanGP settings",
            "prompt": args.prompt.strip(),
            "resolution": f"{width}x{height}",
            "num_inference_steps": int(target["default_steps"][args.quality]),
            "video_length": frames,
            "seed": args.seed,
            "repeat_generation": 1,
        }
    )
    if args.image_start:
        settings["image_start"] = str(Path(args.image_start).expanduser().resolve())
        settings.setdefault("image_prompt_type", "S")
    if args.audio_source:
        settings["audio_source"] = str(Path(args.audio_source).expanduser().resolve())
        settings.setdefault("audio_prompt_type", "A")
    return settings, model_key


def _build_settings(args: argparse.Namespace, vram_gb: float) -> tuple[dict[str, Any], list[str], str]:
    """Build minimal settings payload accepted by Wan2GP parser."""
    warnings = _prompt_quality_warnings(args.prompt)
    if args.model == "auto" and args.task == "auto" and not args.image_start and vram_gb < 16:
        settings = _build_legacy_wan_settings(args, vram_gb)
        model_key = str(settings["model_type"])
    else:
        settings, model_key = _build_catalog_settings(args, vram_gb)

    negative_prompt = args.negative_prompt.strip()
    if not negative_prompt:
        negative_prompt = (
            "text, logo, watermark, blurry, low quality, deformed anatomy, jitter, flicker"
        )
    settings["negative_prompt"] = negative_prompt
    return settings, warnings, model_key


def _resolve_output_path(path_arg: str | None) -> Path:
    """Resolve output path, generating one if absent."""
    if path_arg:
        return Path(path_arg).expanduser().resolve()
    folder = Path.cwd() / "wan2gp_jobs"
    folder.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return (folder / f"wan2gp-settings-{ts}.json").resolve()


def _validate_output_path(output_path: Path) -> None:
    """Prevent writing process files into Wan2GP defaults model folder."""
    if output_path.parent.name.lower() == "defaults":
        raise ValueError(
            "Refusing to write into a 'defaults' folder. "
            "Wan2GP loads defaults as model definitions at startup; this can break boot. "
            "Use another path (for example: ./wan2gp_jobs)."
        )


def main() -> int:
    """CLI entrypoint."""
    try:
        args = _parse_args()
        vram_gb = _detect_vram(args.vram_gb)
        settings, warnings, selected_model = _build_settings(args, vram_gb)
        runtime_flags = _recommended_runtime_flags(vram_gb, args.quality)

        output_path = _resolve_output_path(args.output)
        _validate_output_path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")

        report = {
            "status": "success",
            "settings_file": str(output_path),
            "detected_vram_gb": vram_gb,
            "selected_model": selected_model,
            "settings": settings,
            "quality_warnings": warnings,
            "recommended_runtime_flags": runtime_flags,
            "run_example": (
                "python scripts/wan2gp_operator.py run "
                f"--wan-root <WAN2GP_ROOT> --process \"{output_path}\" "
                f"--attention {runtime_flags['attention']} --profile {runtime_flags['profile']} "
                + (
                    f"--teacache {runtime_flags['teacache']} "
                    if runtime_flags["teacache"] is not None
                    else ""
                )
                + (" --compile" if runtime_flags["compile"] else "")
                + " --dry-run"
            ),
        }
        print(json.dumps(report, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
