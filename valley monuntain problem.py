import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    path_list = list(path)
    print(path_list)
    counter = 0;
    valley_counter=0;
    for path_step in path:
        if path_step == 'U':
            counter = counter + 1
            if counter == 0:
                valley_counter = valley_counter + 1
        else:
            counter = counter - 1

    return valley_counter



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
