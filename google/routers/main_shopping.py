from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base

from crud import (
    create_shopping,update_shopping, get_shopping, delete_shopping,get_orders,get_order
)

from schemas import (
    ShoppingCreate,  ShoppingInDB,ShoppingUpdate
)

router = APIRouter()

Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Shopping CRUD operations
@router.post("/shopping", response_model=ShoppingInDB, tags=["Shopping"])
def create_new_shopping(shopping: ShoppingCreate, db: Session = Depends(get_db)):
    return create_shopping(db, shopping)


@router.get("/shopping", response_model=list[ShoppingInDB], tags=["Shopping"])
def read_shoppings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_shopping(db, skip=skip, limit=limit)

@router.put("/shopping{order_id}", response_model=ShoppingInDB, tags=["Shopping"])
def update_existing_user(order_id: int, shopping_update: ShoppingUpdate, db: Session = Depends(get_db)):
    return update_shopping(db, order_id, shopping_update)


@router.delete("/shopping{order_id}", response_model=ShoppingInDB, tags=["Shopping"])
def delete_existing_shopping(order_id: int, db: Session = Depends(get_db)):
    return delete_shopping(db, order_id=order_id)

#orders
@router.get("/User_orders", response_model=list[ShoppingInDB], tags=["User"])
def get_orders_by_user_product(
    user_id: int, db: Session = Depends(get_db)
):
    return get_order(db, user_id)

@router.get("/Product_orders", response_model=list[ShoppingInDB], tags=["Product"])
def get_orders_by_user_product(
    product_id: int, db: Session = Depends(get_db)
):
    return get_orders(db, product_id)
