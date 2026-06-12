from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: str
    filename: str
    content_type: str
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }