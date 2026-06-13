from app.services.generation_service import GenerationService
from app.services.query_router_service import QueryIntent, QueryRouterService
from app.services.reranking_service import RerankingService
from app.services.search_service import SearchService


class AgentOrchestratorService:
    def __init__(self):
        self.query_router = QueryRouterService()
        self.search_service = SearchService()
        self.reranking_service = RerankingService()
        self.generation_service = GenerationService()

    def run(
        self,
        query: str,
        top_k: int = 3,
        document_id: str | None = None,
    ) -> dict:
        intent = self.query_router.classify(query)

        retrieved_results = self.search_service.search(
            query=query,
            top_k=10,
            document_id=document_id,
        )

        reranked_results = self.reranking_service.rerank(
            query=query,
            results=retrieved_results,
            top_k=top_k,
        )

        contexts = [
            result["text"]
            for result in reranked_results
        ]

        answer = self.generation_service.generate_answer(
            query=query,
            contexts=contexts,
        )

        return {
            "query": query,
            "intent": intent,
            "document_id": document_id,
            "answer": answer,
            "sources": reranked_results,
        }