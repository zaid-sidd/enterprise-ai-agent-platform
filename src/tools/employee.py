EMPLOYEES = {
    "E001": {
        "name": "Aarav Sharma",
        "department": "Network Operations",
        "role": "Network Engineer",
    },
    "E002": {
        "name": "Priya Mehta",
        "department": "Data Engineering",
        "role": "Data Engineer",
    },
    "E003": {
        "name": "Rahul Verma",
        "department": "Cloud Operations",
        "role": "Cloud Engineer",
    },
}


def get_employee(employee_id: str) -> dict:
    """
    Retrieve employee information using an employee ID.
    """

    employee = EMPLOYEES.get(employee_id)

    if not employee:
        raise ValueError(
            f"Employee not found: {employee_id}"
        )

    return {
        "employee_id": employee_id,
        **employee,
    }
