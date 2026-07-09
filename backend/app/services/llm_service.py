import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_reason(candidate_name, evidence):

    prompt = f"""
You are an AI interview assistant.

Candidate:
{candidate_name}

Evidence:
{', '.join(evidence)}

Explain in exactly 2 professional sentences why this person is the most likely interview candidate.

Do not mention confidence scores.
"""

    response = model.generate_content(prompt)

    return response.text