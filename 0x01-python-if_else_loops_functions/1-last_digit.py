#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if last > 5:
    result = "and is greater than 5"
elif last < 6 and not 0:
    result = "and is less than 6 and not 0"
elif last == 0:
    result = "and is 0"

print(f" The last digit of {number:d} is {last} {result}")
