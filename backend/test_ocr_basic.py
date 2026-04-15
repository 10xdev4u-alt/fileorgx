from ai.ocr_processor import TesseractOCR
import os

# Basic test for OCR (will fail if Tesseract is not installed)
def test_ocr():
    ocr = TesseractOCR()
    print("OCR module loaded. Check for Tesseract installation if tests fail.")

if __name__ == "__main__":
    test_ocr()
