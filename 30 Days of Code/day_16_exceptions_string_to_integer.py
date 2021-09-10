#!/bin/python3

import math
import os
import random
import re
import sys


S = input()
    
try:
    s = int(S)
    print(s)
except ValueError:
    print('Bad String')
