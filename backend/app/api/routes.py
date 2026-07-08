from fastapi import APIRouter
from app.services.confidence_engine import identify_candidate

router = APIRouter()

@router.get("/identify")
def identify():
    return identify_candidate()