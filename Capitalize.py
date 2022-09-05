"""
Title     : Capitalize
Domain    : Python
Author    : Fredy
""""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    name = s.split(' ')
    return ' '.join([w.capitalize() for w in name])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
