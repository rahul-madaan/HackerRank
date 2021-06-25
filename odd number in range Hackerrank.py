def oddNumbers(l, r):
    arr = []
    if l%2==0:
       l=l+1
    for i in range(l,r,2):
        arr.append(i)

    print(arr)
    return arr





oddNumbers(10,50)