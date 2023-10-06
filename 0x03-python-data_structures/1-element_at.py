#!/usr/bin/python3

def element_at(my_list, idx):
    items_in_list = len(my_list)

    if (idx < 0 or idx > items_in_list):
        return (None)
    else:
        return (my_list[idx])
