from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.env import Env
from app.schemas.env import EnvCreate, EnvUpdate


class CRUDEnv(CRUDBase[Env, EnvCreate, EnvUpdate]):
    # Declare model specific CRUD operation methods.
    def create(self, db: Session, *, obj_in: EnvCreate) -> Env:
        env = db.query(Env).filter(Env.client_id == obj_in.client_id).first()
        if (env == None):
            return super().create(db=db, obj_in=obj_in)

        return None

env = CRUDEnv(Env)
