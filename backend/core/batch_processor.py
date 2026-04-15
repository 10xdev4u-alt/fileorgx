import os
from core.rule_engine import RuleEngine
from core.organizer import FileOrganizer
from utils.metadata import get_file_metadata
from utils.logger import logger
import asyncio

class BatchProcessor:
    """Handles organizing existing files in bulk."""
    
    def __init__(self, rule_engine: RuleEngine, organizer: FileOrganizer):
        self.rule_engine = rule_engine
        self.organizer = organizer

    async def process_directory(self, directory_path, recursive=False, dry_run=True):
        """Organizes all files in a given directory."""
        results = []
        if not os.path.exists(directory_path):
            logger.error(f"Directory not found: {directory_path}")
            return results

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Skip hidden files
                if file.startswith('.'): continue
                
                res = await self.process_file(file_path, dry_run)
                if res:
                    results.append(res)
            
            if not recursive: break
            
        return results

    async def process_file(self, file_path, dry_run=True):
        """Analyzes and organizes a single file based on rules."""
        metadata = get_file_metadata(file_path)
        if not metadata: return None
        
        matches = self.rule_engine.match(metadata)
        if not matches: return None
        
        # Execute first match (highest priority)
        rule = matches[0]
        if rule.action_type == 'move':
            new_path = self.organizer.move_file(file_path, rule.action_value, dry_run)
            return {
                "file": file_path,
                "action": "move",
                "target": rule.action_value,
                "new_path": new_path,
                "rule": rule.name
            }
        
        return None
