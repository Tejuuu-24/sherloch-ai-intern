from app.services.llm_service import generate_reason

sample = """
Good morning.

My name is Tejaswini Sanam.

Thank you for giving me this opportunity.

I am a final-year AI and ML student.
"""

print(generate_reason(sample))