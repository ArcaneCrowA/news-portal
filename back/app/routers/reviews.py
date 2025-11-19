from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from .. import crud, models
from ..db import get_session

router = APIRouter()


@router.post("/", response_model=models.Review)
def create_review(
    review: models.Review, session: Session = Depends(get_session)
):
    return crud.create_review(session, review)


@router.get("/")
def list_reviews(book_id: int, session: Session = Depends(get_session)):
    return session.exec(
        select(models.Review).where(models.Review.book_id == book_id)
    ).all()
