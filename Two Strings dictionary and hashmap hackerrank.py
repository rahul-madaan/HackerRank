from collections import Counter

def twoStrings(s1, s2):
    res = Counter(s1)

    for i in s2:
        if i in res:
            print("YES")
            return "NO"
    print("NO")


twoStrings('aba', 'dfgfdg')