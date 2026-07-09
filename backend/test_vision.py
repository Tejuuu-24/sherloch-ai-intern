from app.services.vision_service import vision_score

score, evidence = vision_score("participant1.mp4")

print("Vision Score:", score)
print("Evidence:", evidence)