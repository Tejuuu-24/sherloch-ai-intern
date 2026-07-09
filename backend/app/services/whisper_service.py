from faster_whisper import WhisperModel
from pathlib import Path

# -----------------------------
# Load Whisper Model
# -----------------------------

# tiny = fastest
# base = recommended
# small = better accuracy

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

MEDIA_DIR = Path(__file__).parent.parent / "media"

TRANSCRIPT_DIR = Path(__file__).parent.parent / "transcripts"

TRANSCRIPT_DIR.mkdir(exist_ok=True)


def generate_transcript(video_name):
    """
    Converts speech from a video into text.

    Returns:
        transcript (str)
    """

    video_path = MEDIA_DIR / video_name

    if not video_path.exists():

        return ""

    segments, info = model.transcribe(
        str(video_path),
        beam_size=5
    )

    transcript = ""

    for segment in segments:

        transcript += segment.text + " "

    transcript = transcript.strip()

    output_file = TRANSCRIPT_DIR / (
        Path(video_name).stem + ".txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(transcript)

    return transcript