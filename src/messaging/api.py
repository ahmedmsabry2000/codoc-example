from uuid import UUID

from fastapi import FastAPI, HTTPException

from messaging.models import (
    Conversation,
    ConversationCreate,
    Message,
    MessageCreate,
)
from messaging.store import MessageStore, NotFoundError

store = MessageStore()

app = FastAPI(
    title="Messaging API",
    description="Simple in-memory messaging API used as a Codoc example baseline.",
    version="0.1.0",
)


@app.post("/conversations", response_model=Conversation, status_code=201)
def create_conversation(data: ConversationCreate) -> Conversation:
    return store.create_conversation(data)


@app.get("/conversations", response_model=list[Conversation])
def list_conversations() -> list[Conversation]:
    return store.list_conversations()


@app.get("/conversations/{conversation_id}", response_model=Conversation)
def get_conversation(conversation_id: UUID) -> Conversation:
    try:
        return store.get_conversation(conversation_id)
    except NotFoundError as err:
        raise HTTPException(status_code=404, detail=str(err)) from err


@app.post(
    "/conversations/{conversation_id}/messages",
    response_model=Message,
    status_code=201,
)
def send_message(conversation_id: UUID, data: MessageCreate) -> Message:
    try:
        return store.add_message(conversation_id, data)
    except NotFoundError as err:
        raise HTTPException(status_code=404, detail=str(err)) from err


@app.get(
    "/conversations/{conversation_id}/messages",
    response_model=list[Message],
)
def list_messages(conversation_id: UUID) -> list[Message]:
    try:
        return store.list_messages(conversation_id)
    except NotFoundError as err:
        raise HTTPException(status_code=404, detail=str(err)) from err
