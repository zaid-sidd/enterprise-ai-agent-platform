from google.genai import types

from src.agent.state import AgentState
from src.llm import GeminiLLM
from src.tools.executor import execute_tool


llm = GeminiLLM()


def agent_node(state: AgentState) -> AgentState:

    response = llm.generate_with_tools(
        state["messages"]
    )

    state["messages"].append(
        response.candidates[0].content
    )

    return state


def tool_node(state: AgentState) -> AgentState:

    model_content = state["messages"][-1]

    for part in model_content.parts:

        function_call = getattr(
            part,
            "function_call",
            None,
        )

        if not function_call:
            continue

        tool_name = function_call.name
        arguments = dict(function_call.args)

        result = execute_tool(
            tool_name,
            arguments,
        )

        state["tool_calls"].append(
            {
                "name": tool_name,
                "arguments": arguments,
            }
        )

        state["tool_results"].append(
            {
                "name": tool_name,
                "result": result,
            }
        )

        state["messages"].append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=tool_name,
                        response={
                            "result": result
                        },
                    )
                ],
            )
        )

    return state