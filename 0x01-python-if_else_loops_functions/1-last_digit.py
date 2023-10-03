#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
l_number = abs(number) % 10  # l_number is the last digit

if (number < 0):
    l_number *= -1

print(f"Last digit of {number} is {l_number} and is", end=" ")

if l_number > 5:
    print("greater than 5")
elif l_number == 0:
    print("0")
else:
    print("less than 6 and not 0")
