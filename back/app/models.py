from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str

    posts: List["Post"] = Relationship(back_populates="author")
    comments: List["Comment"] = Relationship(back_populates="author")


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str

    posts: List["Post"] = Relationship(back_populates="category")


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

    author: Optional[User] = Relationship(back_populates="posts")
    category: Optional[Category] = Relationship(back_populates="posts")
    comments: List["Comment"] = Relationship(back_populates="post")


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    post_id: int = Field(foreign_key="post.id")
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")

    post: Optional[Post] = Relationship(back_populates="comments")
    author: Optional[User] = Relationship(back_populates="comments")
