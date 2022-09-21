#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# String manipulation problems

# problem starts here
def isValid(s):
    # Write your code here
    # if the characters appear all the same number of times after removing only one character
    # it is valid
    
    count = Counter(s)
    # get frequencies
    # case 1: same frequency
    if len(set(count.values())) == 1:
        return "YES"
    
    # case 2: more than 2 unique frequencies
    elif len(set(count.value())) > 2:
        return "NO"
    
    # case 3: 2 unique frequencies
    else:
        for key in count:
            count[key] -= 1
            temp = list(count.values())
            # remove zeros
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return "YES"
            else:
                count[key] += 1
        return "NO"
    
    
# problem ends here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
