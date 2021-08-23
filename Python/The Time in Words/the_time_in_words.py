#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
    'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three','twenty four', 
    'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
    
    if m == 00:
        return f"{values[h-1]} o' clock"
    if m == 1:
        return f'one minute past {values[h-1]}'
    if m == 15:
        return f'quarter past {values[h-1]}'
    if m == 30:
        return f'half past {values[h-1]}'
    if m == 45:
        return f'quarter to {values[h]}'
    if 1 < m <= 29:
        return f'{values[m-1]} minutes past {values[h-1]}'
    if 31 <= m <= 59:
        return f'{values[60-m-1]} minutes to {values[h]}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
