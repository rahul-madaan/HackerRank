def findSubArray(arr):
    n = len(arr)
    sum = 0
    maxsize = -1
    startindex =0


    # Pick a starting point as i

    for i in range(0, n - 1):
        sum = -1 if (arr[i] == 0) else 1
        for j in range(i + 1, n):
            sum = sum + (-1) if (arr[j] == 0) else sum + 1
            if (sum == 0 and maxsize < j - i + 1):
                maxsize = j - i + 1
                startindex = i

    end_index= startindex + maxsize - 1
    # final = []
    # final.append(startindex)
    # final.append(end_index)
    final = end_index-startindex


    return final


# Driver program to test above functions






a = input()
a = input()
a = a.split(" ")

f = list(map(int, a))
print(findSubArray(f))
