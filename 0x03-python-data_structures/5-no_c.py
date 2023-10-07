#!/usr/bin/env python3

def no_c(my_string):
    new_string = f""
    for character in my_string:
        if character.lower() != 'c':
            new_string += f"{character}"
    return new_string
