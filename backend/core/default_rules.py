# Default rule definitions for Smart File Organizer Pro

DEFAULT_RULES = [
    {
        "name": "Move Screenshots",
        "condition_type": "filename_contains",
        "condition_value": "screenshot",
        "action_type": "move",
        "action_value": "Images/Screenshots",
        "priority": 10
    },
    {
        "name": "Tag Receipts",
        "condition_type": "content_contains",
        "condition_value": "receipt",
        "action_type": "tag",
        "action_value": "Finance",
        "priority": 5
    },
    {
        "name": "Organize PDFs",
        "condition_type": "extension",
        "condition_value": ".pdf",
        "action_type": "move",
        "action_value": "Documents",
        "priority": 1
    },
    {
        "name": "Group Source Code",
        "condition_type": "extension",
        "condition_value": ".py",
        "action_type": "move",
        "action_value": "Developer/Projects",
        "priority": 2
    }
]

def get_default_rules():
    """Returns the list of default rules."""
    return DEFAULT_RULES
