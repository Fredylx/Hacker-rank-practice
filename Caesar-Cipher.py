"""
Title     : Ceaser Cipher
Domain    : Python
Author    : Fredy
"""


#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
    # Write your code here
    #transverse the plain texts
    #k is the roatation
    #s is the text
    '''
    for i in range(len(s)):
        char = s[i]
        #Encrypt  uppercase characters in plain text
        
        if (char.isupper()):
            resuult += chr((ord(char) + k-65) % 26 + 65)
        #Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) +k - 97) % 26 + 97)
        return result
    
    rotate_string = s
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    
    upper.rotate(k)
    lower.rotate(k)
    
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    
    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lower, lower))
'''
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
        else:
            res.append(c)
                       
    return "".join(map(str, res))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
