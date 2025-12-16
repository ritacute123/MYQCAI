import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULEBOOK_PATH = os.path.join(BASE_DIR, "..", "rules", "ilr_framework.json")

def load_ilr_rules():
    with open(RULEBOOK_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_ilr_score(claimed_level, observed_evidence):
    rules = load_ilr_rules()
    level = rules["levels"].get(claimed_level)

    if not level:
        return {
            "claimed_level": claimed_level,
            "decision": "invalid",
            "justification": "Unknown ILR level"
        }

    expected = set(level["expected_evidence"])
    contradictory = set(level["contradictory_evidence"])
    observed = {e["type"] for e in observed_evidence}

    if observed & contradictory:
        decision = "disagree"
    elif observed & expected:
        decision = "agree"
    else:
        decision = "borderline"

    return {
        "claimed_level": claimed_level,
        "decision": decision,
        "matched_evidence": list(observed & expected),
        "conflicting_evidence": list(observed & contradictory),
        "justification": rules["validation_outcomes"][decision]
    }
