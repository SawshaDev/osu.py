from __future__ import annotations

import datetime

# Warning: alot of this code is bad, been meaning to rework everything :>

class Beatmap:
    def __init__(self, data):
        self.data = data
        self.artist = data['beatmapset']['artist']
        self.title = data['beatmapset']['title']
        self.beatmapset = data['beatmapset']
        self.beatmapset_id = data['beatmapset_id']
        self.difficulty_rating = data['difficulty_rating']
        self.id = data['id']
        self.mode = data['mode']
        self.status = data['status']
        self.difficulty = data['version']
        self.cs = data['cs']
        self.drain = data['drain']
        self.last_updated = datetime.datetime.fromisoformat(data['last_updated'].replace('Z', '')) if data['last_updated'] else None
        self.pass_count = data['passcount']
        self.play_count = data['playcount']
        self.url = data['url']    
        self.favorite_count = data['beatmapset']['favourite_count']
        self.nsfw = data['beatmapset']['nsfw']
        self.ranked_date = datetime.datetime.fromisoformat(data['beatmapset']['ranked_date'].replace('Z', '')) if data['beatmapset']['ranked_date'] else None
        self.submitted_date = datetime.datetime.fromisoformat(data['beatmapset']['submitted_date'].replace('Z', ''))  if data['beatmapset']['submitted_date'] else None
        self.max_combo = data['max_combo']
        self.creator = data['beatmapset']['creator']
        self.ar = data['ar']
        self.bpm = data['bpm']

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} title: {self.title!r}, artist: {self.artist!r}>"

    def covers(self, cover: str) -> str:
        if cover not in self.data['beatmapset']['covers']:
            return "Cover not in covers"

        cover_data = self.data['beatmapset']['covers'][cover]
        return cover_data

class BeatmapCompact:
    __slots__ = (
        "beatmapset_id",
        "difficulty_rating",
        "id",
        "mode",
        "status",
        "total_length",
        "user_id",
        "version"
    )
    def __init__(self, data: dict):
        keys = {k: v for k, v in data.items() if k in self.__slots__}
        for k,v in keys.items():
            setattr(self, k, v)
            continue
        


class BeatmapSet:
    __slots__ = (
        "artist",
        "artist_unicode",
        "creator",
        "favourite_count",
        "hype",
        "id",
        "nsfw",
        "offset",
        "play_count",
        "preview_url",
        "source",
        "spotlight",
        "status",
        "title",
        'title_unicode',
        "track_id",
        "user_id",
        "video",
        "json"
    )

    def __init__(self, data: dict):
        self.json = data
        keys = {k: v for k, v in data.items() if k in self.__slots__}
        for k,v in keys.items():
            setattr(self, k, v)
            continue
        
    

    def covers(self, cover: str) -> str:
        if cover not in self.json['covers']:
            covers = ', '.join(self.json['covers'])
            return f"Cover not in covers!\nChoose from {covers}"

        cover_data = self.json['covers'][cover]
        return cover_data
