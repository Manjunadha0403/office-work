from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine,Base
from crud import (
    
    create_product, get_product, update_product, delete_product,
)
from schemas import (
    ProductCreate, ProductUpdate, ProductInDB,
)

router  = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables in the database
Base.metadata.create_all(bind=engine)
# CRUD operations for Product

# Product CRUD operations
@router .post("/products", response_model=ProductInDB, tags=["Product"])
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router .get("/products", response_model=list[ProductInDB], tags=["Product"])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_product(db, skip=skip, limit=limit)

@router .put("/products{product_id}", response_model=ProductInDB, tags=["Product"])
def update_existing_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product_update)

@router .delete("/products{product_id}", response_model=ProductInDB, tags=["Product"])
def delete_existing_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)