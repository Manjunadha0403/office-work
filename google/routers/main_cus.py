# Import necessary dependencies and modules
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from crud import (
    create_user, get_user, update_user, delete_user,
   
)
from schemas import (
    UserCreate, UserUpdate, UserInDB,)
  

from typing import List

# Enum for user type
from enum import Enum

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables in the database
Base.metadata.create_all(bind=engine)


# User CRUD operations
@router.post("/users", response_model=UserInDB, tags=["User"])
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user=user)

@router.get("/users", response_model=list[UserInDB], tags=["User"])
def read_users(skip: int = 0,limit: int = 10,  db: Session = Depends(get_db)):
    return get_user(db, skip=skip, limit=limit)

@router.put("/users{user_id}", response_model=UserInDB, tags=["User"])
def update_existing_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_update)

@router.delete("/users{user_id}", response_model=UserInDB, tags=["User"])
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
