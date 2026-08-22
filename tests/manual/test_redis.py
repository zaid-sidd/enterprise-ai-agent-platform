from src.db.redis_client import get_redis


def main():

    redis_client = get_redis()

    redis_client.set(
        "python_test",
        "Redis connection works",
    )

    value = redis_client.get(
        "python_test"
    )

    print("Redis connection successful.")
    print(value)


if __name__ == "__main__":
    main()
