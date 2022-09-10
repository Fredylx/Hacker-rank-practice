"""
Title     : Time Conversion
Domain    : Python
Author    : Fredy
"""

# Time Conversion
#Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# 1) 12 AM -> 00
# 2) 1AM to 12PM -> do nothing
# 3) 1PM to 11PM -> take hour and add 12

def timeConversion(s):
    # 
    timeState == s[-2:]
    if timeState == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    if timeState == 'AM' and s[:2] = '12':
        s = '00' + s[2:]
    retturn s[:-2]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
