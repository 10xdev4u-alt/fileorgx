import json
from ai.llm_client import OllamaClient
from ai.prompts import FILE_ANALYSIS_SYSTEM_PROMPT, FILE_ANALYSIS_PROMPT_TEMPLATE
from utils.logger import logger

class FileAnalyzer:
    """Analyzes files using LLM and metadata."""
    
    def __init__(self, client: OllamaClient = None):
        self.client = client or OllamaClient()

    async def analyze_file(self, metadata, content_snippet="No content available."):
        """Analyzes a file and returns organization suggestions."""
        prompt = FILE_ANALYSIS_PROMPT_TEMPLATE.format(
            name=metadata.get('name', 'unknown'),
            file_type=metadata.get('file_type', 'unknown'),
            size=metadata.get('size', 0),
            path=metadata.get('path', 'unknown'),
            content_snippet=content_snippet
        )
        
        response = await self.client.generate_response(
            prompt, 
            system_prompt=FILE_ANALYSIS_SYSTEM_PROMPT
        )
        
        if response:
            try:
                # Clean the response if LLM adds markdown or fluff
                if '```json' in response:
                    response = response.split('```json')[1].split('```')[0].strip()
                elif '```' in response:
                    response = response.split('```')[1].split('```')[0].strip()
                
                return json.loads(response)
            except (json.JSONDecodeError, IndexError) as e:
                logger.error(f"Failed to parse LLM response: {e}")
                return None
        return None
