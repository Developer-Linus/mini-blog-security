#Pydantic models
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None
class UserCreate(UserBase):
    password: str
class UserInDB(UserBase):
    hashed_password: str
    disabled: bool = False
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: str | None = None
class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    owner: str