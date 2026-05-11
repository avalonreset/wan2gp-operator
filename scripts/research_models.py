#!/usr/bin/env python3
"""
Report current operator guidance for open-source video model targets.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

from model_catalog import HOT_MODEL_KEY, PRACTICAL_MODEL_KEY, list_model_targets


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Show current open-source video model guidance")
    parser.add_argument("--wan-root", help="Optional WanGP root to inspect for installed version")
    return parser.parse_args()


def _read_wangp_version(wan_root: str | None) -> dict[str, Any] | None:
    if not wan_root:
        return None
    root = Path(wan_root).expanduser().resolve()
    wgp_file = root / "wgp.py"
    if not wgp_file.exists():
        return {"wan_root": str(root), "error": "missing wgp.py"}
    text = wgp_file.read_text(encoding="utf-8", errors="replace")
    version = None
    for line in text.splitlines():
        if line.strip().startswith("WanGP_version"):
            version = line.split("=", 1)[-1].strip().strip('"').strip("'")
            break
    commit = None
    if (root / ".git").exists():
        try:
            commit = subprocess.check_output(
                ["git", "-C", str(root), "rev-parse", "HEAD"],
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip()
        except Exception:
            commit = None
    return {"wan_root": str(root), "version": version, "commit": commit}


def main() -> int:
    args = _parse_args()
    report = {
        "status": "success",
        "as_of": "2026-05-10",
        "headline": "LTX-2.3 22B is the hottest general open-source audio-video target; ACE-Step 1.5 XL LM 4B is the high-quality local song target for RTX 4090-class music generation.",
        "hot_model_key": HOT_MODEL_KEY,
        "practical_default_key": PRACTICAL_MODEL_KEY,
        "music_quality_key": "ace15-xl-lm-4b",
        "rationale": [
            "LTX-2.3 adds native synchronized audio-video generation, stronger prompt handling, improved image-to-video, portrait support, and open weights.",
            "WanGP v11.61 includes LTX-2.3 defaults plus FlashVSR native upsampling and still keeps Wan 2.2, Hunyuan, Magi Human, and other families accessible through one browser UI.",
            "Current WanGP defaults include ACE-Step 1.5 XL Turbo LM variants; on a 24GB RTX 4090, use the XL 4B DiT plus 4B LM path when quality matters more than speed.",
            "For a 128GB unified-memory DGX/GX10-class box, skip tiny demos unless debugging installation; target LTX-2.3 22B dev or Wan 2.2 14B quality workflows.",
        ],
        "sources": [
            "https://docs.ltx.video/open-source-model/getting-started/overview",
            "https://ltx.io/model/model-blog/ltx-2-3-release",
            "https://github.com/deepbeepmeep/Wan2GP",
            "https://github.com/ace-step/ACE-Step-1.5/releases",
        ],
        "available_targets": list_model_targets(),
        "local_wangp": _read_wangp_version(args.wan_root),
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
