#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return []

    # New list to store replaced elements
    new_list = []

    for number in my_list:
        if number == search:
            new_list.append(replace)
        else:
            new_list.append(number)  # If not, append the element as is
    return (new_list)
