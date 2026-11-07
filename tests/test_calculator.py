import pytest

from calculator import CalculatorError, add, divide, subtract


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
