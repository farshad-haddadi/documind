from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import create_document
from app.services.ingestion_service import IngestionService
from app.services.indexing_service import IndexingService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    document = create_document(db=db, file=file)

    ingestion_service = IngestionService()
    await ingestion_service.ingest_document(document.id)

    indexing_service = IndexingService()
    indexing_service.build_index()

    return document