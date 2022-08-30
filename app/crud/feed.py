from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.feed import Feed
from app.schemas.env_feed import EnvFeedCreate
from app.schemas.feed import FeedCreate, FeedRequest, FeedUpdate

from sqlalchemy import or_
from .env_feed import env_feed

class CRUDFeed(CRUDBase[Feed, FeedCreate, FeedUpdate]):
    def create(self, db: Session, *, obj_in: FeedRequest) -> Feed:
        result = db.query(Feed).filter(or_(Feed.company_scrape_id == obj_in.company_scrape_id, Feed.feed_id == obj_in.feed_id)).first()
       
        if (result == None):
            feed = super().create(db=db, obj_in = FeedCreate(company_id= obj_in.company_id, company_scrape_id= obj_in.company_scrape_id, feed_id= obj_in.feed_id, type = obj_in.type))
         
            for env in obj_in.envs:
                env_feed.create(db=db, obj_in = EnvFeedCreate(env_id=env, feed_id = feed.id))
            
            return feed

        return None


feed = CRUDFeed(Feed)
