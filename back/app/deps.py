from fastapi import Depends, HTTPException
from sqlmodel import Session

from .db import get_session
