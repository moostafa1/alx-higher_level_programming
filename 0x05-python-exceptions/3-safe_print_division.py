#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        print("Inside result: {:.1f}".format(a / b))
        print("{:d} / {:d} = {:.1f}".format(a, b, a / b))
    except ZeroDivisionError:
        print("Inside result: None")
