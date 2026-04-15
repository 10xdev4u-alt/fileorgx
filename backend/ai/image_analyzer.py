import cv2
import numpy as np
from PIL import Image
from utils.logger import logger

class ImagePreprocessor:
    """Provides image enhancement for better OCR results."""
    
    @staticmethod
    def to_grayscale(image_path):
        """Converts an image to grayscale."""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    @staticmethod
    def thresholding(gray_img):
        """Applies adaptive thresholding to an image."""
        # Clean up image before thresholding
        denoised = cv2.fastNlMeansDenoising(gray_img, None, 10, 7, 21)
        # Apply adaptive thresholding
        thresh = cv2.adaptiveThreshold(
            denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
        return thresh

    @staticmethod
    def remove_noise(gray_img):
        """Removes noise from a grayscale image."""
        return cv2.medianBlur(gray_img, 3)

    def preprocess_for_ocr(self, image_path, output_path=None):
        """Applies full preprocessing pipeline and returns the image."""
        try:
            gray = self.to_grayscale(image_path)
            # Apply noise removal then thresholding
            cleaned = self.remove_noise(gray)
            processed = self.thresholding(cleaned)
            
            if output_path:
                cv2.imwrite(output_path, processed)
            
            return processed
        except Exception as e:
            logger.error(f"Error during image preprocessing: {str(e)}")
            return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        processor = ImagePreprocessor()
        output = "processed_test.png"
        processor.preprocess_for_ocr(sys.argv[1], output)
        print(f"Processed image saved to: {output}")
    else:
        print("Usage: python image_analyzer.py <image_path>")
