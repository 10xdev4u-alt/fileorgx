import pytesseract
import easyocr
from PIL import Image
from utils.logger import logger
import os
import numpy as np

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

class EasyOCRProcessor:
    """OCR processor using EasyOCR."""
    
    def __init__(self, languages=['en']):
        self.reader = easyocr.Reader(languages)

    def extract_text(self, image_path):
        """Extracts text from an image file."""
        try:
            if not os.path.exists(image_path):
                return None
            
            results = self.reader.readtext(image_path)
            text = " ".join([res[1] for res in results])
            return text.strip()
        except Exception as e:
            logger.error(f"Error during EasyOCR: {str(e)}")
            return None

class OCRManager:
    """Manages multiple OCR engines with fallback logic."""
    
    def __init__(self):
        self.tesseract = TesseractOCR()
        self._easyocr = None

    @property
    def easyocr(self):
        if self._easyocr is None:
            self._easyocr = EasyOCRProcessor()
        return self._easyocr

    def extract_text(self, image_path):
        """Extracts text trying Tesseract first, then EasyOCR."""
        text = self.tesseract.extract_text(image_path)
        
        if not text or len(text.strip()) < 5:
            logger.info("Tesseract failed or returned low-quality text, trying EasyOCR...")
            text = self.easyocr.extract_text(image_path)
            
        return text

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        ocr = TesseractOCR()
        print(f"Extracted Text:\n{ocr.extract_text(sys.argv[1])}")
    else:
        print("Usage: python ocr_processor.py <image_path>")
