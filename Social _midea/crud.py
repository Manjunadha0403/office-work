# crud.py
from sqlalchemy.orm import Session
from models import User, Post
from schemas import UserCreate, UserUpdate, PostCreate
from fastapi import UploadFile

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

# async def create_post(db: Session, post_create: PostCreate, post1: UploadFile):
#     # Assuming `Post` model has a relationship with `User` and `PostCreate`
#     try:
#         contents= await post1.read()
#         post_c = Post(**post_create.dict(),user_post_data=contents)  
#         db.add(post_c)
#         db.commit()
#         db.refresh(post_c)
#         return post_c
#     finally:
#         return None
    
def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.post_id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
