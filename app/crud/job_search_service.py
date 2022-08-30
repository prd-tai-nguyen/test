import requests
import hashlib
import time

from typing import Optional, List

from sqlalchemy.orm import Session

from app.schemas.env import EnvCreate
from app.schemas.job_search_service import CreateMetaDataRequest, CreatedByType, RefreshJobRequest, UpdateFailRequest

from .feed import feed as feed_service
from .env_feed import env_feed as env_feed_service


class JobSearchService():
    def get_token(timestamp: str, env: EnvCreate):
        s = env.client_id + timestamp + env.client_secret
        return hashlib.sha256(s.encode("utf-8")).hexdigest()

    def call_api(self, env: EnvCreate, *, payload: object):
        timestamp = time.time()

        headers = {
            "API-clientid": env.client_id,
            "API-timestamp": timestamp,
            "API-token": self.get_token(timestamp=timestamp, env=env)
        }

        result = requests.post(env.api_url, json=payload, headers=headers)
        return result

    def create_metadata(self, db: Session, * , obj_in: CreateMetaDataRequest):
        payload = {
            "company_scrape_id": obj_in.company_scrape_id,
            "type": obj_in.type,
            "company_id": obj_in.company_id,
            "feed_id": obj_in.feed_id
        }

        env_feeds = env_feed_service.get_env(db=db, feed_id = obj_in.feed_id)
        for env_feed in env_feeds:
            self.call_api(env=env_feed.env, payload=payload)

    def refresh_job(self, db: Session, *, obj_in : RefreshJobRequest):
        payload = {
            "company_id": obj_in.feed_id,
            "job_feed_url": obj_in.s3_url,
            "reload_all_jobs": False,
            "session_id": obj_in.session_id
        }

        env_feeds = env_feed_service.get_env(db=db, feed_id=obj_in.feed_id)
        for env_feed in env_feeds:
            self.call_api(env=env_feed.env, payload=payload)

    def update_failed(self, db: Session, * , obj_in : UpdateFailRequest):
        created_by = CreatedByType.SCRAPE if obj_in.session_id is None else CreatedByType.OLIVIA
        
        payload = {
            "feed_id": obj_in.feed_id,
            "created_by": created_by,
            "session_id": obj_in.session_id,
            "errors": obj_in.message
        }

        env_feeds = env_feed_service.get_env(db=db, feed_id=obj_in.feed_id)
        for env_feed in env_feeds:
            self.call_api(env=env_feed.env, payload=payload)


job_search_service = JobSearchService()
