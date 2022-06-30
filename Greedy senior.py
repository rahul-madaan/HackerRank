t = int(input())
for i in range(t):
    inp = list(map(int,input().strip().split(" ")))
    cost = (inp[0]-1)*1 + inp[0]*(inp[1]-1)
    print("YES") if cost == inp[2] else print("NO")
