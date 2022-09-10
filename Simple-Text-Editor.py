"""
Title     : Simple Text Editor
Domain    : Python
Author    : Fredy
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
stack = []
string = ""
# the input to the string 
for _ in range(int(input())):
    t = input().split()
    # check for query type
    # append the string
    if t[0] == '1':
        stack.append(string)
        string += t[1]
    elif t[0] =='2':
        stack.append(string)
        string = string[:-int(t[1])]
    # print char of the string
    elif t[0] == '3':
        print(string[int(t[1])-1]) # minus 1 because the stack starts at 0
        # undo operation
    elif t[0] =='4':
        string = stack.pop()
