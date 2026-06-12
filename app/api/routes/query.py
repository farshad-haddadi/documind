from fastapi import APIRouter, Query

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