#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_size = len(my_list) - 1

    if (idx < 0 or idx > list_size):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
