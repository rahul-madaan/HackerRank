t = int(input())


while(t!=0):
    flag =0
    str = input()
    for i in range(len(str)):
        if str[i] !='a':
            flag = 1
            break

    if flag == 0:
        print("NO")
    else:
        o=str
        str = str+"a"
        r= str
        r = r[::-1]
        if r!=str:
            print("YES")
            print(str)
        else:
            print("YES")
            print("a" + o)
    t=t-1