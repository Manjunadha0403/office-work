from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,backref
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    user_name = Column(String)
    user_address = Column(String)
    user_ph = Column(Integer)
    password = Column(String)
    is_active = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True,index=True)
    product_name = Column(String)
    product_colour = Column(String)
    product_size = Column(String)
    product_description = Column(String)
    is_active = Column(Boolean, default=True) 

class Shopping(Base):
    __tablename__ = "shopping"
    order_id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    description= Column(String,unique=True,nullable=True)
    shopp= relationship("User",backref=backref("users_shopping"),foreign_keys=[user_id])
    shopping = relationship("Product",backref=backref("product_shopping"),foreign_keys=[product_id])