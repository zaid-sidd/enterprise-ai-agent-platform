from src.db.repository import (
    create_conversation,
    add_message,
    get_messages,
)


def main():

    conversation_id = create_conversation()

    print(
        "Created conversation:",
        conversation_id,
    )

    add_message(
        conversation_id,
        "user",
        "What is 25 * 4 + 10?",
    )

    add_message(
        conversation_id,
        "assistant",
        "The result is 110.",
    )

    messages = get_messages(
        conversation_id
    )

    print("\nMessages:")

    for message in messages:
        print(
            message["role"],
            "→",
            message["content"],
        )


if __name__ == "__main__":
    main()
