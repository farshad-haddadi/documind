from sentence_transformers import SentenceTransformer


class EmbeddingService:
    _model = None

    def __init__(self):
        if EmbeddingService._model is None:
            

            EmbeddingService._model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2"
            )

            

        self.model = EmbeddingService._model

    def embed_text(self, text: str):
        return self.model.encode(text).tolist()