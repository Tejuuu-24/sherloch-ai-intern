# import json
# from pathlib import Path

# # Get the data folder path
# DATA_DIR = Path(__file__).parent.parent / "data"


# def identify_candidate():
#     """
#     Reads participant and candidate data,
#     calculates confidence score,
#     and returns the most likely candidate.
#     """

#     # Read participants
#     with open(DATA_DIR / "participants.json", "r") as f:
#         participants = json.load(f)

#     # Read candidate profile
#     with open(DATA_DIR / "candidate.json", "r") as f:
#         candidate = json.load(f)

#     # Find highest speaking duration
#     highest_speaking = max(
#         participant["speaking_duration"] for participant in participants
#     )

#     best_candidate = None
#     best_score = -1
#     best_evidence = []

#     # Loop through every participant
#     for participant in participants:

#         score = 0
#         evidence = []

#         # Rule 1 - Display name match
#         if participant["display_name"].lower() == candidate["name"].lower():
#             score += 30
#             evidence.append("Display name matched")

#         # Rule 2 - Email match
#         if participant["email"].lower() == candidate["email"].lower():
#             score += 30
#             evidence.append("Candidate email matched")

#         # Rule 3 - Camera ON
#         if participant["camera"]:
#             score += 10
#             evidence.append("Camera active")

#         # Rule 4 - Highest speaking duration
#         if participant["speaking_duration"] == highest_speaking:
#             score += 20
#             evidence.append("Highest speaking duration")

#         # Rule 5 - Transcript contains candidate name
#         if candidate["name"].lower() in participant["transcript"].lower():
#             score += 10
#             evidence.append("Introduced themselves")

#         # Save highest scoring participant
#         if score > best_score:
#             best_score = score
#             best_candidate = participant
#             best_evidence = evidence

#     return {
#         "candidate": best_candidate["display_name"],
#         "confidence": best_score,
#         "evidence": best_evidence
#     }

# import json
# from pathlib import Path
# from typing import Dict, List

# # -----------------------------
# # Configuration
# # -----------------------------
# DATA_DIR = Path(__file__).parent.parent / "data"

# NAME_SCORE = 30
# EMAIL_SCORE = 30
# CAMERA_SCORE = 10
# SPEAKING_SCORE = 20
# TRANSCRIPT_SCORE = 10


# def load_json(filename: str):
#     """Load JSON file from the data folder."""
#     with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
#         return json.load(file)


# def identify_candidate() -> Dict:
#     """
#     Identifies the most likely interview candidate using
#     multiple evidence signals.
#     """

#     # -----------------------------
#     # Load data
#     # -----------------------------
#     participants = load_json("participants.json")
#     candidate = load_json("candidate.json")

#     # Handle empty participant list
#     if not participants:
#         return {
#             "candidate": None,
#             "confidence": 0,
#             "evidence": [],
#             "reason": "No participants found."
#         }

#     # Highest speaking duration
#     highest_speaking = max(
#         participant["speaking_duration"]
#         for participant in participants
#     )

#     best_candidate = None
#     best_score = -1
#     best_evidence: List[str] = []

#     # -----------------------------
#     # Score every participant
#     # -----------------------------
#     for participant in participants:

#         score = 0
#         evidence = []

#         # Display Name Match
#         if participant["display_name"].strip().lower() == candidate["name"].strip().lower():
#             score += NAME_SCORE
#             evidence.append("Display name matched")

#         # Email Match
#         if participant["email"].strip().lower() == candidate["email"].strip().lower():
#             score += EMAIL_SCORE
#             evidence.append("Candidate email matched")

#         # Camera Status
#         if participant["camera"]:
#             score += CAMERA_SCORE
#             evidence.append("Camera active")

#         # Highest Speaking Duration
#         if participant["speaking_duration"] == highest_speaking:
#             score += SPEAKING_SCORE
#             evidence.append("Highest speaking duration")

#         # Transcript Match
#         if candidate["name"].lower() in participant["transcript"].lower():
#             score += TRANSCRIPT_SCORE
#             evidence.append("Introduced themselves")

#         # Save best candidate
#         if score > best_score:
#             best_score = score
#             best_candidate = participant
#             best_evidence = evidence

#     # -----------------------------
#     # Generate Explanation
#     # -----------------------------
#     reason = (
#         f"{best_candidate['display_name']} was selected because "
#         + ", ".join(best_evidence).lower()
#         + "."
#     )

#     return {
#         "candidate": best_candidate["display_name"],
#         "confidence": best_score,
#         "evidence": best_evidence,
#         "reason": reason
#     }

from app.services.participant_service import (
    load_candidate,
    load_participants,
)

from app.services.metadata_service import metadata_score
from app.services.transcript_service import transcript_score
from app.services.vision_service import vision_score
from app.services.llm_service import generate_reason

# Maximum possible score
MAX_SCORE = 120


def identify_candidate():
    """
    Identifies the most likely interview candidate by combining
    metadata, transcript, and vision-based evidence.
    """

    # Load data
    participants = load_participants()
    candidate = load_candidate()

    # Handle empty participant list
    if not participants:
        return {
            "candidate": None,
            "confidence": 0,
            "evidence": [],
            "reason": "No participants found."
        }

    # Find highest speaking duration
    highest_speaking = max(
        participant["speaking_duration"]
        for participant in participants
    )

    best_candidate = None
    best_score = -1
    best_evidence = []

    # Evaluate every participant
    for participant in participants:

        score = 0
        evidence = []

        # -----------------------------
        # Metadata Analysis
        # -----------------------------
        metadata_points, metadata_evidence = metadata_score(
            participant,
            candidate
        )

        score += metadata_points
        evidence.extend(metadata_evidence)

        # -----------------------------
        # Speaking Duration
        # -----------------------------
        if participant["speaking_duration"] == highest_speaking:
            score += 20
            evidence.append("Highest speaking duration")

        # -----------------------------
        # Transcript Analysis
        # -----------------------------
        transcript_points, transcript_evidence = transcript_score(
            participant     
        )

        score += transcript_points
        evidence.extend(transcript_evidence)

        # -----------------------------
        # Vision Analysis
        # -----------------------------
        vision_points, vision_evidence = vision_score(
            participant["video"]
        )

        score += vision_points
        evidence.extend(vision_evidence)

        # -----------------------------
        # Save Best Candidate
        # -----------------------------
        if score > best_score:
            best_score = score
            best_candidate = participant
            best_evidence = evidence

    # Convert raw score into percentage
    confidence = round((best_score / MAX_SCORE) * 100)

    # Generate explanation using Gemini
    reason = generate_reason(
        best_candidate["display_name"],
        best_evidence
    )

    return {
        "candidate": best_candidate["display_name"],
        "confidence": confidence,
        "evidence": best_evidence,
        "reason": reason
    }