from src.tools.tool_registry import (
    TOOL_DEFINITIONS,
    AVAILABLE_TOOLS,
)


print("Registered tools:")

for tool in TOOL_DEFINITIONS:
    print("-", tool["name"])

print("\nExecutable tools:")

for name in AVAILABLE_TOOLS:
    print("-", name)
