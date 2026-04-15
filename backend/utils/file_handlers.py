import os
from utils.logger import logger

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    import docx
except ImportError:
    docx = None

class FileHandler:
    """Base class for extracting text from various file formats."""
    
    @staticmethod
    def extract_text_from_pdf(file_path):
        """Extracts text from a PDF file."""
        if not PdfReader:
            logger.warning("pypdf not installed. Skipping PDF text extraction.")
            return None
        try:
            reader = PdfReader(file_path)
            text = ""
            # Extract from first few pages to keep it fast
            for page in reader.pages[:5]:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            logger.error(f"Error extracting PDF: {str(e)}")
            return None

    @staticmethod
    def extract_text_from_docx(file_path):
        """Extracts text from a DOCX file."""
        if not docx:
            logger.warning("python-docx not installed. Skipping DOCX extraction.")
            return None
        try:
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        except Exception as e:
            logger.error(f"Error extracting DOCX: {str(e)}")
            return None

    @staticmethod
    def extract_text_from_code(file_path):
        """Extracts text from code/text files."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Read first 2KB for context
                return f.read(2048).strip()
        except Exception as e:
            logger.error(f"Error reading code file: {str(e)}")
            return None

def get_content_extractor(file_type, extension):
    """Returns the appropriate extraction method based on file type."""
    if extension == '.pdf':
        return FileHandler.extract_text_from_pdf
    elif extension in ['.docx', '.doc']:
        return FileHandler.extract_text_from_docx
    elif extension in ['.txt', '.py', '.js', '.ts', '.md', '.json', '.html', '.css']:
        return FileHandler.extract_text_from_code
    return None
