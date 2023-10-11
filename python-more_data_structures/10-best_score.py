#!/usr/bin/python3

def best_score(a_dictionary):
    best = 0
    name = ""
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > best:
            best = value
            name = key
    return name
