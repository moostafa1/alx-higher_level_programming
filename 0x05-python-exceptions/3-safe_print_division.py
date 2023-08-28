#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        print("Inside result: ", end="")
        print("{}".format(a / b))
        return a / b
    except ZeroDivisionError:
        print("None")
        return None
