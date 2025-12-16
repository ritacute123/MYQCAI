def recommend_ilr(segments):
    candidate_text = " ".join(
        seg["text"] for seg in segments if seg["role"] == "Candidate"
    )

    word_count = len(candidate_text.split())

    if word_count < 50:
        level = "ILR 1"
    elif word_count < 150:
        level = "ILR 2"
    else:
        level = "ILR 3"

    return {
        "recommended_level": level,
        "word_count": word_count,
        "justification": "Heuristic based on fluency and response length"
    }
