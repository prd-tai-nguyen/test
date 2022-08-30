from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app import crud

from app.api.dependencies import get_db

router = APIRouter()


@router.get("",
            response_model=List[schemas.feed.FeedResponse])
def read(db: Session = Depends(get_db),
                  skip: int = 0,
                  limit: int = 100) -> Any:
    """
    Retrieve all feed.
    """
    envs = crud.feed.get_multi(db, skip=skip, limit=limit)
    return envs


@router.post("",
             response_model=schemas.feed.FeedResponse)
def create(*,
                   db: Session = Depends(get_db),
                   feed_in: schemas.feed.FeedResponse) -> Any:
    """
    Create new feed.
    """
    feed = crud.feed.create(db, obj_in=feed_in)
    if feed is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Feed already exist in the system.",
        )
    return feed


@router.put("/{id}",
            response_model=schemas.feed.FeedResponse)
def update(*,
                   db: Session = Depends(get_db),
                   id: int,
                   env_in: schemas.env.EnvUpdate) -> Any:
    """ 
    Update existing feed.
    """
    env = crud.feed.get(db, model_id=id)
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
    Delete existing feed.
    """
    env = crud.feed.get(db, model_id=id)
    if not env:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The env with this ID does not exist in the system.",
        )
    crud.env.remove(db, model_id=env.id)
    return {"message": f"Env with ID = {id} deleted."}
