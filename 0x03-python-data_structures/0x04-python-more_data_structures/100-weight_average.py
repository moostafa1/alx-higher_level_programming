#!/usr/bin/python3
def mul(tup):
    mult = 1
    for i in tup:
        mult *= i
    return mult


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        total = 0
        weights = 0

        for tup in my_list:
            total += (mul(tup))
            weights += tup[-1]
    return total / weights
