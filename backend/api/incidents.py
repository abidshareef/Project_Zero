from fastapi import APIRouter
from backend.models import Incident
from backend.services.hindsight import memory

router = APIRouter()


@router.post("/ingest")
def ingest_incident(incident: Incident):
    incident_id = incident.incident_id or f"{incident.machine_id}-incident"
    content = (
        f"Incident {incident_id}: machine {incident.machine_id} "
        f"({incident.machine_type}). Symptoms: {', '.join(incident.symptoms)}. "
        f"Measurements: {incident.measurements}. "
        f"Environment: {', '.join(incident.environment)}. "
        f"Description: {incident.description}."
    )
    memory.retain(content=content, context="Project Zero incident ingestion")
    return {"status": "stored", "incident_id": incident_id}
