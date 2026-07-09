import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_reason(transcript: str):

    prompt = f"""
You are an AI interview analyzer.

Your task is NOT to evaluate the candidate.

Your task is ONLY to determine whether this participant
appears to be the interview candidate.

Analyze the transcript carefully.

Return ONLY valid JSON.

Format:

{{
"is_candidate": true,
"score": 20,
"reason": "..."
}}

Scoring:

20 = clearly interview candidate

10 = possibly candidate

0 = not candidate

Transcript:

{transcript}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown if Gemini adds it
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)