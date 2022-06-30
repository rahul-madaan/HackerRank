a = int(input())
price = list(map(int, input().strip().split(" ")))

t = int(input())

budget = []
for i in range(t):
    budget.append(int(input()))
afford_list = [0] * t

price = sorted(price)


def Count(arr, k,n):
    left = 0
    right = n - 1
    lg = n
    while left <= right:
        m = int(left + (right - left) / 2)
        if arr[m] > k:
            lg = m
            right = m - 1
        else:
            left = m + 1
    return n - lg


arr = price
n = a
ans = []
for i in range(t):
    K = budget[i]
    ans.append(str(a-Count(arr, K, n)))

print("\n".join(ans))
