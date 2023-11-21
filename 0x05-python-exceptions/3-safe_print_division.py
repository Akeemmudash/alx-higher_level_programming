#!/usr/bin/python3

def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result."""
    try:
        quotient = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
