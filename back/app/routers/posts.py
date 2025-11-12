from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..crud import create_post, delete_post, update_post
from ..db import get_session
from ..models import Post

router = APIRouter()


@router.get("/")
def list_posts(session: Session = Depends(get_session)):
    posts = session.exec(select(Post).order_by(Post.created_at.desc())).all()
    return posts


@router.get("/{post_id}")
def get_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/")
def create(post: Post, session: Session = Depends(get_session)):
    return create_post(session, post)


@router.put("/{post_id}")
def update(post_id: int, data: Post, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404)
    return update_post(session, post, **data.dict(exclude_unset=True))


@router.delete("/{post_id}")
def delete(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404)
    delete_post(session, post)
    return {"ok": True}
