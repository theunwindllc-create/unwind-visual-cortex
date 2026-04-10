from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Dict, Any, List


class NarrativeArc(Enum):
    RAGS_TO_RICHES = "rise"
    TRAGEDY = "fall"
    MAN_IN_A_HOLE = "fall-rise"
    ICARUS = "rise-fall"
    CINDERELLA = "rise-fall-rise"
    OEDIPUS = "fall-rise-fall"


class CopywritingFramework(Enum):
    PAS = "Problem-Agitate-Solution"
    BAB = "Before-After-Bridge"
    SCQA = "Situation-Challenge-Question-Answer"
    FAB = "Features-Advantages-Benefits"


class HookType(Enum):
    CURIOSITY_GAP = "curiosity_gap"
    PATTERN_INTERRUPT = "pattern_interrupt"
    UNEXPECTED_CONFESSION = "unexpected_confession"
    VISUAL_ANCHOR = "visual_anchor"
    CONFLICT_STATEMENT = "conflict_statement"


class EmotionTrigger(Enum):
    FEAR_URGENCY = "fear_urgency"
    CONFIDENCE_TRUST = "confidence_trust"
    DESIRE_VANITY = "desire_vanity"
    SURPRISE_CURIOSITY = "surprise_curiosity"


class AgentState(Enum):
    IDLE = "idle"
    RESEARCHING = "researching"
    SCRIPTING = "scripting"
    EVALUATING = "evaluating"
    REFINING = "refining"
    COMPLETE = "complete"
    ERROR = "error"


@dataclass
class TrendData:
    topic: str
    trending_keywords: List[str] = field(default_factory=list)
    top_performing_hooks: List[str] = field(default_factory=list)
    dominant_sentiment: str = "neutral"
    average_niche_retention: float = 0.0
    timestamp: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VADScore:
    valence: float = 0.0
    arousal: float = 0.0
    dominance: float = 0.0

    @property
    def is_viral_broadcast(self) -> bool:
        return self.arousal > 0.7 and self.dominance > 0.6

    @property
    def is_engagement_driver(self) -> bool:
        return self.arousal > 0.7 and self.dominance < 0.4


@dataclass
class ScriptSegment:
    timestamp_start: float
    timestamp_end: float
    scene_description: str
    spoken_dialogue: str
    on_screen_text: str
    sound_design: str
    emotion_trigger: EmotionTrigger
    vad_score: Optional[VADScore] = None
    visual_cue: str = ""
    pacing_note: str = ""


@dataclass
class ScriptDocument:
    title: str
    target_duration_seconds: int
    narrative_arc: NarrativeArc
    copywriting_framework: CopywritingFramework
    hook_type: HookType
    target_platform: str
    segments: List[ScriptSegment] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def total_segments(self) -> int:
        return len(self.segments)


@dataclass
class ViralityScore:
    hook_strength: float = 0.0
    retention_prediction: float = 0.0
    emotional_arc_intensity: float = 0.0
    stepps_compliance: float = 0.0
    vad_dynamic_range: float = 0.0
    loop_seamlessness: float = 0.0
    geo_readiness: float = 0.0
    overall_score: float = 0.0
    feedback: str = ""
    pass_threshold: bool = False

    def compute_overall(self, weights: Optional[Dict[str, float]] = None) -> float:
        if weights is None:
            weights = {
                "hook_strength": 0.25,
                "retention_prediction": 0.25,
                "emotional_arc_intensity": 0.15,
                "stepps_compliance": 0.10,
                "vad_dynamic_range": 0.10,
                "loop_seamlessness": 0.10,
                "geo_readiness": 0.05,
            }
        self.overall_score = (
            self.hook_strength * weights["hook_strength"]
            + self.retention_prediction * weights["retention_prediction"]
            + self.emotional_arc_intensity * weights["emotional_arc_intensity"]
            + self.stepps_compliance * weights["stepps_compliance"]
            + self.vad_dynamic_range * weights["vad_dynamic_range"]
            + self.loop_seamlessness * weights["loop_seamlessness"]
            + self.geo_readiness * weights["geo_readiness"]
        )
        self.pass_threshold = self.overall_score >= 75.0
        return self.overall_score


@dataclass
class AgentMemoryEntry:
    session_id: str
    topic: str
    script_hash: str
    virality_score: float
    key_insight: str
    timestamp: str
    source: str = "self_evaluation"


class ScriptingError(RuntimeError):
    pass
