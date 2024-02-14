from pydantic import BaseModel,EmailStr
from typing import List
class UserCreate(BaseModel):
    email: EmailStr
    user_name: str
    user_address: str
    user_ph: int
    password: str
    is_active: bool

class UserUpdate(UserCreate):
    pass
    

class UserInDB(UserCreate):
    id: int
    email:EmailStr
    

class ProductCreate(BaseModel):
    product_name: str
    product_colour: str
    product_size: str
    product_description: str
    is_active:bool

class ProductUpdate(BaseModel):
    product_name: str
    product_colour: str
    product_size: str
    product_description: str

class ProductInDB(ProductCreate):
    product_id: int
     

class ShoppingCreate(BaseModel):
    user_id: int
    product_id: int
    description:str

class ShoppingUpdate(BaseModel):
    user_address:str
    user_ph:int
    
class ShoppingInDB(ShoppingCreate):
    order_id: int
    shopp:UserCreate
    shopping:ProductCreate

class OrderDetailsCreate(BaseModel):
    user_id: int
    product_id: int
    order_status: str

class OrderDetails(OrderDetailsCreate):
    order_id: int
