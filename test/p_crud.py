from sqlalchemy.orm import Session
from fastapi import UploadFile
from p_s import PostCreate, UserCreate, UserUpdate,PostComments
from p_m import Post, User

# User CRUD operations

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_login(db: Session, user_email: str, user_password: str):
    return db.query(User).filter(User.email == user_email, User.password == user_password).first()

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        for field, value in user_update.dict().items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.post_id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()