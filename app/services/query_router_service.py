from enum import Enum


class QueryIntent(str, Enum):
    QUESTION_ANSWERING = "question_answering"
    SUMMARIZATION = "summarization"
    COMPARISON = "comparison"
    EVIDENCE_LOOKUP = "evidence_lookup"


class QueryRouterService:
    def classify(self, query: str) -> QueryIntent:
        query_lower = query.lower()

        if any(word in query_lower for word in ["summarize", "summary", "overview"]):
            return QueryIntent.SUMMARIZATION

        if any(word in query_lower for word in ["compare", "difference", "differences"]):
            return QueryIntent.COMPARISON

        if any(word in query_lower for word in ["evidence", "source", "citation", "where does it say"]):
            return QueryIntent.EVIDENCE_LOOKUP

        return QueryIntent.QUESTION_ANSWERING