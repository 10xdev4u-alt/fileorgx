# Standard Tag Taxonomy for Smart File Organizer Pro

DEFAULT_CATEGORIES = {
    "Work": [
        "Project", "Meeting", "Report", "Presentation", "Contact", "Design", "Code"
    ],
    "Personal": [
        "Photo", "Video", "Music", "Letter", "Travel", "Hobby", "Health"
    ],
    "Finances": [
        "Invoice", "Receipt", "Bank Statement", "Tax", "Investment", "Subscription"
    ],
    "Legal": [
        "Contract", "ID", "Insurance", "Certificate", "Permit", "Policy"
    ],
    "Education": [
        "Course", "Assignment", "Exam", "Note", "Resource", "Certificate"
    ],
    "Media": [
        "Image", "Video", "Audio", "Ebook", "Vector", "Screenshot"
    ],
    "Archive": [
        "Backup", "Old", "Log", "Reference", "Misc"
    ]
}

def get_all_categories():
    """Returns a list of all defined categories."""
    return list(DEFAULT_CATEGORIES.keys())

def get_tags_for_category(category):
    """Returns standard tags for a given category."""
    return DEFAULT_CATEGORIES.get(category, [])

def suggest_category_for_tag(tag_name):
    """Attempts to find a category for a given tag."""
    tag_name = tag_name.lower().strip()
    for cat, tags in DEFAULT_CATEGORIES.items():
        if tag_name in [t.lower() for t in tags]:
            return cat
    return "Other"
