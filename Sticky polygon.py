def length(a):
    maxi = max(a)
    sum = 0
    for i in a:
        sum = sum + i

    sum = sum - maxi

    if sum<=maxi:
        print(maxi-sum+1)



a = input()
a = input()
a = a.split(" ")

a = list(map(int, a))

length(a)