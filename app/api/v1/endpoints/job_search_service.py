from typing import Any, List
from unittest import result

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app import crud

from app.api.dependencies import get_db

router = APIRouter()


@router.post("",
            response_model=schemas.Message)
def refresh_job(
                    db: Session = Depends(get_db), 
                    obj_in = schemas.job_search_service.RefreshJobRequest) -> Any:
    result = crud.job_search_service.refresh_job(db = db, obj_in = obj_in)
    return result


@router.post("",
            response_model=schemas.Message)
def update_failed(*,
                   db: Session = Depends(get_db),
                   obj_in: schemas.job_search_service.UpdateFailRequest) -> Any:
    result = crud.job_search_service.update_failed(db = db, obj_in = obj_in)
    return result


@router.post("",
            response_model=schemas.Message)
def create_metadata(*,
                   db: Session = Depends(get_db),
                   obj_in: schemas.job_search_service.CreateMetaDataRequest) -> Any:

    result = crud.job_search_service.create_metadata(db = db, obj_in = obj_in)
    return result