#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    count = Counter(ar)
    pairs = 0
    
    for value in count.values():
        pairs += value // 2
    return pairs

   # Another good solution with a set 
   # colours = set()
   # for i in range(len(ar)):
   #     if ar[i] in colours:
   #         pairs += 1
   #         colours.remove(ar[i])
   #     else:
   #         colours.add(ar[i])
   # return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
