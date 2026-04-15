import json
import re
from utils.logger import logger

class RuleEngine:
    """Processes organization rules and matches them against files."""
    
    def __init__(self):
        self.rules = []

    def load_rules_from_db(self, db_rules):
        """Loads rules from the database model."""
        self.rules = db_rules

    def match(self, file_metadata, content=""):
        """Checks if a file matches any of the loaded rules."""
        matched_rules = []
        for rule in self.rules:
            if self._check_condition(rule, file_metadata, content):
                matched_rules.append(rule)
        
        # Sort by priority
        return sorted(matched_rules, key=lambda x: x.priority, reverse=True)

    def _check_condition(self, rule, metadata, content):
        """Internal helper to check if a specific rule condition is met."""
        c_type = rule.condition_type
        c_val = rule.condition_value
        
        try:
            if c_type == 'extension':
                return metadata.get('extension', '').lower() == c_val.lower()
            elif c_type == 'filename_contains':
                return c_val.lower() in metadata.get('name', '').lower()
            elif c_type == 'content_contains':
                return c_val.lower() in content.lower()
            elif c_type == 'regex':
                return bool(re.search(c_val, content)) or bool(re.search(c_val, metadata.get('name', '')))
            elif c_type == 'size_greater_than':
                return metadata.get('size', 0) > int(c_val)
        except Exception as e:
            logger.error(f"Error checking rule condition: {e}")
            
        return False

    def execute_actions(self, file_path, matched_rules):
        """Executes actions for the matched rules."""
        actions = []
        for rule in matched_rules:
            actions.append({
                "type": rule.action_type,
                "value": rule.action_value,
                "rule_name": rule.name
            })
        return actions
