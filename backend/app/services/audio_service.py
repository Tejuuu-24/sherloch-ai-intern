from pathlib import Path
import subprocess

MEDIA_DIR = Path(__file__).parent.parent / "media"
AUDIO_DIR = Path(__file__).parent.parent / "audio"

AUDIO_DIR.mkdir(exist_ok=True)


def extract_audio(video_name):
    """
    Extract audio from a video using FFmpeg.
    """

    video_path = MEDIA_DIR / video_name
    audio_path = AUDIO_DIR / (Path(video_name).stem + ".wav")

    if audio_path.exists():
        return audio_path

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_path),
        "-ar",
        "16000",
        "-ac",
        "1",
        str(audio_path)
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return audio_path