from app.services.whisper_service import generate_transcript

text = generate_transcript("candidate.mp4")

print()

print("Transcript")

print("--------------------------------")

print(text)