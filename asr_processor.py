import whisper

MODEL = whisper.load_model("small")

def compute_confidence(text):
    words = len(text.split())
    if words >= 15:
        return 0.90
    elif words >= 7:
        return 0.75
    return 0.60


def transcribe_audio(audio_path):
    result = MODEL.transcribe(audio_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": float(seg["start"]),
            "end": float(seg["end"]),
            "text": seg["text"].strip(),
            "speaker": "UNKNOWN",
            "role": "UNKNOWN",
            "confidence": compute_confidence(seg["text"])
        })

    return segments
