from typing import Generator

from app.database.session import SessionLocal


def get_db() -> Generator:
    with SessionLocal() as session:
        yield session
