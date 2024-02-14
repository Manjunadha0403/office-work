from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from crud import (create_users, get_users, get_login, update_user, delete_user
                ,create_posts,get_post,delete_post
                ,create_comments,get_comment,get_comments,delete_comment
                ,get_user_posts,get_posts_comments)

from schemas import  UserCreate, UserUpdate,UserInDB,PostCreate,PostInDB,CommentCreate,CommentInDB

from database import SessionLocal,Base,engine

app = FastAPI()
# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User CRUD operations
#Create a new user
@app.post("/users",tags=["user"])
def create_user(user: UserCreate,db: Session = Depends(get_db)):
    return create_users(db, user=user)

# Get all users
@app.get("/users", response_model=List[UserInDB],tags=["user"])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# Get user login for authentication purpose
@app.get("/users/login",tags=["user"])
def user_login(user_email: str, user_password: str, db: Session = Depends(get_db)):
    return get_login(db, user_email=user_email,user_password= user_password)

# Update user by user_id
@app.put("/users{user_id}",tags=["user"])
def update_user_info(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id=user_id,user_update= user_update)

# Delete user by user_id
@app.delete("/users{user_id}",tags=["user"])
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db,user_id= user_id)

@app.get("/User_posts", response_model=list[PostInDB], tags=["user"])
def get_postss_by_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_posts(db, user_id=user_id)
#post apis
@app.post("/posts",tags=["Posts"])
def create_post(post: PostCreate,user_id:int, db: Session = Depends(get_db)):
    return create_posts(db, post_create=post,user_id=user_id)


# Get a post by post_id
@app.get("/posts{post_id}", response_model=PostInDB,tags=["Posts"])
def read_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return get_post(db, post_id)

# Delete a post by post_id
@app.delete("/posts{post_id}",tags=["Posts"])
def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)

# Get post by id in db
@app.get("/posts{user_id}", response_model=PostInDB,tags=["Posts"])
def read_post_by_id(user_id: int, db: Session = Depends(get_db)):
  return get_user_posts(db, user_id=user_id)

#Get post by post id
@app.get("/Post_comments", response_model=list[CommentInDB], tags=["Posts"])
def get_comment_by_post(post_id: int, db: Session = Depends(get_db)):
    return get_posts_comments(db, post_id=post_id)

#comment apis
@app.post("/comment",tags=["comment"])
def create_comment(comment: CommentCreate,user_id:int,post_id:int, db: Session = Depends(get_db)):
    return create_comments(db, comment_create=comment,user_id=user_id,post_id=post_id)

# Get all posts
@app.get("/comments", response_model=List[CommentInDB],tags=["comment"])
def read_all_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_comments(db, skip=skip, limit=limit)

# Get a post by post_id
@app.get("/comment{comment_id}", response_model=CommentInDB,tags=["comment"])
def read_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    return get_comment(db, comment_id=comment_id)

# Delete a post by post_id
@app.delete("/comment{comment_id}",tags=["comment"])
def delete_comment_by_id(post_id: int,comment_id:int, db: Session = Depends(get_db)):
    return delete_comment(db, post_id=post_id,comment_id=comment_id)
