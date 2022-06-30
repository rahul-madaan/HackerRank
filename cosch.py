def maxi(x):
    maximum = 0
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
        maximum = max(maximum, sum)
    return maximum


t = int(input())
ans = []

for i in range(t):
    _ = input()
    team1 = list(map(int, input().strip().split(" ")))
    _ = input()
    team2 = list(map(int, input().strip().split(" ")))
    maxt1 = maxi(team1)
    maxt2 = maxi(team2)
    ans.append(str(maxt1 + maxt2))

print("\n".join(ans))
