from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database.base_class import Base
from sqlalchemy.orm import relationship

class EnvFeed(Base):
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(Integer, ForeignKey("feed.id"))
    env_id = Column(Integer, ForeignKey("env.id"))

    feed = relationship("feed", back_populates="env_feed")
    env = relationship("env", back_populates="env_feed")