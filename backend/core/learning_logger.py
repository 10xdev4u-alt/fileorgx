from sqlalchemy.orm import Session
from database.models import AIDecision
import json
from utils.logger import logger

class LearningLogger:
    """Logs AI suggestions and user actions for future ML training."""
    
    def __init__(self, db: Session):
        self.db = db

    def log_suggestion(self, file_id, suggestion, confidence):
        """Logs an initial AI suggestion."""
        decision = AIDecision(
            file_id=file_id,
            suggestion=json.dumps(suggestion),
            confidence=int(confidence * 100),
            user_action="pending"
        )
        self.db.add(decision)
        self.db.commit()
        return decision.id

    def log_correction(self, decision_id, action, correction=None):
        """Updates a logged suggestion with user feedback."""
        decision = self.db.query(AIDecision).filter(AIDecision.id == decision_id).first()
        if decision:
            decision.user_action = action
            if correction:
                decision.correction = json.dumps(correction)
            self.db.commit()
            logger.info(f"Logged user {action} for decision {decision_id}")
            return True
        return False
