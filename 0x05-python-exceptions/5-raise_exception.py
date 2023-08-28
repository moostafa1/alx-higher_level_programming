#!/usr/bin/python3

def raise_exception():
    x = "hello"
    if not isinstance(x, int):
        raise TypeError("Exception raised")
