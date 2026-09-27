# operations.py
# Basic Math Calculator - Operations Module
# Contains simple mathematical functions for the 7 calculator operations.
# Handles division by zero using conditional statements without exception handling.

def add(num1, num2):
    """
    Returns the sum of num1 and num2.
    Uses the addition arithmetic operator (+).
    """
    return num1 + num2


def subtract(num1, num2):
    """
    Returns the difference when num2 is subtracted from num1.
    Uses the subtraction arithmetic operator (-).
    """
    return num1 - num2


def multiply(num1, num2):
    """
    Returns the product of num1 and num2.
    Uses the multiplication arithmetic operator (*).
    """
    return num1 * num2


def divide(num1, num2):
    """
    Returns the quotient of num1 divided by num2.
    Uses the standard division arithmetic operator (/).
    If num2 is 0, returns None to avoid division by zero.
    """
    if num2 == 0:
        return None
    else:
        return num1 / num2


def floor_divide(num1, num2):
    """
    Returns the floor division result of num1 divided by num2.
    Uses the floor division arithmetic operator (//).
    If num2 is 0, returns None to avoid division by zero.
    """
    if num2 == 0:
        return None
    else:
        return num1 // num2


def modulus(num1, num2):
    """
    Returns the remainder of num1 divided by num2.
    Uses the modulus arithmetic operator (%).
    If num2 is 0, returns None to avoid division by zero.
    """
    if num2 == 0:
        return None
    else:
        return num1 % num2


def power(num1, num2):
    """
    Returns num1 raised to the power of num2.
    Uses the exponentiation arithmetic operator (**).
    """
    return num1 ** num2
