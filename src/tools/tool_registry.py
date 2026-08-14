from src.tools.calculator import calculate
from src.tools.employee import get_employee


TOOL_DEFINITIONS = [
    {
        "name": "calculate",
        "description": (
            "Evaluate a basic mathematical expression "
            "and return the numeric result."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": (
                        "A mathematical expression such as "
                        "'25 * 4 + 10'."
                    ),
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_employee",
        "description": (
            "Retrieve employee information using an employee ID."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": (
                        "The employee ID, for example E001."
                    ),
                }
            },
            "required": ["employee_id"],
        },
    },
]


AVAILABLE_TOOLS = {
    "calculate": calculate,
    "get_employee": get_employee,
}