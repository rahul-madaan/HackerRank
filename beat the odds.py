# https://codeforces.com/problemset/problem/1691/A

t = int(input())
for _ in range(t):
    n = int(input())
    l = input().strip().split()
    l = list(map(int,l))
    odd = 0
    even = 0
    for i in l:
        if i%2==0:
            even =+ 1
        else:
            odd +=1
    print(min(odd,even))