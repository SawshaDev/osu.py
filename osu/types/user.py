from typing import TypedDict

from typing_extensions import NotRequired

class PartialUser(TypedDict):
    id: int
    username: str
    avatar_url: NotRequired[str]
    discord: NotRequired[str]