from fastapi import APIRouter
from backend.models import DiagnosisRequest
from backend.services.diagnosis_engine import diagnose

router = APIRouter()


@router.post("")
def run_diagnosis(payload: DiagnosisRequest):
    return diagnose(payload.incident, payload.budget)
