#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = sorted(list(a_dictionary))
    sorted_dict = {k:a_dictionary[k] for k in dict_keys}
    return sorted_dict
