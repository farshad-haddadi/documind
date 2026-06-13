from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.db.models import Document
from app.utils.file_utils import save_upload_file
import os

def create_document(db: Session, file: UploadFile) -> Document:
    document = Document(
        filename=file.filename or "unknown",
        content_type=file.content_type or "application/octet-stream",
        storage_path="pending",
        status="uploaded",
    )

    db.add(document)
    db.flush()
    db.refresh(document)

    storage_path = save_upload_file(file=file, document_id=document.id)
    document.storage_path = storage_path

    db.commit()
    db.refresh(document)

    return document

def list_documents(db: Session) -> list[Document]:
    return (
        db.query(Document)
        .order_by(Document.created_at.desc())
        .all()
    )

def get_document(
    db: Session,
    document_id: str,
):
    return (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

def delete_document(
    db: Session,
    document_id: str,
) -> bool:
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if document is None:
        return False

    if os.path.exists(document.storage_path):
        os.remove(document.storage_path)

    db.delete(document)
    db.commit()

    return True