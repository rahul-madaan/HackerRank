# https://codeforces.com/problemset/problem/1719/A

n = int(input())

for i in range(n):
    inp = list(map(int, input().split(" ")))
    if (inp[0] % 2 == 1 and inp[1] % 2 == 1) or ((inp[0] % 2 == 0 and inp[1] % 2 == 0)):
        print("Tonya")
    else:
        print("Burenka")