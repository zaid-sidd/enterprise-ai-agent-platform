from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from src.agent.state import AgentState
from src.agent.nodes import (
    agent_node,
    tool_node,
)
from src.agent.router import route_after_agent


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node(
        "agent",
        agent_node,
    )

    graph.add_node(
        "tools",
        tool_node,
    )

    graph.add_edge(
        START,
        "agent",
    )

    graph.add_conditional_edges(
        "agent",
        route_after_agent,
        {
            "tools": "tools",
            "end": END,
        },
    )

    graph.add_edge(
        "tools",
        "agent",
    )

    return graph.compile()