"""
Title     : Average Function
Domain    : Python
Author    : Fredy
"""

#!/bin/python3
#Mini-Max Sum
#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.




import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#Min sum , find the lowest four add them
#Max sum , find the largest four add them
#minus both
#    min = []
#    max = []
    
#    for n in i:

def miniMaxSum(arr):
    # 

    s = 0
    minnum = 999999999
    maxnum = 0
    n = len(arr)
    for i in range(n):
        s += arr[i]
        minnum = min(minnum, arr[i])
        maxnum = max(maxnum, arr[i])
    print(s-maxnum, s-minnum)
    
#    print(sum(arr)-max(arr), sum(arr)-min(arr))
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
