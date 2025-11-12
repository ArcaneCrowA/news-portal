from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..models import Category, Post

router = APIRouter()


@router.get("/")
def list_categories(session: Session = Depends(get_session)):
    return session.exec(select(Category)).all()


@router.post("/")
def create_category(
    category: Category, session: Session = Depends(get_session)
):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


@router.get("/{slug}")
def get_category_posts(slug: str, session: Session = Depends(get_session)):
    stmt = select(Post).join(Category).where(Category.slug == slug)
    return session.exec(stmt).all()
