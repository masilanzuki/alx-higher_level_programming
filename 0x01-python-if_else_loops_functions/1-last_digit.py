#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
lastint = number % 10
if (number < 0):
    number *= -1
    lastint = number % 10
    lastint *= -1
    number *= -1

if (lastint > 5):
    print("{} {} is {} and is greater than 5".format(str, number, lastint))

elif (lastint == 0):
    print("{} {} is {} and is 0".format(str, number, lastint))
elif (lastint < 6 and lastint != 0):
    print("{} {} is {} and is less than 6 and not 0".format(str, number, lastint))
