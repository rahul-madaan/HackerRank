# https://codeforces.com/problemset/problem/1725/A

inp = list(map(int,input().split()))
n = inp[0]
m = inp[1]


if m == 1:
    print(n-1)
else:
    print(n*(m-1))
