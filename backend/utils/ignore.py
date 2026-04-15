import fnmatch
import os

class IgnoreMatcher:
    """Matches file paths against .gitignore-style patterns."""
    
    def __init__(self, patterns=None):
        self.patterns = patterns or [
            '*.tmp',
            '*.log',
            'node_modules/*',
            '.git/*',
            '__pycache__/*',
            '.DS_Store',
            'Thumbs.db'
        ]

    def should_ignore(self, file_path):
        """Checks if a file should be ignored based on its name or path."""
        file_name = os.path.basename(file_path)
        
        for pattern in self.patterns:
            if fnmatch.fnmatch(file_name, pattern) or fnmatch.fnmatch(file_path, pattern):
                return True
        return False

    def add_pattern(self, pattern):
        """Adds a new ignore pattern."""
        if pattern not in self.patterns:
            self.patterns.append(pattern)
