from datetime import datetime
from enum import Enum
from typing import Optional, List
from uuid import UUID

from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field


class User(BaseModel):
    login: str = Field(min_length=3)


class UserCreate(User):
    password: str = Field(min_length=6)


class UserInDb(User):
    id: UUID
    telegram_id: Optional[int] = None
    password_hash: Optional[str] = None
    disabled: Optional[bool] = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    photo_url: Optional[str] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: str = Field(..., min_length=3)
    scopes: List[str] = []


class TelegramUserData(BaseModel):
    id: int
    first_name: str
    username: str
    photo_url: str
    auth_date: int
    hash: str


class Question(BaseModel):
    question: str
    response: int
    answer1: str
    answer2: str
    answer3: str
    answer4: str


class QuestionInDb(Question):
    id: UUID
    owner: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class Scopes(str, Enum):
    USER = "user"
    ADMIN = "admin"
    ROOT = "root"


SCOPES = {Scopes.USER.value: "Read information about the current user"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token", scopes=SCOPES)
