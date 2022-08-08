def magicstick(cls, input1, input2, input3):
    total = 99999999999
    for i in range(len(input2)):
        temp = 0
        for j in range(len(input3)):
            if i!=j:
                mini = abs(input2[i]-input2[j]) * input3[j]
                temp = temp+mini
        if temp<total:
            total = temp

    return(total)

mincost([1,2,3],[20,30,40])