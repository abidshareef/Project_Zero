from fastapi import FastAPI
from backend.api.incidents import router as incidents_router
from backend.api.memory import router as memory_router
from backend.api.diagnosis import router as diagnosis_router

app = FastAPI(
    title="Project Zero",
    version="0.1.0",
    description="Experience-based diagnostic intelligence powered by persistent memory.",
)

app.include_router(incidents_router, prefix="/api/incidents", tags=["incidents"])
app.include_router(memory_router, prefix="/api/memory", tags=["memory"])
app.include_router(diagnosis_router, prefix="/api/diagnosis", tags=["diagnosis"])


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "project-zero"}
