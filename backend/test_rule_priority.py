from core.rule_engine import RuleEngine
from database.models import Rule

def test_rule_priority():
    engine = RuleEngine()
    
    # Rules with overlapping conditions but different priorities
    rules = [
        Rule(name="Low Priority Move", condition_type="extension", condition_value=".txt", action_type="move", action_value="Archive", priority=1),
        Rule(name="High Priority Move", condition_type="extension", condition_value=".txt", action_type="move", action_value="Important", priority=10),
        Rule(name="Medium Priority Tag", condition_type="extension", condition_value=".txt", action_type="tag", action_value="Text", priority=5)
    ]
    engine.load_rules_from_db(rules)
    
    # Test match
    meta = {"name": "test.txt", "extension": ".txt"}
    matches = engine.match(meta)
    
    print(f"Matched rules in order of priority:")
    for r in matches:
        print(f"- {r.name} (Priority: {r.priority})")
    
    assert matches[0].name == "High Priority Move"
    assert matches[1].name == "Medium Priority Tag"
    assert matches[2].name == "Low Priority Move"

if __name__ == "__main__":
    test_rule_priority()
