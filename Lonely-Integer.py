#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# logic
# same input = 0
# diff input = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 1
# A ^ A = 0

def lonelyinteger(a):
    result = 0          # set a result starting at 0
    for num in a:       # parse through a
        result ^= num   # follow logic
    return result       # return

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
