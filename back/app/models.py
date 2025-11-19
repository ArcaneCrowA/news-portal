from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    bio: str

    books: List["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    published_date: datetime = Field(default_factory=datetime.utcnow)


class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="book.id")
    reviewer_name: str
    rating: int = Field(ge=1, le=5)
    comment: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
