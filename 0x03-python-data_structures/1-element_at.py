#!/usr/bin/python3
def element_at(my_list, idx):
    """returnin element at a given positive index"""
    if idx < 0 or idx not in range(len(my_list)):
        return None
    return my_list[idx]
