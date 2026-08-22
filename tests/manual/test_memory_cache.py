from src.agent.memory import (
    load_conversation_messages,
)
from src.db.cache import (
    delete_cached_conversation,
)
from src.db.repository import (
    create_conversation,
    add_message,
)


def main():

    conversation_id = create_conversation()

    add_message(
        conversation_id,
        "user",
        "My employee ID is E001.",
    )

    add_message(
        conversation_id,
        "assistant",
        "Got it. Your employee ID is E001.",
    )

    delete_cached_conversation(
        conversation_id
    )

    print("First load:")

    messages = load_conversation_messages(
        conversation_id
    )

    for message in messages:
        print(
            message.role,
            "→",
            message.parts[0].text,
        )

    print("\nSecond load:")

    messages = load_conversation_messages(
        conversation_id
    )

    for message in messages:
        print(
            message.role,
            "→",
            message.parts[0].text,
        )


if __name__ == "__main__":
    main()
