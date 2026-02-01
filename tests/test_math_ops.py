import pytest

from myproj import add, division, multiply, subtract


def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 15


def test_multiply(numbers):
    a, b = numbers
    assert multiply(a, b) == 50


def test_subtract(numbers):
    a, b = numbers
    assert subtract(a, b) == 5


def test_division(numbers):
    a, b = numbers
    assert division(a, b) == 2.0


def test_division_returns_float():
    result = division(7, 2)
    assert isinstance(result, float)


def test_division_by_zero():
    with pytest.raises(ValueError):
        division(10, 0)
