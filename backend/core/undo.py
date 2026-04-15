import os
import shutil
from sqlalchemy.orm import Session
from database.models import ActionHistory
from utils.logger import logger

class UndoManager:
    """Manages the undo stack and reversals of file operations."""
    
    def __init__(self, db: Session):
        self.db = db

    def record_action(self, file_id, action_type, src, dest):
        """Records an action in the history for potential undo."""
        history = ActionHistory(
            file_id=file_id,
            action_type=action_type,
            src_path=src,
            dest_path=dest
        )
        self.db.add(history)
        self.db.commit()
        return history.id

    def undo_action(self, action_id):
        """Reverses a previously executed action."""
        action = self.db.query(ActionHistory).filter(ActionHistory.id == action_id).first()
        if not action or action.is_undone:
            return False

        try:
            if action.action_type == 'move' or action.action_type == 'rename':
                # Move back from dest to src
                if os.path.exists(action.dest_path):
                    os.rename(action.dest_path, action.src_path)
                    action.is_undone = 1
                    self.db.commit()
                    logger.info(f"Undid {action.action_type}: {action.dest_path} -> {action.src_path}")
                    return True
            elif action.action_type == 'copy':
                # Delete the copy
                if os.path.exists(action.dest_path):
                    os.remove(action.dest_path)
                    action.is_undone = 1
                    self.db.commit()
                    return True
        except Exception as e:
            logger.error(f"Failed to undo action {action_id}: {e}")
            
        return False
