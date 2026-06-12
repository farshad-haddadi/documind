from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.retrieval_service import RetrievalService

router = APIRouter(
    prefix="/query",
    tags=["Query"],
)


@router.get("/chunks")
def get_chunks(
    limit: int = 5,
    db: Session = Depends(get_db),
):
    service = RetrievalService()

    chunks = service.retrieve(
        db=db,
        query="test",
        limit=limit,
    )

    return [
        {
            "id": chunk.id,
            "text": chunk.text[:200],
        }
        for chunk in chunks
    ]