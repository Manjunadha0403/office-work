from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'sqlite:///./test.db' with your desired database URL
DATABASE_URL = "sqlite:///./social_media.db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for defining models
Base = declarative_base()
