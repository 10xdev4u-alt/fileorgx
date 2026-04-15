from sqlalchemy.orm import Session
from database.models import File, Tag
from utils.logger import logger

class TagManager:
    """Manages tag creation and assignment for files."""
    
    def __init__(self, db: Session):
        self.db = db

    def get_or_create_tag(self, tag_name, category=None):
        """Gets an existing tag or creates a new one."""
        tag_name = tag_name.lower().strip()
        tag = self.db.query(Tag).filter(Tag.name == tag_name).first()
        
        if not tag:
            tag = Tag(name=tag_name, category=category)
            self.db.add(tag)
            self.db.commit()
            self.db.refresh(tag)
            logger.info(f"Created new tag: {tag_name}")
            
        return tag

    def assign_tags_to_file(self, file_id, tag_names, category=None):
        """Assigns a list of tags to a file."""
        file = self.db.query(File).filter(File.id == file_id).first()
        if not file:
            logger.error(f"File not found: {file_id}")
            return False

        current_tags = {t.name for t in file.tags}
        
        for name in tag_names:
            if name.lower().strip() not in current_tags:
                tag = self.get_or_create_tag(name, category)
                file.tags.append(tag)
        
        self.db.commit()
        return True
