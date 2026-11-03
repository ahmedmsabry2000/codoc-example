from datetime import UTC, datetime
from uuid import UUID, uuid4

from messaging.models import Conversation, ConversationCreate, Message, MessageCreate


class NotFoundError(KeyError):
    """Raised when a conversation or message does not exist."""


class MessageStore:
    """Process-local in-memory store for conversations and messages."""

    def __init__(self) -> None:
        self._conversations: dict[UUID, Conversation] = {}
        self._messages: dict[UUID, list[Message]] = {}

    def create_conversation(self, data: ConversationCreate) -> Conversation:
        conversation = Conversation(
            id=uuid4(),
            title=data.title,
            created_at=datetime.now(UTC),
        )
        self._conversations[conversation.id] = conversation
        self._messages[conversation.id] = []
        return conversation

    def list_conversations(self) -> list[Conversation]:
        return sorted(
            self._conversations.values(),
            key=lambda item: item.created_at,
        )

    def get_conversation(self, conversation_id: UUID) -> Conversation:
        try:
            return self._conversations[conversation_id]
        except KeyError as err:
            raise NotFoundError(f"conversation {conversation_id} not found") from err

    def add_message(self, conversation_id: UUID, data: MessageCreate) -> Message:
        self.get_conversation(conversation_id)
        message = Message(
            id=uuid4(),
            conversation_id=conversation_id,
            sender=data.sender,
            body=data.body,
            created_at=datetime.now(UTC),
        )
        self._messages[conversation_id].append(message)
        return message

    def list_messages(self, conversation_id: UUID) -> list[Message]:
        self.get_conversation(conversation_id)
        return list(self._messages[conversation_id])
