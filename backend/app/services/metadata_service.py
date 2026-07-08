NAME_SCORE = 30
EMAIL_SCORE = 30
CAMERA_SCORE = 10

def metadata_score(participant, candidate):
    score = 0
    evidence = []

    if participant["display_name"].lower() == candidate["name"].lower():
        score += NAME_SCORE
        evidence.append("Display name matched")

    if participant["email"].lower() == candidate["email"].lower():
        score += EMAIL_SCORE
        evidence.append("Candidate email matched")

    if participant["camera"]:
        score += CAMERA_SCORE
        evidence.append("Camera active")

    return score, evidence