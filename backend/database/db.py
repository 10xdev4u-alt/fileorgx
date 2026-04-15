from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Rule
from core.default_rules import get_default_rules

DATABASE_URL = "sqlite:///./file_organizer.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(Rule).count() == 0:
        for r in get_default_rules():
            rule = Rule(**r)
            db.add(rule)
        db.commit()
    db.close()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
