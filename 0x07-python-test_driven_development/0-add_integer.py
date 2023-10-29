#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First integer.
        b (int or float, optional): Second integer (default is 98).

    Returns:
        int: The result of the addition.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)

    # Perform the addition
    result = a + b

    # Return the result
    return (result)
