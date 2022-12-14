from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

print(settings.DB_URI)
engine = create_engine(settings.DB_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
