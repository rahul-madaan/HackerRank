def addition(a, b):
    return a + b


repetition = int(input())

for i in range(repetition):
    line = input()
    line = line.split(" ")
    a = int(line[0])
    b = int(line[1])
    print(addition(a,b))