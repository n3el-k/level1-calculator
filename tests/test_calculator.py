import pytest

from calculator import CalculatorError, add, divide, evaluate, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2, -3) == 1


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero_gives_a_clear_error():
    with pytest.raises(CalculatorError, match="divide by zero"):
        divide(1, 0)


def test_evaluate_follows_order_of_operations():
    assert evaluate("2 + 3 * 4") == 14


def test_evaluate_handles_brackets_and_decimals():
    assert evaluate("(2 + 3) * 4") == 20
    assert evaluate("1.5 * 2") == 3


def test_evaluate_rejects_invalid_input():
    with pytest.raises(CalculatorError):
        evaluate("2 + + ")


def test_evaluate_rejects_empty_input():
    with pytest.raises(CalculatorError):
        evaluate("   ")
