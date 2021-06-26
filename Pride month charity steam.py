def simpleGame(scores):
    s1 = 0
    s2 = 0
    front = 1
    lol=0
    if len(scores)%2 ==1:
        lol=1
    for i in range(int (len(scores)/2 )):
        if front == 1:
            s1 = s1 + scores[0]
            num = scores.pop(0)
            if num % 2 == 0:
                if front == 1:
                    front = 0
                else:
                    front = 1
        elif front == 0:
            s1 = s1 + scores[-1]
            num = scores.pop()
            if num % 2 == 0:
                if front == 1:
                    front = 0
                else:
                    front = 1

        if front == 1:
            s2 = s2 + scores[0]
            num = scores.pop(0)
            if num % 2 == 0:
                if front == 1:
                    front = 0
                else:
                    front = 1
        elif front == 0:
            s2 = s2 + scores[-1]
            num = scores.pop()
            if num % 2 == 0:
                if front == 1:
                    front = 0
                else:
                    front = 1
    if lol==1:
        s1=s1+scores[0]
    print(s1)
    print(s2)
    print(s1-s2)
    return s1-s2

simpleGame([2,1,4])
