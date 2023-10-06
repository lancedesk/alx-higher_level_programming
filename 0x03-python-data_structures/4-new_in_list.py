#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_size = len(my_list) - 1
    temporary_list = my_list[:]

    if (idx < 0 or idx > list_size):
        return (my_list)
    else:
        temporary_list[idx] = element
        return (temporary_list)
