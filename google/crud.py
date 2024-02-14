from sqlalchemy.orm import Session
from models import (User, Product, Shopping)
from schemas import (
    UserCreate, UserUpdate,
    ProductCreate, ProductUpdate,
    ShoppingCreate,ShoppingUpdate)
 
# User CRUD operations
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    for field, value in user_update.dict().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

# Product CRUD operations
def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    for field, value in product_update.dict().items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

# Shopping CRUD operations
def create_shopping(db: Session, shopping: ShoppingCreate):
    db_shopping = Shopping(**shopping.dict())
    db.add(db_shopping)
    db.commit()
    db.refresh(db_shopping)
    return db_shopping

def get_shopping(db: Session, user_id: int, product_id: int):
    return db.query(Shopping).filter(Shopping.user_id == user_id, Shopping.product_id == product_id).first()

def get_shopping(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Shopping).offset(skip).limit(limit).all()

def update_shopping(db: Session, order_id: int, shopping_update: ShoppingUpdate):
    db_shopping= db.query(Shopping).filter(Shopping.order_id == order_id).first()
    db_user=db.query(User).filter(User.id==db_shopping.user_id).first()
    for field, value in shopping_update.dict().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_shopping

def delete_shopping(db: Session,order_id:int):
    db_shopping = db.query(Shopping).filter(Shopping.order_id==order_id).first()
    db.delete(db_shopping)
    db.commit()
    return db_shopping

def get_order(db: Session, user_id: int):
    return (
        db.query(Shopping)
        .filter(Shopping.user_id == user_id)
        .all()
    )
 
def get_orders(db: Session, user_id: int):
    return (
        db.query(Shopping)
        .filter(Shopping.product_id == user_id)
        .all()
    )