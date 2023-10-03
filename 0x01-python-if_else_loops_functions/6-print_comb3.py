#!/usr/bin/python3

# Print all possible different combinations of two digits
for i in range(10):
    for j in range(i + 1, 10):
        combination = i * 10 + j
        ending = ", " if i != 8 or (i == 8 and j != 9) else "\n"
        print("{:02d}".format(combination), end=ending)
