import faiss
import numpy as np

from app.core.config import get_settings
from app.db.models import Chunk
from app.db.session import SessionLocal
from app.services.embedding_service import EmbeddingService


class IndexingService:
    def __init__(self):
        self.settings = get_settings()
        self.embedder = EmbeddingService()
        self.dimension = 384

    def build_index(self) -> int:
        db = SessionLocal()

        try:
            chunks = db.query(Chunk).order_by(Chunk.id).all()

            if not chunks:
                raise ValueError("No chunks found. Ingest documents first.")

            texts = [chunk.text for chunk in chunks]

            embeddings = [
                self.embedder.embed_text(text)
                for text in texts
            ]

            vectors = np.array(embeddings, dtype=np.float32)

            index = faiss.IndexFlatL2(self.dimension)
            index.add(vectors)

            faiss.write_index(index, self.settings.faiss_index_path)

            for faiss_id, chunk in enumerate(chunks):
                chunk.faiss_index_id = faiss_id

            db.commit()

            return len(chunks)

        finally:
            db.close()

if __name__ == "__main__":
    service = IndexingService()
    count = service.build_index()
    print(f"Indexed chunks: {count}")