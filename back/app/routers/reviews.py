from fastapi import APIRouter, Depends
from sqlmodel import Session

from .. import crud, models
from ..db import get_session

router = APIRouter()


@router.post("/", response_model=models.Review)
def create_review(
    review: models.Review, session: Session = Depends(get_session)
):
    return crud.create_review(session, review)
