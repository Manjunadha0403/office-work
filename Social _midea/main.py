# main.py
from fastapi import FastAPI, HTTPException, Depends,UploadFile,File
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas import PostCreate, UserCreate, UserUpdate
from models import User, Post
from crud import (
    create_user,
    update_user,
    delete_user,
    get_user,
    get_posts,
    delete_post,
)
from Database import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.put("/users/{user_id}", response_model=User)
def update_existing_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_update)

@app.delete("/users/{user_id}", response_model=User)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@app.post("/posts", tags=["Posts"], response_model=Post)
async def create_upload_file(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        user1 = db.query(User).filter(User.user_id == user_id).first()
        post_c = Post(user_post_data=contents, user_id=user1.user_id, is_active=user1.is_active)
        db.add(post_c)
        db.commit()
        db.refresh(post_c)
        return post_c
    finally:
        # Close the file after reading its content
        await file.close()


@app.get("/posts/", response_model=list[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_posts(db, skip=skip, limit=limit)

@app.delete("/posts/{post_id}", response_model=Post)
def delete_existing_post(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)
