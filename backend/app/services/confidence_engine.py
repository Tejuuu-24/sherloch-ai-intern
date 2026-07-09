from app.services.participant_service import (
    load_candidate,
    load_participants
)

from app.services.metadata_service import metadata_score
from app.services.vision_service import vision_score
from app.services.transcript_service import transcript_score
from app.services.llm_service import generate_reason


def identify_candidate():

    participants = load_participants()

    candidate = load_candidate()

    if not participants:

        return {

            "candidate": None,

            "confidence": 0,

            "reason": "No participants found.",

            "participants": []
        }

    participant_results = []

    # ------------------------------------
    # Process Every Participant
    # ------------------------------------

    for participant in participants:

        total_score = 0

        all_evidence = []

        #################################################
        # Metadata Score
        #################################################

        metadata_points, metadata_evidence = metadata_score(

            participant,

            candidate

        )

        total_score += metadata_points

        all_evidence.extend(metadata_evidence)

        #################################################
        # Vision Score
        #################################################

        vision_points, vision_evidence = vision_score(

            participant["video"]

        )

        total_score += vision_points

        all_evidence.extend(vision_evidence)

        #################################################
        # Whisper Transcript
        #################################################

        transcript, transcript_points, transcript_evidence = transcript_score(

            participant["video"]

        )

        total_score += transcript_points

        all_evidence.extend(transcript_evidence)

        #################################################
        # Speaking Duration Score
        #################################################

        words = transcript.split()

        # Approximate speaking duration
        # Average speaking speed = 2.5 words/sec

        speaking_duration = len(words) / 2.5

        speaking_score = 0

        if speaking_duration >= 20:

            speaking_score = 20

        elif speaking_duration >= 15:

            speaking_score = 15

        elif speaking_duration >= 10:

            speaking_score = 10

        elif speaking_duration >= 5:

            speaking_score = 5

        total_score += speaking_score

        all_evidence.append(
            f"Estimated speaking duration: {speaking_duration:.1f} seconds"
        )

        #################################################
        # Store Result
        #################################################

        participant_results.append(

            {

                "participant": participant,

                "score": total_score,

                "transcript": transcript,

                "metadata_evidence": metadata_evidence,

                "vision_evidence": vision_evidence,

                "transcript_evidence": transcript_evidence,

                "speaking_duration": speaking_duration,

                "all_evidence": all_evidence

            }

        )

    #################################################
    # Sort Participants
    #################################################

    participant_results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    winner = participant_results[0]

        #################################################
    # Gemini Explanation
    #################################################

    llm_result = generate_reason(

        winner["participant"],

        winner["transcript"],

        winner["metadata_evidence"],

        winner["vision_evidence"],

        winner["transcript_evidence"],

        winner["speaking_duration"],

        winner["score"]

    )

    #################################################
    # Final Response
    #################################################

    return {

        "candidate": {

            "display_name": winner["participant"]["display_name"],

            "email": winner["participant"]["email"]

        },

        "confidence": llm_result.get(

            "confidence",

            winner["score"]

        ),

        "is_candidate": llm_result.get(

            "is_candidate",

            True

        ),

        "summary": llm_result.get(

            "summary",

            ""

        ),

        "reason": llm_result.get(

            "reason",

            ""

        ),

        "evidence": llm_result.get(

            "evidence",

            winner["all_evidence"]

        ),

        "participants": [

            {

                "display_name": p["participant"]["display_name"],

                "email": p["participant"]["email"],

                "score": p["score"]

            }

            for p in participant_results

        ]

    }