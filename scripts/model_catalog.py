#!/usr/bin/env python3
"""
Curated WanGP model targets for operator-generated settings.

The catalog is intentionally small: it covers the models an operator should
reach for without learning the WanGP UI defaults folder by hand.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


MODEL_TARGETS: dict[str, dict[str, Any]] = {
    "ace15-xl-lm-4b": {
        "label": "ACE-Step 1.5 XL Turbo LM 4B",
        "model_type": "ace_step_v1_5_xl",
        "family": "music",
        "why": "Highest-quality ACE-Step 1.5 path currently exposed by WanGP: XL 4B DiT plus strongest 4B LM preprocessing.",
        "min_vram_gb": 24,
        "default_duration_seconds": 120,
        "reasonable_duration_seconds": 180,
        "default_steps": {"draft": 8, "balanced": 12, "quality": 16},
        "settings": {
            "type": "WanGP settings",
            "model_type": "ace_step_v1_5_xl",
            "base_model_type": "ace_step_v1_5_xl",
            "model_mode": 3,
            "model": {
                "name": "TTS ACE-Step v1.5 XL Turbo LM_4B 4B",
                "architecture": "ace_step_v1_5_xl",
                "description": (
                    "ACE-Step 1.5 XL Turbo with the 4B XL DiT and 4B 5Hz LM path "
                    "for maximum quality and lyric matching in WanGP."
                ),
                "URLs": "ace_step_v1_5_xl",
                "text_encoder_URLs": [
                    "https://huggingface.co/DeepBeepMeep/TTS/resolve/main/acestep-5Hz-lm-4B/acestep-5Hz-lm-4B_bf16.safetensors",
                    "https://huggingface.co/DeepBeepMeep/TTS/resolve/main/acestep-5Hz-lm-4B/acestep-5Hz-lm-4B_quanto_bf16_int8.safetensors",
                ],
                "ace_step15_transformer_variant": "xl_turbo",
                "text_encoder_folder": "acestep-5Hz-lm-4B",
            },
            "alt_prompt": "high-fidelity modern song production, expressive vocals, polished mix",
            "audio_prompt_type": "",
            "audio_scale": 0.5,
            "shift": 1.0,
            "guidance_scale": 1.0,
            "scheduler_type": "euler",
        },
    },
    "ace15-xl-lm-1-7b": {
        "label": "ACE-Step 1.5 XL Turbo LM 1.7B",
        "model_type": "ace_step_v1_5_xl",
        "family": "music",
        "why": "Quality ACE-Step 1.5 XL target with strong lyric control and lower LM overhead than the 4B LM path.",
        "min_vram_gb": 16,
        "default_duration_seconds": 120,
        "reasonable_duration_seconds": 180,
        "default_steps": {"draft": 8, "balanced": 8, "quality": 12},
        "settings": {
            "type": "WanGP settings",
            "model_type": "ace_step_v1_5_xl",
            "base_model_type": "ace_step_v1_5_xl",
            "model_mode": 2,
            "model": {
                "name": "TTS ACE-Step v1.5 XL Turbo LM_1.7B 4B",
                "architecture": "ace_step_v1_5_xl",
                "description": (
                    "ACE-Step 1.5 XL Turbo with the 4B XL DiT and 1.7B 5Hz LM "
                    "for high-quality local song generation in WanGP."
                ),
                "URLs": "ace_step_v1_5_xl",
                "text_encoder_URLs": [
                    "https://huggingface.co/DeepBeepMeep/TTS/resolve/main/acestep-5Hz-lm-1.7B/acestep-5Hz-lm-1.7B_bf16.safetensors",
                    "https://huggingface.co/DeepBeepMeep/TTS/resolve/main/acestep-5Hz-lm-1.7B/acestep-5Hz-lm-1.7B_quanto_bf16_int8.safetensors",
                ],
                "ace_step15_transformer_variant": "xl_turbo",
                "text_encoder_folder": "acestep-5Hz-lm-1.7B",
            },
            "alt_prompt": "high-fidelity modern song production, expressive vocals, polished mix",
            "audio_prompt_type": "",
            "audio_scale": 0.5,
            "shift": 1.0,
            "guidance_scale": 1.0,
            "scheduler_type": "euler",
        },
    },
    "wan22-t2v-14b": {
        "label": "Wan 2.2 Text-to-Video 14B",
        "model_type": "t2v_2_2",
        "family": "wan",
        "why": "Strong general-purpose open video generation; best Wan-family t2v target in WanGP.",
        "min_vram_gb": 16,
        "default_resolution": "1280x720",
        "default_steps": {"draft": 8, "balanced": 16, "quality": 30},
        "settings": {
            "model_type": "t2v_2_2",
            "base_model_type": "t2v_2_2",
            "guidance_phases": 2,
            "switch_threshold": 875,
            "guidance_scale": 4,
            "guidance2_scale": 3,
            "flow_shift": 5,
        },
    },
    "wan22-i2v-14b": {
        "label": "Wan 2.2 Image-to-Video 14B",
        "model_type": "i2v_2_2",
        "family": "wan",
        "why": "Best Wan-family target when the user has a source frame or wants first-frame control.",
        "min_vram_gb": 16,
        "default_resolution": "1280x720",
        "default_steps": {"draft": 8, "balanced": 16, "quality": 30},
        "settings": {
            "model_type": "i2v_2_2",
            "base_model_type": "i2v_2_2",
            "image_prompt_type": "S",
            "guidance_phases": 2,
            "switch_threshold": 875,
            "guidance_scale": 4,
            "guidance2_scale": 3,
            "flow_shift": 5,
        },
    },
    "ltx23-distilled-22b": {
        "label": "LTX-2.3 Distilled 1.1 22B",
        "model_type": "ltx2_22B",
        "family": "ltx",
        "why": "Hot open-source audio-video target for fast iteration with synchronized audio support.",
        "min_vram_gb": 16,
        "default_resolution": "1280x720",
        "default_steps": {"draft": 6, "balanced": 8, "quality": 12},
        "settings": {
            "type": "WanGP settings",
            "model_type": "ltx2_22B",
            "base_model_type": "ltx2_22B",
            "model": {
                "name": "LTX-2 2.3 Distilled 1.1 22B",
                "architecture": "ltx2_22B",
                "description": (
                    "LTX-2.3 distilled 1.1 checkpoint (22B) with faster generation. "
                    "Supports native audio-video generation in WanGP."
                ),
                "URLs": [
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-distilled-1.1_diffusion_model_bf16.safetensors",
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-distilled-1.1_diffusion_model_quanto_bf16_int8.safetensors",
                ],
                "preload_URLs": [
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors|%lora_dir",
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-ic-lora-outpaint.safetensors|%lora_dir",
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-ic-lora-hdr-0.9.safetensors|%lora_dir",
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-ic-lora-hdr-scene-emb.safetensors",
                ],
                "ltx2_hdr_lora_file": "ltx-2.3-22b-ic-lora-hdr-0.9.safetensors",
                "ltx2_hdr_scene_embeddings_file": "ltx-2.3-22b-ic-lora-hdr-scene-emb.safetensors",
                "ltx2_pipeline": "distilled",
            },
        },
    },
    "ltx23-dev-22b": {
        "label": "LTX-2.3 Dev 22B",
        "model_type": "ltx2_22B",
        "family": "ltx",
        "why": "Highest-quality LTX-2.3 target when hardware/time budget matters less than quality.",
        "min_vram_gb": 24,
        "default_resolution": "1280x720",
        "default_steps": {"draft": 12, "balanced": 20, "quality": 30},
        "settings": {
            "type": "WanGP settings",
            "model_type": "ltx2_22B",
            "base_model_type": "ltx2_22B",
            "model": {
                "name": "LTX-2 2.3 Dev 1.0 22B",
                "architecture": "ltx2_22B",
                "description": (
                    "LTX-2.3 dev checkpoint (22B) for higher-quality video and audio generation."
                ),
                "URLs": [
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-dev_diffusion_model.safetensors",
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-dev_diffusion_model_quanto_int8.safetensors",
                ],
                "preload_URLs": [
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/id-lora-celebvhq-ltx2.3.safetensors|%lora_dir",
                    "https://huggingface.co/DeepBeepMeep/LTX-2/resolve/main/ltx-2.3-22b-distilled-lora-384.safetensors|%lora_dir",
                ],
            },
            "sample_solver": "euler",
            "guidance_scale": 3.0,
            "audio_guidance_scale": 7.0,
            "alt_guidance_scale": 3.0,
            "alt_scale": 0.7,
            "perturbation_switch": 2,
            "perturbation_layers": [28],
            "perturbation_start_perc": 0,
            "perturbation_end_perc": 100,
            "apg_switch": 0,
            "cfg_star_switch": 0,
        },
    },
    "magi-human-15b": {
        "label": "Magi Human 15B",
        "model_type": "magi_human",
        "family": "talking-head",
        "why": "Hot specialized open model for audio-driven or generated talking-head video.",
        "min_vram_gb": 16,
        "default_resolution": "448x256",
        "default_steps": {"draft": 16, "balanced": 24, "quality": 32},
        "settings": {
            "type": "WanGP settings",
            "model_type": "magi_human",
            "base_model_type": "magi_human",
            "guidance_scale": 5.0,
            "audio_guidance_scale": 5.0,
            "image_prompt_type": "S",
        },
    },
}


HOT_MODEL_KEY = "ltx23-dev-22b"
PRACTICAL_MODEL_KEY = "ltx23-distilled-22b"


def list_model_targets() -> list[dict[str, Any]]:
    """Return model catalog entries in a stable, displayable shape."""
    rows: list[dict[str, Any]] = []
    for key, target in MODEL_TARGETS.items():
        rows.append(
            {
                "key": key,
                "label": target["label"],
                "family": target["family"],
                "min_vram_gb": target["min_vram_gb"],
                "why": target["why"],
            }
        )
    return rows


def get_model_target(key: str) -> dict[str, Any]:
    """Return a deep copy of a catalog target."""
    if key not in MODEL_TARGETS:
        raise KeyError(f"Unknown model target: {key}")
    return deepcopy(MODEL_TARGETS[key])


def auto_model_key(task: str, has_image: bool, vram_gb: float, quality: str) -> str:
    """Pick a model key from intent, hardware, and quality."""
    if task == "music":
        if vram_gb >= 24 and quality == "quality":
            return "ace15-xl-lm-4b"
        return "ace15-xl-lm-1-7b"
    if task == "vace":
        return "wan22-i2v-14b" if has_image else "wan22-t2v-14b"
    if task == "i2v" or has_image:
        return "wan22-i2v-14b"
    if vram_gb >= 24 and quality == "quality":
        return HOT_MODEL_KEY
    if vram_gb >= 16:
        return PRACTICAL_MODEL_KEY
    return "wan22-t2v-14b"
