import faiss
import numpy as np


class VectorStoreService:
    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        vectors = np.array(
            embeddings,
            dtype=np.float32
        )
        self.index.add(vectors)

    def search(self, embedding, k=5):
        query = np.array(
            [embedding],
            dtype=np.float32
        )

        distances, indices = self.index.search(
            query,
            k
        )

        return distances[0], indices[0]
    