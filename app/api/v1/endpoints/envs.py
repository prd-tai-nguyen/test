from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app import crud

from app.api.dependencies import get_db

router = APIRouter()


@router.get("",
            response_model=List[schemas.env.EnvResponse])
def read(db: Session = Depends(get_db),
                  skip: int = 0,
                  limit: int = 100) -> Any:
    """
    Retrieve all env.
    """
    envs = crud.env.get_multi(db, skip=skip, limit=limit)
    return envs


@router.post("",
             response_model=schemas.env.EnvResponse)
def create(*,
                   db: Session = Depends(get_db),
                   env_in: schemas.env.EnvCreate) -> Any:
    """
    Create new env.
    """
    env = crud.env.create(db, obj_in=env_in)
    if env is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client ID already exist in the system.",
        )
    return env


@router.put("/{id}",
            response_model=schemas.env.EnvResponse)
def update(*,
                   db: Session = Depends(get_db),
                   id: int,
                   env_in: schemas.env.EnvUpdate) -> Any:
    """ 
    Update existing env.
    """
    env = crud.env.get(db, model_id=id)
    if not env:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The env with this ID does not exist in the system.",
        )
    env = crud.env.update(db, db_obj=env, obj_in=env_in)
    return env


@router.delete("/{id}",
               response_model=schemas.Message)
def delete(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete existing env.
    """
    env = crud.env.get(db, model_id=id)
    if not env:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The env with this ID does not exist in the system.",
        )
    crud.env.remove(db, model_id=env.id)
    return {"message": f"Env with ID = {id} deleted."}
