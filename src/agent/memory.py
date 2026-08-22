from google.genai import types

from src.db.repository import get_messages
from src.db.cache import (
    cache_conversation,
    get_cached_conversation,
)


def load_conversation_messages(
    conversation_id: int,
) -> list[types.Content]:

    cached_messages = get_cached_conversation(
        conversation_id
    )

    if cached_messages is not None:
        stored_messages = cached_messages

    else:
        stored_messages = get_messages(
            conversation_id
        )

        cache_messages = [
            {
                "role": message["role"],
                "content": message["content"],
            }
            for message in stored_messages
        ]

        cache_conversation(
            conversation_id,
            cache_messages,
        )

    messages = []

    for message in stored_messages:

        role = message["role"]

        if role == "assistant":
            role = "model"

        messages.append(
            types.Content(
                role=role,
                parts=[
                    types.Part(
                        text=message["content"]
                    )
                ],
            )
        )

    return messages