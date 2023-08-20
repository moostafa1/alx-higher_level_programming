#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    if isinstance(roman_string, str):
        if len(roman_string) == 0:
            return 0
        else:
            signs_lst = [1]
            for idx, k in enumerate(roman_string):
                for i, s in enumerate(roman_string):
                    if i == idx+1:
                        if roman_dict[k] >= roman_dict[s]:
                            signs_lst.insert(idx, 1)
                        else:
                            signs_lst.insert(idx, -1)
            vals_lst = sum([roman_dict[r]*signs_lst[i]
                            for i, r in enumerate(roman_string)])
            return vals_lst
    else:
        return 0
