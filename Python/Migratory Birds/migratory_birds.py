#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
   # d = dict(Counter(arr))
    
   # d = dict()
   
   # for i in arr:
   #     d[i] = d.get(i, 0) + 1
   # return sorted(list(d.items()), key = lambda num: num[1], reverse=True)[0][0]

   # mydict = dict(Counter(arr))
   # maximum = max(mydict, key=mydict.get)  
   # return maximum

   # These both time out on test 4 with lots of numbers :(
       
    typecount = [0 for i in range(5)]
    for i in arr:
        typecount[i-1] += 1
    max_count = max(typecount)
    for i in range(5):
        if typecount[i] == max_count:
            return i+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
