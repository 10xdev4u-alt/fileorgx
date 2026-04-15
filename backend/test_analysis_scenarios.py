import asyncio
from ai.analyzer import FileAnalyzer

async def test_scenarios():
    analyzer = FileAnalyzer()
    
    scenarios = [
        {
            "metadata": {"name": "screenshot_2024.png", "file_type": "image/png", "size": 500000, "path": "/Downloads/screenshot_2024.png"},
            "content": "A picture showing a React code editor with errors."
        },
        {
            "metadata": {"name": "starbucks_receipt.pdf", "file_type": "application/pdf", "size": 150000, "path": "/Downloads/starbucks.pdf"},
            "content": "Starbucks Coffee #1234. Total: $15.50. Date: 2024-04-15."
        }
    ]

    for i, s in enumerate(scenarios):
        print(f"\nTesting Scenario {i+1}: {s['metadata']['name']}")
        result = await analyzer.analyze_file(s['metadata'], s['content'])
        print(f"Analysis Result: {result}")

if __name__ == "__main__":
    # This will only work if Ollama is running and has the model
    try:
        asyncio.run(test_scenarios())
    except Exception as e:
        print(f"Error running test: {e}")
