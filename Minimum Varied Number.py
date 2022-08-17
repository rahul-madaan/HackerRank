# https://codeforces.com/problemset/problem/1714/C
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
final = []
n = int(input())
for i in range(n):
    final = []
    sum = int(input())
    while sum != 0:
        for i in numbers:
            if i <= sum and i not in final:
                sum -= i
                final.append(i)
                break
    print("".join(map(str, final))[::-1])
