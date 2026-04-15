FILE_ANALYSIS_SYSTEM_PROMPT = """
You are a file organization expert. Your task is to analyze file metadata and content 
to provide concise tags and organization suggestions.
"""

FILE_ANALYSIS_PROMPT_TEMPLATE = """
Analyze the following file and provide:
1. A concise category (e.g., Invoice, Personal, Project, Receipt, Document).
2. A list of 3-5 relevant tags.
3. A suggested folder name.
4. A confidence score between 0.0 and 1.0.

File Metadata:
- Name: {name}
- Type: {file_type}
- Size: {size} bytes
- Path: {path}

File Content/OCR Extract (if any):
{content_snippet}

Output in JSON format:
{{
  "category": "...",
  "tags": ["...", "..."],
  "suggested_folder": "...",
  "confidence": 0.0-1.0
}}
"""

DUPLICATE_DETECTION_SYSTEM_PROMPT = """
You are a duplicate file detective. Compare the metadata and content of two files 
to determine if they are duplicates or different versions of the same file.
"""

DUPLICATE_DETECTION_PROMPT_TEMPLATE = """
Compare these two files:

File A:
- Name: {name_a}
- Size: {size_a}
- Content Snippet: {content_a}

File B:
- Name: {name_b}
- Size: {size_b}
- Content Snippet: {content_b}

Are they:
1. Identical duplicates?
2. Different versions of the same file?
3. Unrelated?

Output in JSON format:
{{
  "relationship": "identical | version | unrelated",
  "confidence": 0.0-1.0,
  "reason": "..."
}}
"""
