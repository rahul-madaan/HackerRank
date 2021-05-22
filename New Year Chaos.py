#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    loop = 0
    for i in range(len(q)):
        for j in range(len(q) - i - 1):
            #print(q[i], ",", q[j + i + 1])
            if q[j + i + 1] < q[i]:
                bribes = bribes + 1
                loop = loop + 1
                if loop > 2:
                    print("Too chaotic")
                    return
        loop = 0
    print(bribes)

    # for loop lagao from front to end and find number of smaller elements found after each element.



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
