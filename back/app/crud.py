from typing import List, Optional

from sqlmodel import Session, select

from .models import Category, Comment, Post


def get_post(session: Session, post_id: int) -> Optional[Post]:
    return session.get(Post, post_id)


def list_posts(session: Session, offset: int = 0, limit: int = 10):
    stmt = (
        select(Post)
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    return session.exec(stmt).all()


def list_posts_by_category(
    session: Session, category_slug: str, offset=0, limit=10
):
    stmt = (
        select(Post)
        .join(Category)
        .where(Category.slug == category_slug)
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    return session.exec(stmt).all()


def create_post(session: Session, post: Post) -> Post:
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


def update_post(session: Session, post: Post, **data) -> Post:
    for key, value in data.items():
        setattr(post, key, value)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


def delete_post(session: Session, post: Post):
    session.delete(post)
    session.commit()


def create_comment(session: Session, comment: Comment) -> Comment:
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment


def get_category(session: Session, slug: str) -> Optional[Category]:
    stmt = select(Category).where(Category.slug == slug)
    return session.exec(stmt).first()


def list_categories(session: Session) -> List[Category]:
    return session.exec(select(Category)).all()
