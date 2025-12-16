from datetime import datetime
from typing import Dict

def generate_report(data: Dict) -> Dict:
    return {
        "metadata": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "system": "QC_Automation_Prototype"
        },
        "audio": data["audio"],
        "transcription": data["transcription"],
        "procedural_qc": {"violations": data["procedural_qc"]},
        "score_qc": data["score_qc"],
        "summary": {
            "has_violations": bool(data["procedural_qc"]),
            "score_status": data["score_qc"]["status"]
        }
    }
