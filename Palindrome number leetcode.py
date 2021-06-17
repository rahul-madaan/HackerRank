
def isPalindrome(x: int) -> bool:
    # if (x < 0):
    #     return bool(0)
    # length = len(str(x))
    #
    # listOfDigits = list(str(x))
    # print(listOfDigits)
    # for x in range(length // 2):
    #     if listOfDigits[x] != listOfDigits[length - x-1]:
    #         return bool(0)
    #
    # return bool(1)

    if (x < 0):
        return bool(0)

    copy = x
    rev = 0
    while copy != 0:
        temp = copy % 10
        rev = rev * 10
        rev = rev + temp
        copy = copy // 10

    print(rev)
    if rev == x:
        return bool(1)
    else:
        return bool(0)


print(isPalindrome(123456654321))
