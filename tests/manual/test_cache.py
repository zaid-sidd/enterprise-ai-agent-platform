from src.db.cache import (
    cache_conversation,
    get_cached_conversation,
)


def main():

    conversation_id = 100

    messages = [
        {
            "role": "user",
            "content": "My employee ID is E001.",
        },
        {
            "role": "assistant",
            "content": "Got it. Your employee ID is E001.",
        },
    ]

    cache_conversation(
        conversation_id,
        messages,
    )

    cached = get_cached_conversation(
        conversation_id
    )

    print("Cached conversation:")
    print(cached)


if __name__ == "__main__":
    main()
