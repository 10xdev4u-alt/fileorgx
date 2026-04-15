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

    @staticmethod
    def get_image_hash(image_path):
        """Calculates a perceptual hash of an image."""
        try:
            img = cv2.imread(image_path)
            # Downsample and convert to grayscale
            resized = cv2.resize(img, (8, 8), interpolation=cv2.THREADS)
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            # Calculate average intensity
            avg = gray.mean()
            # Generate hash string from binary comparison
            return "".join(["1" if b > avg else "0" for b in gray.flatten()])
        except Exception as e:
            logger.error(f"Error generating image hash: {str(e)}")
            return None

    @staticmethod
    def calculate_similarity(hash1, hash2):
        """Calculates Hamming distance between two hashes."""
        if not hash1 or not hash2 or len(hash1) != len(hash2):
            return 0.0
        
        diffs = sum(1 for a, b in zip(hash1, hash2) if a != b)
        # Higher similarity = lower distance
        return 1.0 - (diffs / len(hash1))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        processor = ImagePreprocessor()
        output = "processed_test.png"
        processor.preprocess_for_ocr(sys.argv[1], output)
        print(f"Processed image saved to: {output}")
    else:
        print("Usage: python image_analyzer.py <image_path>")
