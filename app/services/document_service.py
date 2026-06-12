from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.db.models import Document
from app.utils.file_utils import save_upload_file


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