from sqlalchemy.orm import Session

from app.db.models import Conversation, Message


class ConversationService:
    def create_conversation(self, db: Session) -> Conversation:
        conversation = Conversation()
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation

    def add_message(
        self,
        db: Session,
        conversation_id: str,
        role: str,
        content: str,
    ) -> Message:
        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    def get_messages(
        self,
        db: Session,
        conversation_id: str,
        limit: int = 10,
    ) -> list[Message]:
        return (
            db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.desc())
            .limit(limit)
            .all()
        )