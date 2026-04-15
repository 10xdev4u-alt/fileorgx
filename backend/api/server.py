from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import get_db, init_db
from database.models import File
from utils.logger import logger

app = FastAPI(title="Smart File Organizer API")

@app.on_event("startup")
def startup_event():
    logger.info("Starting up Smart File Organizer API")
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart File Organizer Pro API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/files")
def list_files(db: Session = Depends(get_db)):
    files = db.query(File).all()
    return {"files": files}
