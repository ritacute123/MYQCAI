from typing import List, Dict

def infer_roles(diarized_segments: List[Dict]) -> Dict[str, str]:
    speakers = []
    for seg in diarized_segments:
        if seg["speaker"] not in speakers:
            speakers.append(seg["speaker"])

    roles = {}
    if speakers:
        roles[speakers[0]] = "Examiner"
        for s in speakers[1:]:
            roles[s] = "Examinee"

    return roles
