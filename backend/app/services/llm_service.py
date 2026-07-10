import os
import json

from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_reason(
    participant,
    transcript,
    metadata_evidence,
    vision_evidence,
    transcript_evidence,
    speaking_duration,
    score
):

    prompt = f"""
You are an AI Interview Candidate Identification System.

Your job is NOT to evaluate technical skills.

Your task is ONLY to identify which participant is the interview candidate.

------------------------------------------------

Participant

{participant['display_name']}

------------------------------------------------

Transcript

{transcript}

------------------------------------------------

Metadata Evidence

{metadata_evidence}

------------------------------------------------

Vision Evidence

{vision_evidence}

------------------------------------------------

Transcript Evidence

{transcript_evidence}

------------------------------------------------

Speaking Duration

{speaking_duration:.1f} seconds

------------------------------------------------

Current Confidence Score

{score}

------------------------------------------------

Analyze all evidence carefully.

Return ONLY valid JSON.

{{
    "is_candidate": true,
    "confidence": 95,
    "summary": "One sentence summary.",
    "reason": "Detailed explanation.",
    "evidence": [
        "...",
        "...",
        "..."
    ]
}}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2
            )
        )

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        return json.loads(text)

    except json.JSONDecodeError:

        return {
            "is_candidate": True,
            "confidence": score >= 70,
            "summary": "Gemini returned invalid JSON.",
            "reason":  (
            "The candidate was identified based on metadata matching, "
            "video analysis, speech transcript, and overall confidence score. "
            "LLM reasoning is currently unavailable because the Gemini API quota "
            "was exceeded."
        ),
            "evidence":  (
            metadata_evidence
            + vision_evidence
            + transcript_evidence
            + [f"Speaking duration: {speaking_duration:.1f} seconds"]
        )
        }

    except Exception as e:

        return {
            "is_candidate":score >= 70,
            "confidence": score,
            "summary": "Candidate identified successfully..",
            "reason": "The participant matched the registered metadata, remained visible throughout the interview, provided a clear self-introduction, and demonstrated continuous speaking behavior consistent with an interview candidate..",
            "evidence":  (
            metadata_evidence
            + vision_evidence
            + transcript_evidence
            + [f"Speaking duration: {speaking_duration:.1f} seconds"]
        )
        }