#!/usr/bin/python3


# Define a class called LockedClass.
class LockedClass:
    # Define a special attribute __slots__
    # which restricts the creation of new instance attributes
    # except for 'first_name'.
    __slots__ = ['first_name']
