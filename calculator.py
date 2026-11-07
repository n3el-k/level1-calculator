"""A small calculator."""


class CalculatorError(Exception):
    """Something the user typed can't be worked out. The message is safe to show them."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise CalculatorError("You can't divide by zero.")
    return a / b


def evaluate(expression: str) -> float:
    """Work out a whole expression like '2 + 3 * 4'."""
    expression = expression.strip()
    if not expression:
        raise CalculatorError("Please type an expression.")
    try:
        return eval(expression)
    except (SyntaxError, NameError):
        raise CalculatorError(f"I can't work out '{expression}'.")
