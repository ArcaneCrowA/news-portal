from fastapi import Depends, HTTPException, Request, status
from sqlmodel import Session

from .db import get_session
from .models import Post, User


# Simple stub for current_user. Replace with real auth (OAuth2 / JWT) in prod.
def get_current_user(
    request: Request, session: Session = Depends(get_session)
) -> User:
    # For demo: user id in query ?as_user=1 (very insecure, demo-only)
    user_id = request.query_params.get("as_user")
    if not user_id:
        # default demo user (id=1) if exists
        user = session.get(User, 1)
        if not user:
            # if no user, raise but you can fallback to anonymous
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No current user. Add ?as_user=1 for demo",
            )
        return user
    user = session.get(User, int(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def require_author(post: Post, user: User):
    if post.author_id != user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to modify this post"
        )
