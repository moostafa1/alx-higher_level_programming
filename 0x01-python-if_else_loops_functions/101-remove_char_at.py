#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = [letter for i, letter in enumerate(str) if i != n]
    return "".join(str_copy)
