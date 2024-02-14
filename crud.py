from sqlalchemy.orm import Session
from schemas import  (UserCreate,UserUpdate,PostCreate,CommentCreate)
from models import (Post_comments, User,Post)
from fastapi import UploadFile
# User CRUD operations
def create_users(db: Session, user: UserCreate):
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

def get_user_posts(db: Session, user_id: int):
    return (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .all()
    )

# CRUD operations for Post

def create_posts(db: Session, post_create: PostCreate, user_id: int):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        db_post = Post(**post_create.dict(),user=user)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post
    else:
        return None
def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.post_id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.post_id == post_id).first()

def get_posts_comments(db: Session, post_id: int):
    return (
        db.query(Post_comments)
        .filter(Post_comments.post_id == post_id)
        .all()
    )

#CRUD POST_COMMENTS
def create_comments(db: Session, comment_create: CommentCreate, post_id: int, user_id: int):
    user = db.query(User).filter(User.user_id == user_id).first()
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if user and post:
        db_comment = Post_comments(**comment_create.dict(), user=user, post=post)
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    else:
        return None

def get_comment(db: Session, comment_id: int):
    return db.query(Post_comments).filter(Post_comments.comment_id == comment_id).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post_comments).offset(skip).limit(limit).all()

def delete_comment(db: Session, post_id: int,coment_id:int):
    db_post = db.query(Post).filter(Post.post_id == post_id).first()
    db_comment = get_comment(db,db_post,coment_id)
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment

