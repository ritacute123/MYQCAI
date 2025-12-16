from qc_engine.asr.asr_processor import transcribe_audio
from qc_engine.asr.role_mapper import infer_roles
from qc_engine.rules.rule_engine import run_qc_rules
from qc_engine.evidence.extractor import extract_evidence
from qc_engine.evaluation.score_validation import validate_ilr_score

def run_pipeline(audio_path, claimed_level):
    transcript = transcribe_audio(audio_path)
    transcript = infer_roles(transcript)

    procedural_qc = run_qc_rules(transcript)
    evidence = extract_evidence(transcript)
    score_qc = validate_ilr_score(claimed_level, evidence)

    return {
        "transcription": transcript,
        "procedural_qc": {
            "violations": procedural_qc
        },
        "score_qc": score_qc,
        "summary": {
            "has_violations": bool(procedural_qc),
            "score_decision": score_qc["decision"]
        }
    }
