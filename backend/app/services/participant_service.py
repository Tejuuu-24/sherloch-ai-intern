import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_participants():
    with open(DATA_DIR / "participants.json", encoding="utf-8") as f:
        return json.load(f)

def load_candidate():
    with open(DATA_DIR / "candidate.json", encoding="utf-8") as f:
        return json.load(f)