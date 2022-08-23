#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
num = str[-1]
num = int(num)
if num > 5:
    return "Last digit of {} is {} and is greater than 5".format(number,num)
elif num == 0:
    return "Last digit of {} is {} and is 0".format(number,num)
else:
    return "Last digit of {} is {} and is less than 6 and not 0".format(number,num)
