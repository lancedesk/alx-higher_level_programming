#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
# Ensuring l_number is always positive
l_number = int(number_string[-1])  # l_number is last number

print(f"Last digit of {number} is {l_number} and is", end=" ")

if (l_number > 5):
    print("greater than 5")
elif (l_number == 0):
    print("0")
elif (l_number < 6 and l_number != 0):
    if (number < 0):
        l_number *= -1
    print("less than 6 and not 0")
