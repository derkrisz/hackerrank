#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    maximum = -63

    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:
                total = sum(arr[i][j:j+3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j+3])
            if total > maximum:
                maximum = total           
    
print(maximum)
    
