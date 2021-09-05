#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    bin_n = ""

    while n != 0:
        bin_n = str(n % 2) + bin_n
        n = n // 2

    mx = max([len(i) for i in bin_n.split("0")])
    
    print(mx)