from __future__ import annotations
import datetime
from typing import Dict, Any




class User:
    def __init__(self, data):
        self.data = data
        self.username = data.get('username')
        self.global_rank = data.get('statistics').get("global_rank") if data.get('statistics').get("global_rank") is not None else 0
        self.pp = data.get("statistics").get("pp")  if data.get('statistics') else "None"
        self.rank = data.get("statistics").get("grade_counts") if data.get('statistics') else "None"
        self.accuracy = f"{data.get('statistics').get('hit_accuracy'):,.2f}"  if data.get('statistics') else "None"
        self.country_rank = data.get('statistics').get("country_rank") if data.get('statistics').get("country_rank") is not None else 0
        self.profile_order = data['profile_order'] if data['profile_order'] else "Cant Get Profile Order!"
        self.country_emoji = f":flag_{data.get('country_code').lower()}:" if data.get("country_code") else "None"
        self.country_code = data.get("country_code") if data.get("country_code") else "None"
        self._country = data.get("country")
        self.avatar_url = data.get("avatar_url")
        self.id = data.get("id")
        self.playstyle = data.get("playstyle") 
        self.playmode = data.get("playmode")
        self.max_combo = data.get("statistics").get("maximum_combo")
        self.level = data.get("statistics").get("level")
        self.follower_count = data.get("follower_count")
        self.total_hits = data.get("statistics").get("total_hits")
        self.total_score = data.get("statistics").get("total_score")
        self.play_count = data.get("statistics").get("play_count")
        self.replays_watched_count = data['replays_watched_counts']

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} username: {self.username!r}, id: {self.id}>"

    def __str__(self) -> str:
        return self.username


    @property
    def joined_at(self) -> datetime.datetime | None:
        if self.data.get("join_date"):
           return datetime.datetime.strptime(self.data.get('join_date'), '%Y-%m-%dT%H:%M:%S+00:00') 
        
        return None

    @property
    def country(self):
        return [self._country['code'], self._country['name']]

    @property
    def raw(self) -> Dict[str, Any]:
        return self.data
