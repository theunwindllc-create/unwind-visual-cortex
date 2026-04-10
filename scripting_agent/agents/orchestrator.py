from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

from ..models.schema import (
    AgentState,
    TrendData,
    ScriptDocument,
    ScriptSegment,
    ViralityScore,
    NarrativeArc,
    CopywritingFramework,
    HookType,
    EmotionTrigger,
    VADScore,
    AgentMemoryEntry,
    ScriptingError,
)
from ..memory.feedback_loop import MemoryStore
from ..tools.virality_engine import ViralityScoring


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stable_session_id(prompt: str) -> str:
    raw = f"{prompt}_{_now_iso()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def _tokenize(text: str) -> List[str]:
    words = []
    for w in text.lower().replace("\n", " ").split(" "):
        w = "".join(ch for ch in w if ch.isalnum() or ch in ["-", "_", "."])
        if not w:
            continue
        if len(w) < 3:
            continue
        words.append(w)
    # de-dupe while preserving order
    seen = set()
    out = []
    for w in words:
        if w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out


@dataclass
class ScriptingPipelineConfig:
    max_refinement_iterations: int = 3
    virality_pass_threshold: float = 75.0
    target_platform: str = "Instagram Reels"
    target_duration_seconds: int = 45
    enable_trend_research: bool = True
    enable_seamless_loop: bool = True
    language: str = "es"
    # portability: baseline uses deterministic heuristics (no external APIs)
    deterministic_only: bool = True


@dataclass
class OrchestratorState:
    user_prompt: str
    config: ScriptingPipelineConfig
    current_state: AgentState = AgentState.IDLE
    trend_data: Optional[TrendData] = None
    script_document: Optional[ScriptDocument] = None
    virality_score: Optional[ViralityScore] = None
    iteration_count: int = 0
    error_log: List[str] = field(default_factory=list)
    session_id: str = ""
    memory_entries: List[AgentMemoryEntry] = field(default_factory=list)
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.session_id:
            self.session_id = _stable_session_id(self.user_prompt)

    def log(self, phase: str, action: str, observation: str) -> None:
        self.trace.append(
            {
                "phase": phase,
                "action": action,
                "observation": observation,
                "iteration": self.iteration_count,
                "timestamp": _now_iso(),
            }
        )


def _gate_entry(state: OrchestratorState) -> str:
    state.current_state = AgentState.IDLE
    state.log(
        "ENTRY",
        "Validate prompt and config",
        f"platform={state.config.target_platform}, duration={state.config.target_duration_seconds}s"
    )

    if not state.user_prompt or len(state.user_prompt.strip()) < 5:
        state.current_state = AgentState.ERROR
        state.error_log.append("Prompt vacío o demasiado corto.")
        return "ERROR"

    if state.config.enable_trend_research:
        return "RESEARCH"
    return "SCRIPT"


def _invoke_research_agent(state: OrchestratorState, memory: MemoryStore) -> TrendData:
    # Baseline deterministic "research": token extraction + local insights.
    topic_words = _tokenize(state.user_prompt)
    top_keywords = topic_words[:8]

    prior_entries = memory.retrieve_by_topic(state.user_prompt, top_k=5)
    insights_summary = memory.summarize_insights(prior_entries)

    hooks = [
        "conflicto_directo",
        "curiosidad_gap",
        "patron_interrumpido",
        "secreto_practico",
    ]

    dominant_sentiment = "neutral"
    return TrendData(
        topic=state.user_prompt,
        trending_keywords=top_keywords,
        top_performing_hooks=hooks,
        dominant_sentiment=dominant_sentiment,
        average_niche_retention=60.0,
        timestamp=_now_iso(),
        metadata={"insights_summary": insights_summary},
    )


def _gate_research(state: OrchestratorState, memory: MemoryStore) -> str:
    state.current_state = AgentState.RESEARCHING
    state.log("RESEARCH", "Run baseline research (tokens + local memory)" , "Synthesizing TrendData...")
    td = _invoke_research_agent(state, memory)
    state.trend_data = td
    state.log(
        "RESEARCH",
        "Research complete",
        f"keywords={len(td.trending_keywords)}"
    )
    return "SCRIPT"


def _make_script_segment(
    idx: int,
    total: int,
    duration: int,
    emotion: EmotionTrigger,
    vad: VADScore,
    spoken: str,
    on_screen: str,
    visual_cue: str,
    pacing_note: str,
) -> ScriptSegment:
    start = (idx / total) * duration
    end = ((idx + 1) / total) * duration
    return ScriptSegment(
        timestamp_start=float(start),
        timestamp_end=float(end),
        scene_description="".join(["".strip()]) or "" ,
        spoken_dialogue=spoken,
        on_screen_text=on_screen,
        sound_design="UI-blips + low-bed cinematic",
        emotion_trigger=emotion,
        vad_score=vad,
        visual_cue=visual_cue,
        pacing_note=pacing_note,
    )


def _invoke_scripting_agent(state: OrchestratorState, memory: MemoryStore) -> ScriptDocument:
    # Deterministic baseline script generation.
    prompt_words = _tokenize(state.user_prompt)
    topic = state.user_prompt.strip()
    keywords = (state.trend_data.trending_keywords if state.trend_data else prompt_words)[:6]

    # Cuban-first constraint: connectivity/hardware fallback in every script.
    try_this = "".join([
        "Try this (15 min): arma un agente local con herramienta->schema->retry; guarda logs en JSON; evalúa con umbral 75 y repite 1 refinamiento."
    ])
    failure_mode = "".join([
        "Modo fallo: el agente 'alucina' un tool-call. Detecta si el resultado viola el esquema y registra el input/output del tool."
    ])

    # Determine hook/narrative based on keywords.
    hook_type = HookType.CURIOSITY_GAP
    narrative_arc = NarrativeArc.MAN_IN_A_HOLE if "fall" in topic.lower() else NarrativeArc.RAGS_TO_RICHES
    framework = CopywritingFramework.PAS

    segments: List[ScriptSegment] = []
    total = 6
    duration = state.config.target_duration_seconds

    # Segment 0: hook
    segments.append(
        _make_script_segment(
            0,
            total,
            duration,
            emotion=EmotionTrigger.SURPRISE_CURIOSITY,
            vad=VADScore(valence=0.2, arousal=0.9, dominance=0.3),
            spoken=("Si tu agente falla y tú solo 'le pides otra vez', estás perdiendo la carrera. Hoy lo arreglamos con un loop de verificación."),
            on_screen=("ERROR→VERIFICAR→REINTENTAR (sin humo)"),
            visual_cue="Estado del agente: Plan→Tool→Observe→Verify",
            pacing_note="Corte rápido; 1 frase por beat; abre con conflicto.",
        )
    )

    # Segment 1-4: mechanism
    cue_map = [
        (EmotionTrigger.CONFIDENCE_TRUST, VADScore(0.6, 0.75, 0.7), "Memoria + poda de contexto", "Pausa breve; explica regla.",
         "Guardas solo lo que sirve: memoria por tema, podas por stale, y recuperas en cada ciclo."),
        (EmotionTrigger.DESIRE_VANITY, VADScore(0.7, 0.8, 0.75), "Evaluación con umbral", "Vuelve al umbral; muestra regla.",
         "No publiques si no pasa el umbral. Evalúa hook + retención + loop seamless."),
        (EmotionTrigger.FEAR_URGENCY, VADScore(0.1, 0.85, 0.2), "Seguridad como frontera", "Un solo límite explícito.",
         "Jaula del agente: schema primero; si viola, se rechaza. Nunca ejecutes comandos sin verificación."),
        (EmotionTrigger.CONFIDENCE_TRUST, VADScore(0.6, 0.7, 0.6), "Try this", "Checklist en pantalla.",
         try_this),
    ]

    for i, (emotion, vad, on, pacing, spoken) in enumerate(cue_map, start=1):
        segments.append(
            _make_script_segment(
                i,
                total,
                duration,
                emotion=emotion,
                vad=vad,
                spoken=spoken,
                on_screen=on,
                visual_cue=on,
                pacing_note=pacing,
            )
        )

    # Segment 5: failure mode + seamless loop close.
    segments.append(
        _make_script_segment(
            5,
            total,
            duration,
            emotion=EmotionTrigger.FEAR_URGENCY,
            vad=VADScore(0.0, 0.8, 0.25),
            spoken=f"{failure_mode} Y si quieres que mejore: ajusta 1 variable, no 10. Eso es evolución consciente.",
            on_screen="Detecta el fallo. Ajusta 1 variable.",
            visual_cue="Seamless loop: vuelta al inicio",
            pacing_note="Cierre que conecta con el hook.",
        )
    )

    seamless_loop = bool(state.config.enable_seamless_loop)

    title = f"Agentes con Recibo Técnico (loop de verificación)"

    script = ScriptDocument(
        title=title,
        target_duration_seconds=duration,
        narrative_arc=narrative_arc,
        copywriting_framework=framework,
        hook_type=hook_type,
        target_platform=state.config.target_platform,
        segments=segments,
        metadata={
            "seamless_loop": seamless_loop,
            "topic_keywords": keywords,
            "try_this": try_this,
            "modo_fallo": failure_mode,
        },
    )

    return script


def _invoke_evaluation_agent(state: OrchestratorState, scoring: ViralityScoring) -> ViralityScore:
    membership_insights = ""
    if state.trend_data and state.trend_data.metadata.get("insights_summary"):
        membership_insights = state.trend_data.metadata["insights_summary"]
    return scoring.score(state.script_document, membership_insights=membership_insights)  # type: ignore[arg-type]


def _gate_script(state: OrchestratorState, memory: MemoryStore) -> str:
    state.current_state = AgentState.SCRIPTING
    state.log("SCRIPT", "Generate ScriptDocument", "Building segments + try_this...")
    if state.trend_data is None:
        state.trend_data = TrendData(topic=state.user_prompt)
    script = _invoke_scripting_agent(state, memory)
    state.script_document = script
    state.log(
        "SCRIPT",
        "Script complete",
        f"segments={script.total_segments}"
    )
    return "EVALUATE"


def _gate_evaluate(state: OrchestratorState, memory: MemoryStore, scoring: ViralityScoring) -> str:
    state.current_state = AgentState.EVALUATING
    state.log("EVALUATE", "Score virality deterministically", "Computing overall score...")

    assert state.script_document is not None
    score = _invoke_evaluation_agent(state, scoring)
    state.virality_score = score
    state.log(
        "EVALUATE",
        "Evaluation complete",
        f"overall={score.overall_score:.1f}/100 pass={score.pass_threshold}"
    )

    if score.pass_threshold:
        return "COMPLETE"

    if state.iteration_count < state.config.max_refinement_iterations:
        return "REFINE"

    return "COMPLETE"


def _gate_refine(state: OrchestratorState, memory: MemoryStore) -> str:
    state.current_state = AgentState.REFINING
    state.iteration_count += 1
    state.log("REFINE", "Reflexion-like refinement", "Adjusting arousal/seg density proxies...")

    assert state.script_document is not None
    # Minimal refinement strategy: increase arousal proxies for segments 0 and 5,
    # and ensure seamless_loop flag.
    for i, seg in enumerate(state.script_document.segments):
        if seg.vad_score is None:
            continue
        if i == 0:
            seg.vad_score.arousal = min(1.0, seg.vad_score.arousal + 0.05)
            seg.vad_score.dominance = max(0.0, seg.vad_score.dominance - 0.05)
        if i == len(state.script_document.segments) - 1:
            seg.vad_score.arousal = min(1.0, seg.vad_score.arousal + 0.03)

    state.script_document.metadata["seamless_loop"] = True
    return "EVALUATE"


def _store_memory(state: OrchestratorState, memory: MemoryStore) -> None:
    assert state.virality_score is not None
    assert state.script_document is not None
    script_text = "\n".join(s.spoken_dialogue for s in state.script_document.segments)

    entry = AgentMemoryEntry(
        session_id=state.session_id,
        topic=state.user_prompt,
        script_hash=memory.hash_script_text(script_text),
        virality_score=state.virality_score.overall_score,
        key_insight=state.virality_score.feedback[:160],
        timestamp=_now_iso(),
        source="self_evaluation",
    )
    memory.store(entry)


def run_scripting_pipeline(user_prompt: str, config: Optional[ScriptingPipelineConfig] = None) -> Dict[str, Any]:
    config = config or ScriptingPipelineConfig()
    state = OrchestratorState(user_prompt=user_prompt, config=config)

    memory = MemoryStore()
    scoring = ViralityScoring(pass_threshold=config.virality_pass_threshold)

    route = _gate_entry(state)
    if route == "ERROR":
        return {
            "ok": False,
            "error": state.error_log,
            "trace": state.trace,
        }

    if route == "RESEARCH":
        route = _gate_research(state, memory)

    if route == "SCRIPT":
        route = _gate_script(state, memory)

    # Gates loop
    while True:
        if route == "EVALUATE":
            route = _gate_evaluate(state, memory, scoring)

        if route == "REFINE":
            route = _gate_refine(state, memory)
            continue

        if route == "COMPLETE":
            if state.script_document is not None and state.virality_score is not None:
                _store_memory(state, memory)
            return {
                "ok": True,
                "session_id": state.session_id,
                "script_document": state.script_document,
                "virality_score": state.virality_score,
                "trace": state.trace,
            }

        if route == "ERROR":
            return {"ok": False, "error": state.error_log, "trace": state.trace}

        raise ScriptingError(f"Unknown route: {route}")
