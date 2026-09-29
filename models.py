from datetime import datetime
from pydantic import BaseModel, Field


class Incident(BaseModel):
    incident_id: str | None = None
    machine_id: str
    machine_type: str
    symptoms: list[str] = Field(min_length=1)
    measurements: dict[str, float | str] = Field(default_factory=dict)
    environment: list[str] = Field(default_factory=list)
    description: str
    timestamp: datetime | None = None


class ExperienceOutcome(BaseModel):
    incident_id: str
    diagnosis: str
    intervention: str
    outcome: str
    lesson: str = ""


class DiagnosisRequest(BaseModel):
    incident: Incident
    budget: str = "mid"


class DiagnosisResponse(BaseModel):
    diagnosis: str
    evidence: list[str] = Field(default_factory=list)
    recommendation: str
    confidence_note: str
    raw_reasoning: str
