TRANSCRIPT_SCORE = 10

def transcript_score(participant, candidate):

    score = 0
    evidence = []

    transcript = participant["transcript"].lower()

    if candidate["name"].lower() in transcript:

        score += TRANSCRIPT_SCORE
        evidence.append("Introduced themselves")

    return score, evidence