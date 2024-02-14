from typing import List, Optional
from pydantic import BaseModel
from fastapi import UploadFile

class UserCreate(BaseModel):
    user_name: str
    email: str
    user_phone:int
    user_gender: str
    user_DOB: int
    marital_status:str
    password: str
    is_active: bool

class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    email: Optional[str] = None
    user_phone: Optional[int] = None
    user_gender: Optional[str] = None
    user_DOB: Optional[int] = None
    marital_status: Optional[str] = None
    password: Optional[str] = None

class UserInDB(UserCreate):
    user_id: int
    
class UserOut(UserCreate):
    pass

class PostCreate(BaseModel):
    user_id: int
    user_post: bytes
    is_active: Optional[bool] = True

class PostInDB(PostCreate):
    post_id: int

class PostOut(BaseModel):
    post_id: int
    user_id: int

class PostComments(BaseModel):
    user_id:int
    post_id:int
    post_comments:str

class UserWithPosts(UserOut):
    posts: List[PostOut] = []