from src.tools.executor import execute_tool


result = execute_tool(
    "calculate",
    {
        "expression": "25 * 4 + 10"
    }
)

print(result)
