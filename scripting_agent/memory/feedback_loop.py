from __future__ import annotations

import json
import hashlib
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from ..models.schema import AgentMemoryEntry


class MemoryStore:
    """Minimal reflexion-like memory store.

    This baseline implementation is keyword-overlap retrieval.
    It is intentionally stdlib-only for portability.
    """

    def __init__(self, store_path: str | Path = ".unwind_scripting_agent_memory/store.json"):
        self.store_path = Path(store_path)
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        self.entries: List[AgentMemoryEntry] = []
        self._load()

    def _load(self) -> None:
        if not self.store_path.exists():
            self.entries = []
            return
        try:
            data = json.loads(self.store_path.read_text(encoding="utf-8"))
            self.entries = [AgentMemoryEntry(**e) for e in data]
        except Exception:
            self.entries = []

    def _save(self) -> None:
        data = [asdict(e) for e in self.entries]
        self.store_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def store(self, entry: AgentMemoryEntry) -> None:
        self.entries.append(entry)
        self._save()

    def retrieve_by_topic(self, topic: str, top_k: int = 5) -> List[AgentMemoryEntry]:
        topic_words = set(topic.lower().split())
        scored = []
        for entry in self.entries:
            entry_words = set(entry.topic.lower().split())
            overlap = len(topic_words & entry_words)
            scored.append((overlap, entry.virality_score, entry))
        scored.sort(key=lambda x: (-x[0], -x[1]))
        return [x[2] for x in scored[:top_k]]

    @staticmethod
    def summarize_insights(entries: List[AgentMemoryEntry]) -> str:
        if not entries:
            return "No prior insights available."
        lines = ["Based on previous script evaluations:"]
        for i, e in enumerate(entries[:5], 1):
            lines.append(f"  {i}. (Score: {e.virality_score:.0f}) {e.key_insight}")
        return "\n".join(lines)

    @staticmethod
    def hash_script_text(text: str) -> str:
        return hashlib.md5(text.encode("utf-8")).hexdigest()[:8]
