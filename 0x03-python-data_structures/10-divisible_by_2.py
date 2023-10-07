#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if (not my_list):
        return (None)

    else:
        new_list = []
        list_size = len(my_list)
        for index in range(list_size):
            new_list.append(my_list[index] % 2 == 0)
        return (new_list)
