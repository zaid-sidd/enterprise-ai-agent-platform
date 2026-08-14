from google.genai import types

from src.agent.graph import build_graph


def main():

    graph = build_graph()

    initial_state = {
        "messages": [
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text="Get the details of employee E001 and calculate 25 * 4 + 10."
                    )
                ],
            )
        ],
        "tool_calls": [],
        "tool_results": [],
    }

    result = graph.invoke(initial_state)

    print("\nTOOL CALLS")
    print(result["tool_calls"])

    print("\nTOOL RESULTS")
    print(result["tool_results"])

    print("\nFINAL MESSAGE")
    print(result["messages"][-1])


if __name__ == "__main__":
    main()
