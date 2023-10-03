#!/usr/bin/python3

# Print numbers from 0 to 99 with proper formatting
for num in range(100):
    print("{:02d}".format(num), end=(", " if num < 99 else "\n"))
