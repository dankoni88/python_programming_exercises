"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""
import pytest


def is_value_a_positive_integer(value):
    return isinstance(value, int) and value >= 0


def factorial(number: int):
    result = 1
    if is_value_a_positive_integer(number):
        if number != 0:
            for i in range(1, number + 1):
                result *= i
            return result
        return result
    raise ValueError


@pytest.mark.parametrize(('number', 'result'), [(0, 1), (8, 40320), (5, 120), (True, 1), (False, 1)])
def test_factorial_valid_values(number, result):
    assert factorial(number) == result


@pytest.mark.parametrize('value', ["A", dict, list, 0.25, -7])
def test_factorial_invalid_values(value):
    with pytest.raises(ValueError):
        factorial(value)
