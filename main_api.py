from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
import schemas
from crud import create_user, get_user, get_users, create_item, get_item, get_items, create_size, create_colour, create_brand

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

# FastAPI routes

# Create User
@app.post("/users/", response_model=schemas.User)
def create_user_route(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

# Get User by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Get All Users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db=db, skip=skip, limit=limit)

# Create Item
@app.post("/items/", response_model=schemas.Item)
def create_item_route(item: schemas.ItemCreate, user_id: int, db: Session = Depends(get_db)):
    return create_item(db=db, item=item, user_id=user_id)

# Get Item by ID
@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Get All Items
@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db=db, skip=skip, limit=limit)

# Create Size
@app.post("/sizes/", response_model=schemas.Size)
def create_size_route(size: schemas.SizeCreate, item_id: int, db: Session = Depends(get_db)):
    return create_size(db=db, size=size, item_id=item_id)

# Create Colour
@app.post("/colours/", response_model=schemas.Colour)
def create_colour_route(colour: schemas.ColourCreate, item_id: int, db: Session = Depends(get_db)):
    return create_colour(db=db, colour=colour, item_id=item_id)

# Create Brand
@app.post("/brands/", response_model=schemas.Brand)
def create_brand_route(brand: schemas.BrandCreate, item_id: int, db: Session = Depends(get_db)):
    return create_brand(db=db, brand=brand, item_id=item_id)
