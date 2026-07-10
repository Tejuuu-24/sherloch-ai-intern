## Evaluation

1. Testing Method

Tested with:

- Correct participant
- Wrong display name
- Missing email
- Multiple participants
- Observer participant
- Interviewer participant

2. Edge Cases

- Wrong Name

Candidate still detected.

- Missing Email

Vision and transcript compensate.

- Multiple Participants

Confidence ranking identifies best match.

- Candidate Joins Late

Supported after transcript generation.

- Similar Voices

Current limitation.


3. Accuracy

Example:

Metadata

Vision

Transcript

Speaking Duration

combined

↓

Confidence

≈ 86%

The system was tested on sample interview videos and produced consistent candidate identification in those scenarios.

4. Limitations
- No face recognition
- No speaker diarization
- Speaking duration estimated
- Offline video processing
- Gemini quota dependency for explanations

5. Bonus Features

- Multiple Weak Signals

✔ Metadata

✔ Vision

✔ Transcript

✔ Speaking Activity

6. Confidence Score

Weighted confidence calculation.

7. Explainability

- Summary

- Reason

- Evidence

8. Real-Time Updates

Designed so confidence can be recalculated as new data arrives (future enhancement).

9. Continuous Learning

Can be extended to learn from historical interview data.

10. Uncertainty Handling

Falls back to deterministic confidence scoring if the LLM is unavailable.