from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Feed(Base):
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(String(255), nullable=False)
    company_scrape_id = Column(String(255), nullable=False, unique=True)
    feed_id = Column(String(255), nullable=False, unique=True)
    type = Column(String(255), nullable=False)

    env_feed = relationship("env_feed", back_populates="feed")