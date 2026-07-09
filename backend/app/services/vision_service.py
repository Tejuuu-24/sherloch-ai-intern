from ultralytics import YOLO
import cv2
from pathlib import Path

# -----------------------------
# Load YOLO Model
# -----------------------------
model = YOLO("yolov8n.pt")

MEDIA_DIR = Path(__file__).parent.parent / "media"


def vision_score(video_name):
    """
    Detects whether a participant is visible throughout the meeting.

    Returns:
        score (int)
        evidence (list)
    """

    video_path = MEDIA_DIR / video_name

    cap = cv2.VideoCapture(str(video_path))

    total_frames = 0
    detected_frames = 0

    confidence_sum = 0
    confidence_count = 0

    max_people = 0

    frame_number = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame_number += 1

        # Process every 10th frame
        if frame_number % 10 != 0:
            continue

        total_frames += 1

        results = model.predict(frame, verbose=False)

        people_in_frame = 0

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                # COCO Class 0 = Person
                if cls == 0:

                    people_in_frame += 1

                    confidence_sum += float(box.conf[0])

                    confidence_count += 1

        if people_in_frame > 0:
            detected_frames += 1

        max_people = max(max_people, people_in_frame)

    cap.release()

    if total_frames == 0:
        return (
            0,
            [
                "Video could not be processed"
            ]
        )

    visibility = (detected_frames / total_frames) * 100

    if confidence_count == 0:
        avg_confidence = 0
    else:
        avg_confidence = confidence_sum / confidence_count

    score = 0

    if visibility >= 90:
        score += 15

    elif visibility >= 70:
        score += 10

    elif visibility >= 50:
        score += 5

    if avg_confidence >= 0.90:
        score += 5

    evidence = [
        f"Participant visible in {visibility:.1f}% of sampled frames",
        f"Average detection confidence: {avg_confidence:.2f}"
    ]

    if max_people == 1:
        evidence.append("Single participant detected")

    elif max_people > 1:
        evidence.append("Multiple participants detected")

    return score, evidence