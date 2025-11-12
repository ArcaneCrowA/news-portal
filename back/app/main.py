from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db

from .routers import categories, comments, posts

app = FastAPI(title="FastAPI News API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(comments.router, prefix="/api/comments", tags=["comments"])
app.include_router(
    categories.router, prefix="/api/categories", tags=["categories"]
)


@app.on_event("startup")
def on_startup():
    init_db()
