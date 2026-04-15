import json
import os
import hashlib
from utils.logger import logger

class FileAnalysisCache:
    """Simple file-based cache for analysis results."""
    
    def __init__(self, cache_dir=".cache/analysis"):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def _get_hash(self, file_path):
        """Generates a hash based on file path and modification time."""
        try:
            mtime = os.path.getmtime(file_path)
            key = f"{file_path}_{mtime}"
            return hashlib.md5(key.encode()).hexdigest()
        except Exception:
            return None

    def get(self, file_path):
        """Retrieves a cached analysis result."""
        h = self._get_hash(file_path)
        if not h: return None
        
        cache_file = os.path.join(self.cache_dir, f"{h}.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error reading cache: {e}")
        return None

    def set(self, file_path, result):
        """Stores an analysis result in the cache."""
        h = self._get_hash(file_path)
        if not h: return
        
        cache_file = os.path.join(self.cache_dir, f"{h}.json")
        try:
            with open(cache_file, 'w') as f:
                json.dump(result, f)
        except Exception as e:
            logger.error(f"Error writing to cache: {e}")
