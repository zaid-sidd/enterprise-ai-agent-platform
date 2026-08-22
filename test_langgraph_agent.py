from google.genai import types

from src.agent.graph import build_graph
from src.db.repository import (
    create_conversation,
    add_message,
    add_tool_call,
)


def main():

    conversation_id = create_conversation()

    user_question = "What is 25 * 4 + 10?"

    add_message(
        conversation_id,
        "user",
        user_question,
    )

    graph = build_graph()

    initial_state = {
        "conversation_id": conversation_id,
        "messages": [
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text=user_question
                    )
                ],
            )
        ],
        "tool_calls": [],
        "tool_results": [],
    }

    result = graph.invoke(initial_state)

    for tool_call, tool_result in zip(
        result["tool_calls"],
        result["tool_results"],
    ):

        add_tool_call(
            conversation_id=conversation_id,
            tool_name=tool_call["name"],
            arguments=tool_call["arguments"],
            result=tool_result["result"],
        )

    final_message = result["messages"][-1]

    final_text = ""

    for part in final_message.parts:

        if getattr(part, "text", None):
            final_text += part.text

    add_message(
        conversation_id,
        "assistant",
        final_text,
    )

    print("\nConversation ID:")
    print(conversation_id)

    print("\nTool Calls:")
    print(result["tool_calls"])

    print("\nTool Results:")
    print(result["tool_results"])

    print("\nFinal Answer:")
    print(final_text)


if __name__ == "__main__":
    main()