from __future__ import annotations

from typing import Optional

from .beatmaps import BeatmapSet, BeatmapCompact

class Score:
    def __init__(self, data: dict):
        self.accuracy: int = data['accuracy']
        self.best_id: int = data['best_id']
        self.created_at: str = data['created_at']
        self.id: int = data['id']
        self.max_combo: int = data['max_combo']
        self.mode: str = data['mode']
        self.mods: list[str] = data['mods']
        self.passed: bool = data['passed']
        self.perfect: bool = data['perfect']
        self.pp: Optional[int] = data['pp'] or 0 
        self.rank: str = data['rank']
        self.replay: bool = data['replay']
        self.statistics: dict = data['statistics']
        self.user_id: int = data['user_id']
        self.beatmapset = BeatmapSet(data['beatmapset'])
        self.beatmap = BeatmapCompact(data['beatmap'])