# test_calculator.py

import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.history[-1] == "Added: 2 + 3 = 5"

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.history[-1] == "Subtracted: 5 - 3 = 2"

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.history[-1] == "Multiplied: 2 * 3 = 6"

def test_divide(calc):
    assert calc.divide(6, 3) == 2
    assert calc.history[-1] == "Divided: 6 / 3 = 2"

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(6, 0)

def test_retrieve_history(calc):
    calc.add(2, 3)
    calc.subtract(5, 3)
    history = calc.retrieve_history()
    assert len(history) == 2
    assert history[0] == "Added: 2 + 3 = 5"
