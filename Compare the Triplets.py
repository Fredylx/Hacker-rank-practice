#!/bin/python3
'''
Author:         Fredy Lopez
Title:          Compare the Triplets
----------------------------------------- Solution ---------------------------------------------
create r
set r as a list
[a,b]
for aa, bb in zip(a,b)
add to r[0] or r[1]
'''
import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    #compare both a [1] & b [1] , then [2], then [3]
    #add to ar = x, y?
    # ar = [x, y] ?
    r = [0,0]
    for aa, bb in zip(a,b):
        if aa > bb:
            r[0] += 1
        elif aa < bb:
            r[1] += 1
    
    return r

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
