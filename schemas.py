from pydantic import BaseModel,EmailStr
from typing import List

class UserCreate(BaseModel):
    user_name:str
    email:EmailStr
    user_phone:int
    user_gender:str
    user_DOB:int
    marital_status:str
    password:str
class UserUpdate(UserCreate):
    pass
class UserInDB(UserCreate):
    user_id:int
    is_active:bool

class PostCreate(BaseModel):
    user_id:int
    is_active:bool
    
class PostInDB(PostCreate):
    post_id:int
    is_active:bool