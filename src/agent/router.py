from src.agent.state import AgentState


def route_after_agent(state: AgentState) -> str:

    last_message = state["messages"][-1]

    if hasattr(last_message, "parts"):

        for part in last_message.parts:

            if getattr(part, "function_call", None):
                return "tools"

    return "end"
