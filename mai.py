from fastapi import FastAPI, File, UploadFile,Depends
from sqlalchemy import Column, LargeBinary, create_engine,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import shutil
import os

# Define the FastAPI app
app = FastAPI()

# Define the SQLAlchemy model
Base = declarative_base()

class YourModel(Base):
    __tablename__ = "your_table"
    id = Column(Integer, primary_key=True)
    user_post_data = Column(LargeBinary, index=True)

# Set up the SQLAlchemy database connection
DATABASE_URL = "sqlite:///./data.db"  # Update this with your database URL
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Create a SessionLocal class to handle database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Define the FastAPI route for file upload
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        
        # Save the file content to the database
        new_entry = YourModel(user_post_data=contents)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        return {"filename": file.filename, "id": new_entry.id}
    finally:
        # Close the file after reading its content
        await file.close()

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4000, reload=True)
