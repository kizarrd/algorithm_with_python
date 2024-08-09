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

def timeConversion(s):
    # Write your code here
    if s[-2] == 'A':
        if int(s[:2]) == 12:
            s = '00' + s[2:]
    else:
        if (pm_time:=int(s[:2])) < 12:
            military_hour = str(pm_time+12)
            s = military_hour + s[2:]
    return s[:-2]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)