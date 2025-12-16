def extract_evidence(transcript):
    evidence = []

    long_turns = [
        s for s in transcript
        if s["role"] == "Examinee" and len(s["text"].split()) > 15
    ]

    if long_turns:
        evidence.append({
            "type": "ability to sustain an exchange",
            "confidence": 0.85
        })

    connected = sum(len(s["text"].split()) for s in transcript if s["role"] == "Examinee")
    if connected > 200:
        evidence.append({
            "type": "connected statements",
            "confidence": 0.80
        })

    return evidence
