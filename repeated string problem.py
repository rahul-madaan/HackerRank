#!/bin/python3

import math
import os
import random
import re
import string
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    s_list = list(s)

    number_of_a = s_list.count("a");
    if number_of_a == 0:
        return 0
    print(len(s))
    number_of_full_str = int(n / len(s))
    remainder_chars = n % len(s)
    total = number_of_full_str * number_of_a + s.count("a",0, remainder_chars)
    print(total)
    return total



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
