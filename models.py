from sqlalchemy import ForeignKey, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship,backref
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    user_phone = Column(Integer, unique=True, index=True)
    user_gender = Column(String)
    user_DOB = Column(String)  # Use Date type for date of birth
    marital_status = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class Post(Base):
    __tablename__ = "posts"  # Use lowercase for table names
    post_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    user_post_data = Column(String)  # Change column name to user_post_data
    is_active = Column(Boolean, default=True)
    user = relationship("User", backref=backref("posts"),foreign_keys=[user_id])


class Post_comments(Base):
    __tablename__ = "Comments"  # Use lowercase for table names
    comment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    post_id = Column(Integer,ForeignKey("posts.post_id"), index=True)
    comment = Column(String)
    is_active = Column(Boolean, default=True)
    user = relationship("User", backref=backref("Comments"),foreign_keys=[user_id])
    post = relationship("Post", backref=backref("Comments"),foreign_keys=[post_id])