# schemas.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    user_name: str
    email: EmailStr
    user_phone: int
    user_gender: str
    user_DOB: str
    marital_status: str
    password: str
    is_active: bool = True 

class UserUpdate(UserCreate):
    pass

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    user_id: int
    user_post_data: bytes
    is_active: bool = True

class Post(PostCreate):
    post_id: int

    class Config:
        orm_mode = True
