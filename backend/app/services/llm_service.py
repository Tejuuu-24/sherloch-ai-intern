# import os
# import json
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")


# def generate_reason(transcript: str):

#     prompt = f"""
# You are an AI system that identifies the interview candidate in a virtual interview.

# You will receive a transcript generated from speech recognition.

# Analyze carefully.

# Determine whether this participant is the interview candidate.

# Look for:

# • Self introduction
# • Education
# • Experience
# • Technical projects
# • Interview style answers
# • Responses to interviewer questions

# Do NOT judge technical ability.

# Return ONLY valid JSON.

# Format:

# {{
# "is_candidate": true,
# "score": 20,
# "confidence": 0.96,
# "reason":"...",
# "evidence":[
# "...",
# "...",
# "..."
# ]
# }}

# Transcript:

# {transcript}
# """

#     response = model.generate_content(prompt)

#     text = response.text.strip()

#     # Remove markdown if Gemini adds it
#     text = text.replace("```json", "")
#     text = text.replace("```", "")

#     return json.loads(text)
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
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

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)