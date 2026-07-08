VISION_SCORE = 20

def vision_score(participant):

    score = 0
    evidence = []

    if participant["camera"]:

        score += VISION_SCORE

        evidence.append("Face visible during meeting")

    return score, evidence