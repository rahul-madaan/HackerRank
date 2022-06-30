a = int(input())
price = list(map(int, input().strip().split(" ")))

t = int(input())

budget = []
for i in range(t):
    budget.append(int(input()))
price = sorted(price)

def insert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return high + 1

for i in range(t):
    print(insert(price,budget[i]+1))
