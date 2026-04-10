from __future__ import annotations

import json
import argparse
import dataclasses
from enum import Enum

from scripting_agent import run_scripting_pipeline, ScriptingPipelineConfig


def to_jsonable(obj):
    """Best-effort recursive serializer for dataclasses + Enums."""
    if obj is None:
        return None

    # Enum (NarrativeArc, etc.)
    if isinstance(obj, Enum):
        return obj.value

    # Dataclasses
    if dataclasses.is_dataclass(obj):
        return {k: to_jsonable(v) for k, v in dataclasses.asdict(obj).items()}

    # Dictionaries
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v) for k, v in obj.items()}

    # Lists/tuples
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(x) for x in obj]

    # Primitive
    try:
        json.dumps(obj)
        return obj
    except TypeError:
        return str(obj)


def main():
    p = argparse.ArgumentParser(
        description="Unwind Visual Cortex - Viral Video Scripting Agent (deterministic baseline)."
    )
    p.add_argument("prompt", type=str, help="Tema/prompt en español para el Reel.")
    p.add_argument("--duration", type=int, default=45, help="Duración objetivo (segundos).")
    p.add_argument("--platform", type=str, default="Instagram Reels", help="Plataforma objetivo.")
    p.add_argument("--threshold", type=float, default=75.0, help="Umbral de pase (0-100).")
    p.add_argument("--max-iters", type=int, default=3, help="Máximo refinamientos.")
    p.add_argument(
        "--memory",
        type=str,
        default=".unwind_scripting_agent_memory/store.json",
        help="Ruta del store de memoria (JSON).",
    )
    args = p.parse_args()

    config = ScriptingPipelineConfig(
        target_duration_seconds=args.duration,
        target_platform=args.platform,
        virality_pass_threshold=args.threshold,
        max_refinement_iterations=args.max_iters,
    )

    out = run_scripting_pipeline(args.prompt, config=config)

    out_json = to_jsonable(out)
    print(json.dumps(out_json, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
