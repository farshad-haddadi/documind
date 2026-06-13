from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.conversation_service import ConversationService
from app.services.generation_service import GenerationService
from app.services.reranking_service import RerankingService
from app.services.search_service import SearchService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    conversation_service = ConversationService()
    search_service = SearchService()
    reranking_service = RerankingService()
    generation_service = GenerationService()

    if request.conversation_id is None:
        conversation = conversation_service.create_conversation(db)
        conversation_id = conversation.id
    else:
        conversation_id = request.conversation_id

    conversation_service.add_message(
        db=db,
        conversation_id=conversation_id,
        role="user",
        content=request.message,
    )

    results = search_service.search(
        query=request.message,
        top_k=10,
    )

    reranked_results = reranking_service.rerank(
        query=request.message,
        results=results,
        top_k=3,
    )

    contexts = [result["text"] for result in reranked_results]

    answer = generation_service.generate_answer(
        query=request.message,
        contexts=contexts,
    )

    conversation_service.add_message(
        db=db,
        conversation_id=conversation_id,
        role="assistant",
        content=answer,
    )

    return ChatResponse(
        conversation_id=conversation_id,
        answer=answer,
    )