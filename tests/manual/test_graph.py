from src.agent.graph import build_graph


graph = build_graph()

initial_state = {
    "messages": [
        "Hello Agent"
    ],
    "tool_calls": [],
    "tool_results": [],
}

result = graph.invoke(initial_state)

print(result)
