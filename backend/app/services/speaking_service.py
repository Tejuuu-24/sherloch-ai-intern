from silero_vad import load_silero_vad, read_audio, get_speech_timestamps

from app.services.audio_service import extract_audio

model = load_silero_vad()


def speaking_score(video_name):

    audio_path = extract_audio(video_name)

    wav = read_audio(str(audio_path), sampling_rate=16000)

    speech = get_speech_timestamps(
        wav,
        model,
        sampling_rate=16000
    )

    total_seconds = 0

    for segment in speech:

        start = segment["start"] / 16000
        end = segment["end"] / 16000

        total_seconds += end - start

    evidence = [
        f"Speaking time: {total_seconds:.1f} seconds"
    ]

    if total_seconds >= 20:

        score = 20

    elif total_seconds >= 15:

        score = 15

    elif total_seconds >= 10:

        score = 10

    elif total_seconds >= 5:

        score = 5

    else:

        score = 0

    return score, evidence