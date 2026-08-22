from src.db.repository import (
    create_conversation,
    add_tool_call,
)


def main():

    conversation_id = create_conversation()

    tool_call_id = add_tool_call(
        conversation_id=conversation_id,
        tool_name="calculate",
        arguments={
            "expression": "25 * 4 + 10"
        },
        result=110,
    )

    print(
        "Created conversation:",
        conversation_id,
    )

    print(
        "Created tool call:",
        tool_call_id,
    )


if __name__ == "__main__":
    main()
