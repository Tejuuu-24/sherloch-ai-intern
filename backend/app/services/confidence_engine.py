import json
from pathlib import Path

# Get the data folder path
DATA_DIR = Path(__file__).parent.parent / "data"


def identify_candidate():
    """
    Reads participant and candidate data,
    calculates confidence score,
    and returns the most likely candidate.
    """

    # Read participants
    with open(DATA_DIR / "participants.json", "r") as f:
        participants = json.load(f)

    # Read candidate profile
    with open(DATA_DIR / "candidate.json", "r") as f:
        candidate = json.load(f)

    # Find highest speaking duration
    highest_speaking = max(
        participant["speaking_duration"] for participant in participants
    )

    best_candidate = None
    best_score = -1
    best_evidence = []

    # Loop through every participant
    for participant in participants:

        score = 0
        evidence = []

        # Rule 1 - Display name match
        if participant["display_name"].lower() == candidate["name"].lower():
            score += 30
            evidence.append("Display name matched")

        # Rule 2 - Email match
        if participant["email"].lower() == candidate["email"].lower():
            score += 30
            evidence.append("Candidate email matched")

        # Rule 3 - Camera ON
        if participant["camera"]:
            score += 10
            evidence.append("Camera active")

        # Rule 4 - Highest speaking duration
        if participant["speaking_duration"] == highest_speaking:
            score += 20
            evidence.append("Highest speaking duration")

        # Rule 5 - Transcript contains candidate name
        if candidate["name"].lower() in participant["transcript"].lower():
            score += 10
            evidence.append("Introduced themselves")

        # Save highest scoring participant
        if score > best_score:
            best_score = score
            best_candidate = participant
            best_evidence = evidence

    return {
        "candidate": best_candidate["display_name"],
        "confidence": best_score,
        "evidence": best_evidence
    }