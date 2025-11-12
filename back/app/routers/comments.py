from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..models import Comment

router = APIRouter()


@router.get("/post/{post_id}")
def list_comments(post_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Comment).where(Comment.post_id == post_id)).all()


@router.post("/")
def create_comment(comment: Comment, session: Session = Depends(get_session)):
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment
