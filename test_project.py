# tests/test_project.py
# Test suite for Basic Math Calculator
# Uses PLAIN Python assert statements ONLY.
# No unittest, pytest, or external testing libraries are used.

import os
import sys

# Ensure parent directory is in search path to import project modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import operations
from calculator import Calculator, ZERO_DIVISORS
from main import is_valid_number, parse_number, check_parity_bitwise


def test_addition():
    print("Testing addition...")
    assert operations.add(10, 5) == 15
    assert operations.add(-4, 9) == 5
    assert operations.add(2.5, 3.5) == 6.0
    print("  -> Addition tests passed!")


def test_subtraction():
    print("Testing subtraction...")
    assert operations.subtract(10, 4) == 6
    assert operations.subtract(5, 12) == -7
    assert operations.subtract(4.5, 1.5) == 3.0
    print("  -> Subtraction tests passed!")


def test_multiplication():
    print("Testing multiplication...")
    assert operations.multiply(6, 7) == 42
    assert operations.multiply(-3, 4) == -12
    assert operations.multiply(2.5, 4) == 10.0
    print("  -> Multiplication tests passed!")


def test_division():
    print("Testing normal division and division by zero...")
    assert operations.divide(20, 4) == 5.0
    assert operations.divide(7, 2) == 3.5
    # Division by zero must return None (safe handling without exceptions)
    assert operations.divide(10, 0) is None
    print("  -> Division tests passed!")


def test_floor_division():
    print("Testing floor division...")
    assert operations.floor_divide(17, 5) == 3
    assert operations.floor_divide(10, 3) == 3
    assert operations.floor_divide(9, 0) is None
    print("  -> Floor division tests passed!")


def test_modulus():
    print("Testing modulus...")
    assert operations.modulus(17, 5) == 2
    assert operations.modulus(10, 2) == 0
    assert operations.modulus(5, 0) is None
    print("  -> Modulus tests passed!")


def test_power():
    print("Testing power (exponentiation)...")
    assert operations.power(2, 3) == 8
    assert operations.power(5, 2) == 25
    assert operations.power(9, 0.5) == 3.0
    print("  -> Power tests passed!")


def test_number_validation():
    print("Testing input validation without try/except...")
    # Valid numeric strings
    assert is_valid_number("42") is True
    assert is_valid_number("3.1415") is True
    assert is_valid_number("-15") is True
    assert is_valid_number("+8.5") is True
    assert is_valid_number("0") is True

    # Invalid strings
    assert is_valid_number("abc") is False
    assert is_valid_number("12a3") is False
    assert is_valid_number("3.14.15") is False
    assert is_valid_number("-") is False
    assert is_valid_number("") is False
    assert is_valid_number("   ") is False
    print("  -> Number validation tests passed!")


def test_parse_number():
    print("Testing type conversion parsing...")
    assert parse_number("42") == 42
    assert type(parse_number("42")) is int
    assert parse_number("3.5") == 3.5
    assert type(parse_number("3.5")) is float
    print("  -> Type conversion tests passed!")


def test_bitwise_parity():
    print("Testing bitwise parity check...")
    assert check_parity_bitwise(10) == "Even"
    assert check_parity_bitwise(7) == "Odd"
    assert check_parity_bitwise(0) == "Even"
    assert check_parity_bitwise(-3) == "Odd"
    print("  -> Bitwise parity tests passed!")


def test_calculator_class():
    print("Testing Calculator class state and data structures...")
    calc = Calculator()

    # Initial state
    assert len(calc.get_history()) == 0
    assert len(calc.results_array) == 0
    assert calc.operations_count == 0
    assert len(calc.unique_operators) == 0
    assert calc.get_summary() is None

    # Perform sample calculations
    calc.add_calculation(10, '+', 5, 15.0)
    calc.add_calculation(20, '-', 8, 12.0)
    calc.add_calculation(3, '*', 4, 12.0)

    # Validate history list of tuples
    history = calc.get_history()
    assert len(history) == 3
    assert history[0] == (10, '+', 5, 15.0)
    assert history[1] == (20, '-', 8, 12.0)
    assert history[2] == (3, '*', 4, 12.0)

    # Validate array data structure
    assert len(calc.results_array) == 3
    assert calc.results_array[0] == 15.0
    assert calc.results_array[1] == 12.0
    assert calc.results_array[2] == 12.0

    # Validate unique operators set
    assert calc.unique_operators == {'+', '-', '*'}

    # Validate summary tuple: (count, total_sum, avg_result, unique_ops_count)
    summary = calc.get_summary()
    assert summary is not None
    count, total_sum, avg_result, unique_ops_count = summary
    assert count == 3
    assert total_sum == 39.0
    assert avg_result == 13.0
    assert unique_ops_count == 3

    # Validate clear_history
    calc.clear_history()
    assert len(calc.get_history()) == 0
    assert len(calc.results_array) == 0
    assert calc.operations_count == 0
    print("  -> Calculator class tests passed!")


def test_frozen_set():
    print("Testing ZERO_DIVISORS frozen set...")
    assert '/' in ZERO_DIVISORS
    assert '//' in ZERO_DIVISORS
    assert '%' in ZERO_DIVISORS
    assert '+' not in ZERO_DIVISORS
    assert '*' not in ZERO_DIVISORS
    print("  -> Frozen set tests passed!")


def run_all_tests():
    print("========================================")
    print("RUNNING BASIC MATH CALCULATOR TEST SUITE")
    print("========================================")

    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_floor_division()
    test_modulus()
    test_power()
    test_number_validation()
    test_parse_number()
    test_bitwise_parity()
    test_calculator_class()
    test_frozen_set()

    print("========================================")
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("========================================")


if __name__ == '__main__':
    run_all_tests()
