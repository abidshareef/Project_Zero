from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.hindsight import memory

router = APIRouter()


class MemoryWrite(BaseModel):
    content: str
    context: str | None = None


class MemoryQuery(BaseModel):
    query: str
    budget: str = "mid"


@router.post("/retain")
def retain(payload: MemoryWrite):
    memory.retain(payload.content, payload.context)
    return {"status": "stored"}


@router.post("/recall")
def recall(payload: MemoryQuery):
    result = memory.recall(payload.query, payload.budget)
    return {
        "results": [
            {
                "text": getattr(item, "text", ""),
                "type": getattr(item, "type", None),
            }
            for item in getattr(result, "results", [])
        ]
    }


@router.post("/reflect")
def reflect(payload: MemoryQuery):
    result = memory.reflect(payload.query, payload.budget)
    return {
        "text": result.text,
        "based_on": [
            getattr(item, "text", "")
            for item in getattr(getattr(result, "based_on", None), "memories", []) or []
        ],
    }
