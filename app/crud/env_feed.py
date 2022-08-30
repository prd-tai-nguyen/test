from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.env_feed import EnvFeed
from app.schemas.env_feed import EnvFeedCreate


class CRUDEnvFeed(CRUDBase[EnvFeed, EnvFeedCreate, None]):

    def get_env(self, db: Session, feed_id: int) -> list[EnvFeed]:
        return db.query(EnvFeed).filter(EnvFeed.feed_id == feed_id).all()


env_feed = CRUDEnvFeed(EnvFeed)
