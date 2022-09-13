"""
Title     : Calendar Module
Domain    : Python
Author    : Fredy
Created   : 9/10/2022
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
import the calendar year
print out nicely
look for the day
'''

import calendar
month, day, year = map(int, input().split())
print(str(calendar.day_name[calendar.weekday(year, month, day)]).upper())

