from typing import Optional

from pydantic import BaseModel
from .env import EnvBase
from .feed import FeedBase

class EnvFeedBase(BaseModel):
    env_id: Optional[int]
    feed_id: Optional[int]

    env: list[EnvBase] = []
    feed: list[FeedBase] = []


class EnvFeedCreate(EnvFeedBase):
    env_id: int
    feed_id: int