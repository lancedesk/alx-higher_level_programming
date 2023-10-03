#!/usr/bin/python3
# ASCII values for lowercase alphabet
for char in range(97, 123):
    # Skip ASCII values for 'q' and 'e'
    if (char == 113 or char == 101):
        continue;
    print("{}".format(chr(char)), end='')
