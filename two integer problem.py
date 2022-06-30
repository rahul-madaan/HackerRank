def fun(a, b):

    if (abs(a - b) %10) == 0:
        return (abs(a - b) // 10)
    else:
        return (abs(a - b) // 10) + 1


repetition = int(input())

for i in range(repetition):
    line = input()
    line = line.split(" ")
    a = int(line[0])
    b = int(line[1])
    print(fun(a, b))
