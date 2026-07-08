from fastapi import FastAPI

app = FastAPI(
    title="Sherlock AI Candidate Identifier",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Sherlock AI Candidate Identifier Running"
    }