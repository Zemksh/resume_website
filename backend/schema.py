from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Notecreate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True