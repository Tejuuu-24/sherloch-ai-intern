import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_reason(transcript: str):

    prompt = f"""
You are an AI system that identifies the interview candidate in a virtual interview.

You will receive a transcript generated from speech recognition.

Analyze carefully.

Determine whether this participant is the interview candidate.

Look for:

• Self introduction
• Education
• Experience
• Technical projects
• Interview style answers
• Responses to interviewer questions

Do NOT judge technical ability.

Return ONLY valid JSON.

Format:

{{
"is_candidate": true,
"score": 20,
"confidence": 0.96,
"reason":"...",
"evidence":[
"...",
"...",
"..."
]
}}

Transcript:

{transcript}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown if Gemini adds it
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)