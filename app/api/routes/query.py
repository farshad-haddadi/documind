from fastapi import APIRouter, Query

from app.services.search_service import SearchService
from app.services.reranking_service import RerankingService
from app.services.generation_service import GenerationService
from app.services.query_router_service import QueryRouterService

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
    query_router = QueryRouterService()
    intent = query_router.classify(q)

    search_service = SearchService()
    reranking_service = RerankingService()
    generation_service = GenerationService()

    results = search_service.search(
        query=q,
        top_k=10,
        document_id=document_id,
    )

    reranked_results = reranking_service.rerank(
        query=q,
        results=results,
        top_k=top_k,
    )

    contexts = [
        result["text"]
        for result in reranked_results
    ]

    answer = generation_service.generate_answer(
        query=q,
        contexts=contexts,
    )

    return {
        "question": q,
        "intent": intent,
        "document_id": document_id,
        "answer": answer,
        "sources": reranked_results,
    }