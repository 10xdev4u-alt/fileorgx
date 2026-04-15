import os
import mimetypes
from datetime import datetime
from pathlib import Path

def get_file_metadata(file_path):
    """Extracts metadata from a file."""
    path = Path(file_path)
    if not path.exists():
        return None

    stats = path.stat()
    
    # MIME type detection
    mime_type, _ = mimetypes.guess_type(file_path)
    
    return {
        "name": path.name,
        "path": str(path.absolute()),
        "size": stats.st_size,
        "file_type": mime_type or "application/octet-stream",
        "created_at": datetime.fromtimestamp(stats.st_ctime),
        "modified_at": datetime.fromtimestamp(stats.st_mtime),
        "extension": path.suffix.lower()
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(get_file_metadata(sys.argv[1]))
    else:
        print("Usage: python metadata.py <file_path>")
