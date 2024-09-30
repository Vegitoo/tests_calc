from src.calc import Calculator
import pytest

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5, "Błąd w dodawaniu"

def test_subtraction():
    calc = Calculator()
    assert calc.sub(10, 3) == 7, "Błąd w odejmowaniu"

def test_multiplication():
    calc = Calculator()
    assert calc.mul(6, 5) == 30, "Błąd w mnożeniu"

def test_division():
    calc = Calculator()
    assert calc.div(10, 2) == 5, "Błąd w dzieleniu"

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)

def test_addition_large_numbers():
    calc = Calculator()
    assert calc.add(1000000000000, 1000000000000) == 2000000000000, "Błąd w dodawaniu dużych liczb"

def test_multiplication_by_zero():
    calc = Calculator()
    assert calc.mul(10, 0) == 0, "Błąd w mnożeniu przez zero"

def test_negative_subtraction():
    calc = Calculator()
    assert calc.sub(-5, -3) == -2, "Błąd w odejmowaniu liczb ujemnych"

def test_float_division():
    calc = Calculator()
    assert calc.div(5, 2) == 2.5, "Błąd w dzieleniu liczb po przecinku"
