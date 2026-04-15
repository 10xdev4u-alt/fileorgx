import pytesseract
from PIL import Image
from utils.logger import logger
import os

class TesseractOCR:
    """OCR processor using Tesseract."""
    
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image_path):
        """Extracts text from an image file."""
        try:
            if not os.path.exists(image_path):
                logger.error(f"Image path does not exist: {image_path}")
                return None
            
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            logger.error(f"Error during Tesseract OCR: {str(e)}")
            return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        ocr = TesseractOCR()
        print(f"Extracted Text:\n{ocr.extract_text(sys.argv[1])}")
    else:
        print("Usage: python ocr_processor.py <image_path>")
