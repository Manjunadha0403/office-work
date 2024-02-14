from pydantic import BaseModel,EmailStr
from typing import List,Optional

class UserCreate(BaseModel):
    user_name:str
    email:EmailStr
    user_phone:int
    user_gender:str
    user_DOB:str
    marital_status:str
    password:str

class UserUpdate(BaseModel):
    user_phone:Optional[int] = None
    user_gender:Optional[str] = None
    user_DOB:Optional[str] =None
    marital_status:Optional[str]=None
    password:Optional[str]=None

class UserInDB(UserCreate):
    user_id:int
    is_active:bool

class PostCreate(BaseModel):
    user_post_data:str
    
class PostInDB(PostCreate):
    post_id:int
    is_active:bool

class CommentCreate(BaseModel):
    comment:str
    
class CommentInDB(CommentCreate):
    comment_id:int
    is_active:bool