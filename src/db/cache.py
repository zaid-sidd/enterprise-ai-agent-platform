import json

from src.db.redis_client import get_redis


CACHE_TTL = 3600


def cache_conversation(
    conversation_id: int,
    messages: list[dict],
) -> None:

    redis_client = get_redis()

    key = f"conversation:{conversation_id}"

    redis_client.setex(
        key,
        CACHE_TTL,
        json.dumps(messages),
    )


def get_cached_conversation(
    conversation_id: int,
) -> list[dict] | None:

    redis_client = get_redis()

    key = f"conversation:{conversation_id}"

    data = redis_client.get(key)

    if data is None:
        return None

    return json.loads(data)


def delete_cached_conversation(
    conversation_id: int,
) -> None:

    redis_client = get_redis()

    key = f"conversation:{conversation_id}"

    redis_client.delete(key)
