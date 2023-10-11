#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return

    unique_set = set(my_list)
    return sum(unique_set)
