from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.db import get_db, init_db
from database.models import File, Rule
from utils.logger import logger
import traceback
from typing import List

app = FastAPI(title="Smart File Organizer API")

@app.get("/rules/export")
def export_rules(db: Session = Depends(get_db)):
    rules = db.query(Rule).all()
    return [{"name": r.name, "condition_type": r.condition_type, "condition_value": r.condition_value, 
             "action_type": r.action_type, "action_value": r.action_value, "priority": r.priority} for r in rules]

@app.post("/rules/import")
def import_rules(rules: List[dict], db: Session = Depends(get_db)):
    count = 0
    for r_data in rules:
        if not db.query(Rule).filter(Rule.name == r_data['name']).first():
            db.add(Rule(**r_data))
            count += 1
    db.commit()
    return {"imported": count}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    logger.error(traceback.format_exc())
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred.", "message": str(exc)},
    )

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
