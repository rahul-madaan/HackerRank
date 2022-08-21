# https://codeforces.com/problemset/problem/1702/A
# import math
#
# n = int(input())
#
# for i in range(n):
#     num = int(input())
#     if num<10:
#         print(num-1)
#     elif num<100:
#         print(num-10)
#     else:
#         root = math.ceil(num**(1/10))
#         print(num - 10**root)
#
import math

n = int(input())

for i in range(n):
    num = int(input())
    count = (len(str(num)))
    rem = num - 10**(count-1)
    print(rem)