
def isPalindrome(x: int) -> bool:
    if (x < 0):
        return bool(0)
    length = len(str(x))

    listOfDigits = list(str(x))
    print(listOfDigits)
    for x in range(length // 2):
        if listOfDigits[x] != listOfDigits[length - x-1]:
            return bool(0)

    return bool(1)





print(isPalindrome(123456654321))
