"""
Title     : Diagonal Difference
Domain    : Python
Author    : Fredy
"""

#!/bin/python3
# Diagonal Difference
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.



import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#lt = [1][1] + [2][2] + [3][3] + ...
#rt = [1][n-1-1] + [2][n-1-2] + ...
# return abs

def diagonalDifference(arr):
    # Write your code here
    leftdiagonal = rightdiagonal = 0
    for i in range (n):
        leftdiagonal += arr[i][i]
        rightdiagonal += arr[i][n-1-i]
    return abs(leftdiagonal-rightdiagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
