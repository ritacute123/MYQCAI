EXAMINER_CUES = [
    "now part",
    "thank you",
    "i'm going to ask",
    "please start",
    "the next situation",
    "in this part of the test",
    "let me ask you",
    "your topic is",
    "you now have"
]

def infer_roles(segments):
    for seg in segments:
        text = seg["text"].lower()
        if any(cue in text for cue in EXAMINER_CUES):
            seg["role"] = "Examiner"
        else:
            seg["role"] = "Examinee"
    return segments
