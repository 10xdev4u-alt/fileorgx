import asyncio
from core.batch_processor import BatchProcessor
from core.rule_engine import RuleEngine
from core.organizer import FileOrganizer
from database.models import Rule
import os
import shutil

async def test_batch():
    # Setup
    test_dir = "./test_batch_dir"
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, "test1.pdf"), "w") as f: f.write("test")
    with open(os.path.join(test_dir, "test2.txt"), "w") as f: f.write("test")
    
    rules = [
        Rule(name="PDFs", condition_type="extension", condition_value=".pdf", action_type="move", action_value="PDFs", priority=1)
    ]
    engine = RuleEngine()
    engine.load_rules_from_db(rules)
    organizer = FileOrganizer(base_path="./organized_batch")
    
    processor = BatchProcessor(engine, organizer)
    results = await processor.process_directory(test_dir, dry_run=False)
    
    print(f"Batch results: {results}")
    
    # Cleanup
    shutil.rmtree(test_dir)
    shutil.rmtree("./organized_batch")

if __name__ == "__main__":
    asyncio.run(test_batch())
