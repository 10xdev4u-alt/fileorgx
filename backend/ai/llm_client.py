import ollama
from core.config import settings
from utils.logger import logger

class OllamaClient:
    """Wrapper for Ollama API to interact with local LLMs."""
    
    def __init__(self, model=None, host=None):
        self.model = model or settings.llm_model
        self.client = ollama.Client(host=host or settings.ollama_base_url)

    async def generate_response(self, prompt, system_prompt=None):
        """Generates a response from the LLM."""
        try:
            options = {
                "temperature": 0.2,
                "top_p": 0.9,
            }
            messages = []
            if system_prompt:
                messages.append({'role': 'system', 'content': system_prompt})
            
            messages.append({'role': 'user', 'content': prompt})
            
            response = self.client.chat(
                model=self.model,
                messages=messages,
                options=options
            )
            return response['message']['content']
        except Exception as e:
            logger.error(f"Error generating LLM response: {str(e)}")
            return None

    def check_health(self):
        """Checks if the Ollama server is reachable."""
        try:
            # Simple list command to check connectivity
            self.client.list()
            return True
        except Exception:
            return False

if __name__ == "__main__":
    client = OllamaClient()
    print(f"Ollama Health: {client.check_health()}")
