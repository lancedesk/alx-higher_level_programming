#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            # Add other characters as they are
            result += char
    # Print the resulting string followed by a newline character
    print(result)
