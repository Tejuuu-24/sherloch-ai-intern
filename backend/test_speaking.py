
from app.services.speaking_service import speaking_score

score, evidence = speaking_score("candidate.mp4")

print("Score:", score)

print(evidence)