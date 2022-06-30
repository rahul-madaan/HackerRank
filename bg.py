t = int(input())
for _ in range(t):
    bunches = int(input())
    bananas = list(map(int, input().strip().split(" ")))
    second = True
    for i in bananas[:-1]:
        if i == 1:
            second = not second
    print("First") if second==True else print("Second")