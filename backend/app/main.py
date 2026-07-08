# from fastapi import FastAPI

# app = FastAPI(
#     title="Sherlock AI Candidate Identifier",
#     version="1.0.0"
# )

# @app.get("/")
# def home():
#     return {
#         "message": "Sherlock AI Candidate Identifier Running"
#     }

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Sherlock AI Candidate Identifier",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Sherlock AI Candidate Identifier Running"
    }