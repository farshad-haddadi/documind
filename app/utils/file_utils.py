from pathlib import Path

from fastapi import UploadFile


UPLOAD_DIR = Path("data/raw")


def save_upload_file(file: UploadFile, document_id: str) -> str:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_extension = Path(file.filename or "").suffix
    storage_path = UPLOAD_DIR / f"{document_id}{file_extension}"

    with storage_path.open("wb") as buffer:
        buffer.write(file.file.read())

    return str(storage_path)