from typing import Optional

from pydantic import BaseModel


class FeedBase(BaseModel):
    company_id: Optional[str]
    company_scrape_id: Optional[str]
    feed_id: Optional[str]
    type: Optional[str]


class FeedRequest(FeedBase):
    company_id: str
    company_scrape_id: str
    feed_id: str
    type: str
    envs: list[int]


class FeedCreate(FeedBase):
    company_id: str
    company_scrape_id: str
    feed_id: str
    type: str
 

class FeedUpdate(FeedBase):
    type: str


class FeedResponse(FeedBase):
    id: Optional[int]
    envs: list[str] = []

    class Config:
        orm_mode = True
