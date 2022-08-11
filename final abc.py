n = 10
a = 0
b = 1
c = 1
while c < n:
    b *= c
    a += (b / c)
    c += 1
print(a)
