from sqlmodel import Session, select

from . import models


def get_book(session: Session, book_id: int):
    return session.get(models.Book, book_id)


def list_books(session: Session, offset: int = 0, limit: int = 10):
    return session.exec(select(models.Book).offset(offset).limit(limit)).all()


def create_book(session: Session, book: models.Book):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def create_review(session: Session, review: models.Review):
    session.add(review)
    session.commit()
    session.refresh(review)
    return review


def create_author(session: Session, author: models.Author):
    session.add(author)
    session.commit()
    session.refresh(author)
    return author
