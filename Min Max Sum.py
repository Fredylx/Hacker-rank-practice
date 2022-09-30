#!/bin/python3

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

def miniMaxSum(arr):
    # Write your code here
    s = 0   #sum
    maximun = 99999999
    minnimum = 0
    n = len(arr)
    for i in range(n):
        s += arr[i]
        minnimum = min(minnimum, arr[i])
        maximun = max(maximun, arr[i])
        
    print(s-minnimum, s-maximun)
    '''
    min = []
    max = []
    
    for i in range(0, len(arr)):
        # logic
        if a > max:
            max = a
        elif a < min:
            min = a
        
    print(min)
    print(max)
    '''

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
