from core.tagger import TagManager
from database.db import SessionLocal, init_db
from database.models import File

def test_tagger():
    init_db()
    db = SessionLocal()
    
    # Create dummy file if not exists
    test_file = db.query(File).filter(File.path == "dummy.txt").first()
    if not test_file:
        test_file = File(name="dummy.txt", path="dummy.txt")
        db.add(test_file)
        db.commit()
    
    tagger = TagManager(db)
    tagger.assign_tags_to_file(test_file.id, ["AI", "Smart", "Test"], "Automation")
    print(f"Tags for dummy.txt: {[t.name for t in test_file.tags]}")
    
    db.close()

if __name__ == "__main__":
    test_tagger()
