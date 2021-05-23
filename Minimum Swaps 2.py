#!/bin/python3

import math
import os
import random
import re
import sys
def swapPosition(q,i,j): #(queue,position1, position2)
    a=q[j]
    q[j]=q[i]
    q[i]=a
    return q

# Complete the minimumSwaps function below.
def minimumSwaps(q):
    for i in range(len(q)):
        for j in range(len(q) - i - 1):




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()
