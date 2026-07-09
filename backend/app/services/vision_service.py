from ultralytics import YOLO
import cv2
from pathlib import Path

# --------------------------------
# Load YOLO model only once
# --------------------------------

model = YOLO("yolov8n.pt")

MEDIA_DIR = Path(__file__).parent.parent / "media"


def vision_score(video_name):
    """
    Detects whether a participant is visible
    throughout the meeting.

    Returns:
        score,
        evidence
    """

    video_path = MEDIA_DIR / video_name

    cap = cv2.VideoCapture(str(video_path))

    total_frames = 0
    detected_frames = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        total_frames += 1

        results = model(frame, verbose=False)

        person_found = False

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                # COCO class 0 = person
                if cls == 0:
                    person_found = True
                    break

        if person_found:
            detected_frames += 1

    cap.release()

    if total_frames == 0:

        return (
            0,
            [
                "Video could not be processed"
            ]
        )

    visibility = (detected_frames / total_frames) * 100

    evidence = [
        f"Participant visible in {visibility:.1f}% of frames"
    ]

    if visibility >= 90:

        score = 20

    elif visibility >= 70:

        score = 15

    elif visibility >= 50:

        score = 10

    elif visibility >= 20:

        score = 5

    else:

        score = 0

    return score, evidence