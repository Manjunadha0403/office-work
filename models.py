from sqlalchemy import ForeignKey, Boolean, Column, Integer, String, LargeBinary, Date
from sqlalchemy.orm import relationship,backref
from Database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    user_phone = Column(Integer, unique=True, index=True)
    user_gender = Column(String)
    user_DOB = Column(Date)  # Use Date type for date of birth
    marital_status = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)

class Post(Base):
    __tablename__ = "posts"  # Use lowercase for table names
    post_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    user_post_data = Column(LargeBinary)  # Change column name to user_post_data
    is_active = Column(Boolean, default=True)
    user = relationship("User", backref=backref("posts"),foreign_keys=[user_id])
