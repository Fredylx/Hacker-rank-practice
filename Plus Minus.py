"""
Title     : Plus Minus
Domain    : Python
Author    : Fredy
"""


#!/bin/python3
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
#Plus Minus

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# if num > 1: += neg
# if num < 1: += pos
# if num = 0: += zero

def plusMinus(arr):
    pos = neg = zero = 0
    length = len(arr)
    for i in range(0, len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg +=1
    
    
    print("{:.6f}".format(float(pos/length)))
    print("{:.6f}".format(float(neg/length)))
    print("{:.6f}".format(float(zero/length)))  

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
