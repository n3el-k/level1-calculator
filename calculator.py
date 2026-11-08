"""A small calculator."""

import ast


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


# Long enough for any real sum. Each operator is worked out one step deeper, so a much
# longer input could crash the calculator instead of giving a clear error.
MAX_LENGTH = 200

# Only these operators are allowed. Anything else in the input is rejected.
OPERATORS = {ast.Add: add, ast.Sub: subtract, ast.Mult: multiply, ast.Div: divide}


def evaluate(expression: str) -> float:
    """Work out a whole expression like '2 + 3 * 4'.

    The input is parsed into a tree and only numbers and + - * / are worked out.
    It is never run as code.
    """
    expression = expression.strip()
    if not expression:
        raise CalculatorError("Please type an expression.")
    if len(expression) > MAX_LENGTH:
        raise CalculatorError(f"That expression is too long. Keep it under {MAX_LENGTH} characters.")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise CalculatorError(f"I can't work out '{expression}'.")
    return _work_out(tree.body, expression)


def _work_out(node: ast.AST, expression: str) -> float:
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_work_out(node.operand, expression)
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _work_out(node.left, expression)
        right = _work_out(node.right, expression)
        return OPERATORS[type(node.op)](left, right)
    raise CalculatorError(f"I can't work out '{expression}'. Use numbers and + - * / only.")
