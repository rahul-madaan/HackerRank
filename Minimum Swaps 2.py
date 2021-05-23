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
    swap = 0
    i=0
    while i != len(q)-1:
        if q[i] == i+1:
            i=i+1
        else:
            q = swapPosition(q,i,q[i]-1)
            swap = swap + 1
    return swap




"""
    swap =0;
    for i in range(len(q)):
        if q[i] != i+1:
           for j in range(len(q) - i - 1):
               if i+1 == q[j+i+1]:
                   q = swapPosition(q,i,j+i+1)
                   swap = swap+1
                   break;
    return swap
"""





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()
