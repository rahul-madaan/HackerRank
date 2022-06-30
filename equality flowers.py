
def max_flower(s):
    a = 0
    num = s[0]
    i = 0
    b = 0
    flag = 0
    final = []
    j = 0
    while(i!=len(s)):
        if s[i] == num:
            if flag == 1:
                min_num = min(a,b)
                fin = 2 * min_num
                final.append(fin)
                a = j
                flag = 0
            a = a + 1
            i = i + 1
            if a == b:
                fin = a + b
                final.append(fin)
                b = 0
        elif s[i] != num:
            b = b + 1
            flag = 1
            i = i + 1
            if a == b:
                fin = a + b
                final.append(fin)
                a = 0

    final
    return max(final)





a = input()
a = input()
a = a.split(" ")

a = list(map(int,a))

print(max_flower(a))
