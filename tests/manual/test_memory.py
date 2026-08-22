from src.db.repository import (
    create_conversation,
    add_message,
)

from src.agent.memory import (
    load_conversation_messages,
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

    add_message(
        conversation_id,
        "user",
        "What department am I in?",
    )

    messages = load_conversation_messages(
        conversation_id
    )

    print("Conversation ID:")
    print(conversation_id)

    print("\nLoaded messages:")

    for message in messages:

        text = message.parts[0].text

        print(
            message.role,
            "→",
            text,
        )


if __name__ == "__main__":
    main()
