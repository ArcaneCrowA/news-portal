from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db

from .routers import books, reviews

app = FastAPI(title="FastAPI Book API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/api/books", tags=["books"])
app.include_router(reviews.router, prefix="/api/reviews", tags=["reviews"])


@app.on_event("startup")
def on_startup():
    init_db()
