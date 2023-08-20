#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for k in a_dictionary:
        if a_dictionary.get(k) == value:
            keys_to_del.append(k)
    for v in keys_to_del:
        a_dictionary.pop(v)
    return a_dictionary
