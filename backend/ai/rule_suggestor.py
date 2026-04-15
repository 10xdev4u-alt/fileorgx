import json
from ai.llm_client import OllamaClient
from utils.logger import logger

RULE_SUGGESTION_PROMPT = """
Analyze the following file movement and suggest a general organization rule.
File: {file_name}
Moved from: {src}
Moved to: {dest}

Suggest a rule in JSON format:
{{
  "name": "Brief rule name",
  "condition_type": "extension | filename_contains | content_contains",
  "condition_value": "...",
  "action_type": "move",
  "action_value": "{dest_folder}",
  "priority": 5
}}
"""

class RuleSuggestor:
    """Suggests rules based on user manual actions."""
    
    def __init__(self, client: OllamaClient = None):
        self.client = client or OllamaClient()

    async def suggest_rule(self, file_name, src, dest):
        """Generates a rule suggestion based on a single move action."""
        dest_folder = dest.split('/')[-2] if '/' in dest else dest
        
        prompt = RULE_SUGGESTION_PROMPT.format(
            file_name=file_name,
            src=src,
            dest=dest,
            dest_folder=dest_folder
        )
        
        response = await self.client.generate_response(prompt)
        if response:
            try:
                # Basic JSON cleaning
                if '```json' in response:
                    response = response.split('```json')[1].split('```')[0].strip()
                return json.loads(response)
            except Exception as e:
                logger.error(f"Error parsing rule suggestion: {e}")
        return None
