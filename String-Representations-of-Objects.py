"""
Title     : String Representations of Objects
Domain    : Python
Author    : Fredy
"""

#!/bin/python3

import math
import os
import random
import re
import sys



class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit
        
    def __str__(self):
        return 'Car with the maximum speed of ' + str(self.max_speed) + ' ' + str(self.unit)

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        
    def __str__(self):
        return 'Boat with the maximum speed of ' + str(max_speed) + ' knots'

        
car = Car(120, 'km/h')
print(car)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
