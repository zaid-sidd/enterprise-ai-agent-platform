from src.tools.tool_registry import AVAILABLE_TOOLS


def execute_tool(tool_name: str, arguments: dict):
    if tool_name not in AVAILABLE_TOOLS:
        raise ValueError(f"Unknown tool: {tool_name}")

    tool = AVAILABLE_TOOLS[tool_name]

    return tool(**arguments)
