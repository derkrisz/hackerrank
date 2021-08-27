#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    is_n_even = N % 2 == 0
    
    if not is_n_even or (is_n_even and 6 <= N <= 20):
        print('Weird')
    elif (is_n_even and 2 <= N <= 5) or (is_n_even and N > 20):
        print('Not Weird')