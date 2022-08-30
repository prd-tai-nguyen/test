from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class RefreshJobRequest(BaseModel):
    feed_id: str
    session_id: str | None
    s3_url: str


class UpdateFailRequest(BaseModel):
    feed_id: str
    session_id: str | None
    message: str


class CreateMetaDataRequest(BaseModel):
    company_scrape_id: str
    type: str
    company_id: str
    feed_id: str


class CreatedByType(IntEnum):
    OLIVIA = 1
    SCRAPE = 0