t = int(input())
for _ in range(t):
    bunches = int(input())
    bananas = list(map(int, input().strip().split(" ")))
    if bananas[0] == 1:
        counter = 1
        for i in range(len(bananas[:-1])):
            if bananas[i]==1:
                counter +=1
            else:
                break
        print("Second") if counter %2 ==0 else print("First")
    else:
        print("First")