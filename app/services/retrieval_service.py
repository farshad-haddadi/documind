from sqlalchemy.orm import Session

from app.db.models import Chunk


class RetrievalService:
    def retrieve(self, db: Session, query: str, limit: int = 5):
        return (
            db.query(Chunk)
            .limit(limit)
            .all()
        )