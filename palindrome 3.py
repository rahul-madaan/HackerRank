a = int(input())

for i in range(a):
    b = input()
    x = list(b)
    l = len(x)
    num = 0
    for j in range(l):
        x.insert(j, "a")
        if x != x[::-1]:
            z = ''.join(map(str, x))
            print("YES")
            print(z)
            num = 1
        del x[j]
        if num == 1:
            break
    if num == 0:
        print("NO")
