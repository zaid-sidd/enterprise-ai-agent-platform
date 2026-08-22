from typing import TypedDict, Any


class AgentState(TypedDict):

    conversation_id: int
    messages: list[Any]
    tool_calls: list[dict]
    tool_results: list[dict]