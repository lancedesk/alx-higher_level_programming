#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
# Ensuring l_number is always positive
l_number = abs(int(number_string[-1]))  # l_number is last number

if (number < 0):
    l_number *= -1

if (l_number > 5):
    print(f"Last digit of {number} is {l_number} and is greater than 5")
elif (l_number == 0):
    print(f"Last digit of {number} is {l_number} and is 0")
elif (l_number < 6 and l_number != 0):
    print(f"Last digit of {number} is {l_number} and is less than 6 and not 0")
