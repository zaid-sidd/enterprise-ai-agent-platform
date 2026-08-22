from google.genai import types

from src.agent.graph import build_graph
from src.agent.memory import load_conversation_messages
from src.db.repository import (
    create_conversation,
    add_message,
)


def main():

    conversation_id = create_conversation()

    first_question = "My employee ID is E001."

    add_message(
        conversation_id,
        "user",
        first_question,
    )

    first_messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text=first_question
                )
            ],
        )
    ]

    graph = build_graph()

    first_state = {
        "conversation_id": conversation_id,
        "messages": first_messages,
        "tool_calls": [],
        "tool_results": [],
    }

    first_result = graph.invoke(
        first_state
    )

    first_answer = ""

    for part in first_result["messages"][-1].parts:

        if getattr(part, "text", None):
            first_answer += part.text

    add_message(
        conversation_id,
        "assistant",
        first_answer,
    )

    second_question = (
        "What department is my employee ID E001 "
        "associated with?"
    )

    history = load_conversation_messages(
        conversation_id
    )

    history.append(
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text=second_question
                )
            ],
        )
    )

    second_state = {
        "conversation_id": conversation_id,
        "messages": history,
        "tool_calls": [],
        "tool_results": [],
    }

    second_result = graph.invoke(
        second_state
    )

    second_answer = ""

    for part in second_result["messages"][-1].parts:

        if getattr(part, "text", None):
            second_answer += part.text

    print("\nConversation ID:")
    print(conversation_id)

    print("\nPrevious Answer:")
    print(first_answer)

    print("\nMemory-loaded messages:")
    print(len(history))

    print("\nFinal Answer:")
    print(second_answer)


if __name__ == "__main__":
    main()
