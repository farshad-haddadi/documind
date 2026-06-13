from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import create_document, list_documents, get_document
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

@router.get("", response_model=list[DocumentResponse])
def get_documents(
    db: Session = Depends(get_db),
):
    return list_documents(db)

@router.get("/{document_id}")
def get_document_by_id(
    document_id: str,
    db: Session = Depends(get_db),
):
    document = get_document(db=db, document_id=document_id)

    if document is None:
        return {"error": "Document not found"}

    return {
        "id": document.id,
        "filename": document.filename,
        "content_type": document.content_type,
        "status": document.status,
        "created_at": document.created_at,
        "chunk_count": len(document.chunks),
    }