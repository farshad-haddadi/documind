from sentence_transformers import CrossEncoder


class RerankingService:
    def __init__(self):
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query: str,
        results: list[dict],
        top_k: int = 3,
    ) -> list[dict]:
        if not results:
            return []

        pairs = [
            (query, result["text"])
            for result in results
        ]

        scores = self.model.predict(pairs)

        scored_results = []

        for result, score in zip(results, scores):
            result["rerank_score"] = float(score)
            scored_results.append(result)

        scored_results.sort(
            key=lambda item: item["rerank_score"],
            reverse=True,
        )

        return scored_results[:top_k]