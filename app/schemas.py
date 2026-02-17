from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.types import conint


# ----------------------------
# Users
# ----------------------------
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ----------------------------
# Posts
# ----------------------------
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    Post: Post
    Votes: int


    

# ----------------------------
# Token
# ----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


# ----------------------------
# Vote
# ----------------------------
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # type: ignore
