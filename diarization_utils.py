from typing import List, Dict

def diarize_audio(segments: List[Dict]) -> List[Dict]:
    diarized = []
    for i, seg in enumerate(segments):
        diarized.append({**seg, "speaker": f"SPEAKER_{i % 2 + 1}"})
    return diarized
