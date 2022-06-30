# https://codeforces.com/problemset/problem/1690/A

n = int(input())
for i in range(n):
    total = int(input())
    rem = total % 3
    mid = total // 3
    low = mid - 1
    high = mid + 1

    if rem == 1:
        high += 1
    elif rem == 2:
        high += 1
        mid += 1

    print(mid,high, low)