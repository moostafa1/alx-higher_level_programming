#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = [replace if val == search else val for val in my_list]
    return lst
