from app.services.whisper_service import generate_transcript
from app.services.llm_service import generate_reason


def transcript_score(participant):

    transcript = generate_transcript(
        participant["video"]
    )

    result = generate_reason(transcript)

    evidence = result.get("evidence", [])

    evidence.append(result["reason"])

    return result["score"], evidence