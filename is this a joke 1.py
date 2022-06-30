def check(a, b, c):
    for i in range(len(a)):
        if a[i] in c:
            c.remove(a[i])
        else:
            print("NO")
            return

    for i in range(len(b)):
        if b[i] in c:
            c.remove(b[i])
        else:
            print("NO")
            return
    if len(c) ==0:
        print("YES")
        return
    else:
        print("NO")
        return

a = input()
b = input()
c = input()

c = list(c)

check(a, b, c)
