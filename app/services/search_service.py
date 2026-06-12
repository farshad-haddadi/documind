import faiss
import numpy as np

from app.core.config import get_settings
from app.db.models import Chunk
from app.db.session import SessionLocal
from app.services.embedding_service import EmbeddingService


class SearchService:
    def __init__(self):
        self.settings = get_settings()
        self.embedder = EmbeddingService()

    def search(self, query: str, top_k: int = 5):
        index = faiss.read_index(
            self.settings.faiss_index_path
        )

        query_vector = np.array(
            [self.embedder.embed_text(query)],
            dtype=np.float32,
        )

        distances, indices = index.search(
            query_vector,
            top_k,
        )

        db = SessionLocal()

        try:
            results = []

            for faiss_id in indices[0]:
                chunk = (
                    db.query(Chunk)
                    .filter(
                        Chunk.faiss_index_id == int(faiss_id)
                    )
                    .first()
                )

                if chunk:
                    results.append(
                        {
                            "chunk_id": chunk.id,
                            "document_id": chunk.document_id,
                            "text": chunk.text,
                        }
                    )

            return results

        finally:
            db.close()