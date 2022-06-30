def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            result = greater
            break
        greater += 1

    return result


def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


t = int(input())

for i in range(t):
    a = int(input())
    print("1 " + str(a-1))
    


