a = int(input())
price = list(map(int, input().strip().split(" ")))

t = int(input())

budget = []
for i in range(t):
    budget.append(int(input()))
afford_list = [0] * t

price = sorted(price)


def last(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif (x < arr[mid]):
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)

    return -1


# Driver Code
arr = price
n = a
ans = []
for i in range(t):
    K = budget[i]
    ans.append(str(last(arr, 0, n - 1, K, n) + 1))

print("\n".join(ans))
