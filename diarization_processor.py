from pyannote.audio import Pipeline
import os

# Local diarization (no token required if model cached)
PIPELINE = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=False
)

def diarize(audio_path):
    diarization = PIPELINE(audio_path)
    segments = []

    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "start": round(turn.start, 2),
            "end": round(turn.end, 2),
            "speaker": speaker
        })

    return segments
