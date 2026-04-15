import asyncio
from ai.rule_suggestor import RuleSuggestor

async def test_suggestor():
    suggestor = RuleSuggestor()
    print("Rule suggestor module loaded.")

if __name__ == "__main__":
    asyncio.run(test_suggestor())
