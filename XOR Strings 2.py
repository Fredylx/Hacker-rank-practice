'''
Author: Fredy H Lopez (found in discussions
Created: nov 7, 2022
Style: Python 3

---------------------------- Solution ----------------------------
Debug the follwoing code.
The following is the answer which is removing un-needed ; at the end on lines
Adding a += to the if and else statement
'''
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))



