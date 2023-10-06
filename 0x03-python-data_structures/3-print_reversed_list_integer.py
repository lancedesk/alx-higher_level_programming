#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list) - 1
    index = 0

    while (index <= list_size):
        print("{:d}".format(my_list[list_size - index]))
        index += 1
