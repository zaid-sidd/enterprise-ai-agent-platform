from src.db.connection import get_connection

from psycopg.types.json import Jsonb

def create_conversation() -> int:

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO conversations
                DEFAULT VALUES
                RETURNING id;
                """
            )

            conversation_id = cursor.fetchone()[0]

        connection.commit()

    return conversation_id


def add_message(
    conversation_id: int,
    role: str,
    content: str,
) -> int:

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO messages (
                    conversation_id,
                    role,
                    content
                )
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (
                    conversation_id,
                    role,
                    content,
                ),
            )

            message_id = cursor.fetchone()[0]

        connection.commit()

    return message_id


def add_tool_call(
    conversation_id: int,
    tool_name: str,
    arguments: dict,
    result,
) -> int:

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO tool_calls (
                    conversation_id,
                    tool_name,
                    arguments,
                    result
                )
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                """,
                (
                    conversation_id,
                    tool_name,
                    Jsonb(arguments),
                    Jsonb(result),
                ),
            )

            tool_call_id = cursor.fetchone()[0]

        connection.commit()

    return tool_call_id


def get_messages(conversation_id: int) -> list[dict]:

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    id,
                    role,
                    content,
                    created_at
                FROM messages
                WHERE conversation_id = %s
                ORDER BY id;
                """,
                (conversation_id,),
            )

            rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "role": row[1],
            "content": row[2],
            "created_at": row[3],
        }
        for row in rows
    ]

def conversation_exists(
    conversation_id: int,
) -> bool:

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT EXISTS(
                    SELECT 1
                    FROM conversations
                    WHERE id = %s
                );
                """,
                (conversation_id,),
            )

            return cursor.fetchone()[0]