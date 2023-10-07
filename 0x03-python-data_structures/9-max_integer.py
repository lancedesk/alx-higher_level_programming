#!/usr/bin/python3

def max_integer(my_list=[]):

    if not my_list:
        return (None)

    else:
        max_number = my_list[0]
        list_size = len(my_list)
        for index in range(list_size):
            if (my_list[index] > max_number):
                max_number = my_list[index]

        return (max_number)
