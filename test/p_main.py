from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from p_crud import (create_user, get_users, get_login, update_user, delete_user
                ,get_post,get_posts,get_user_posts,delete_post)
from p_s import PostCreate, UserCreate, UserUpdate,PostInDB
from p_m import Post,User
from Database import SessionLocal,Base,engine

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

# Create a new user
@app.post("/users",tags=["user"])
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user=user)

# Get all users
@app.get("/users", response_model=List[UserCreate],tags=["user"])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# Get user login for authentication purpose
@app.get("/users/login",tags=["user"])
def user_login(user_email: str, user_password: str, db: Session = Depends(get_db)):
    return get_login(db, user_email, user_password)

# Update user by user_id
@app.put("/users{user_id}",tags=["user"])
def update_user_info(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_update)

# Delete user by user_id
@app.delete("/users{user_id}",tags=["user"])
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)

# CRUD operations for Post
@app.get("/User_post", response_model=list[PostInDB], tags=["user"])
def get_posts(
    user_id: int, db: Session = Depends(get_db)
):
    return get_user_posts(db, user_id)

# Create a new post with file upload
@app.post("/posts",tags=["Posts"])
async def create_upload_file(user_id:int,file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents= await file.read()
        user1=db.query(User).filter(User.user_id==user_id).first()
        post_c = Post(user_post_data=contents,user_id=user1.user_id,is_active=user1.is_active)  
        db.add(post_c)
        db.commit()
        db.refresh(post_c)
        return post_c
    finally:
        # Close the file after reading its content
        await file.close()

        
    
# Get all posts
@app.get("/posts", response_model=List[PostCreate],tags=["Posts"])
def read_all_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_posts(db, skip=skip, limit=limit)

# Get a post by post_id
@app.get("/posts{post_id}", response_model=PostCreate,tags=["Posts"])
def read_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return get_post(db, post_id)

# Delete a post by post_id
@app.delete("/posts{post_id}",tags=["Posts"])
def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)