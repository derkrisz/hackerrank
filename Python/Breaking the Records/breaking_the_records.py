#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_count = max_count = 0
    minimum_record = maximum_record = scores[0] 
    
    for score in scores[1:]:
        if score > maximum_record:
            max_count += 1
            maximum_record = score
        elif score < minimum_record:
            min_count += 1
            minimum_record = score
    
    return [max_count, min_count]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

