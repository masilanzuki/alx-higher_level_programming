#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
lst = number % 10
if (number < 0):
    number *= -1
    lst = number % 10
    lst *= -1
    number *= -1

if (lst > 5):
    print("{} {} is {} and is greater than 5".format(str, number, lst))

elif (lst == 0):
    print("{} {} is {} and is 0".format(str, number, lst))
elif (lst < 6 and lst != 0):
    print("{} {} is {} and is less than 6 and not 0".format(str, number, lst))
