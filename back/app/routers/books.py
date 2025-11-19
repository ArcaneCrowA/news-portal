from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session

from .. import crud, models
from ..db import get_session

router = APIRouter()


class AuthorCreate(BaseModel):
    name: str
    bio: str


class BookCreate(BaseModel):
    title: str
    description: str
    published_date: datetime
    author: AuthorCreate


@router.get("/", response_model=List[models.Book])
def list_books(
    session: Session = Depends(get_session), offset: int = 0, limit: int = 10
):
    return crud.list_books(session, offset=offset, limit=limit)


@router.get("/{book_id}", response_model=models.Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = crud.get_book(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=models.Book)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    author = models.Author(name=book.author.name, bio=book.author.bio)
    author = crud.create_author(session, author)
    book_to_create = models.Book(
        title=book.title,
        description=book.description,
        author_id=author.id,
        published_date=book.published_date,
    )
    return crud.create_book(session, book_to_create)
