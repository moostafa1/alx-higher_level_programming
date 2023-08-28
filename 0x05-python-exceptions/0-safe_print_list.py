#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        cnt = 0
        for i in my_list:
           cnt += 1
        if x > cnt:
            x = cnt
        string = ''.join([str(v) for i, v in enumerate(my_list) if i < x])
        print("{}".format(string))
        return x
    except:
        print("\aPlease check that x is positive integer")
