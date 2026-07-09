import subprocess
from pathlib import Path

MEDIA_DIR = Path(__file__).parent.parent / "media"
AUDIO_DIR = Path(__file__).parent.parent / "audio"

AUDIO_DIR.mkdir(exist_ok=True)


def extract_audio(video_name):

    video_path = MEDIA_DIR / video_name

    output_audio = AUDIO_DIR / (
        Path(video_name).stem + ".wav"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_path),
        "-ar",
        "16000",
        "-ac",
        "1",
        str(output_audio)
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return output_audio