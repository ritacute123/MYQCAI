import json
from pathlib import Path
from typing import Dict

ILR_PATH = Path(__file__).parents[1] / "rules" / "ilr_framework.json"

def compare_scores(claimed_level: str, observed_evidence: Dict) -> Dict:
    with open(ILR_PATH, "r", encoding="utf-8") as f:
        framework = json.load(f)

    if claimed_level not in framework["levels"]:
        return {"status": "disagree", "reason": "Invalid ILR level"}

    contradictory = framework["levels"][claimed_level]["contradictory_evidence"]
    text = " ".join(observed_evidence["signals"]).lower()

    for c in contradictory:
        if c.lower() in text:
            return {
                "claimed_level": claimed_level,
                "status": "disagree",
                "justification": framework["validation_outcomes"]["disagree"]
            }

    return {
        "claimed_level": claimed_level,
        "status": "agree",
        "justification": framework["validation_outcomes"]["agree"]
    }
