from ai.llm_client import OllamaClient
import asyncio

async def test_llm():
    client = OllamaClient()
    if client.check_health():
        print("Ollama is reachable.")
        response = await client.generate_response("Say hello in one word.")
        print(f"LLM Response: {response}")
    else:
        print("Ollama is NOT reachable.")

if __name__ == "__main__":
    asyncio.run(test_llm())
