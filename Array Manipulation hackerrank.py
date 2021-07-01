def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for i in range(len(queries)):
        start_index = queries[i][0] -1
        stop_index = queries[i][1]
        val = queries[i][2]
        arr[start_index] = arr[start_index] + val
        arr[stop_index] = arr[stop_index] - val
    print(arr)

    val = 0
    for i in range(len(arr)):
        val = val + arr[i]
        arr[i] = val

    print(arr)
    return max(arr)


arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
