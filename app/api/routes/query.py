from fastapi import APIRouter, Query

from app.services.agent_orchestrator_service import AgentOrchestratorService
from app.services.search_service import SearchService

router = APIRouter(
    prefix="/query",
    tags=["Query"],
)


@router.get("/chunks")
def get_chunks(
    q: str = Query(..., description="Search query"),
    top_k: int = Query(5, ge=1, le=20),
):
    service = SearchService()

    return service.search(
        query=q,
        top_k=top_k,
    )


@router.get("/ask")
def ask_question(
    q: str = Query(..., description="Question to answer"),
    top_k: int = Query(3, ge=1, le=10),
    document_id: str | None = Query(None),
):
    orchestrator = AgentOrchestratorService()

    return orchestrator.run(
        query=q,
        top_k=top_k,
        document_id=document_id,
    )