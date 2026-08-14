def calculate(expression: str) -> float:
    """
    Evaluate a basic mathematical expression.
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {},
        )

        if not isinstance(result, (int, float)):
            raise ValueError("Expression must return a number.")

        return float(result)

    except Exception as exc:
        raise ValueError(
            f"Invalid mathematical expression: {expression}"
        ) from exc
