from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ConversationCreate(BaseModel):
    title: str | None = None


class Conversation(BaseModel):
    id: UUID
    title: str | None = None
    created_at: datetime


class MessageCreate(BaseModel):
    sender: str = Field(min_length=1)
    body: str = Field(min_length=1)


class Message(BaseModel):
    id: UUID
    conversation_id: UUID
    sender: str
    body: str
    created_at: datetime
