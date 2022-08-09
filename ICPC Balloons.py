# https://codeforces.com/problemset/problem/1703/B

t = int(input())
for i in range(t):
    _ = input()
    inp = input()
    inp = [char for char in inp]
    checked = []
    score = 0
    for i in inp:
        if i in checked:
            score += 1
        else:
            score += 2
            checked.append(i)
    print(score)