#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the input dictionary is None or empty
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)

    # Find the key with the maximum value
    best_key = max(a_dictionary, key=a_dictionary.get)
    return (best_key)
