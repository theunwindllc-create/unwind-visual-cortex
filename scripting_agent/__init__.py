"""Reusable Viral Video Scripting Agent (Unwind Visual Cortex compatible).

This module is intentionally lightweight: it runs with the Python standard library
out of the box, and provides a deterministic baseline pipeline.
"""

from .agents.orchestrator import run_scripting_pipeline, ScriptingPipelineConfig
