from pathlib import Path

from app.services.llm_service import generate_reason

TRANSCRIPT_DIR = Path(__file__).parent.parent / "transcripts"


def transcript_score(participant):

    transcript_file = TRANSCRIPT_DIR / participant["transcript"]

    with open(transcript_file, "r", encoding="utf-8") as f:
        transcript = f.read()

    result = generate_reason(transcript)

    evidence = [
        result["reason"]
    ]

    return result["score"], evidence