"""
Title     : Counting Sort
Domain    : Python
Author    : Fredy
""""

#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # 
    count = [0] * 100           #contraint from numbers 0 - 99, create an arr of zero and * by 100
    
    for num in arr:             #iterate through the array
        count[num] += 1         #find the index of the number and add 1
    
    return count
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



