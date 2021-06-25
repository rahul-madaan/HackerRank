

def rotLeft(a, d):
    # Write your code here
    length = len(a)
    rotations = d%length
    for i in range(rotations):
        front = a[0]
        a.remove(front)
        a.append(front)
    print(a)
    return a


rotLeft([1,2,3,4],13)