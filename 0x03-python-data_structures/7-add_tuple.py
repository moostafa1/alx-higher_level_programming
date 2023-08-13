#!/usr/bin/python3

def check_tuple_len(tup):
    if len(tup) > 2:
        tup = tup[:2]
    elif len(tup) < 2:
        for i in range(2 - len(tup)):
            tup += (0,)
            if len(tup) == 2:
                break
    return tuple(tup)



def add_tuple(tuple_a=(), tuple_b=()):
    a_plus_b = tuple([check_tuple_len(tuple_a)[i] + 
        check_tuple_len(tuple_b)[i] 
        for i in range(len(check_tuple_len(tuple_a)))])
    return a_plus_b
