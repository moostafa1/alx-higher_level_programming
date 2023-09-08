#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    t = text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ",
                                                                   ":\n\n")
    print(t, end="")
