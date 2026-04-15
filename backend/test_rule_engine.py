from core.rule_engine import RuleEngine
from database.models import Rule

def test_rule_engine():
    engine = RuleEngine()
    
    # Mock some rules
    rules = [
        Rule(name="PDF Mover", condition_type="extension", condition_value=".pdf", action_type="move", action_value="Documents/PDFs", priority=1),
        Rule(name="Receipt Filter", condition_type="filename_contains", condition_value="receipt", action_type="tag", action_value="Finance", priority=2)
    ]
    engine.load_rules_from_db(rules)
    
    # Test match
    meta = {"name": "coffee_receipt.pdf", "extension": ".pdf", "size": 1000}
    matches = engine.match(meta)
    
    print(f"Matched rules for {meta['name']}: {[r.name for r in matches]}")
    assert len(matches) == 2
    assert matches[0].name == "Receipt Filter" # Higher priority

if __name__ == "__main__":
    test_rule_engine()
