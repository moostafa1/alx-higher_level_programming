#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if len(a_dictionary) > 0:
            return max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
        else:
            return None
