from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional

from ..models.schema import ScriptDocument, ScriptSegment, VADScore, ViralityScore


class RetentionCurveModel:
    """Exponential retention curve baseline.

    R(t) = exp(-lambda * t) + floor

    This is a structural heuristic to support deterministic gating.
    """

    def __init__(self, decay_rate: float = 0.008, retention_floor: float = 0.20):
        self.decay_rate = decay_rate
        self.retention_floor = retention_floor

    def predict_retention(self, time_seconds: float) -> float:
        retention = math.exp(-self.decay_rate * time_seconds) + self.retention_floor
        return max(0.0, min(1.0, retention))

    def predict_apv(self, duration_seconds: int, resolution: int = 100) -> float:
        total = 0.0
        for i in range(resolution):
            t = (i / resolution) * duration_seconds
            total += self.predict_retention(t)
        return (total / resolution) * 100.0


@dataclass
class ViralityScoring:
    """Deterministic structural scoring for the baseline agent."""

    pass_threshold: float = 75.0

    def _estimate_decay_from_script(self, script: ScriptDocument) -> float:
        # Lower decay implies better retention.
        base_decay = 0.010

        if not script.segments:
            return base_decay

        first_seg = script.segments[0]
        if first_seg.vad_score and first_seg.vad_score.arousal > 0.8:
            base_decay -= 0.002

        total_duration = max(1, script.target_duration_seconds)
        cuts_per_second = len(script.segments) / total_duration
        if cuts_per_second > 0.10:
            base_decay -= 0.001

        vad_scores = [s.vad_score for s in script.segments if s.vad_score is not None]
        if len(vad_scores) >= 2:
            arousal_range = max(v.arousal for v in vad_scores) - min(v.arousal for v in vad_scores)
            if arousal_range > 0.3:
                base_decay -= 0.001

        if script.metadata.get("seamless_loop", False):
            base_decay -= 0.001

        return max(0.002, base_decay)

    def score(self, script: ScriptDocument, membership_insights: Optional[str] = None) -> ViralityScore:
        # Compute structural features.
        segments = script.segments
        total_duration = max(1, script.target_duration_seconds)

        # Hook strength proxy: arousal in first segment + open-loop token.
        first_arousal = 0.0
        if segments and segments[0].vad_score is not None:
            first_arousal = segments[0].vad_score.arousal

        hook_strength = min(100.0, first_arousal * 100.0)

        # Retention prediction via decay estimation.
        decay = self._estimate_decay_from_script(script)
        model = RetentionCurveModel(decay_rate=decay, retention_floor=0.20)
        apv = model.predict_apv(total_duration)
        retention_prediction = max(0.0, min(100.0, apv))

        # Emotional intensity: arousal variance.
        vad_scores = [s.vad_score for s in segments if s.vad_score is not None]
        if len(vad_scores) >= 2:
            arousals = [v.arousal for v in vad_scores]
            mean = sum(arousals) / len(arousals)
            var = sum((x - mean) ** 2 for x in arousals) / len(arousals)
            emotional_arc_intensity = min(100.0, (var ** 0.5) * 220.0)
        elif vad_scores:
            emotional_arc_intensity = min(100.0, vad_scores[0].arousal * 110.0)
        else:
            emotional_arc_intensity = 20.0

        # STEPPS compliance proxy: look for tokens in on-screen text.
        text_blob = " ".join(s.on_screen_text for s in segments).lower()
        stepps_points = 0
        for token in ["secreto", "verdad", "impacto", "paso", "check", "práctico", "ejemplo", "cambio", "real"]:
            if token in text_blob:
                stepps_points += 1
        stepps_compliance = min(100.0, stepps_points * 12.5)

        # VAD dynamic range proxy.
        if vad_scores:
            vad_dynamic_range = min(100.0, (max(v.arousal for v in vad_scores) - min(v.arousal for v in vad_scores)) * 160.0)
        else:
            vad_dynamic_range = 30.0

        loop_seamlessness = 90.0 if script.metadata.get("seamless_loop", False) else 40.0
        geo_readiness = min(100.0, 20.0 + 10.0 * len(segments))

        score = ViralityScore(
            hook_strength=hook_strength,
            retention_prediction=retention_prediction,
            emotional_arc_intensity=emotional_arc_intensity,
            stepps_compliance=stepps_compliance,
            vad_dynamic_range=vad_dynamic_range,
            loop_seamlessness=loop_seamlessness,
            geo_readiness=geo_readiness,
        )
        score.compute_overall()

        # Feedback string for refinement loop.
        feedback_parts = []
        if score.hook_strength < 60:
            feedback_parts.append("Sube la arousal del primer segmento y crea un conflicto/curiosidad explícita.")
        if score.retention_prediction < 65:
            feedback_parts.append("Aumenta densidad de segmentos (más cortes) y añade micro-bucles de verificación.")
        if score.stepps_compliance < 60:
            feedback_parts.append("Inserta más elementos de valor práctico: pasos, checklist y un ejemplo real.")
        if score.loop_seamlessness < 80:
            feedback_parts.append("Asegura un cierre que conecte con el inicio (seamless loop).")

        score.feedback = " ".join(feedback_parts) if feedback_parts else "Apto para publicación."
        score.pass_threshold = score.overall_score >= self.pass_threshold
        return score
