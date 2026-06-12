from pathlib import Path

from pypdf import PdfReader


class IngestionService:
    async def ingest_document(self, document_id: str):
        pass

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
    