import os
import shutil
from utils.logger import logger
from pathlib import Path

class FileOrganizer:
    """Handles physical file operations like moving and renaming."""
    
    def __init__(self, base_path=None):
        self.base_path = base_path or os.path.expanduser("~/SmartFileOrganizer")
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def _get_unique_path(self, target_path):
        """Generates a unique path by appending a suffix if the file exists."""
        if not os.path.exists(target_path):
            return target_path
        
        path = Path(target_path)
        name = path.stem
        ext = path.suffix
        directory = path.parent
        
        counter = 1
        while True:
            new_name = f"{name}_{counter}{ext}"
            new_path = directory / new_name
            if not new_path.exists():
                return str(new_path)
            counter += 1

    def move_file(self, src_path, target_dir, dry_run=False, on_conflict='rename'):
        """Moves a file with specified conflict resolution strategy."""
        try:
            dest_dir = os.path.join(self.base_path, target_dir)
            file_name = os.path.basename(src_path)
            dest_path = os.path.join(dest_dir, file_name)
            
            if os.path.exists(dest_path):
                if on_conflict == 'skip':
                    logger.info(f"Skipping {src_path} as {dest_path} already exists.")
                    return None
                elif on_conflict == 'rename':
                    dest_path = self._get_unique_path(dest_path)
                elif on_conflict == 'overwrite':
                    logger.warning(f"Overwriting {dest_path}")
                    if not dry_run:
                        os.remove(dest_path)

            if dry_run:
                logger.info(f"[Dry Run] Would move {src_path} to {dest_path}")
                return dest_path

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            shutil.move(src_path, dest_path)
            logger.info(f"Moved {src_path} to {dest_path}")
            return dest_path
        except Exception as e:
            logger.error(f"Error moving file: {e}")
            return None

    def copy_file(self, src_path, target_dir, dry_run=False):
        """Copies a file to a target directory."""
        try:
            dest_dir = os.path.join(self.base_path, target_dir)
            dest_path = os.path.join(dest_dir, os.path.basename(src_path))
            
            if dry_run:
                logger.info(f"[Dry Run] Would copy {src_path} to {dest_path}")
                return dest_path

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            shutil.copy2(src_path, dest_path)
            logger.info(f"Copied {src_path} to {dest_path}")
            return dest_path
        except Exception as e:
            logger.error(f"Error copying file: {e}")
            return None

    def rename_file(self, src_path, new_name, dry_run=False):
        """Renames a file in its current directory."""
        try:
            p = Path(src_path)
            new_path = p.with_name(new_name)
            
            if dry_run:
                logger.info(f"[Dry Run] Would rename {src_path} to {new_path}")
                return str(new_path)

            os.rename(src_path, new_path)
            logger.info(f"Renamed {src_path} to {new_path}")
            return str(new_path)
        except Exception as e:
            logger.error(f"Error renaming file: {e}")
            return None
