import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULES_PATH = os.path.join(BASE_DIR, "rules.json")

def run_qc_rules(transcript):
    with open(RULES_PATH, "r", encoding="utf-8") as f:
        rules = json.load(f)

    findings = []

    for rule in rules:
        rule_id = rule.get("id")
        description = rule.get("description", "").lower()

        if "repeat" in description:
            examiner_turns = [s for s in transcript if s["role"] == "Examiner"]
            if len(examiner_turns) > 10:
                findings.append(f"{rule_id}: {rule.get('description')}")

    return findings
