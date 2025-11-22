#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        k = a / b
    except ZeroDivisionError:
        k = None
    return k
