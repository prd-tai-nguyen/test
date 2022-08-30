from sqlalchemy import Column, Integer, String, Float

from app.database.base_class import Base
from sqlalchemy.orm import relationship


class Env(Base):
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String(255), nullable=False, unique=True)
    client_secret = Column(String(255), nullable=False)
    api_url = Column(String(255), nullable=False)

    env_feed = relationship("env_feed", back_populates="env")