def max_food(diamond, ruby):
    maxi = max(diamond,ruby)
    mini = min(diamond,ruby)
    if min == 0:
        print(0)
    elif diamond == ruby:
        print((diamond*2) // 3)
    elif mini <= maxi // 2:
        print(mini)
    elif maxi > mini // 2:  # even odd case
        diff = mini - (maxi // 2) + (maxi % 2)
        final = (maxi//2) + (diff//3)
        print(final)


a = int(input())
for i in range(a):
    b = input()
    b = b.split(" ")
    b = list(map(int, b))
    diamond = b[0]
    ruby = b[1]
    max_food(diamond, ruby)
