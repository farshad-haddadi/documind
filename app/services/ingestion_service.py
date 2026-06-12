from pathlib import Path

from pypdf import PdfReader

from app.db.models import Chunk, Document
from app.db.session import SessionLocal


class IngestionService:
    async def ingest_document(self, document_id: str) -> int:
        db = SessionLocal()

        try:
            document = db.get(Document, document_id)

            if document is None:
                raise ValueError(f"Document not found: {document_id}")

            text = self.extract_text(Path(document.storage_path))
            chunks = self.chunk_text(text)

            for index, chunk_text in enumerate(chunks):
                chunk = Chunk(
                    document_id=document.id,
                    chunk_index=index,
                    text=chunk_text,
                )
                db.add(chunk)

            document.status = "processed"

            db.commit()

            return len(chunks)

        finally:
            db.close()

    def extract_text(self, file_path: Path) -> str:
        reader = PdfReader(file_path)

        pages_text = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            pages_text.append(page_text)

        return "\n".join(pages_text)

    def chunk_text(self, text: str, chunk_size: int = 1000) -> list[str]:
        return [
            text[i : i + chunk_size]
            for i in range(0, len(text), chunk_size)
            if text[i : i + chunk_size].strip()
        ]
    