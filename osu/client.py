from __future__ import annotations
import aiohttp
from typing import Union, Any, Optional
import logging


from .errors import NoBeatMapFound, NoUserFound
from .http import HTTPClient
from .models import User, Beatmap, Score, BeatmapCompact, BeatmapSet

logger = logging.getLogger(__name__)


class Client:
    def __init__(self, *, client_id: int, client_secret: str):
        self.id = client_id
        self.secret = client_secret
        self.beatmap_types = ['favourite', 'graveyard', 'loved', 'most_played', 'pending', 'ranked']
        self.special_types = ['most_played']
        self.score_types = ['best', 'firsts', 'recent']
        self.http: HTTPClient = HTTPClient(client_id=client_id, client_secret=client_secret)


    async def __aenter__(self):
        return self

    async def __aexit__(self, *error_details):
        await self.http.close()

    async def close(self):
        await self.http.close()

    async def fetch_user(self, user_id: Union[str, int]) -> User:
        """Fetches a user using either an ID or Username"""

        user = await self.http.get_user(user_id)
        
        if 'error' in user.keys() and user['error'] is None:
            raise NoUserFound("No user was found by that name or id!")
        
        return User(user)

    async def fetch_user_score(self, user: int, *, type: str, limit: int = 1, include_fails: bool = False) -> list[Score]:
        """Fetches scores for a user based on a type and limit"""
    
        if type not in self.score_types:
            types = ', '.join(self.score_types)
            raise ValueError(f"Score type must be in {types}")

        params = {
            "limit": limit,
            "include_fails": f"{0 if not include_fails else 1}"
        }

        json = await self.http.get_user_scores(user, type,params)
        beatmaps = []
        
        for beatmap in json:
            beatmaps.append(Score(beatmap))
                
        return beatmaps

    async def fetch_user_beatmaps(self, /, user: int, type: str, limit: int) -> list[BeatmapSet] | list[dict[str, Union[BeatmapSet, BeatmapCompact]]]:
        """Fetches beatmaps for a user based on a type and limit""" 
        params = {
            "limit": limit
        }
        
        if type not in self.beatmap_types:
            types = ', '.join(self.beatmap_types)
            raise ValueError(f"Beatmap type must be in {types}")

        json = await self.http.get_user_beatmaps(user, type,params)
    
        beatmaps = []
        
        for beatmap in json:
            if type in self.special_types:
                beatmaps.append({"beatmapset":BeatmapSet(beatmap['beatmapset']), "beatmap": BeatmapCompact(beatmap['beatmap'])})
            else:
                beatmaps.append(BeatmapSet(beatmap))
                
        return beatmaps
    
    async def _tests(self, method: str, /, endpoint: str, params: Optional[dict[str, Any]] = None):
        headers = await self.http._make_headers()
        async with self.http._session.request(method, self.http.API_URL + endpoint, params=params, headers=headers) as resp:
            json = await resp.json()

        return json

    async def fetch_beatmap(self, beatmap: Union[str, int]) -> Beatmap: 
        """Fetches a beatmap"""
        json = await self.http.get_beatmap(beatmap)

        if 'error' in json.keys() and json['error'] is None:
            raise NoBeatMapFound("No beatmap was found by that ID!")

        return Beatmap(json)
