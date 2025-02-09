'''My Calculator Test
from calculator import add, subtract

def test_addition():
    Test that addition function works 
    assert add(2, 2) == 4

def test_subtraction():
    Test that subtraction function works 
    assert subtract(2, 2) == 0 '''

import pytest
from calculator.operations import Calculator

def test_add(setup_calculator):
    calc = setup_calculator
    result = calc.add(1, 2)  # example of a method on Calculator
    assert result == 3
def setup_calculator():
    Calculator.clear_history()
    return Calculator

def test_add(setup_calculator):
    assert setup_calculator.operate("+", 3, 2) == 5

def test_subtract(setup_calculator):
    assert setup_calculator.operate("-", 5, 2) == 3

def test_multiply(setup_calculator):
    assert setup_calculator.operate("*", 4, 3) == 12

def test_divide(setup_calculator):
    assert setup_calculator.operate("/", 8, 2) == 4

def test_divide_by_zero(setup_calculator):
    with pytest.raises(ZeroDivisionError):
        setup_calculator.operate("/", 10, 0)

def test_history_tracking(setup_calculator):
    setup_calculator.operate("+", 3, 3)
    setup_calculator.operate("*", 2, 2)
    history = setup_calculator.get_history()
    assert len(history) == 2
