import json
from ai.llm_client import OllamaClient
from ai.prompts import FILE_ANALYSIS_SYSTEM_PROMPT, FILE_ANALYSIS_PROMPT_TEMPLATE
from ai.ocr_processor import OCRManager
from ai.image_analyzer import ImagePreprocessor
from utils.logger import logger
from utils.cache import FileAnalysisCache
import os

class FileAnalyzer:
    """Analyzes files using LLM, OCR, and metadata."""
    
    def __init__(self, client: OllamaClient = None):
        self.client = client or OllamaClient()
        self.ocr = OCRManager()
        self.preprocessor = ImagePreprocessor()
        self.cache = FileAnalysisCache()

    async def analyze_file(self, file_path, metadata):
        """Analyzes a file and returns organization suggestions."""
        # Check cache first
        cached = self.cache.get(file_path)
        if cached:
            logger.info(f"Using cached analysis for: {file_path}")
            return cached

        content_snippet = "No content available."
        
        # ... (rest of logic) ...
        # After getting result
        if result:
            self.cache.set(file_path, result)
        return result
        
        # Extract content if it's an image
        if metadata.get('file_type', '').startswith('image/'):
            logger.info(f"Extracting OCR text from: {file_path}")
            # Optional: Preprocess image for better OCR
            # processed_path = file_path + ".tmp.png"
            # self.preprocessor.preprocess_for_ocr(file_path, processed_path)
            content_snippet = self.ocr.extract_text(file_path)
        
        prompt = FILE_ANALYSIS_PROMPT_TEMPLATE.format(
            name=metadata.get('name', 'unknown'),
            file_type=metadata.get('file_type', 'unknown'),
            size=metadata.get('size', 0),
            path=metadata.get('path', 'unknown'),
            content_snippet=content_snippet or "No readable text found via OCR."
        )
        
        response = await self.client.generate_response(
            prompt, 
            system_prompt=FILE_ANALYSIS_SYSTEM_PROMPT
        )
        
        if response:
            try:
                if '```json' in response:
                    response = response.split('```json')[1].split('```')[0].strip()
                elif '```' in response:
                    response = response.split('```')[1].split('```')[0].strip()
                
                result = json.loads(response)
                # Ensure confidence exists
                if 'confidence' not in result:
                    result['confidence'] = 0.5
                return result
            except (json.JSONDecodeError, IndexError) as e:
                logger.error(f"Failed to parse LLM response: {e}")
                return None
        return None
