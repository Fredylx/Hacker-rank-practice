"""
Title     : Time Delta
Domain    : Python
Author    : Fredy
Created   : 09/10/2022
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    # we have inputs already and it seems like we have the delta too
    #format
    f = "%a %d %b %Y %H:%M:%S %z"
    #datetime
    dt1 = dt.datetime.strptime(t1, f)
    dt2 = dt.datetime.strptime(t2, f)
    return f"{round(abs((dt1-dt2).total_seconds()))}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
