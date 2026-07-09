NAME_SCORE = 30
EMAIL_SCORE = 30
CAMERA_SCORE = 10


def metadata_score(participant, candidate):

    score = 0
    evidence = []

    # Display Name Match
    if (
        participant["display_name"].lower()
        == candidate["name"].lower()
    ):
        score += NAME_SCORE
        evidence.append("Display name matched")

    # Email Match
    if (
        participant["email"].lower()
        == candidate["email"].lower()
    ):
        score += EMAIL_SCORE
        evidence.append("Candidate email matched")

    # Camera Status
    if participant.get("camera", False):
        score += CAMERA_SCORE
        evidence.append("Camera active")

    return score, evidence