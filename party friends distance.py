a = input()
alist = a.split(" ")
for i in range(len(alist)):
    alist[i] = int(alist[i])

alist = sorted(alist)
print((alist[1]-alist[0])+(alist[2]-alist[1]))