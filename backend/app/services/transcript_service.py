# from app.services.whisper_service import generate_transcript
# from app.services.llm_service import generate_reason


# def transcript_score(participant):

#     transcript = generate_transcript(
#         participant["video"]
#     )

#     result = generate_reason(transcript)

#     evidence = result.get("evidence", [])

#     evidence.append(result["reason"])

#     return result["score"], evidence
from app.services.whisper_service import generate_transcript

# -----------------------------
# Transcript Scoring
# -----------------------------

KEYWORDS = [
    "my name is",
    "i am",
    "experience",
    "project",
    "internship",
    "artificial intelligence",
    "machine learning",
    "python",
    "thank you"
]


def transcript_score(video_name):
    """
    Generates transcript and assigns a score
    based on interview-related keywords.

    Returns:
        transcript
        score
        evidence
    """

    transcript = generate_transcript(video_name)

    transcript_lower = transcript.lower()

    score = 0

    evidence = []

    matched = []

    for keyword in KEYWORDS:

        if keyword in transcript_lower:

            matched.append(keyword)

            score += 2

    if score > 20:
        score = 20

    if matched:

        evidence.append(
            f"Interview keywords detected: {', '.join(matched)}"
        )

    else:

        evidence.append(
            "No interview-related keywords detected"
        )

    return transcript, score, evidence