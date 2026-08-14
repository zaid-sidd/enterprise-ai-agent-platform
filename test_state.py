from src.agent.state import AgentState


state: AgentState = {
    "messages": [],
    "tool_calls": [],
    "tool_results": [],
}


state["messages"].append(
    "What is 25 * 4 + 10?"
)

state["tool_calls"].append(
    {
        "name": "calculate",
        "arguments": {
            "expression": "25 * 4 + 10"
        },
    }
)

state["tool_results"].append(
    {
        "name": "calculate",
        "result": 110.0,
    }
)


print(state)
