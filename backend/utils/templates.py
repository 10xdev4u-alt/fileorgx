# Standard folder templates for Smart File Organizer Pro

import os
from utils.logger import logger

FOLDER_TEMPLATES = {
    "Media": ["Photos", "Videos", "Audio", "Raw", "Edits"],
    "Development": ["src", "docs", "tests", "assets", "build"],
    "Finance": ["Receipts", "Invoices", "Statements", "Taxes", "Misc"],
    "Work": ["Projects", "Meetings", "Archive", "Current"],
    "Personal": ["Travel", "Hobbies", "Health", "Home"],
}

def apply_template(base_path, template_name):
    """Creates a standard folder structure from a template."""
    subfolders = FOLDER_TEMPLATES.get(template_name)
    if not subfolders:
        logger.error(f"Template {template_name} not found.")
        return False
    
    try:
        for folder in subfolders:
            path = os.path.join(base_path, folder)
            if not os.path.exists(path):
                os.makedirs(path)
                logger.info(f"Created folder: {path}")
        return True
    except Exception as e:
        logger.error(f"Failed to apply folder template: {e}")
        return False

def get_available_templates():
    """Returns a list of available folder templates."""
    return list(FOLDER_TEMPLATES.keys())
