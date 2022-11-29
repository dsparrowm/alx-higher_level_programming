#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = number % 10
if res == 0:
    print(f"Last digit of {number:d} is {res:d} and is {res:d}")
elif res < 6 and res != 0:
    print(f"Last digit of {number:d} is {res:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {res:d} and is greater than 5")
