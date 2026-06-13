import threading

from fastapi import APIRouter, Depends, File, UploadFile

from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import create_document, delete_document, get_document, list_documents
from app.services.ingestion_service import IngestionService
from app.services.indexing_service import IndexingService


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


def process_document_background(document_id: str) -> None:
    ingestion_service = IngestionService()
    indexing_service = IndexingService()

    ingestion_service.ingest_document_sync(document_id=document_id)
    indexing_service.build_index()


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    document = create_document(db=db, file=file)

    return document

@router.post("/{document_id}/process")
def process_document(
    document_id: str,
):
    process_document_background(document_id)

    return {
        "message": "Document processed successfully",
        "document_id": document_id,
    }


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


@router.delete("/{document_id}")
def remove_document(
    document_id: str,
    db: Session = Depends(get_db),
):
    deleted = delete_document(
        db=db,
        document_id=document_id,
    )

    if not deleted:
        return {"error": "Document not found"}

    return {
        "message": "Document deleted successfully",
        "document_id": document_id,
    }